/*
 * Editorial content of the home page: copy, tones and the real excerpts used
 * by the specimens. Modules, sections and page counts are derived from the
 * documentation source in `catalog.server.ts`, so they never drift from the
 * content. Files are referenced by their path under content/docs and resolved
 * to URLs at build time; `tests/home-content.test.ts` checks they exist.
 */

/** Highlighter tone per study module (top-level folder). New modules cycle through the spare tones. */
export const moduleTones: Record<string, Tone> = {
  politics: 'pink',
  english: 'blue',
  math: 'yellow',
  '408': 'green',
  algorithm: 'violet',
};

export const TONES = ['pink', 'blue', 'yellow', 'green', 'violet', 'orange'] as const;
export type Tone = (typeof TONES)[number];

/** Initial-exam schedule used by the tear-off countdown calendar. */
export const examSchedule = {
  startsAt: '2026-12-19T08:30:00+08:00',
  note: '按 2026 年 12 月 19 日 08:30（北京时间）估算，具体考试安排以官方公告为准。',
} as const;

/** One sheet of the tear-off calendar: a reminder plus the almanac's 宜 / 忌. */
export const calendarSheets = [
  { quote: '把今天的一点弄懂，就是向前走了一步。', good: '弄懂一个知识点', avoid: '贪多求快' },
  { quote: '先完成眼前这一题，再慢慢走向下一个目标。', good: '专心做完一节', avoid: '频繁切换科目' },
  { quote: '复习不必每天完美，愿你每天都有一点收获。', good: '记下今天学会的', avoid: '和别人比进度' },
  { quote: '累了就休息一下，回来再继续也来得及。', good: '按时睡觉', avoid: '熬夜硬撑' },
  { quote: '把错题变成理解，把理解留给下一次尝试。', good: '重做一道错题', avoid: '只看答案不动笔' },
] as const;

/** Specimens: one live sample of each kind of study material, linked to where it comes from. */
export const specimens = {
  math: {
    module: 'math',
    title: '公式和图像放在一起看',
    formulaFile: 'math/formulas/advanced-mathematics/01-第一章 函数、极限、连续.mdx',
    formula: 'e^x=1+x+\\frac{1}{2!}x^2+\\cdots+\\frac{1}{n!}x^n+o(x^n)',
    plotFile: 'math/visualizations/index.mdx',
  },
  english: {
    module: 'english',
    title: '词卡正面记词，背面看语境',
    file: 'english/vocabulary/module-01.mdx',
    /** Real cards from data/vocabulary, in this order. */
    words: ['evidence', 'approach', 'individual', 'social'],
  },
  politics: {
    module: 'politics',
    title: '答案先遮住，想好再揭开',
    file: 'politics/27肖帽子题背诵版/01-marxism/01-chapter.mdx',
    items: [
      { prompt: '物质的根本属性是', answer: '运动' },
      { prompt: '“心诚则灵，心不诚则不灵”的说法是', answer: '夸大了意识能动作用的唯心主义观点' },
      { prompt: '自然界与人类社会、客观世界与主观世界相分化的关键是', answer: '人的实践活动' },
    ],
  },
  algorithm: {
    module: 'algorithm',
    title: '每一步都看得见的算法',
    file: 'algorithm/02-array/02-二分查找-循环不变量与边界的统一写法.mdx',
    nums: [1, 3, 5, 7, 9, 11, 13, 15, 17],
    target: 15,
  },
} as const;
