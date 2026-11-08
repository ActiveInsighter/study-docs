'use client';

import type { INode, IPureNode } from 'markmap-common';
import type { Markmap } from 'markmap-view';
import type { Toolbar } from 'markmap-toolbar';
import { useCallback, useEffect, useRef, useState } from 'react';
import {
  MIND_MAP_BRANCH_COLORS,
  createToolbarIcon,
  enhanceToolbarAccessibility,
  type ToolbarIconName,
} from '@/components/mdx/mind-map-toolbar';

const EMPTY_MESSAGE = '思维导图内容为空。请补充至少一个标题。';
const RENDER_ERROR_MESSAGE = '思维导图暂时无法生成，请检查 Markdown 的层级结构。';
const FOCUS_HASH_PREFIX = '#focus=';
const FIT_MAX_SCALE = 1.1;
/** Below this zoom, CJK labels stop being readable without zooming in. */
const MIN_READABLE_SCALE = 0.62;

export type MindMapStatus = 'loading' | 'ready' | 'error';

export interface MindMapImagePreview {
  src: string;
  alt: string;
  href: string;
}

interface ZoomTransformLike {
  k: number;
  x: number;
  y: number;
  scale(k: number): ZoomTransformLike;
  translate(x: number, y: number): ZoomTransformLike;
}

interface Padding {
  top: number;
  right: number;
  bottom: number;
  left: number;
}

/** Keep the floating header and toolbar from covering the fitted map. */
function measurePadding(svg: SVGSVGElement): Padding {
  const stage = svg.parentElement;
  const svgRect = svg.getBoundingClientRect();
  const header = stage?.querySelector('.mind-map-header')?.getBoundingClientRect();
  const toolbar = stage?.querySelector('.mind-map-toolbar-host')?.getBoundingClientRect();
  const gap = 20;
  return {
    top: header && header.height > 0 ? header.bottom - svgRect.top + gap : gap,
    right: gap,
    bottom: toolbar && toolbar.height > 0 ? svgRect.bottom - toolbar.top + gap : gap,
    left: gap,
  };
}

function measureFit(mm: Markmap, svg: SVGSVGElement) {
  const { width, height } = svg.getBoundingClientRect();
  const padding = measurePadding(svg);
  const { x1, y1, x2, y2 } = mm.state.rect;
  const contentWidth = Math.max(x2 - x1, 1);
  const contentHeight = Math.max(y2 - y1, 1);
  const availableWidth = Math.max(width - padding.left - padding.right, 48);
  const availableHeight = Math.max(height - padding.top - padding.bottom, 48);
  const scale = Math.min(
    availableWidth / contentWidth,
    availableHeight / contentHeight,
    FIT_MAX_SCALE,
  );
  return { availableHeight, availableWidth, contentHeight, contentWidth, padding, scale, x1, y1 };
}

/**
 * Like `Markmap.fit`, but respects overlays and never zooms out past a
 * readable scale: oversized maps start at the root, ready to pan.
 */
async function fitView(mm: Markmap) {
  const svg = mm.svg.node() as (SVGSVGElement & { __zoom?: ZoomTransformLike }) | null;
  const current = svg?.__zoom;
  if (!svg || !current || !mm.state.data) return mm.fit(FIT_MAX_SCALE);

  const fit = measureFit(mm, svg);
  const k = Math.max(fit.scale, Math.min(MIN_READABLE_SCALE, FIT_MAX_SCALE));
  const rootRect = mm.state.data.state.rect;
  const x =
    fit.contentWidth * k <= fit.availableWidth
      ? fit.padding.left + (fit.availableWidth - fit.contentWidth * k) / 2 - fit.x1 * k
      : fit.padding.left - fit.x1 * k;
  const y =
    fit.contentHeight * k <= fit.availableHeight
      ? fit.padding.top + (fit.availableHeight - fit.contentHeight * k) / 2 - fit.y1 * k
      : fit.padding.top + fit.availableHeight / 2 - (rootRect.y + rootRect.height / 2) * k;

  // d3-zoom keeps the element's transform on `__zoom`; derive identity from it.
  const identity = current.scale(1 / current.k).translate(-current.x, -current.y);
  const target = identity.translate(x, y).scale(k);
  await mm
    .transition(mm.svg)
    .call(mm.zoom.transform as never, target)
    .end()
    .catch(() => undefined);
}

/**
 * Render the initial tree. When the caller did not pin a depth and the full
 * default depth would be unreadably small, fold back to the first two levels.
 */
async function showInitialView(mm: Markmap, root: IPureNode, adaptive: boolean) {
  await mm.setData(root);
  const svg = mm.svg.node() as SVGSVGElement | null;
  const data = mm.state.data;
  if (adaptive && svg && data && measureFit(mm, svg).scale < MIN_READABLE_SCALE) {
    data.children?.forEach((child) => {
      if (child.children?.length) child.payload = { ...child.payload, fold: 1 };
    });
    await mm.renderData();
  }
  await fitView(mm);
}

