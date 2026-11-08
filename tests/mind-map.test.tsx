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
    expect(root.content).toBe('计算机系统');
    expect(root.children[0].content).toBe('硬件');
    expect(root.children[0].children[0].content).toBe('CPU');
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

describe('transformMindMapMarkdown', () => {
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
      '- 图',
      '',
      '  <a href="/images/a.svg"><img src="/images/a.svg" alt="图" width="240" height="120" loading="lazy" /></a>',
    ].join('\n'),
  );
  const nodes = flatten(root);
  const find = (text: string) => nodes.find((node) => node.content.includes(text));

  it('renders formulas with KaTeX HTML only, including CJK text in math', () => {
    const math = find('katex');
    expect(math?.content).toContain('class="katex"');
    expect(math?.content).not.toContain('<math');
    expect(math?.content).not.toContain('katex-error');
  });

  it('highlights code blocks and keeps tables as HTML', () => {
    expect(find('<pre')?.content).toContain('hljs-keyword');
    expect(find('<table')?.content).toContain('<th>i</th>');
  });

  it('keeps CJK text readable and lets markmap measure images eagerly', () => {
    expect(JSON.stringify(root)).not.toMatch(/&#x[0-9a-f]{3,};/i);
    expect(root.content).toBe('复杂度');
    const image = find('<img');
    expect(image?.content).toContain('width="240"');
    expect(image?.content).not.toContain('loading="lazy"');
    expect(image?.content).toContain('decoding="async"');
  });
});

describe('MindMap', () => {
  it('renders a labelled, interactive shell while the browser renderer loads', () => {
    const html = renderToStaticMarkup(
      <MindMap data={JSON.stringify(transformMindMapMarkdown('# 计算机系统'))} title="计算机系统知识结构" />,
    );

    expect(html).toContain('data-mind-map="true"');
    expect(html).toContain('data-variant="embedded"');
    expect(html).toContain('aria-label="计算机系统知识结构"');
    expect(html).toContain('mind-map-toolbar-host');
    expect(html).toContain('滚轮或双指缩放');
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
