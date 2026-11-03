import type { Tone } from './content';
import type { StudyModule } from './types';

/*
 * Lays the study modules out as a two-sided mind map: the site in the middle,
 * modules on either side, their sections fanning out beyond them.
 *
 * Horizontal positions are percentages of the map's width and vertical
 * positions are pixels, so the same numbers place the HTML labels and the SVG
 * branches (drawn in a `0 0 100 height` viewBox stretched to the box). Pure
 * and deterministic: it runs at build time and is unit-tested.
 */

export interface MapLeaf {
  name: string;
  href: string;
  pages: number | null;
  /** "另有 N 个专题": stands in for sections beyond the cap and links to the module. */
  more: boolean;
  x: number;
  y: number;
}

export interface MapBranch {
  key: string;
  name: string;
  href: string;
  tone: Tone;
  pages: number;
  side: 'left' | 'right';
  x: number;
  y: number;
  leaves: MapLeaf[];
  /** SVG path from the root to the module. */
  trunk: string;
  /** SVG paths from the module to each leaf. */
  twigs: string[];
}

export interface MindMapLayout {
  height: number;
  root: { x: number; y: number };
  branches: MapBranch[];
}

export const MIND_MAP = {
  /** Rows per module, including the "more" row. */
  maxLeaves: 6,
  rowHeight: 34,
  moduleGap: 24,
  padding: 40,
  rootX: 50,
  moduleOffset: 17,
  leafOffset: 31,
} as const;

function curve(x1: number, y1: number, x2: number, y2: number): string {
  const middle = (x1 + x2) / 2;
  const f = (value: number) => Number(value.toFixed(2));
  return `M ${f(x1)} ${f(y1)} C ${f(middle)} ${f(y1)}, ${f(middle)} ${f(y2)}, ${f(x2)} ${f(y2)}`;
}

function leavesOf(module: StudyModule): Omit<MapLeaf, 'x' | 'y'>[] {
  const { maxLeaves } = MIND_MAP;
  if (module.sections.length <= maxLeaves) {
    return module.sections.map((section) => ({ ...section, more: false }));
  }
  const shown = module.sections.slice(0, maxLeaves - 1);
  return [
    ...shown.map((section) => ({ ...section, more: false })),
    { name: `另有 ${module.sections.length - shown.length} 个专题`, href: module.href, pages: null, more: true },
  ];
}

const sideHeight = (rows: number, modules: number) =>
  modules === 0 ? 0 : rows * MIND_MAP.rowHeight + (modules - 1) * MIND_MAP.moduleGap;

/**
 * Splits modules between the two sides so the taller side is as short as
 * possible; ties keep earlier modules on the left. Order within a side
 * follows the source order.
 */
export function splitSides(rowCounts: readonly number[]): ('left' | 'right')[] {
  const count = rowCounts.length;
  if (count > 16) {
    // Exhaustive search is only for the handful of study modules.
    return rowCounts.map((_, index) => (index % 2 === 0 ? 'left' : 'right'));
  }
  let best: ('left' | 'right')[] = [];
  let bestScore: [number, number, number] = [Infinity, Infinity, Infinity];
  for (let mask = 0; mask < 1 << count; mask++) {
    const sides = rowCounts.map((_, index) => ((mask >> index) & 1 ? 'right' : 'left') as 'left' | 'right');
    const totals = { left: { rows: 0, modules: 0 }, right: { rows: 0, modules: 0 } };
    // Moving an earlier module to the right costs more, so ties keep it on the left.
    let order = 0;
    sides.forEach((side, index) => {
      totals[side].rows += rowCounts[index] ?? 0;
      totals[side].modules += 1;
      if (side === 'right') order += 2 ** (count - 1 - index);
    });
    const left = sideHeight(totals.left.rows, totals.left.modules);
    const right = sideHeight(totals.right.rows, totals.right.modules);
    const score: [number, number, number] = [Math.max(left, right), Math.abs(left - right), order];
    const better = score.findIndex((value, index) => value !== bestScore[index]);
    if (better >= 0 && (score[better] ?? 0) < (bestScore[better] ?? 0)) {
      bestScore = score;
      best = sides;
    }
  }
  return best;
}

export function layoutMindMap(modules: readonly StudyModule[]): MindMapLayout {
  const { rowHeight, moduleGap, padding, rootX, moduleOffset, leafOffset } = MIND_MAP;
  const leafSets = modules.map(leavesOf);
  const sides = splitSides(leafSets.map((leaves) => leaves.length));

  const heightOf = (side: 'left' | 'right') => {
    const indexes = sides.flatMap((value, index) => (value === side ? [index] : []));
    return sideHeight(
      indexes.reduce((sum, index) => sum + (leafSets[index]?.length ?? 0), 0),
      indexes.length,
    );
  };
  const contentHeight = Math.max(heightOf('left'), heightOf('right'));
  const height = contentHeight + padding * 2;
  const root = { x: rootX, y: height / 2 };

  const cursor = {
    left: padding + (contentHeight - heightOf('left')) / 2,
    right: padding + (contentHeight - heightOf('right')) / 2,
  };

  const branches = modules.map((module, index): MapBranch => {
    const side = sides[index] ?? 'left';
    const direction = side === 'left' ? -1 : 1;
    const leafX = rootX + direction * leafOffset;
    const moduleX = rootX + direction * moduleOffset;
    const leaves = (leafSets[index] ?? []).map((leaf, row) => ({
      ...leaf,
      x: leafX,
      y: cursor[side] + row * rowHeight + rowHeight / 2,
    }));
    cursor[side] += leaves.length * rowHeight + moduleGap;
    const first = leaves[0]?.y ?? root.y;
    const last = leaves.at(-1)?.y ?? root.y;
    const y = (first + last) / 2;
    return {
      key: module.key,
      name: module.name,
      href: module.href,
      tone: module.tone,
      pages: module.pages,
      side,
      x: moduleX,
      y,
      leaves,
      trunk: curve(root.x, root.y, moduleX, y),
      twigs: leaves.map((leaf) => curve(moduleX, y, leaf.x, leaf.y)),
    };
  });

  return { height, root, branches };
}
