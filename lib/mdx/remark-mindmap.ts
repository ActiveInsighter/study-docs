import { transformMindMapMarkdown } from '../mind-map/transform';
import type { Root } from 'mdast';
import type { Transformer } from 'unified';
import { visit } from 'unist-util-visit';

export interface RemarkMdxMindmapOptions {
  /** The fenced-code language that should become a mind map. */
  lang?: string;
}

function toMDX(code: string) {
  // Markdown → markmap tree happens once at build time: math is rendered by
  // KaTeX and code by highlight.js here, so the browser only loads the view.
  const data = JSON.stringify(transformMindMapMarkdown(code));

  return {
    type: 'mdxJsxFlowElement' as const,
    name: 'MindMap',
    attributes: [
      {
        type: 'mdxJsxAttribute' as const,
        name: 'data',
        value: data,
      },
    ],
    children: [],
  };
}

/** Convert non-empty `mindmap` code fences into the shared MindMap component. */
export function remarkMdxMindmap(
  options: RemarkMdxMindmapOptions = {},
): Transformer<Root, Root> {
  const { lang = 'mindmap' } = options;

  return (tree) => {
    visit(tree, 'code', (node, index, parent) => {
      if (
        node.lang !== lang ||
        !node.value.trim() ||
        typeof index !== 'number' ||
        !parent
      ) {
        return;
      }

      parent.children[index] = toMDX(node.value);
    });
  };
}
