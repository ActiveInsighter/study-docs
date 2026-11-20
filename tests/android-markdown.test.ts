import { describe, expect, it } from 'vitest';
import { renderAndroidMarkdown, renderStaticMarkdown } from '../lib/markdown-export.mjs';

describe('Android Markdown export', () => {
  it('preserves authored Markdown and emits native containers for answers and callouts', async () => {
    const source = [
      '---', 'title: 练习', '---', '# 练习', '', '<Question id="q1" type="single">',
      '求 $x$。', '<Option correct>A 的内容</Option>', '<Solution>',
      '<Callout type="warn" title="检查条件">保留公式 $x^2$。</Callout>',
      '</Solution>', '</Question>', '', '~~~md', ':::warning code example', '~~~',
    ].join('\n');
    const result = renderAndroidMarkdown(source, { title: '练习' });
    expect(result).toMatch(/^# 练习\n/);
    expect(result.match(/^# 练习$/gm)).toHaveLength(1);
    expect(result).toContain(':::question {id="q1" type="single" number="1"}');
    expect(result).toContain(':::option {label="A" correct="true"}');
    expect(result).toContain(':::solution 参考答案与解析\n\n**答案：** A');
    expect(result).toContain(':::warning 检查条件\n\n保留公式 $x^2$。');
    expect(result).toContain('~~~md\n:::warning code example\n~~~');

    const ai = await renderStaticMarkdown(source, { title: '练习', url: '/docs/exercise' });
    expect(ai).toContain('# 练习 (/docs/exercise)');
    expect(ai).toContain('**题目 ID：** q1');
    expect(ai).not.toContain(':::solution');
  });

  it('exports Steps, Tabs, Cards and WordCards for Android', () => {
    const source = [
      '<Steps><Step title="一">内容</Step></Steps>',
      '<Tabs items={["JS"]}><Tab>\n\n```js\n1\n```\n\n</Tab></Tabs>',
      '<WordCardModeToggle />',
      '<WordCards words={kaoyanWords.slice(0, 1)} />',
    ].join('\n\n');
    const result = renderAndroidMarkdown(source, { title: '组件' });
    expect(result).toContain(':::steps');
    expect(result).toContain(':::step 一');
    expect(result).toContain(':::tabs');
    expect(result).toContain(':::tab JS');
    expect(result).toContain(':::wordcards');
    expect(result).not.toContain('WordCardModeToggle');
  });
});