interface UseMindMapOptions {
  /** Build-time markmap tree, serialized as JSON. Preferred. */
  data?: string;
  /** Markdown transformed in the browser (direct `<MindMap markdown>` usage). */
  markdown?: string;
  initialExpandLevel: number;
  /** Fold to two levels when the default depth is too dense to read. */
  adaptiveExpand: boolean;
  maxWidth: number;
  fullscreenTargetRef: React.RefObject<HTMLElement | null>;
  onNavigate: (href: string) => void;
  onPreviewImage: (image: MindMapImagePreview) => void;
}

async function loadRoot(data: string | undefined, markdown: string | undefined) {
  if (data) return JSON.parse(data) as IPureNode;

  const [{ Transformer }, { default: katex }] = await Promise.all([
    import('markmap-lib'),
    import('katex'),
  ]);
  // markmap-lib's browser KaTeX plugin renders through `window.katex`.
  Object.assign(window, { katex });
  return new Transformer().transform((markdown ?? '').trim()).root;
}

function textOf(node: INode | IPureNode) {
  return node.content
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&gt;/g, '>')
    .replace(/&lt;/g, '<')
    .replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Find the node whose label matches `label`, plus its ancestors. */
function findPathByLabel(root: INode, label: string) {
  const target = label.replace(/\s+/g, ' ').trim();
  let partial: INode[] | undefined;

  const walk = (node: INode, path: INode[]): INode[] | undefined => {
    const nextPath = [...path, node];
    const text = textOf(node);
    if (text === target) return nextPath;
    if (!partial && text.startsWith(target)) partial = nextPath;
    for (const child of node.children ?? []) {
      const found = walk(child, nextPath);
      if (found) return found;
    }
    return undefined;
  };

  return walk(root, []) ?? partial;
}

function readFocusLabel(hash: string) {
  if (!hash.startsWith(FOCUS_HASH_PREFIX)) return null;
  try {
    return decodeURIComponent(hash.slice(FOCUS_HASH_PREFIX.length));
  } catch {
    return null;
  }
}

function setFold(node: INode, fold: number, recursive: boolean) {
  if (node.children?.length) node.payload = { ...node.payload, fold };
  if (recursive) node.children?.forEach((child) => setFold(child, fold, true));
}

function enhanceInteractiveNodes(svg: SVGSVGElement) {
  svg
    .querySelectorAll<SVGCircleElement>('g.markmap-node > circle')
    .forEach((circle) => {
      const group = circle.parentElement;
      const label = group
        ?.querySelector<SVGForeignObjectElement>('foreignObject')
        ?.textContent?.trim();

      circle.setAttribute('tabindex', '0');
      circle.setAttribute('role', 'button');
      circle.setAttribute(
        'aria-expanded',
        String(!group?.classList.contains('markmap-fold')),
      );
      circle.setAttribute(
        'aria-label',
        label ? `${label.slice(0, 80)}，展开或收起分支` : '展开或收起分支',
      );
    });
}

