import { copyFile, readdir, readFile, rename, stat, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const CLOUDFLARE_DYNAMIC_REDIRECT_LIMIT = 100;

function countSplats(value) {
  return (value.match(/\*/g) ?? []).length;
}

export function buildCloudflareRedirects(rewrites) {
  if (!Array.isArray(rewrites) || rewrites.length === 0) {
    throw new Error('Expected at least one EdgeOne rewrite to translate for Cloudflare.');
  }
  if (rewrites.length > CLOUDFLARE_DYNAMIC_REDIRECT_LIMIT) {
    throw new Error(
      `Cloudflare Static Assets supports at most ${CLOUDFLARE_DYNAMIC_REDIRECT_LIMIT} dynamic _redirects rules; got ${rewrites.length}.`,
    );
  }

  const lines = [
    '# Generated from .static-docs/edgeone.json by scripts/prepare-cloudflare-static-assets.mjs.',
    '# HTTP 200 rules are internal proxy rewrites: the browser URL stays unchanged.',
  ];

  for (const rewrite of rewrites) {
    const source = rewrite?.source;
    const destination = rewrite?.destination;
    if (typeof source !== 'string' || typeof destination !== 'string') {
      throw new Error(`Invalid rewrite entry: ${JSON.stringify(rewrite)}`);
    }
    if (!source.startsWith('/') || !destination.startsWith('/')) {
      throw new Error(`Cloudflare redirects must stay on-site: ${source} -> ${destination}`);
    }
    if (countSplats(source) > 1) {
      throw new Error(`Cloudflare _redirects supports only one splat per source: ${source}`);
    }
    lines.push(`${source} ${destination} 200`);
  }

  return `${lines.join('\n')}\n`;
}

export function buildCloudflareHeaders() {
  return [
    '# Explicit UTF-8 charset for direct Markdown views served by Workers Static Assets.',
    '/*.md',
    '  Content-Type: text/markdown; charset=utf-8',
    '',
  ].join('\n');
}

export function buildCloudflareAssetsIgnore() {
  return [
    '# EdgeOne deployment metadata is not a public Cloudflare asset.',
    'edgeone.json',
    '',
  ].join('\n');
}

/**
 * Characters Next.js puts in segment-prefetch file names that Workers Static
 * Assets serves only under another spelling. The Next client requests
 * `__next.docs.$oc$slug.__PAGE__.txt` with a literal `$`, and the asset server
 * answers 307 → `%24`, so every prefetch paid an extra round trip.
 */
const NON_CANONICAL_NAME_CHARACTER = '$';
const CANONICAL_REPLACEMENT = '~';

async function listFiles(directory, prefix = '') {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
    if (entry.isDirectory()) files.push(...(await listFiles(path.join(directory, entry.name), relative)));
    else if (entry.isFile()) files.push(relative);
  }
  return files;
}

/**
 * Rename `$` in file names to `~` (unreserved, so never redirected) and return
 * 200 rewrites from the spellings clients request: one splat rule per top-level
 * directory and file name, plus exact rules for files directly inside it.
 */
export async function canonicalizeAssetNames(outputRoot) {
  const rewrites = new Map();
  let renamed = 0;
  const addRewrite = (source, destination) => {
    for (const spelling of [source, source.replaceAll('$', '%24')]) {
      rewrites.set(spelling, { source: spelling, destination });
    }
  };

  for (const relative of await listFiles(outputRoot)) {
    const name = path.posix.basename(relative);
    if (!name.includes(NON_CANONICAL_NAME_CHARACTER)) continue;

    const canonicalName = name.replaceAll(NON_CANONICAL_NAME_CHARACTER, CANONICAL_REPLACEMENT);
    const directory = path.posix.dirname(relative);
    const target = path.join(outputRoot, directory, canonicalName);
    try {
      await stat(target);
      throw new Error(`Cannot rename ${relative}: ${directory}/${canonicalName} already exists.`);
    } catch (error) {
      if (error?.code !== 'ENOENT') throw error;
    }
    await rename(path.join(outputRoot, relative), target);
    renamed++;

    const [top, ...rest] = directory === '.' ? [] : directory.split('/');
    if (!top) {
      addRewrite(`/${name}`, `/${canonicalName}`);
    } else if (rest.length === 0) {
      addRewrite(`/${top}/${name}`, `/${top}/${canonicalName}`);
    } else {
      addRewrite(`/${top}/*/${name}`, `/${top}/:splat/${canonicalName}`);
    }
  }

  return { renamed, rewrites: [...rewrites.values()] };
}

async function ensureRootIndex(outputRoot) {
  const rootIndexPath = path.join(outputRoot, 'index.html');

  try {
    await stat(rootIndexPath);
    return false;
  } catch {
    const docsIndexPath = path.join(outputRoot, 'docs', 'index.html');
    await stat(docsIndexPath);
    await copyFile(docsIndexPath, rootIndexPath);
    return true;
  }
}

export async function prepareCloudflareStaticAssets(outputRoot = path.resolve('.static-docs')) {
  const edgeOneConfigPath = path.join(outputRoot, 'edgeone.json');
  const redirectsPath = path.join(outputRoot, '_redirects');
  const assetsIgnorePath = path.join(outputRoot, '.assetsignore');
  const headersPath = path.join(outputRoot, '_headers');
  const notFoundPath = path.join(outputRoot, '404.html');

  const edgeOneConfig = JSON.parse(await readFile(edgeOneConfigPath, 'utf8'));
  const canonicalNames = await canonicalizeAssetNames(outputRoot);
  const redirects = buildCloudflareRedirects([...edgeOneConfig.rewrites, ...canonicalNames.rewrites]);

  await stat(notFoundPath);
  const restoredRootIndex = await ensureRootIndex(outputRoot);
  await Promise.all([
    writeFile(redirectsPath, redirects, 'utf8'),
    writeFile(assetsIgnorePath, buildCloudflareAssetsIgnore(), 'utf8'),
    writeFile(headersPath, buildCloudflareHeaders(), 'utf8'),
  ]);

  console.log(`[cloudflare-assets] Wrote ${redirectsPath}.`);
  console.log(`[cloudflare-assets] Wrote ${headersPath} with UTF-8 Markdown Content-Type.`);
  console.log('[cloudflare-assets] Translated EdgeOne RSC rewrites to Cloudflare 200 proxy rewrites.');
  console.log(
    `[cloudflare-assets] Renamed ${canonicalNames.renamed} files with '$' in their names; added ${canonicalNames.rewrites.length} rewrites for their requested spellings.`,
  );
  console.log('[cloudflare-assets] Confirmed 404.html for not_found_handling=404-page.');
  if (restoredRootIndex) {
    console.log('[cloudflare-assets] Restored missing root index.html from docs/index.html.');
  } else {
    console.log('[cloudflare-assets] Confirmed root index.html exists.');
  }
}

const isDirectRun =
  process.argv[1] && path.resolve(process.argv[1]) === path.resolve(fileURLToPath(import.meta.url));

if (isDirectRun) {
  await prepareCloudflareStaticAssets();
}
