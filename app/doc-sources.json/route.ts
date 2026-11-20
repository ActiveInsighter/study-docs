import { androidMarkdownVersion } from '@/lib/markdown-export.mjs';
import { source } from '@/lib/source';
import type { Folder, Item, Node } from 'fumadocs-core/page-tree';

export const dynamic = 'force-static';

type SourcePage = { kind: 'page'; name: string; url: string };
type SourceFolder = { kind: 'folder'; name: string; children: SourceNode[] };
type SourceNode = SourcePage | SourceFolder;

function pageOf(page: Item): SourcePage {
  const url = decodeURI(page.url).replace(/\/+$/u, '');
  return {
    kind: 'page',
    name: typeof page.name === 'string' ? page.name : url.split('/').at(-1) ?? url,
    url,
  };
}

function folderOf(node: Folder): SourceFolder {
  const children = node.index ? [pageOf(node.index), ...childrenOf(node.children)] : childrenOf(node.children);
  return { kind: 'folder', name: typeof node.name === 'string' ? node.name : '未命名目录', children };
}

function childrenOf(nodes: Node[]): SourceNode[] {
  const children: SourceNode[] = [];
  for (const node of nodes) {
    if (node.type === 'folder') children.push(folderOf(node));
    else if (node.type === 'page' && !node.external) children.push(pageOf(node));
  }
  return children;
}

export function GET() {
  const children = childrenOf(source.getPageTree().children);
  const modules = children.filter((node): node is SourceFolder => node.kind === 'folder');
  const loosePages = children.filter((node) => node.kind === 'page');
  if (loosePages.length) modules.push({ kind: 'folder', name: '其他', children: loosePages });
  return Response.json({ androidMarkdownVersion, modules });
}