export function useMindMap({
  data,
  markdown,
  initialExpandLevel,
  adaptiveExpand,
  maxWidth,
  fullscreenTargetRef,
  onNavigate,
  onPreviewImage,
}: UseMindMapOptions) {
  const svgRef = useRef<SVGSVGElement>(null);
  const toolbarHostRef = useRef<HTMLDivElement>(null);
  const markmapRef = useRef<Markmap | null>(null);
  const callbacksRef = useRef({ onNavigate, onPreviewImage });
  callbacksRef.current = { onNavigate, onPreviewImage };

  const hasContent = Boolean(data?.trim() || markdown?.trim());
  const [status, setStatus] = useState<MindMapStatus>(
    hasContent ? 'loading' : 'error',
  );
  const [errorMessage, setErrorMessage] = useState<string | null>(
    hasContent ? null : EMPTY_MESSAGE,
  );

  const focusLabel = useCallback(async (label: string) => {
    const instance = markmapRef.current;
    const root = instance?.state.data;
    if (!instance || !root) return false;

    const path = findPathByLabel(root, label);
    if (!path) return false;

    const target = path[path.length - 1];
    path.slice(0, -1).forEach((ancestor) => setFold(ancestor, 0, false));
    await instance.renderData();
    await instance.setHighlight(target);
    await instance.ensureVisible(target, { left: 96, right: 96, top: 96, bottom: 96 });
    return true;
  }, []);

  useEffect(() => {
    let cancelled = false;
    const svg = svgRef.current;
    const toolbarHost = toolbarHostRef.current;
    let toolbar: Toolbar | undefined;
    let nodeObserver: MutationObserver | undefined;
    let resizeObserver: ResizeObserver | undefined;
    let resizeFrame: number | undefined;
    const cleanups: Array<() => void> = [];

    markmapRef.current?.destroy();
    markmapRef.current = null;
    svg?.replaceChildren();
    toolbarHost?.replaceChildren();

    if (!hasContent || !svg) {
      setStatus('error');
      setErrorMessage(EMPTY_MESSAGE);
      return;
    }

    setStatus('loading');
    setErrorMessage(null);

    async function render() {
      try {
        const [{ Markmap, deriveOptions }, { Toolbar }, root] = await Promise.all([
          import('markmap-view'),
          import('markmap-toolbar'),
          loadRoot(data, markdown),
        ]);
        if (cancelled || !svg) return;

        const prefersReducedMotion =
          typeof window.matchMedia === 'function' &&
          window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        const instance = Markmap.create(svg, {
          ...deriveOptions({
            color: [...MIND_MAP_BRANCH_COLORS],
            colorFreezeLevel: 2,
            lineWidth: [3, 2.25, 1.5],
          }),
          autoFit: false,
          duration: prefersReducedMotion ? 0 : 280,
          fitRatio: 0.94,
          initialExpandLevel,
          maxInitialScale: FIT_MAX_SCALE,
          maxWidth,
          nodeMinHeight: 22,
          paddingX: 10,
          pan: true,
          spacingHorizontal: 88,
          spacingVertical: 10,
          zoom: true,
        });
        markmapRef.current = instance;

        // Official markmap toolbar, with the site's icons, Chinese labels and
        // a few extra actions registered through its public API.
        toolbar = new Toolbar();
        toolbar.showBrand = false;
        toolbar.attach(instance);
        const item = (
          id: string,
          title: string,
          icon: ToolbarIconName,
          onClick?: (event: Event) => void,
        ) => {
          const existing = toolbar!.registry[id];
          toolbar!.register({
            id,
            title,
            content: createToolbarIcon(icon),
            onClick: onClick ?? existing?.onClick,
          });
        };
        const run = (action: (mm: Markmap) => Promise<unknown>) => () => {
          const mm = markmapRef.current;
          if (mm) void action(mm);
        };
        const isFullscreen = () =>
          Boolean(fullscreenTargetRef.current) &&
          document.fullscreenElement === fullscreenTargetRef.current;
        const fullscreenSupported =
          typeof document.documentElement.requestFullscreen === 'function';

        item('zoomIn', '放大', 'zoomIn');
        item('zoomOut', '缩小', 'zoomOut');
        item('fit', '适应窗口', 'fit', run(fitView));
        item('recurse', '联动子分支：开启后点击节点圆点会同时展开或收起全部下级', 'recurse');
        item(
          'expandAll',
          '全部展开',
          'expandAll',
          run(async (mm) => {
            if (!mm.state.data) return;
            setFold(mm.state.data, 0, true);
            await mm.renderData();
            await fitView(mm);
          }),
        );
        item(
          'collapseAll',
          '折叠到第一层',
          'collapseAll',
          run(async (mm) => {
            if (!mm.state.data) return;
            mm.state.data.children?.forEach((child) => setFold(child, 1, true));
            await mm.renderData();
            await fitView(mm);
          }),
        );
        item(
          'reset',
          '恢复初始视图',
          'reset',
          run(async (mm) => {
            const freshRoot = await loadRoot(data, markdown);
            await mm.setHighlight(null);
            await showInitialView(mm, freshRoot, adaptiveExpand);
          }),
        );
        const renderFullscreenItem = () =>
          item(
            'fullscreen',
            isFullscreen() ? '退出全屏' : '全屏查看',
            isFullscreen() ? 'exitFullscreen' : 'fullscreen',
            () => {
              const target = fullscreenTargetRef.current;
              if (!target) return;
              const request = isFullscreen()
                ? document.exitFullscreen()
                : target.requestFullscreen();
              request.catch(() => {
                // Fullscreen can be denied by the browser or an embedding host.
              });
            },
          );
        renderFullscreenItem();

        const toolbarItems = [
          'zoomIn',
          'zoomOut',
          'fit',
          'recurse',
          'expandAll',
          'collapseAll',
          'reset',
          ...(fullscreenSupported ? ['fullscreen'] : []),
        ];
        const renderToolbar = () => {
          toolbar!.setItems(toolbarItems);
          enhanceToolbarAccessibility(toolbar!.el, toolbarItems, ['recurse']);
        };
        renderToolbar();
        toolbarHost?.replaceChildren(toolbar.el);

        const handleFullscreenChange = () => {
          renderFullscreenItem();
          const recurseActive = toolbar!.el
            .querySelector('[data-toolbar-item="recurse"]')
            ?.classList.contains('active');
          renderToolbar();
          if (recurseActive) {
            const recurse = toolbar!.el.querySelector('[data-toolbar-item="recurse"]');
            recurse?.classList.add('active');
            recurse?.setAttribute('aria-pressed', 'true');
          }
        };
        document.addEventListener('fullscreenchange', handleFullscreenChange);
        cleanups.push(() =>
          document.removeEventListener('fullscreenchange', handleFullscreenChange),
        );

        // Keyboard access to fold toggles.
        enhanceInteractiveNodes(svg);
        nodeObserver = new MutationObserver(() => enhanceInteractiveNodes(svg));
        nodeObserver.observe(svg, {
          attributes: true,
          attributeFilter: ['class'],
          childList: true,
          subtree: true,
        });
        const handleKeyDown = (event: KeyboardEvent) => {
          const target = event.target;
          if (!(target instanceof Element) || !target.matches('circle[role="button"]')) return;
          if (event.key !== 'Enter' && event.key !== ' ') return;
          event.preventDefault();
          target.dispatchEvent(new MouseEvent('click', { bubbles: true }));
        };
        svg.addEventListener('keydown', handleKeyDown);
        cleanups.push(() => svg.removeEventListener('keydown', handleKeyDown));

        // Links and images inside node content.
        const handleClick = (event: MouseEvent) => {
          if (event.defaultPrevented || event.button !== 0) return;
          const target = event.target;
          if (!(target instanceof Element)) return;

          const image = target.closest('img');
          if (image) {
            event.preventDefault();
            const link = image.closest('a');
            callbacksRef.current.onPreviewImage({
              src: image.currentSrc || image.src,
              alt: image.alt,
              href: link?.href ?? image.src,
            });
            return;
          }

          const link = target.closest('a');
          const href = link?.getAttribute('href');
          if (!link || !href || event.metaKey || event.ctrlKey || event.shiftKey) return;

          const label = readFocusLabel(href);
          if (label) {
            event.preventDefault();
            window.history.replaceState(null, '', href);
            void focusLabel(label);
            return;
          }
          if (href.startsWith('/') && !href.startsWith('//') && link.target !== '_blank') {
            event.preventDefault();
            callbacksRef.current.onNavigate(href);
          }
        };
        svg.addEventListener('click', handleClick);
        cleanups.push(() => svg.removeEventListener('click', handleClick));

        const handleHashChange = () => {
          const label = readFocusLabel(window.location.hash);
          if (label) void focusLabel(label);
        };
        window.addEventListener('hashchange', handleHashChange);
        cleanups.push(() => window.removeEventListener('hashchange', handleHashChange));

        await showInitialView(instance, root, adaptiveExpand);
        if (cancelled) return;

        const initialFocus = readFocusLabel(window.location.hash);
        if (initialFocus) await focusLabel(initialFocus);

        // Refit when the canvas changes size (sidebar, fullscreen, rotation).
        const resizeTarget = svg.parentElement ?? svg;
        let previousWidth = resizeTarget.clientWidth;
        let previousHeight = resizeTarget.clientHeight;
        if (typeof ResizeObserver !== 'undefined') {
          resizeObserver = new ResizeObserver(([entry]) => {
            if (!entry || cancelled || markmapRef.current !== instance) return;
            const { width, height } = entry.contentRect;
            const changed =
              Math.abs(width - previousWidth) > 8 ||
              Math.abs(height - previousHeight) > 8;
            previousWidth = width;
            previousHeight = height;
            if (!changed) return;
            if (resizeFrame !== undefined) cancelAnimationFrame(resizeFrame);
            resizeFrame = requestAnimationFrame(() => {
              if (!cancelled && markmapRef.current === instance) {
                void fitView(instance);
              }
            });
          });
          resizeObserver.observe(resizeTarget);
        }

        if (!cancelled) setStatus('ready');
      } catch {
        if (cancelled) return;
        markmapRef.current?.destroy();
        markmapRef.current = null;
        svg?.replaceChildren();
        toolbarHost?.replaceChildren();
        setStatus('error');
        setErrorMessage(RENDER_ERROR_MESSAGE);
      }
    }

    void render();

    return () => {
      cancelled = true;
      cleanups.forEach((cleanup) => cleanup());
      nodeObserver?.disconnect();
      resizeObserver?.disconnect();
      if (resizeFrame !== undefined) cancelAnimationFrame(resizeFrame);
      markmapRef.current?.destroy();
      markmapRef.current = null;
      svg?.replaceChildren();
      toolbar?.el.remove();
    };
  }, [
    data,
    markdown,
    hasContent,
    initialExpandLevel,
    adaptiveExpand,
    maxWidth,
    focusLabel,
    fullscreenTargetRef,
  ]);

  return { errorMessage, status, svgRef, toolbarHostRef };
}
