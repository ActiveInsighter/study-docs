export interface SourcePage {
  kind: 'page';
  name: string;
  url: string;
  questions: number;
}

export interface SourceFolder {
  kind: 'folder';
  name: string;
  children: SourceNode[];
  questions: number;
}

export type SourceNode = SourcePage | SourceFolder;

export interface SourceTree {
  modules: SourceFolder[];
}

export const OTHER_MODULE = '其他';

export function normalizeDocPath(path: string): string {
  let decoded = path;
  try { decoded = decodeURI(path); } catch { /* keep raw path */ }
  const bare = decoded.split(/[?#]/u)[0] ?? decoded;
  return bare.replace(/\/+$/u, '') || '/';
}

export interface PageTreeLike {
  type?: string;
  name?: unknown;
  url?: string;
  external?: boolean;
  root?: boolean;
  index?: { name?: unknown; url: string } | null;
  children?: PageTreeLike[];
}

function textOf(name: unknown, fallback: string): string {
  if (typeof name === 'string' && name.trim()) return name.trim();
  if (typeof name === 'number') return String(name);
  return fallback;
}

function lastSegment(url: string) {
  return normalizeDocPath(url).split('/').filter(Boolean).at(-1) ?? url;
}

function folderOf(node: PageTreeLike, count: (url: string) => number): SourceFolder {
  const children: SourceNode[] = [];
  if (node.index?.url) {
    const url = normalizeDocPath(node.index.url);
    children.push({ kind: 'page', name: textOf(node.index.name, lastSegment(url)), url, questions: count(url) });
  }
  for (const child of node.children ?? []) {
    const converted = convert(child, count);
    if (converted) children.push(converted);
  }
  return {
    kind: 'folder',
    name: textOf(node.name, '未命名目录'),
    children,
    questions: children.reduce((sum, child) => sum + child.questions, 0),
  };
}

function convert(node: PageTreeLike, count: (url: string) => number): SourceNode | null {
  if (node.type === 'folder') return folderOf(node, count);
  if (node.type === 'page' && node.url && !node.external) {
    const url = normalizeDocPath(node.url);
    return { kind: 'page', name: textOf(node.name, lastSegment(url)), url, questions: count(url) };
  }
  return null;
}

export function buildSourceTree(root: PageTreeLike, count: (url: string) => number = () => 0): SourceTree {
  const modules: SourceFolder[] = [];
  const loose: SourceNode[] = [];
  for (const child of root.children ?? []) {
    const converted = convert(child, count);
    if (!converted) continue;
    if (converted.kind === 'folder') modules.push(converted);
    else loose.push(converted);
  }
  if (loose.length > 0) {
    modules.push({
      kind: 'folder',
      name: OTHER_MODULE,
      children: loose,
      questions: loose.reduce((sum, node) => sum + node.questions, 0),
    });
  }
  return { modules };
}

export function countQuestionsInMdx(raw: string): number {
  const matches = raw.match(/<Question\b/gu);
  return matches ? matches.length : 0;
}
