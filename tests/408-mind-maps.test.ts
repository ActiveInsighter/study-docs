import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

const root = resolve(process.cwd());
const docsRoot = join(root, 'content/docs/408/mind-maps');
const assetRoot = join(root, 'public/images/408-mind-maps');
const courses = [
  ['data-structures', '数据结构', 8],
  ['computer-organization', '计算机组成原理', 7],
  ['operating-systems', '操作系统', 5],
  ['computer-networks', '计算机网络', 6],
] as const;
const fence = String.fromCharCode(96).repeat(4);

function chapterFiles(course: string) {
  return readdirSync(join(docsRoot, course))
    .filter((name) => /^\d{2}-[a-z0-9-]+\.mdx$/.test(name))
    .sort();
}

describe('408 chapter mind maps', () => {
  it('pins the Markmap packages to one release', () => {
    const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
    const lock = JSON.parse(readFileSync(join(root, 'package-lock.json'), 'utf8'));
    for (const name of ['markmap-lib', 'markmap-view', 'markmap-toolbar']) {
      expect(pkg.dependencies[name]).toBe('0.18.12');
      expect(lock.packages[''].dependencies[name]).toBe('0.18.12');
      expect(lock.packages['node_modules/' + name].version).toBe('0.18.12');
    }
  });

  it('splits the four courses into 26 chapter pages listed in meta.json', () => {
    const sectionMeta = JSON.parse(readFileSync(join(docsRoot, 'meta.json'), 'utf8'));
    expect(sectionMeta.pages).toEqual(['index', ...courses.map(([course]) => course)]);
    expect(readdirSync(docsRoot).filter((name) => name.endsWith('.mdx'))).toEqual(['index.mdx']);

    let total = 0;
    for (const [course, title, count] of courses) {
      const files = chapterFiles(course);
      const meta = JSON.parse(readFileSync(join(docsRoot, course, 'meta.json'), 'utf8'));
      expect(files).toHaveLength(count);
      expect(meta.title).toBe(title);
      expect(meta.pages).toEqual(['index', ...files.map((file) => file.replace(/\.mdx$/, ''))]);
      expect(existsSync(join(docsRoot, course, 'index.mdx'))).toBe(true);
      total += files.length;
    }
    expect(total).toBe(26);
  });

  it('gives every chapter exactly one mind map in the full-canvas layout', () => {
    const numerals = '一二三四五六七八九十';
    for (const [course, , count] of courses) {
      const files = chapterFiles(course);
      files.forEach((file, index) => {
        const document = readFileSync(join(docsRoot, course, file), 'utf8');
        const chapter = '第' + numerals[index] + '章';
        expect(document).toMatch(new RegExp('^---\\ntitle: "' + chapter + ' [^"]+"\\n'));
        expect(document).toMatch(/\nlayout: mind-map\n---\n/);
        expect(document.split(fence + 'mindmap\n')).toHaveLength(2);
        expect(document.trimEnd().endsWith(fence)).toBe(true);
        expect(document).toMatch(new RegExp('\\n# ' + chapter + ' '));
        expect(document).not.toMatch(/<a id="topic-/);
        expect(document).not.toMatch(/\]\(#topic-/);
      });
      expect(files).toHaveLength(count);
    }
  });

  it('resolves cross-chapter links, focus links and local SVG references', () => {
    const referencedAssets = new Set<string>();
    const pageUrls = new Set(
      courses.flatMap(([course]) =>
        chapterFiles(course).map((file) => '/docs/408/mind-maps/' + course + '/' + file.replace(/\.mdx$/, '')),
      ),
    );

    for (const [course] of courses) {
      for (const file of chapterFiles(course)) {
        const document = readFileSync(join(docsRoot, course, file), 'utf8');
        for (const [, target] of document.matchAll(/\]\((\/docs\/408\/mind-maps\/[^)#]+)(?:#[^)]*)?\)/g)) {
          expect(pageUrls.has(target)).toBe(true);
        }
        for (const [, label] of document.matchAll(/#focus=([^)]+)\)/g)) {
          expect(decodeURIComponent(label).trim().length).toBeGreaterThan(0);
        }
        for (const [, filename] of document.matchAll(/\/images\/408-mind-maps\/([a-z0-9-]+\.svg)/g)) {
          referencedAssets.add(filename);
          expect(existsSync(join(assetRoot, filename))).toBe(true);
        }
      }
    }
    expect(readdirSync(assetRoot).filter((name) => name.endsWith('.svg'))).toHaveLength(616);
    expect(referencedAssets.size).toBeGreaterThan(600);
  });

  it('renders mind-map pages as a full canvas without TOC, title block or footer', () => {
    const page = readFileSync(join(root, 'app/docs/[[...slug]]/page.tsx'), 'utf8');
    const config = readFileSync(join(root, 'source.config.ts'), 'utf8');
    expect(config).toContain("layout: z.enum(['mind-map']).optional()");
    expect(page).toContain("page.data.layout === 'mind-map'");
    expect(page).toContain('tableOfContent={{ enabled: false }}');
    expect(page).toContain('tableOfContentPopover={{ enabled: false }}');
    expect(page).toContain('footer={{ enabled: false }}');
    expect(page).toContain('variant="page"');
  });
});
