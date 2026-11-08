import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

const root = resolve(process.cwd());
const docsRoot = join(root, 'content/docs/408/mind-maps');
const assetRoot = join(root, 'public/images/408-mind-maps');
const chapters = [
  ['数据结构', 8],
  ['计算机组成原理', 7],
  ['操作系统', 5],
  ['计算机网络', 6],
] as const;

describe('408 chapter mind maps', () => {
  it('pins both Markmap packages to the latest stable release', () => {
    const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
    const lock = JSON.parse(readFileSync(join(root, 'package-lock.json'), 'utf8'));
    for (const name of ['markmap-lib', 'markmap-view']) {
      expect(pkg.dependencies[name]).toBe('0.18.12');
      expect(lock.packages[''].dependencies[name]).toBe('0.18.12');
      expect(lock.packages['node_modules/' + name].version).toBe('0.18.12');
    }
  });

  it('has 26 balanced chapter maps, valid anchors and local SVG references', () => {
    const referencedAssets = new Set<string>();
    const startFence = new RegExp('^' + String.fromCharCode(96).repeat(4) + 'mindmap\\s*$', 'gm');
    const endFence = new RegExp('^' + String.fromCharCode(96).repeat(4) + '\\s*$', 'gm');

    for (const [course, chapterCount] of chapters) {
      const document = readFileSync(join(docsRoot, course + '思维导图.mdx'), 'utf8');
      expect(document).toMatch(/^---\n[\s\S]*?\nfull: true\n---\n/);
      expect(document.match(startFence) ?? []).toHaveLength(chapterCount);
      expect(document.match(endFence) ?? []).toHaveLength(chapterCount);
      expect(document.match(/^## 第[一二三四五六七八九十]+章 /gm) ?? []).toHaveLength(chapterCount);

      const anchors = [...document.matchAll(/<a id="(topic-[^"]+)" \/>/g)]
        .map((match) => match[1]);
      expect(new Set(anchors).size).toBe(anchors.length);
      const anchorSet = new Set(anchors);
      for (const [, reference] of document.matchAll(/\]\(#(topic-[^)]+)\)/g)) {
        expect(anchorSet.has(reference)).toBe(true);
      }
      for (const [, filename] of document.matchAll(/\/images\/408-mind-maps\/([a-z0-9-]+\.svg)/g)) {
        referencedAssets.add(filename);
        expect(existsSync(join(assetRoot, filename))).toBe(true);
      }
    }
    expect(readdirSync(assetRoot).filter((name) => name.endsWith('.svg'))).toHaveLength(616);
    expect(referencedAssets.size).toBeGreaterThan(600);
  });

  it('renders 408 maps in full width without a right TOC or mobile TOC', () => {
    const page = readFileSync(join(root, 'app/docs/[[...slug]]/page.tsx'), 'utf8');
    expect(page).toContain("page.path.startsWith('408/mind-maps/')");
    expect(page).toContain('full={useFullPage}');
    expect(page).toContain('toc={is408MindMapPage ? [] : data.toc}');
    expect(page).toContain('tableOfContent={is408MindMapPage ? { enabled: false } : undefined}');
    expect(page).toContain('tableOfContentPopover={is408MindMapPage ? { enabled: false } : undefined}');
  });
});
