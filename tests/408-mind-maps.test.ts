import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';
import { transformMindMapDocument } from '../lib/mind-map/transform';
import { compareMindMapPaths } from '../lib/mind-map/navigation';

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
  it('pins the Markmap 1.0 packages to one release and drops the 0.18 line', () => {
    const pkg = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
    const lock = JSON.parse(readFileSync(join(root, 'package-lock.json'), 'utf8'));
    const names = ['core', 'parse', 'render', 'view', 'toolbar', 'plugin-math'];
    for (const name of names.map((entry) => '@markmap/' + entry)) {
      expect(pkg.dependencies[name]).toBe('1.0.0');
      expect(lock.packages[''].dependencies[name]).toBe('1.0.0');
      expect(lock.packages['node_modules/' + name].version).toBe('1.0.0');
    }
    for (const legacy of ['markmap-lib', 'markmap-view', 'markmap-toolbar', '@markmap/canvas']) {
      expect(pkg.dependencies[legacy]).toBeUndefined();
    }
  });

  it('lists 26 chapter guides and 402 ordered sections in the four course menus', () => {
    const sectionMeta = JSON.parse(readFileSync(join(docsRoot, 'meta.json'), 'utf8'));
    expect(sectionMeta.pages).toEqual(['index', ...courses.map(([course]) => course)]);
    let sections = 0;
    let chapters = 0;
    for (const [course, title, count] of courses) {
      const files = chapterFiles(course);
      const meta = JSON.parse(readFileSync(join(docsRoot, course, 'meta.json'), 'utf8'));
      expect(meta.title).toBe(title);
      expect(new Set(meta.pages).size).toBe(meta.pages.length);
      expect([...meta.pages].sort()).toEqual(['index', ...files.map((file) => file.replace(/\.mdx$/, ''))].sort());
      expect([...files].sort(compareMindMapPaths).map((file) => file.replace(/\.mdx$/, ''))).toEqual(meta.pages.slice(1));
      const guides = files.filter((file) => /^\d{2}-[a-z]/.test(file));
      expect(guides).toHaveLength(count);
      for (const guide of guides) {
        const prefix = guide.slice(0, 2);
        const children = files.filter((file) => file.startsWith(prefix + '-') && /^\d{2}-\d+-/.test(file))
          .sort((a, b) => Number(a.split('-')[1]) - Number(b.split('-')[1]));
        expect(children.length).toBeGreaterThan(0);
        const start = meta.pages.indexOf(guide.replace(/\.mdx$/, ''));
        expect(meta.pages.slice(start + 1, start + 1 + children.length)).toEqual(children.map((file) => file.replace(/\.mdx$/, '')));
        chapters++;
        sections += children.length;
      }
    }
    expect(chapters).toBe(26);
    expect(sections).toBe(402);
  });

  it('keeps every guide and section as one full-canvas map with working two-sided options', () => {
    for (const [course] of courses) {
      for (const file of chapterFiles(course)) {
        const document = readFileSync(join(docsRoot, course, file), 'utf8');
        expect(document).toMatch(/^---\ntitle: \"[^\"]+\"\n/);
        expect(document).toContain('\nlayout: mind-map\n');
        expect(document.split(fence + 'mindmap\n')).toHaveLength(2);
        const markdown = document.split(fence + 'mindmap\n')[1].slice(0, -fence.length - 1);
        const parsed = transformMindMapDocument(markdown);
        expect(parsed.options).toMatchObject({ layout: 'two-sided', theme: 'cards', foldLevel: 3 });
        expect(parsed.root.children.length).toBeGreaterThan(1);
        // Every source image must survive Markmap parsing, including restored pictures.
        const serialized = JSON.stringify(parsed.root);
        for (const [, name] of markdown.matchAll(/src="\/images\/408-mind-maps\/([^\"]+)"/g)) {
          expect(serialized, course + '/' + file + ': ' + name).toContain('/images/408-mind-maps/' + name);
        }
        expect(document).not.toMatch(/\\\(|\\\)/);
        expect(document.trimEnd().endsWith(fence)).toBe(true);
      }
    }
  });

  it('resolves all links and preserves sized SVGs without unaccounted orphan assets', () => {
    const referenced = new Set<string>();
    const pageUrls = new Set(['/docs/408/mind-maps', ...courses.flatMap(([course]) => [
      '/docs/408/mind-maps/' + course,
      ...chapterFiles(course).map((file) => '/docs/408/mind-maps/' + course + '/' + file.replace(/\.mdx$/, '')),
    ])]);
    for (const directory of ['', ...courses.map(([course]) => course)]) {
      for (const file of readdirSync(join(docsRoot, directory)).filter((name) => name.endsWith('.mdx'))) {
        const document = readFileSync(join(docsRoot, directory, file), 'utf8');
        for (const [, target] of document.matchAll(/\]\((\/docs\/408\/mind-maps[^)#]*)(?:#[^)]*)?\)/g)) {
          expect(pageUrls.has(target.replace(/\/$/, '')), directory + '/' + file + ': ' + target).toBe(true);
        }
        expect(document).not.toMatch(/\]\(\.\.?\//);
        for (const tag of document.matchAll(/<img\b[^>]+>/g)) {
          const name = /src="\/images\/408-mind-maps\/([^\"]+)"/.exec(tag[0])?.[1];
          expect(name, tag[0]).toBeDefined();
          expect(tag[0]).toMatch(/width="\d+"/);
          expect(tag[0]).toMatch(/height="\d+"/);
          expect(tag[0]).toMatch(/alt="[^\"]+"/);
          expect(existsSync(join(assetRoot, name!)), name).toBe(true);
          referenced.add(name!);
        }
      }
    }
    const report = JSON.parse(readFileSync(join(root, 'reports/408-mind-map-image-migration.json'), 'utf8'));
    const replacements = new Set<string>(report.placements.filter((entry: { asset: string; selectedAsset: string }) => entry.asset !== entry.selectedAsset).map((entry: { asset: string }) => entry.asset));
    const assets = readdirSync(assetRoot);
    expect(assets).toHaveLength(612);
    expect(referenced.size).toBe(530);
    expect(assets.filter((name) => !referenced.has(name) && !replacements.has(name))).toEqual([]);
    expect(new Set(report.placements.map((entry: { asset: string }) => entry.asset)).size).toBe(223);
    for (const entry of report.placements) {
      const target = readFileSync(join(docsRoot, entry.target), 'utf8');
      expect(target, entry.asset + ' -> ' + entry.target).toContain('/images/408-mind-maps/' + entry.selectedAsset);
      if (entry.branch) {
        const branch = target.split('## ' + entry.branch + '\n')[1]?.split('\n## ')[0];
        expect(branch, entry.asset).toContain('/images/408-mind-maps/' + entry.selectedAsset);
      }
    }
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
