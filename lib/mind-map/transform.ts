import type { MarkmapNode } from '@markmap/core';
import { parse } from '@markmap/parse';
import { remarkMath } from '@markmap/plugin-math';

export type MindMapNode = MarkmapNode;

// Source offsets only serve editors; dropping them keeps the serialized tree small.
function stripPositions<T>(value: T): T {
  if (Array.isArray(value)) return value.map(stripPositions) as T;
  if (!value || typeof value !== 'object') return value;
  const result: Record<string, unknown> = {};
  for (const [key, entry] of Object.entries(value)) {
    if (key !== 'position') result[key] = stripPositions(entry);
  }
  return result as T;
}

/**
 * Parse mind-map Markdown into a Markmap tree at build time, with TeX math.
 * The browser then only needs `@markmap/view`.
 */
export function transformMindMapMarkdown(markdown: string): MindMapNode {
  return transformMindMapDocument(markdown).root;
}

/** Keep document options alongside the tree so layouts survive build-time parsing. */
export function transformMindMapDocument(markdown: string) {
  const { root, frontmatter } = parse(markdown.trim(), { plugins: [remarkMath] });
  return { root: stripPositions(root), options: frontmatter.markmap };
}
