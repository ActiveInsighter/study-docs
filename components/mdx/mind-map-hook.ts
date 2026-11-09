'use client';

import type { Inline, MarkmapNode, Matrix, Primitive } from '@markmap/core';
import type { Markmap, ViewOptions } from '@markmap/view';
import { useCallback, useEffect, useRef, useState } from 'react';

const EMPTY_MESSAGE = '思维导图内容为空。请补充至少一个标题。';
const RENDER_ERROR_MESSAGE = '思维导图暂时无法生成，请检查 Markdown 的层级结构。';
const FOCUS_HASH_PREFIX = '#focus=';
/** Visible nodes above which the first view folds back to the root's children. */
const DENSE_MAP_NODES = 48;
/**
 * Smallest scale the first view opens at. Fitting a large map into the window
 * shrinks its labels past reading (15% on a phone), so it opens no smaller than this
 * on the root instead, and 适应窗口 still shows the whole map.
 */
const READABLE_SCALE = { narrow: 0.6, wide: 0.9 } as const;
const NARROW_WIDTH = 640;

export type MindMapStatus = 'loading' | 'ready' | 'error';
export type MindMapColorScheme = 'light' | 'dark';

export interface MindMapImagePreview {
  src: string;
  alt: string;
}

interface UseMindMapOptions {
  /** Build-time Markmap tree, serialized as JSON. Preferred. */
  data?: string;
  documentOptions?: string;
  /** Markdown parsed in the browser (direct `<MindMap markdown>` usage). */
  markdown?: string;
  /** Fold nodes at this depth and deeper; `undefined` picks one from the map's size. */
  foldLevel?: number;
  wrapWidth: number;
  fitPadding: number;
  colorScheme: MindMapColorScheme;
  onNavigate: (href: string) => void;
  onPreviewImage: (image: MindMapImagePreview) => void;
}

async function loadDocument(data: string | undefined, markdown: string | undefined, documentOptions: string | undefined) {
  if (data) return {
    root: JSON.parse(data) as MarkmapNode,
    options: documentOptions ? JSON.parse(documentOptions) as unknown : undefined,
  };

  const [{ parse }, { remarkMath }] = await Promise.all([
    import('@markmap/parse'),
    import('@markmap/plugin-math'),
  ]);
  const { root, frontmatter } = parse((markdown ?? '').trim(), { plugins: [remarkMath] });
  return { root, options: frontmatter.markmap };
}

function inlineText(content: readonly Inline[]): string {
  return content
    .map((inline) => {
      if ('value' in inline && typeof inline.value === 'string') return inline.value;
      if ('children' in inline) return inlineText(inline.children as Inline[]);
      return '';
    })
    .join('')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Id of the node whose label matches `label`, preferring an exact match. */
function findNodeId(root: MarkmapNode, label: string) {
  const target = label.replace(/\s+/g, ' ').trim();
  let partial: string | undefined;
  const walk = (node: MarkmapNode): string | undefined => {
    const text = inlineText(node.content);
    if (text === target) return node.id;
    if (!partial && text.startsWith(target)) partial = node.id;
    for (const child of node.children) {
      const found = walk(child);
      if (found) return found;
    }
    return undefined;
  };
  return walk(root) ?? partial;
}

/** Alt text the Markdown gives an image (`![alt](src)` or a raw `<img alt>`). */
function findImageAlt(root: MarkmapNode, src: string): string | undefined {
  const fromInlines = (items: readonly Inline[]): string | undefined => {
    for (const inline of items) {
      if (inline.type === 'image' && inline.url === src) return inline.alt ?? undefined;
      if (inline.type === 'html' && inline.value.includes(src)) {
        const alt = /\balt\s*=\s*(?:"([^"]*)"|'([^']*)')/u.exec(inline.value);
        if (alt) return alt[1] ?? alt[2];
      }
      if ('children' in inline) {
        const found = fromInlines(inline.children as Inline[]);
        if (found) return found;
      }
    }
    return undefined;
  };
  const walk = (node: MarkmapNode): string | undefined =>
    fromInlines(node.content) ?? node.children.map(walk).find(Boolean);
  return walk(root);
}

