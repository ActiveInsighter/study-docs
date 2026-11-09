import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';
import { transformMindMapDocument } from '../lib/mind-map/transform';
import { compareMindMapPaths } from '../lib/mind-map/navigation';
import { loader, type VirtualFile } from 'fumadocs-core/source';

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

function chapterFolders(course: string) {
  return readdirSync(join(docsRoot, course), { withFileTypes: true })
    .filter((entry) => entry.isDirectory()).map((entry) => entry.name).sort();
}

function chapterFiles(course: string) {
  return chapterFolders(course).flatMap((chapter) =>
    readdirSync(join(docsRoot, course, chapter))
      .filter((name) => name.endsWith('.mdx'))
      .map((name) => chapter + '/' + name),
  ).sort(compareMindMapPaths);
}

function pageUrl(course: string, file: string) {
  return '/docs/408/mind-maps/' + course + '/' + file.replace(/(?:\/index)?\.mdx$/, '');
}

describe('408 chapter mind maps', () => {
  it('renders the actual Fumadocs tree with sections only inside their chapter', () => {
    const files: VirtualFile[] = [];
    for (const path of readdirSync(docsRoot, { recursive: true }) as string[]) {
      if (path.endsWith('meta.json')) files.push({ type: 'meta', path, data: JSON.parse(readFileSync(join(docsRoot, path), 'utf8')) });
      else if (path.endsWith('.mdx')) files.push({ type: 'page', path, data: { title: /^title: "(.*)"/m.exec(readFileSync(join(docsRoot, path), 'utf8'))?.[1] } });
    }
    const tree = loader({ baseUrl: '/docs/408/mind-maps', source: { files } }).getPageTree();
    const folders = tree.children.filter((node) => node.type === 'folder');
    expect(folders).toHaveLength(4);
    for (const [course, , count] of courses) {
      const folder = folders.find((node) => node.$ref?.folder === course)!;
      expect(folder.children.filter((node) => node.type === 'page')).toHaveLength(1);
      const chapters = folder.children.filter((node) => node.type === 'folder');
      expect(chapters).toHaveLength(count);
      for (const chapter of chapters) {
        const directory = chapter.$ref!.folder!;
        const meta = JSON.parse(readFileSync(join(docsRoot, directory, 'meta.json'), 'utf8'));
        const pages = chapter.children.filter((node) => node.type === 'page');
        expect(pages.map((node) => node.url)).toEqual(meta.pages.map((name: string) => '/docs/408/mind-maps/' + directory + (name === 'index' ? '' : '/' + name)));
      }
    }
  });

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

  it('nests all 402 sections in 26 ordered chapter folders', () => {
    const sectionMeta = JSON.parse(readFileSync(join(docsRoot, 'meta.json'), 'utf8'));
    expect(sectionMeta.pages).toEqual(['index', ...courses.map(([course]) => course)]);
    let sections = 0;
    let chapters = 0;
    for (const [course, title, count] of courses) {
      const folders = chapterFolders(course);
      const meta = JSON.parse(readFileSync(join(docsRoot, course, 'meta.json'), 'utf8'));
      expect(folders).toHaveLength(count);
      expect(meta.title).toBe(title);
      expect(meta.pages).toEqual(['index', ...folders]);
      expect(readdirSync(join(docsRoot, course)).filter((name) => name.endsWith('.mdx'))).toEqual(['index.mdx']);
      for (const folder of folders) {
        const files = readdirSync(join(docsRoot, course, folder)).filter((name) => name.endsWith('.mdx'));
        const children = files.filter((file) => file !== 'index.mdx').sort(compareMindMapPaths);
        const chapterMeta = JSON.parse(readFileSync(join(docsRoot, course, folder, 'meta.json'), 'utf8'));
        expect(files).toContain('index.mdx');
        expect(chapterMeta.pages).toEqual(['index', ...children.map((file) => file.replace(/\.mdx$/, ''))]);
        expect(chapterMeta.defaultOpen).toBe(false);
        expect(children.length).toBeGreaterThan(0);
        for (const file of children) expect(file).toMatch(new RegExp('^' + folder.slice(0, 2) + '-\\d+-'));
        const order = [...files].map((file) => folder + '/' + file).sort(compareMindMapPaths);
        expect(order[0]).toBe(folder + '/index.mdx');
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
      ...chapterFiles(course).map((file) => pageUrl(course, file)),
    ])]);
    const documents = readdirSync(docsRoot, { recursive: true }).filter((name) => typeof name === 'string' && name.endsWith('.mdx')) as string[];
    expect(documents).toHaveLength(433);
    for (const file of documents) {
      const document = readFileSync(join(docsRoot, file), 'utf8');
      for (const [, target] of document.matchAll(/\]\((\/docs\/408\/mind-maps[^)#]*)(?:#[^)]*)?\)/g)) {
        expect(pageUrls.has(target.replace(/\/$/, '')), file + ': ' + target).toBe(true);
      }
      for (const [, target] of document.matchAll(/href="(\/docs\/408\/mind-maps[^\"]*)"/g)) {
        expect(pageUrls.has(target.replace(/\/$/, '')), file + ': ' + target).toBe(true);
      }
      expect(document).not.toMatch(/\]\(\.\.?\//);
      expect(document).not.toContain('xmind:#');
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
    const report = JSON.parse(readFileSync(join(root, 'reports/408-mind-map-image-migration.json'), 'utf8'));
    const replacements = new Set<string>(report.placements.filter((entry: { asset: string; selectedAsset: string }) => entry.asset !== entry.selectedAsset).map((entry: { asset: string }) => entry.asset));
    const assets = readdirSync(assetRoot);
    expect(assets).toHaveLength(612);
    expect(referenced.size).toBe(497);
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

  it('keeps audited defective source figures superseded and chip diagrams portable', () => {
    const report = JSON.parse(readFileSync(join(root, 'reports/408-mind-map-image-migration.json'), 'utf8'));
    const redraws = ['ds-0133', 'ds-0176', 'ds-0064', 'ds-0152', 'ds-0206', 'ds-0003', 'ds-0078', 'ds-0209', 'ds-0025', 'ds-0161', 'ds-0052', 'co-0232', 'co-0178', 'co-0194', 'co-0089', 'co-0075', 'co-0238', 'os-0089', 'os-0105', 'os-0081', 'os-0093', 'os-0112'];
    for (const stem of redraws) {
      const entries = report.placements.filter((entry: { asset: string }) => entry.asset === stem + '.svg');
      expect(entries.length, stem).toBeGreaterThan(0);
      for (const entry of entries) expect(entry.selectedAsset, stem).not.toBe(entry.asset);
    }
    expect(readFileSync(join(assetRoot, 'co-0123.svg'), 'utf8')).toContain('>n-1</tspan>');
    for (const name of report.compatibilityRepairs) {
      const svg = readFileSync(join(assetRoot, name), 'utf8');
      expect(svg, name).not.toMatch(/font-size="[\d.]+%"/);
      expect(svg, name).toContain('<tspan');
    }
  });

  it('resolves every legacy section route to a canonical nested page without chains', () => {
    const routes = JSON.parse(readFileSync(join(root, 'lib/mind-map/legacy-routes.json'), 'utf8')) as Record<string, string>;
    const canonical = new Set(courses.flatMap(([course]) => chapterFiles(course).map((file) => pageUrl(course, file))));
    expect(Object.keys(routes)).toHaveLength(402);
    for (const [old, target] of Object.entries(routes)) {
      expect(canonical.has(old), old).toBe(false);
      expect(canonical.has(target), target).toBe(true);
      expect(routes[target]).toBeUndefined();
      expect(old.split('/').length + 1).toBe(target.split('/').length);
    }
  });

  it('retains the source audit and a real target for each primary XMind branch', () => {
    const report = JSON.parse(readFileSync(join(root, 'reports/408-source-audit.json'), 'utf8'));
    expect(report.sources).toHaveLength(4);
    expect(report.branches).toHaveLength(176);
    expect(report.summary.sourceImageReferences).toBe(911);
    for (const source of report.sources) {
      expect(source.zipCrcValid).toBe(true);
      expect(source.missingImageResources).toEqual([]);
    }
    for (const branch of report.branches) {
      expect(branch.targetSections.length).toBeGreaterThan(0);
      for (const target of branch.targetSections) expect(existsSync(join(docsRoot, target)), target).toBe(true);
    }
    for (const stale of report.sourceBrokenTopicLinks) expect(existsSync(join(docsRoot, stale.websiteTarget))).toBe(true);
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
