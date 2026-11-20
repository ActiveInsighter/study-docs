import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { fromMarkdown } from 'mdast-util-from-markdown';
import { mdxFromMarkdown } from 'mdast-util-mdx';
import { mdxjs } from 'micromark-extension-mdxjs';
import { exportQuestionMarkdown } from './question-markdown.mjs';

export function splitFrontmatter(content) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/.exec(content);
  if (!match) return { frontmatter: '', body: content };

  return { frontmatter: match[1], body: content.slice(match[0].length) };
}

export function parseFrontmatterTitle(frontmatter) {
  const match = /^title:\s*(.+)$/m.exec(frontmatter);
  if (!match) return null;

  return match[1].trim().replace(/^["']|["']$/g, '').trim();
}

function countUnbalancedDelimiters(text) {
  let depth = 0;
  for (const character of text) {
    if (character === '{' || character === '(' || character === '[') depth += 1;
    if (character === '}' || character === ')' || character === ']') depth -= 1;
  }
  return depth;
}

const JSX_OPEN_TAG = /^<([A-Z][\w.-]*)((?:\s[^<>]*)?)\/?>/;
const JSX_CLOSE_TAG = /^<\/[A-Z][\w.-]*>/;
const JSX_TRAILING_CLOSE_TAGS = /(?:\s*<\/[A-Z][\w.-]*>)+\s*$/;
const JSX_COMMENT_LINE = /^\{\/\*.*\*\/\}$/;
// Labels keep question structure readable once the wrapper tags are gone.
const JSX_LABELS = new Map([
  ['ExamAnswer', '答案：'],
  ['ExamExplanation', '解析：'],
]);

function isJsxComponentLine(trimmedLine) {
  return /^<\/?[A-Z][\w.-]*(\s|>|\/>)/.test(trimmedLine);
}

/**
 * Scan JSX tag text for the `>` that closes the opening tag, skipping quoted
 * strings and `{...}` attribute expressions. Returns the scanner state so a
 * tag whose attributes span several lines can be followed line by line.
 */
function scanJsxTag(text, state = { depth: 0, quote: null }) {
  for (let index = 0; index < text.length; index += 1) {
    const character = text[index];
    if (state.quote) {
      if (character === state.quote) state.quote = null;
      continue;
    }
    if (character === '"' || character === "'" || character === '`') state.quote = character;
    else if (character === '{') state.depth += 1;
    else if (character === '}') state.depth -= 1;
    else if (character === '>' && state.depth === 0) return { ...state, closed: true };
  }
  return { ...state, closed: false };
}

function getJsxAttribute(attributes, name) {
  const match = new RegExp(`\\b${name}=(?:"([^"]*)"|'([^']*)')`).exec(attributes);
  return match ? (match[1] ?? match[2]) : undefined;
}

/**
 * Turn a line that starts with a JSX component tag into plain markdown.
 * Wrapper tags are dropped but the text between them is kept, so
 * `<ExamOption>A. foo</ExamOption>` becomes `A. foo`.
 */
function unwrapJsxComponentLine(trimmedLine) {
  let rest = trimmedLine;
  let label;

  for (;;) {
    const close = JSX_CLOSE_TAG.exec(rest);
    if (close) {
      rest = rest.slice(close[0].length).trimStart();
      continue;
    }

    const open = JSX_OPEN_TAG.exec(rest);
    if (!open) break;

    const [tag, name, attributes] = open;
    if (!tag.endsWith('/>')) {
      label ??=
        JSX_LABELS.get(name) ??
        getJsxAttribute(attributes, 'title') ??
        (name === 'Tab' ? getJsxAttribute(attributes, 'value') : undefined);
    }
    rest = rest.slice(tag.length).trimStart();
  }

  // A tag we cannot parse on one line (for example attributes spread over
  // several lines) is dropped, matching the previous behaviour.
  if (/^<\/?[A-Z]/.test(rest)) return [];

  const text = rest.replace(JSX_TRAILING_CLOSE_TAGS, '').trim();
  if (label) return [text ? `**${label}** ${text}` : `**${label}**`];
  return text ? [text] : [];
}

const vocabularyFiles = {
  kaoyanWords: ['01-core', '02-advanced', '03-expanded', '04-foundation']
    .map((name) => `kaoyan-source/${name}.json`),
  phraseWords: ['phrase-source/kaoyan-phrases.json'],
  supplementalWords: ['supplemental-source/other-frequency.json'],
};
const vocabularyCache = new Map();

function loadVocabulary(name) {
  if (!Object.hasOwn(vocabularyFiles, name)) {
    throw new Error(`Unknown WordCards vocabulary: ${name}`);
  }
  if (!vocabularyCache.has(name)) {
    const directories = [
      path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../data/vocabulary'),
      path.resolve('data/vocabulary'),
    ];
    const files = vocabularyFiles[name];
    const directory = directories.find((base) =>
      files.every((file) => fs.existsSync(path.join(base, file))),
    );
    if (!directory) throw new Error(`Missing vocabulary files for ${name}`);
    vocabularyCache.set(name, files.flatMap((file) =>
      JSON.parse(fs.readFileSync(path.join(directory, file), 'utf8')),
    ));
  }
  return vocabularyCache.get(name);
}

// Decode inline vocabulary as data. MDX expressions are parsed and never executed.
function readWordCardLiteral(node) {
  switch (node?.type) {
    case 'Literal':
      if (node.value === null || ['string', 'number', 'boolean'].includes(typeof node.value)) return node.value;
      break;
    case 'ArrayExpression':
      return node.elements.map(readWordCardLiteral);
    case 'ObjectExpression':
      return Object.fromEntries(node.properties.map((property) => {
        if (property.type !== 'Property' || property.kind !== 'init' || property.computed) {
          throw new Error('WordCards objects require literal properties.');
        }
        const key = property.key.type === 'Identifier' ? property.key.name : readWordCardLiteral(property.key);
        return [key, readWordCardLiteral(property.value)];
      }));
  }
  throw new Error(`Unsupported WordCards expression: ${node?.type ?? 'missing'}`);
}

function readWordCards(tag) {
  const [element] = fromMarkdown(tag, {
    extensions: [mdxjs()],
    mdastExtensions: [mdxFromMarkdown()],
  }).children;
  const prop = element.attributes?.find((attribute) => attribute.name === 'words');
  const expression = prop?.value?.data?.estree?.body[0]?.expression;
  if (expression?.type === 'Identifier') return loadVocabulary(expression.name);
  if (expression?.type === 'CallExpression' && expression.callee.type === 'MemberExpression'
    && !expression.callee.computed && expression.callee.property.name === 'slice'
    && expression.callee.object.type === 'Identifier') {
    const bounds = expression.arguments.map(readWordCardLiteral);
    if (bounds.length <= 2 && bounds.every(Number.isInteger)) {
      return loadVocabulary(expression.callee.object.name).slice(...bounds);
    }
  }
  if (expression?.type === 'ArrayExpression') return readWordCardLiteral(expression);
  throw new Error('WordCards requires inline entries or a vocabulary slice.');
}

function renderWordCards(tag, android) {
  const words = readWordCards(tag);
  if (!words.length) return '';
  if (android) {
    return `\n\n:::wordcards\n\`\`\`json\n${JSON.stringify(words)}\n\`\`\`\n:::\n\n`;
  }
  const lines = words.map((entry) => {
    const phonetic = entry.phonetic ? ` \`${entry.phonetic}\`` : '';
    const meanings = (entry.meanings ?? [])
      .map((meaning) => `${meaning.pos ? `*${meaning.pos}* ` : ''}${meaning.text}`)
      .join('；');
    return `- **${entry.word}**${phonetic}${meanings ? ` — ${meanings}` : ''}`;
  });
  return `\n\n${lines.join('\n')}\n\n`;
}

/**
 * Remove MDX module syntax (import/export statements), JSX comments and
 * component wrapper tags while preserving markdown content, math delimiters,
 * text nested inside components, and fenced code blocks untouched.
 */
export function stripMdxRuntimeSyntax(body, options) {
  const lines = exportQuestionMarkdown(body, { ...options, renderWordCards }).split(/\r?\n/);
  const kept = [];
  let codeFence = null;
  let statementDepth = 0;
  // Scanner state while inside an opening tag whose attributes span lines.
  let openTag = null;

  for (const line of lines) {
    const trimmed = line.trim();

    if (openTag) {
      const state = scanJsxTag(line, openTag);
      openTag = state.closed ? null : state;
      continue;
    }

    const fence = /^ {0,3}(`{3,}|~{3,})(.*)/.exec(line);
    if (codeFence) {
      if (fence && fence[1][0] === codeFence[0] && fence[1].length >= codeFence.length && !fence[2].trim()) codeFence = null;
      kept.push(line);
      continue;
    }
    if (fence) {
      codeFence = fence[1];
      kept.push(line);
      continue;
    }
    // Component expansion adds paragraph boundaries; avoid excessive blank lines.
    if (!trimmed && kept.at(-1)?.trim() === '') continue;

    if (statementDepth > 0) {
      statementDepth += countUnbalancedDelimiters(line);
      if (statementDepth <= 0) statementDepth = 0;
      continue;
    }

    if (/^(import|export)[\s{(]/.test(trimmed)) {
      statementDepth = countUnbalancedDelimiters(line);
      continue;
    }

    if (JSX_COMMENT_LINE.test(trimmed)) continue;

    // `<MathPlot2D` followed by attributes on later lines: drop the whole tag.
    if (/^<[A-Z][\w.-]*(\s|$)/.test(trimmed)) {
      const state = scanJsxTag(trimmed.slice(1));
      if (!state.closed) {
        openTag = state;
        continue;
      }
    }

    if (isJsxComponentLine(trimmed)) {
      kept.push(...unwrapJsxComponentLine(trimmed));
      continue;
    }

    // Multi-line components close at the end of their last text line.
    kept.push(trimmed.endsWith('>') ? line.replace(JSX_TRAILING_CLOSE_TAGS, '') : line);
  }

  return kept.join('\n');
}

/**
 * Render a source document as standalone Markdown, shared by static downloads
 * and the LLM route through `lib/get-llm-text.ts`.
 */
export async function renderStaticMarkdown(content, { title, url }) {
  const { body } = splitFrontmatter(content);
  const cleanedBody = stripMdxRuntimeSyntax(body).trim();

  return `# ${title} (${url})\n\n${cleanedBody}\n`;
}


/** Android reader format v1. Containers carry semantic component names. */
export const androidMarkdownVersion = 1;

function resolveAndroidDocLink(link, sourcePath) {
  if (!/^\.{1,2}\//u.test(link)) return link;
  const [, pathname, suffix] = /^([^?#]+)(.*)$/u.exec(link);
  let decodedPath;
  try {
    decodedPath = decodeURI(pathname);
  } catch {
    return link;
  }
  const sourceDirectory = path.posix.dirname(sourcePath.replace(/^\/+/, ''));
  const resolved = path.posix.resolve('/docs', sourceDirectory, decodedPath);
  if (resolved === '/docs') return '/docs' + suffix;
  if (!resolved.startsWith('/docs/')) return link;

  const slug = resolved.slice('/docs/'.length).replace(/\.(md|mdx)$/iu, '').replace(/(^|\/)index$/iu, '');
  const encoded = slug.split('/').filter(Boolean).map(encodeURIComponent).join('/');
  return `/docs${encoded ? `/${encoded}` : ''}${suffix}`;
}

export function renderAndroidMarkdown(content, { title, sourcePath }) {
  const { body } = splitFrontmatter(content);
  const cleanedBody = stripMdxRuntimeSyntax(body, {
    android: true,
    resolveLink: sourcePath ? (link) => resolveAndroidDocLink(link, sourcePath) : undefined,
  }).trim();
  if (/^#\s/u.test(cleanedBody)) return `${cleanedBody}\n`;
  return `# ${title}${cleanedBody ? `\n\n${cleanedBody}` : ''}\n`;
}
