import { transformMindMapDocument } from '../mind-map/transform';
import type { Root } from 'mdast';
import type { Transformer } from 'unified';
import { visit } from 'unist-util-visit';

export interface RemarkMdxMindmapOptions {
  /** The fenced-code language that should become a mind map. */
  lang?: string;
}

function toMDX(code: string) {
  // Markdown → Markmap tree happens once at build time, so the browser skips
  // the Markdown parser and only loads the view.
  const document = transformMindMapDocument(code);
  const data = JSON.stringify(document.root);

  return {
    type: 'mdxJsxFlowElement' as const,
    name: 'MindMap',
    attributes: [
      {
        type: 'mdxJsxAttribute' as const,
        name: 'data',
        value: data,
      },
      ...(document.options == null ? [] : [{
        type: 'mdxJsxAttribute' as const,
        name: 'documentOptions',
        value: JSON.stringify(document.options),
      }]),
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