function readFocusLabel(hash: string) {
  if (!hash.startsWith(FOCUS_HASH_PREFIX)) return null;
  try {
    return decodeURIComponent(hash.slice(FOCUS_HASH_PREFIX.length));
  } catch {
    return null;
  }
}

/** Two levels below the root, or only the root's children when that is too dense. */
function pickFoldLevel(root: MarkmapNode) {
  let visible = 1;
  for (const child of root.children) visible += 1 + child.children.length;
  return visible > DENSE_MAP_NODES ? 1 : 2;
}

function applyMatrix([a, b, c, d, e, f]: Matrix, x: number, y: number) {
  return [a * x + c * y + e, b * x + d * y + f] as const;
}

function multiplyMatrix(m: Matrix, n: Matrix): Matrix {
  return [
    m[0] * n[0] + m[2] * n[1],
    m[1] * n[0] + m[3] * n[1],
    m[0] * n[2] + m[2] * n[3],
    m[1] * n[2] + m[3] * n[3],
    m[0] * n[4] + m[2] * n[5] + m[4],
    m[1] * n[4] + m[3] * n[5] + m[5],
  ];
}

/** The image drawn at a layout point (from the rendered primitives). */
function imageAt(primitives: readonly Primitive[], x: number, y: number): string | undefined {
  let found: string | undefined;
  const walk = (items: readonly Primitive[], matrix: Matrix) => {
    for (const item of items) {
      if (item.kind === 'group') {
        walk(item.children, item.transform ? multiplyMatrix(matrix, item.transform) : matrix);
      } else if (item.kind === 'image') {
        const [x1, y1] = applyMatrix(matrix, item.x, item.y);
        const [x2, y2] = applyMatrix(matrix, item.x + item.w, item.y + item.h);
        if (x >= Math.min(x1, x2) && x <= Math.max(x1, x2) && y >= Math.min(y1, y2) && y <= Math.max(y1, y2)) {
          found = item.src;
        }
      }
    }
  };
  walk(primitives, [1, 0, 0, 1, 0, 0]);
  return found;
}

