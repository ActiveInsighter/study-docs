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

  it('keeps comparisons and indented fences from swallowing component boundaries', () => {
    const source = [
      '若 $0<x<n$，则继续。',
      '',
      '<Callout type="info">保留说明</Callout>',
      '',
      '  ~~~md',
      '<Callout>保留代码示例</Callout>',
      '  ~~~',
    ].join('\n');
    const result = renderAndroidMarkdown(source, { title: '比较' });
    expect(result).toContain('若 $0<x<n$，则继续。');
    expect(result).toContain(':::info\n\n保留说明\n\n:::');
    expect(result).toContain('  ~~~md\n<Callout>保留代码示例</Callout>\n  ~~~');
  });

  it('keeps Fumadocs callout variants distinct, including titleless callouts', () => {
    const result = renderAndroidMarkdown([
      '<Callout>默认说明</Callout>',
      '<Callout type="tip">提示别名</Callout>',
      '<Callout type="idea">灵感</Callout>',
      '<Callout type="success" title="核对完成">通过</Callout>',
      '<Callout type="error">错误</Callout>',
    ].join('\n\n'), { title: '提示块' });
    expect(result).toContain(':::info\n\n默认说明\n\n:::');
    expect(result).toContain(':::info\n\n提示别名\n\n:::');
    expect(result).toContain(':::idea\n\n灵感\n\n:::');
    expect(result).toContain(':::success 核对完成\n\n通过\n\n:::');
    expect(result).toContain(':::danger\n\n错误\n\n:::');
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
  it('exports imported and inline vocabularies, SVG diagrams, and text outlines', () => {
    const result = renderAndroidMarkdown([
      '<WordCards words={phraseWords.slice(0, 2)} />',
      '<WordCards words={supplementalWords.slice(0, 3)} />',
      "<WordCards words={[{word: 'test', meanings: [{text: '测试'}]}]} />",
      '<InlineSvg src="/images/示意图.svg" alt={"示意图"} />',
      '<MindMap markdown={String.raw`# 知识树\n- 要点`} />',
      '~~~mdx', '<WordCards words={inlineExample} />', '~~~',
    ].join('\n\n'), { title: '内容' });
    const groups = [...result.matchAll(/^:::wordcards\n```json\n(.*)$/gm)]
      .map((match) => JSON.parse(match[1]));
    expect(groups.map((group) => group.length)).toEqual([2, 3, 1]);
    expect(groups[2][0]).toEqual({ word: 'test', meanings: [{ text: '测试' }] });
    expect(result).toContain('![示意图](</images/示意图.svg>)');
    expect(result).toContain('> # 知识树\n> - 要点');
    expect(result).toContain('<WordCards words={inlineExample} />');
  });
  it('resolves relative document and card links using the published source path', () => {
    const result = renderAndroidMarkdown([
      '[导论](./导论/#例题)',
      '<Card title="导论" href="./导论/" />',
      '示例：`[导论](./导论/)`',
    ].join('\n\n'), {
      title: '目录',
      sourcePath: 'politics/classified-questions/marxism-principles/index.mdx',
    });
    expect(result).toContain('[导论](/docs/politics/classified-questions/marxism-principles/%E5%AF%BC%E8%AE%BA#例题)');
    expect(result).toContain('href="/docs/politics/classified-questions/marxism-principles/%E5%AF%BC%E8%AE%BA"');
    expect(result).toContain('`[导论](./导论/)`');
  });
  it('exports image markup, spaced math, and structured fill-in answers', () => {
    const source = [
      '<Question type="blank">',
      '若 $ f(x)$ 满足 $ 0<x<2 $，求 <Blank answer="\\frac{1}{2}" aliases={[\'0.5\', \'1/2\']} kind="math" />。',
      '<Solution><img src="/img/示意图 (1).svg" alt="图 &amp; 例" />',
      '<Image src="../figures/example.svg" alt="组件图" />',
      '![网页附图](https://cdn.example.test/figure.webp)',
      '<a href="/details"><img src="/images/chart.jpg" alt="缩略图" /></a></Solution>',
      '</Question>',
      '代码：`$ x $`',
      '~~~html', '<img src="/sample.png">', '~~~',
    ].join('\n');
    const result = renderAndroidMarkdown(source, { title: '图片和公式', sourcePath: 'course/chapter/lesson.mdx' });
    expect(result).toContain('若 $f(x)$ 满足 $0<x<2$');
    expect(result).toContain('![图 & 例](</img/示意图 (1).svg>)');
    expect(result).toContain('![组件图](</docs/course/figures/example.svg>)');
    expect(result).toContain('![网页附图](https://cdn.example.test/figure.webp)');
    expect(result).toContain('[![缩略图](</images/chart.jpg>)](</details>)');
    expect(result).toContain('`$ x $`');
    expect(result).toContain('~~~html\n<img src="/sample.png">\n~~~');
    const blanks = /^:::question .*blanks="((?:[^"\\]|\\.)*)"/m.exec(result)?.[1];
    expect(blanks).toBeDefined();
    expect(JSON.parse(blanks!.replace(/\\(["\\])/g, '$1')))
      .toEqual([{ answer: '\\frac{1}{2}', aliases: ['0.5', '1/2'], kind: 'math' }]);
  });
});
