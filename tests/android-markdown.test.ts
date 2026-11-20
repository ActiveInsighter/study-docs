import { describe, expect, it } from 'vitest';
import { buildSourceTree } from '../lib/doc-sources';
import { renderAndroidMarkdown } from '../lib/markdown-export.mjs';
import { getStaticAndroidMarkdownOutputPath } from '../scripts/static-docs-markdown.mjs';

describe('study-docs android markdown & source tree', () => {
  it('maps source paths to .android.md output paths', () => {
    expect(getStaticAndroidMarkdownOutputPath('408/index.mdx')).toBe('docs/408.android.md');
    expect(getStaticAndroidMarkdownOutputPath('math/01.mdx')).toBe('docs/math/01.android.md');
  });

  it('emits structured custom blocks for study-docs components', async () => {
    const raw = `---
title: 归并排序
---

<Callout type="note" title="要点">
时间复杂度为 $O(n \\log n)$。
</Callout>

<CardStep title="思路分析" source="408 真题">
采用分治策略。
</CardStep>
`;
    const rendered = await renderAndroidMarkdown(raw, { title: '归并排序' });
    expect(rendered.startsWith('# 归并排序\n')).toBe(true);
    expect(rendered).toContain(':::note 要点\n\n时间复杂度为 $O(n \\log n)$。\n\n:::');
    expect(rendered).toContain(':::step 思路分析\n**来源：** 408 真题\n\n采用分治策略。\n\n:::');
  });

  it('builds source tree modules from page tree', () => {
    const tree = buildSourceTree({
      children: [
        {
          type: 'folder',
          name: '408',
          children: [
            { type: 'page', name: '绪论', url: '/docs/408/intro' },
          ],
        },
      ],
    });
    expect(tree.modules).toHaveLength(1);
    expect(tree.modules[0].name).toBe('408');
  });
});
