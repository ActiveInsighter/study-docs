import type { Root } from 'mdast';
import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';
import { MindMap } from '../components/mdx/mind-map';
import { remarkMdxMindmap } from '../lib/mdx/remark-mindmap';
import { transformMindMapMarkdown, type MindMapNode } from '../lib/mind-map/transform';

vi.mock('next/navigation', () => ({
  useRouter: () => ({ push: vi.fn() }),
}));

function transform(tree: Root) {
  remarkMdxMindmap()(tree, undefined as never, undefined as never);
  return tree;
}

function flatten(node: MindMapNode): MindMapNode[] {
  return [node, ...node.children.flatMap(flatten)];
}

function text(node: MindMapNode) {
  return node.content.map((inline) => ('value' in inline ? inline.value : '')).join('');
}

describe('remarkMdxMindmap', () => {
  it('converts mindmap code fences into MindMap components with a build-time tree', () => {
    const tree = transform({
      type: 'root',
      children: [
        {
          type: 'code',
          lang: 'mindmap',
          value: '\n# 计算机系统\n\n## 硬件\n- CPU\n',
        },
      ],
    } as Root);

    const node = tree.children[0] as unknown as {
      type: string;
      name: string;
      attributes: Array<{ name: string; value: string }>;
    };
    expect(node.type).toBe('mdxJsxFlowElement');
    expect(node.name).toBe('MindMap');
    expect(node.attributes.map((attribute) => attribute.name)).toEqual(['data']);

    const root = JSON.parse(node.attributes[0].value) as MindMapNode;
    expect(text(root)).toBe('计算机系统');
    expect(text(root.children[0])).toBe('硬件');
    expect(text(root.children[0].children[0])).toBe('CPU');
  });

  it('only transforms non-empty mindmap fences and leaves other code alone', () => {
    const normalCode = {
      type: 'code' as const,
      lang: 'tsx',
      value: '<MindMap />',
    };
    const emptyMindmap = {
      type: 'code' as const,
      lang: 'mindmap',
      value: '   ',
    };
    const tree = transform({
      type: 'root',
      children: [normalCode, emptyMindmap],
    } as Root);

    expect(tree.children[0]).toBe(normalCode);
    expect(tree.children[1]).toBe(emptyMindmap);
  });
});

describe('transformMindMapMarkdown (Markmap 1.0)', () => {
  const fence = String.fromCharCode(96).repeat(3);
  const root = transformMindMapMarkdown(
    [
      '# 复杂度',
      '## 公式',
      '- 渐进 $O(n\\log_2 n)$ 个节点',
      '## 代码',
      '- 示例',
      '',
      '  ' + fence + 'cpp',
      '  int main() { return 0; }',
      '  ' + fence,
      '## 表格',
      '- 三元组',
      '',
      '  | i | j |',
      '  |---|---|',
      '  | 1 | 3 |',
      '## 配图',
      '- <img src="/images/408-mind-maps/a.svg" alt="图" width="240" height="120">',
    ].join('\n'),
  );
  const nodes = flatten(root);
  const find = (label: string) => nodes.find((node) => text(node).startsWith(label));

  it('keeps TeX in labels as inline math for the MathJax content plugin', () => {
    const math = find('渐进')?.content.find((inline) => inline.type === 'inlineMath');
    expect(math).toMatchObject({ type: 'inlineMath', value: 'O(n\\log_2 n)' });
  });

  it('turns code blocks and tables into notes', () => {
    expect(find('示例')?.notes[0]?.block).toMatchObject({ type: 'code', lang: 'cpp' });
    expect(find('三元组')?.notes[0]?.block.type).toBe('table');
  });

  it('keeps sized images and strips source positions', () => {
    const image = nodes
      .flatMap((node) => node.content)
      .find((inline) => inline.type === 'image');
    expect(image).toMatchObject({
      type: 'image',
      url: '/images/408-mind-maps/a.svg',
      data: { width: 240, height: 120 },
    });
    expect(JSON.stringify(root)).not.toContain('"position"');
  });
});

describe('MindMap', () => {
  it('renders a labelled shell while the Markmap view loads', () => {
    const html = renderToStaticMarkup(
      <MindMap data={JSON.stringify(transformMindMapMarkdown('# 计算机系统'))} title="计算机系统知识结构" />,
    );

    expect(html).toContain('data-mind-map="true"');
    expect(html).toContain('data-variant="embedded"');
    expect(html).toContain('aria-label="计算机系统知识结构"');
    expect(html).toContain('mind-map-surface-host');
    expect(html).toContain('mind-map-toolbar-host');
    expect(html).toContain('正在生成思维导图');
  });

  it('renders the page variant with its header overlay', () => {
    const html = renderToStaticMarkup(
      <MindMap markdown="# 树" variant="page" header={<h1>第五章 树与二叉树</h1>} />,
    );

    expect(html).toContain('data-variant="page"');
    expect(html).toContain('<div class="mind-map-header"><h1>第五章 树与二叉树</h1></div>');
    expect(html).not.toContain('--mind-map-height');
  });

  it('renders a useful empty state for direct component usage', () => {
    const html = renderToStaticMarkup(<MindMap markdown="  " />);

    expect(html).toContain('data-status="error"');
    expect(html).toContain('思维导图内容为空');
  });
});
