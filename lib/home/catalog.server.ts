import { readdirSync, readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import type * as PageTree from 'fumadocs-core/page-tree';
import katex from 'katex';
import type { WordCardData } from '@/components/vocabulary/model';
import { source } from '@/lib/source';
import { moduleTones, specimens, TONES, type Tone } from './content';
import { layoutMindMap, type MindMapLayout } from './mind-map-layout';
import type { StudyModule, WordCard } from './types';

/*
 * Everything the home page derives from the documentation, computed once at
 * build time: the study modules and their sections (the sidebar's own page
 * tree), the mind-map layout, the URLs the specimens link to, and the real
 * excerpts they show. Server components render it; client islands receive
 * only plain, small slices.
 */

export interface StudyHomeData {
  modules: StudyModule[];
  totals: { pages: number; sections: number };
  map: MindMapLayout;
  links: {
    formulas: string;
    plots: string;
    vocabulary: string;
    recall: string;
    algorithm: string;
  };
  formulaHtml: string;
  words: WordCard[];
}

/** Links keep the trailing slash the static export serves directly. */
export function withTrailingSlash(url: string): string {
  return url.endsWith('/') ? url : `${url}/`;
}

function textOf(name: PageTree.Node['name'], fallback: string): string {
  return typeof name === 'string' && name.trim() ? name.trim() : fallback;
}

function countPages(folder: PageTree.Folder): number {
  let pages = folder.index ? 1 : 0;
  for (const child of folder.children) {
    if (child.type === 'page' && !child.external) pages += 1;
    else if (child.type === 'folder') pages += countPages(child);
  }
  return pages;
}

function firstUrl(folder: PageTree.Folder): string | null {
  if (folder.index) return folder.index.url;
  for (const child of folder.children) {
    if (child.type === 'page' && !child.external) return child.url;
    if (child.type === 'folder') {
      const url = firstUrl(child);
      if (url) return url;
    }
  }
  return null;
}

function toneOf(key: string, used: Set<Tone>): Tone {
  const tone = moduleTones[key] ?? TONES.find((candidate) => !used.has(candidate)) ?? 'blue';
  used.add(tone);
  return tone;
}

function loadModules(): StudyModule[] {
  const used = new Set<Tone>();
  return source.getPageTree().children.flatMap((node): StudyModule[] => {
    if (node.type !== 'folder') return [];
    const href = firstUrl(node);
    if (!href) return [];
    const key = node.$ref?.folder ?? href.split('/').filter(Boolean).at(-1) ?? 'module';
    const sections = node.children.flatMap((child) => {
      if (child.type !== 'folder') return [];
      const url = firstUrl(child);
      return url ? [{ name: textOf(child.name, url), href: withTrailingSlash(url), pages: countPages(child) }] : [];
    });
    return [
      {
        key,
        name: textOf(node.name, key),
        href: withTrailingSlash(href),
        tone: toneOf(key, used),
        pages: countPages(node),
        sections,
      },
    ];
  });
}

function pageUrl(file: string, fallback: string): string {
  const page = source.getPages().find((candidate) => candidate.path === file);
  if (!page) console.warn(`[home] ${file} is not a documentation page; linking to ${fallback} instead.`);
  return withTrailingSlash(page?.url ?? fallback);
}

/** The requested cards, read from the vocabulary source files (never bundled into the page). */
function loadWords(words: readonly string[]): WordCard[] {
  const directory = resolve(process.cwd(), 'data/vocabulary/kaoyan-source');
  const wanted = new Map<string, WordCard>();
  let files: string[] = [];
  try {
    files = readdirSync(directory).filter((file) => file.endsWith('.json')).sort();
  } catch {
    console.warn('[home] Vocabulary source is missing; the word-card specimen is left out.');
  }
  for (const file of files) {
    if (wanted.size === words.length) break;
    const cards = JSON.parse(readFileSync(join(directory, file), 'utf8')) as WordCardData[];
    for (const card of cards) {
      if (!words.includes(card.word) || wanted.has(card.word)) continue;
      const example = card.senses?.find((sense) => sense.examples?.length)?.examples?.[0] ?? null;
      wanted.set(card.word, {
        word: card.word,
        phonetic: card.phonetic ?? '',
        label: card.label ?? '',
        meanings: card.meanings.slice(0, 3).map((meaning) => ({ pos: meaning.pos ?? '', text: meaning.text })),
        example: example ? { text: example.text, translation: example.translation } : null,
      });
    }
  }
  return words.flatMap((word) => wanted.get(word) ?? []);
}

let cached: StudyHomeData | undefined;

export function getStudyHomeData(): StudyHomeData {
  if (cached) return cached;
  const modules = loadModules();
  const hrefOf = (key: string) => modules.find((module) => module.key === key)?.href ?? '/docs/';
  cached = {
    modules,
    totals: {
      pages: modules.reduce((sum, module) => sum + module.pages, 0),
      sections: modules.reduce((sum, module) => sum + module.sections.length, 0),
    },
    map: layoutMindMap(modules),
    links: {
      formulas: pageUrl(specimens.math.formulaFile, hrefOf('math')),
      plots: pageUrl(specimens.math.plotFile, hrefOf('math')),
      vocabulary: pageUrl(specimens.english.file, hrefOf('english')),
      recall: pageUrl(specimens.politics.file, hrefOf('politics')),
      algorithm: pageUrl(specimens.algorithm.file, hrefOf('algorithm')),
    },
    formulaHtml: katex.renderToString(specimens.math.formula, {
      displayMode: true,
      throwOnError: false,
      strict: 'ignore',
    }),
    words: loadWords(specimens.english.words),
  };
  return cached;
}
