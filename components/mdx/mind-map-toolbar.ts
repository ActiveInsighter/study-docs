'use client';

/**
 * Helpers for the official markmap toolbar (`markmap-toolbar`).
 *
 * The toolbar renders plain `<div>` items; these helpers give them the site's
 * Lucide-style icons and the button semantics the library leaves out.
 */

/** First-level branch colours. Mid-tone hues stay legible on light and dark canvases. */
export const MIND_MAP_BRANCH_COLORS = [
  '#4f7cff',
  '#16a37f',
  '#f08c2e',
  '#8b5cf6',
  '#e5487b',
  '#0ea5c6',
  '#c99a12',
  '#6875f5',
  '#ef5a4c',
  '#3fa34d',
] as const;

// Lucide icon geometry (ISC licence), drawn on a 24×24 grid with strokes.
const ICONS = {
  zoomIn: ['M5 12h14', 'M12 5v14'],
  zoomOut: ['M5 12h14'],
  fit: [
    'M3 7V5a2 2 0 0 1 2-2h2',
    'M17 3h2a2 2 0 0 1 2 2v2',
    'M21 17v2a2 2 0 0 1-2 2h-2',
    'M7 21H5a2 2 0 0 1-2-2v-2',
    'M8 12h8',
    'M12 8v8',
  ],
  recurse: [
    'M21 12h-8',
    'M21 6H8',
    'M21 18h-8',
    'M3 6v4c0 1.1.9 2 2 2h3',
    'M3 10v6c0 1.1.9 2 2 2h3',
  ],
  expandAll: ['m7 15 5 5 5-5', 'm7 9 5-5 5 5'],
  collapseAll: ['m7 20 5-5 5 5', 'm7 4 5 5 5-5'],
  reset: ['M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8', 'M3 3v5h5'],
  fullscreen: ['M15 3h6v6', 'm21 3-7 7', 'm3 21 7-7', 'M9 21H3v-6'],
  exitFullscreen: ['m14 10 7-7', 'M20 10h-6V4', 'm3 21 7-7', 'M4 14h6v6'],
} as const;

export type ToolbarIconName = keyof typeof ICONS;

const SVG_NS = 'http://www.w3.org/2000/svg';

export function createToolbarIcon(name: ToolbarIconName) {
  const svg = document.createElementNS(SVG_NS, 'svg');
  svg.setAttribute('viewBox', '0 0 24 24');
  svg.setAttribute('width', '18');
  svg.setAttribute('height', '18');
  svg.setAttribute('fill', 'none');
  svg.setAttribute('stroke', 'currentColor');
  svg.setAttribute('stroke-width', '2');
  svg.setAttribute('stroke-linecap', 'round');
  svg.setAttribute('stroke-linejoin', 'round');
  svg.setAttribute('aria-hidden', 'true');
  for (const d of ICONS[name]) {
    const path = document.createElementNS(SVG_NS, 'path');
    path.setAttribute('d', d);
    svg.append(path);
  }
  return svg;
}

const SEPARATE_BEFORE = new Set(['recurse', 'reset']);

/**
 * Give each toolbar item button semantics, keyboard support and a stable
 * `data-toolbar-item` hook. `toggles` lists items that keep a pressed state.
 */
export function enhanceToolbarAccessibility(
  root: HTMLElement,
  ids: readonly string[],
  toggles: readonly string[] = [],
) {
  root.setAttribute('role', 'toolbar');
  root.setAttribute('aria-label', '思维导图工具');
  root.classList.add('mind-map-toolbar');

  // markmap-toolbar renders items in the order passed to `setItems`.
  const items = root.querySelectorAll<HTMLElement>('.mm-toolbar-item');
  items.forEach((item, index) => {
    const title = item.getAttribute('title') ?? '';
    const id = ids[index] ?? '';
    item.dataset.toolbarItem = id;
    item.setAttribute('role', 'button');
    item.setAttribute('tabindex', '0');
    item.setAttribute('aria-label', title);
    if (!id) return;
    if (SEPARATE_BEFORE.has(id)) item.dataset.separated = 'true';
    if (toggles.includes(id)) {
      item.setAttribute('aria-pressed', String(item.classList.contains('active')));
    }
  });

  if (root.dataset.keyboardReady) return;
  root.dataset.keyboardReady = 'true';
  root.addEventListener('keydown', (event) => {
    const item = (event.target as Element | null)?.closest<HTMLElement>('.mm-toolbar-item');
    if (!item || (event.key !== 'Enter' && event.key !== ' ')) return;
    event.preventDefault();
    item.click();
  });
  root.addEventListener('click', (event) => {
    const item = (event.target as Element | null)?.closest<HTMLElement>('.mm-toolbar-item');
    if (item?.hasAttribute('aria-pressed')) {
      // markmap-toolbar toggles `.active` in its own handler first.
      queueMicrotask(() =>
        item.setAttribute('aria-pressed', String(item.classList.contains('active'))),
      );
    }
  });
}