export function useMindMap({
  data,
  documentOptions,
  markdown,
  foldLevel,
  wrapWidth,
  fitPadding,
  colorScheme,
  onNavigate,
  onPreviewImage,
}: UseMindMapOptions) {
  const surfaceRef = useRef<HTMLDivElement>(null);
  const markmapRef = useRef<Markmap | null>(null);
  // The live view, for the React toolbar; null until the map is drawn.
  const [markmap, setMarkmap] = useState<Markmap | null>(null);
  const [initialLevel, setInitialLevel] = useState<number | null>(null);
  const callbacksRef = useRef({ onNavigate, onPreviewImage });
  callbacksRef.current = { onNavigate, onPreviewImage };
  const colorSchemeRef = useRef(colorScheme);
  colorSchemeRef.current = colorScheme;

  const hasContent = Boolean(data?.trim() || markdown?.trim());
  const [status, setStatus] = useState<MindMapStatus>(hasContent ? 'loading' : 'error');
  const [errorMessage, setErrorMessage] = useState<string | null>(
    hasContent ? null : EMPTY_MESSAGE,
  );

  const focusLabel = useCallback((label: string) => {
    const mm = markmapRef.current;
    const root = mm?.tree;
    if (!mm || !root) return false;
    const id = findNodeId(root, label);
    return id ? mm.focusNode(id) : false;
  }, []);

  useEffect(() => {
    let cancelled = false;
    const surface = surfaceRef.current;
    const cleanups: Array<() => void> = [];

    if (!hasContent || !surface) {
      setStatus('error');
      setErrorMessage(EMPTY_MESSAGE);
      return;
    }

    setStatus('loading');
    setErrorMessage(null);

    async function render() {
      try {
        const { root, options: documentOptionsValue } = await loadDocument(data, markdown, documentOptions);
        const [{ Markmap, resolveViewOptions }, { defaultContentPlugins }, { mathContent }] =
          await Promise.all([
            import('@markmap/view'),
            import('@markmap/render'),
            import('@markmap/plugin-math'),
          ]);
        if (cancelled || !surface) return;

        const doc = surface.ownerDocument;
        const element = doc.createElementNS('http://www.w3.org/2000/svg', 'svg');
        element.setAttribute('class', 'mind-map-surface');
        element.setAttribute('role', 'img');
        element.setAttribute('aria-label', surface.getAttribute('aria-label') ?? '思维导图');
        surface.replaceChildren(element);
        cleanups.push(() => element.remove());

        const resolved = resolveViewOptions({ wrapWidth }, documentOptionsValue).options;
        const options: ViewOptions = {
          ...resolved,
          plugins: [...defaultContentPlugins, mathContent],
          colorScheme: colorSchemeRef.current,
          foldLevel: foldLevel ?? resolved.foldLevel ?? pickFoldLevel(root),
          fitPadding,
          fitMaxScale: 1.25,
        };
        const mm = Markmap.create(element, root, options);
        markmapRef.current = mm;

        // The first fit happens now, or once the element is laid out.
        const sized = () => {
          const box = element.getBoundingClientRect();
          return box.width > 0 && box.height > 0;
        };
        const openReadable = () => {
          const { width } = element.getBoundingClientRect();
          if (!width || !mm.tree) return;
          const readable = width < NARROW_WIDTH ? READABLE_SCALE.narrow : READABLE_SCALE.wide;
          if (mm.transform.k < readable) mm.focusNode(mm.tree.id, { scale: readable, animate: false });
        };
        if (sized()) openReadable();
        else {
          const stop = mm.on('zoom', () => {
            stop();
            openReadable();
          });
          cleanups.push(stop);
        }
        cleanups.push(() => {
          mm.destroy();
          if (markmapRef.current === mm) markmapRef.current = null;
        });

        setMarkmap(mm);
        setInitialLevel(Number.isFinite(options.foldLevel) ? options.foldLevel ?? null : null);
        cleanups.push(() => setMarkmap((current) => (current === mm ? null : current)));

        // Site links inside labels navigate in-app; focus links move to a node;
        // images open in the preview dialog. Hit-test in layout
        // coordinates before the view handles the click.
        const handleClick = (event: MouseEvent) => {
          if (event.defaultPrevented || event.button !== 0) return;
          const box = element.getBoundingClientRect();
          const [x, y] = mm.transform.invert([event.clientX - box.x, event.clientY - box.y]);
          const hit = mm.hitAt(x, y);

          if (hit?.kind === 'link') {
            const { href } = hit;
            const label = readFocusLabel(href);
            if (label) {
              event.preventDefault();
              window.history.replaceState(null, '', href);
              focusLabel(label);
            } else if (
              href.startsWith('/') &&
              !href.startsWith('//') &&
              !event.metaKey &&
              !event.ctrlKey &&
              !event.shiftKey
            ) {
              event.preventDefault();
              callbacksRef.current.onNavigate(href);
            }
            return;
          }
          if (hit) return;

          const src = mm.result ? imageAt(mm.result.primitives, x, y) : undefined;
          if (src) {
            event.preventDefault();
            callbacksRef.current.onPreviewImage({
              src,
              alt: (mm.tree && findImageAlt(mm.tree, src)) || '配图',
            });
          }
        };
        element.addEventListener('click', handleClick as EventListener, true);
        cleanups.push(() => element.removeEventListener('click', handleClick as EventListener, true));

        const handleHashChange = () => {
          const label = readFocusLabel(window.location.hash);
          if (label) focusLabel(label);
        };
        window.addEventListener('hashchange', handleHashChange);
        cleanups.push(() => window.removeEventListener('hashchange', handleHashChange));
        handleHashChange();

        setStatus('ready');
      } catch {
        if (cancelled) return;
        cleanups.splice(0).forEach((cleanup) => cleanup());
        setStatus('error');
        setErrorMessage(RENDER_ERROR_MESSAGE);
      }
    }

    void render();

    return () => {
      cancelled = true;
      cleanups.splice(0).forEach((cleanup) => cleanup());
    };
  }, [
    data,
    documentOptions,
    markdown,
    hasContent,
    foldLevel,
    wrapWidth,
    fitPadding,
    focusLabel,
  ]);

  // Follow the site's light / dark theme without rebuilding the map.
  useEffect(() => {
    const mm = markmapRef.current;
    if (!mm || mm.options.colorScheme === colorScheme) return;
    mm.setOptions({ ...mm.options, colorScheme });
  }, [colorScheme, status]);

  return { errorMessage, status, surfaceRef, markmap, initialLevel };
}
