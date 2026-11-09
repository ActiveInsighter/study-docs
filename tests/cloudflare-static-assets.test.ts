import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { describe, expect, it } from 'vitest';
// @ts-expect-error The deployment helper is intentionally a Node.js ESM script.
import {
  buildCloudflareAssetsIgnore,
  buildCloudflareHeaders,
  buildCloudflareRedirects,
  buildMindMapLegacyRedirects,
  canonicalizeAssetNames,
  CLOUDFLARE_DYNAMIC_REDIRECT_LIMIT,
  CLOUDFLARE_STATIC_REDIRECT_LIMIT,
} from '../scripts/prepare-cloudflare-static-assets.mjs';

describe('Cloudflare Workers Static Assets deployment', () => {
  it('preserves all 402 section bookmarks and Markdown links with exact 301s', () => {
    const routes = JSON.parse(readFileSync(resolve('lib/mind-map/legacy-routes.json'), 'utf8'));
    const legacy = buildMindMapLegacyRedirects(routes) as Array<{ source: string; destination: string }>;
    expect(legacy).toHaveLength(1206);
    expect(new Set(legacy.map((entry) => entry.source)).size).toBe(1206);
    const text = buildCloudflareRedirects([{ source: '/docs/*/index.txt', destination: '/docs/:splat/__next._full.txt' }], legacy);
    for (const [source, target] of Object.entries(routes)) {
      expect(text).toContain(`${source} ${target}/ 301\n`);
      expect(text).toContain(`${source}/ ${target}/ 301\n`);
      expect(text).toContain(`${source}.md ${target}.md 301\n`);
    }
    expect(text.indexOf(' 301\n')).toBeLessThan(text.indexOf(' 200\n'));
    expect(legacy.length).toBeLessThan(CLOUDFLARE_STATIC_REDIRECT_LIMIT);
  });

  it('rejects redirect chains, loops, wildcard aliases and oversized static lists', () => {
    const base = '/docs/408/mind-maps/data-structures/';
    expect(() => buildMindMapLegacyRedirects({ [base + 'a']: base + 'b', [base + 'b']: base + 'c' })).toThrow(/Invalid legacy/);
    expect(() => buildMindMapLegacyRedirects({ [base + 'a']: base + 'a' })).toThrow(/Invalid legacy/);
    expect(() => buildMindMapLegacyRedirects({ [base + '*']: base + 'a' })).toThrow(/Invalid legacy/);
    expect(() => buildCloudflareRedirects([{ source: '/docs/*/index.txt', destination: '/docs/:splat/__next._full.txt' }], Array.from({ length: 2001 }, () => ({ source: '/a', destination: '/b' })))).toThrow(/2000 static/);
  });

  it('uses an assets-only SSG configuration with canonical trailing-slash handling', () => {
    const config = JSON.parse(readFileSync(resolve('wrangler.jsonc'), 'utf8'));

    expect(config.name).toBe('study-docs');
    expect(config.main).toBeUndefined();
    expect(config.workers_dev).toBe(true);
    expect(config.routes).toEqual([
      { pattern: 'study-docs.any1.tech', custom_domain: true },
    ]);
    expect(config.assets).toEqual({
      directory: './.static-docs',
      not_found_handling: '404-page',
      html_handling: 'auto-trailing-slash',
    });
  });

  it('translates guarded EdgeOne RSC rewrites to Cloudflare 200 proxy rewrites', () => {
    const redirects = buildCloudflareRedirects([
      {
        source: '/docs/*/index.txt',
        destination: '/docs/:splat/__next._full.txt',
      },
      {
        source: '/docs/*/__next.docs.txt',
        destination: '/docs/__next.docs.txt',
      },
    ]);

    expect(redirects).toContain('/docs/*/index.txt /docs/:splat/__next._full.txt 200');
    expect(redirects).toContain('/docs/*/__next.docs.txt /docs/__next.docs.txt 200');

    const ruleLines = redirects
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 0 && !line.startsWith('#'));

    expect(ruleLines.every((line) => /\s200$/.test(line))).toBe(true);
  });


  it('keeps Cloudflare dynamic redirects within the documented limit', () => {
    expect(CLOUDFLARE_DYNAMIC_REDIRECT_LIMIT).toBe(100);
    const tooMany = Array.from({ length: 101 }, (_, index) => ({
      source: `/docs/path-${index}/*`,
      destination: `/docs/path-${index}/:splat`,
    }));

    expect(() => buildCloudflareRedirects(tooMany)).toThrow(/at most 100 dynamic/);
  });

  it('refuses unsupported multi-splat or external redirects', () => {
    expect(() =>
      buildCloudflareRedirects([
        { source: '/docs/*/nested/*', destination: '/docs/:splat' },
      ]),
    ).toThrow(/only one splat/);

    expect(() =>
      buildCloudflareRedirects([
        { source: '/docs/*', destination: 'https://example.com/:splat' },
      ]),
    ).toThrow(/stay on-site/);
  });

  it('forces direct Markdown responses to UTF-8', () => {
    const headers = buildCloudflareHeaders();

    expect(headers).toContain('/*.md');
    expect(headers).toContain('Content-Type: text/markdown; charset=utf-8');
  });

  it('excludes EdgeOne deployment metadata from Cloudflare asset upload', () => {
    expect(buildCloudflareAssetsIgnore()).toContain('\nedgeone.json\n');
  });

  it('renames $ segment payloads and rewrites both requested spellings with 200s', async () => {
    const root = mkdtempSync(join(tmpdir(), 'cf-assets-'));
    try {
      const page = '__next.docs.$oc$slug.__PAGE__.txt';
      for (const dir of ['docs', 'docs/408/mind-maps', 'docs/politics']) {
        mkdirSync(join(root, dir), { recursive: true });
        writeFileSync(join(root, dir, page), dir);
      }
      writeFileSync(join(root, '__next.!KGhvbWUp.__PAGE__.txt'), 'home');

      const { renamed, rewrites } = await canonicalizeAssetNames(root);
      expect(renamed).toBe(3);
      expect(existsSync(join(root, 'docs/408/mind-maps', page))).toBe(false);
      expect(readFileSync(join(root, 'docs/408/mind-maps/__next.docs.~oc~slug.__PAGE__.txt'), 'utf8')).toBe(
        'docs/408/mind-maps',
      );
      // `!` is already served as is and stays untouched.
      expect(existsSync(join(root, '__next.!KGhvbWUp.__PAGE__.txt'))).toBe(true);

      const redirects = buildCloudflareRedirects(rewrites);
      expect(redirects).toContain(
        '/docs/*/__next.docs.$oc$slug.__PAGE__.txt /docs/:splat/__next.docs.~oc~slug.__PAGE__.txt 200',
      );
      expect(redirects).toContain(
        '/docs/*/__next.docs.%24oc%24slug.__PAGE__.txt /docs/:splat/__next.docs.~oc~slug.__PAGE__.txt 200',
      );
      expect(redirects).toContain('/docs/__next.docs.$oc$slug.__PAGE__.txt /docs/__next.docs.~oc~slug.__PAGE__.txt 200');
      expect(rewrites).toHaveLength(4);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });
});
