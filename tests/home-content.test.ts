import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { describe, expect, it } from 'vitest';
import { specimens } from '@/lib/home/content';
import { layoutMindMap, MIND_MAP, splitSides } from '@/lib/home/mind-map-layout';
import type { StudyModule } from '@/lib/home/types';

const moduleOf = (key: string, sections: number): StudyModule => ({
  key,
  name: key,
  href: `/docs/${key}/`,
  tone: 'blue',
  pages: sections * 3,
  sections: Array.from({ length: sections }, (_, index) => ({
    name: `${key}-${index}`,
    href: `/docs/${key}/${index}/`,
    pages: 3,
  })),
});

describe('mind map layout', () => {
  it('balances the two sides', () => {
    // politics, english, math, 408, algorithm (capped to 6 rows)
    expect(splitSides([4, 6, 6, 3, 6])).toEqual(['left', 'left', 'right', 'left', 'right']);
  });

  it('caps long modules with a "more" leaf that links to the module', () => {
    const layout = layoutMindMap([moduleOf('algorithm', 14), moduleOf('math', 2)]);
    const algorithm = layout.branches.find((branch) => branch.key === 'algorithm')!;
    expect(algorithm.leaves).toHaveLength(MIND_MAP.maxLeaves);
    expect(algorithm.leaves.at(-1)).toMatchObject({ more: true, href: '/docs/algorithm/', name: '另有 9 个专题' });
  });

  it('places modules and leaves on their side, centred on the root', () => {
    const layout = layoutMindMap([moduleOf('a', 4), moduleOf('b', 5), moduleOf('c', 3)]);
    expect(layout.root).toEqual({ x: MIND_MAP.rootX, y: layout.height / 2 });
    for (const branch of layout.branches) {
      const direction = branch.side === 'left' ? -1 : 1;
      expect(branch.x).toBe(MIND_MAP.rootX + direction * MIND_MAP.moduleOffset);
      expect(branch.twigs).toHaveLength(branch.leaves.length);
      for (const leaf of branch.leaves) {
        expect(leaf.x).toBe(MIND_MAP.rootX + direction * MIND_MAP.leafOffset);
        expect(leaf.y).toBeGreaterThan(0);
        expect(leaf.y).toBeLessThan(layout.height);
      }
      expect(branch.trunk.startsWith(`M ${MIND_MAP.rootX} `)).toBe(true);
    }
  });
});

describe('home specimen sources', () => {
  it.each([
    specimens.math.formulaFile,
    specimens.math.plotFile,
    specimens.english.file,
    specimens.politics.file,
    specimens.algorithm.file,
  ])('%s exists', (file) => {
    expect(existsSync(resolve(process.cwd(), 'content/docs', file))).toBe(true);
  });

  it('quotes the formula and recall answers from their pages', () => {
    const formulas = readFileSync(resolve(process.cwd(), 'content/docs', specimens.math.formulaFile), 'utf8');
    expect(formulas).toContain(specimens.math.formula);
    const recall = readFileSync(resolve(process.cwd(), 'content/docs', specimens.politics.file), 'utf8');
    for (const item of specimens.politics.items) {
      expect(recall).toContain(item.prompt);
      expect(recall).toContain(`**${item.answer}**`);
    }
  });

  it('finds every word card in the vocabulary source', () => {
    const core = JSON.parse(
      readFileSync(resolve(process.cwd(), 'data/vocabulary/kaoyan-source/01-core.json'), 'utf8'),
    ) as { word: string }[];
    const words = new Set(core.map((card) => card.word));
    for (const word of specimens.english.words) expect(words.has(word)).toBe(true);
  });
});
