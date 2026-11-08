import markdownItKatex from '@vscode/markdown-it-katex';
import katex from 'katex';
import { Transformer, builtInPlugins } from 'markmap-lib';

export type MindMapNode = ReturnType<Transformer['transform']>['root'];

/**
 * Markmap plugins used at build time.
 *
 * - `frontmatter`, `hljs` and `checkbox` are the official plugins.
 * - `katex` is replaced by the same markdown-it plugin markmap uses, configured
 *   like the site's rehype-katex: HTML-only output, the project's KaTeX version
 *   and no warnings for CJK text in math mode. The site already loads the
 *   KaTeX stylesheet and fonts, so no CDN assets are needed in the browser.
 * - `sourceLines` and `npmUrl` only serve editors / CDN asset loading.
 */
const katexPlugin = {
  name: 'katex',
  transform(hooks: Transformer['hooks']) {
    hooks.parser.tap((md) => {
      md.use(markdownItKatex, {
        katex,
        output: 'html',
        strict: 'ignore',
        throwOnError: false,
      });
    });
    return {};
  },
};

const plugins = [
  ...builtInPlugins.filter((plugin) =>
    ['frontmatter', 'hljs', 'checkbox'].includes(plugin.name),
  ),
  katexPlugin,
] as ConstructorParameters<typeof Transformer>[0];

let transformer: Transformer | undefined;

function getTransformer() {
  transformer ??= new Transformer(plugins);
  return transformer;
}

// markmap's HTML parser escapes every non-ASCII character as a numeric entity,
// which inflates Chinese text roughly eightfold. Characters outside the HTML
// syntax set are safe to restore verbatim.
function restoreEntities(html: string) {
  return html.replace(/&#x([0-9a-f]+);/gi, (entity, hex: string) => {
    const codePoint = Number.parseInt(hex, 16);
    return codePoint >= 0xa0 ? String.fromCodePoint(codePoint) : entity;
  });
}

const IMAGE_TAG = /<img\b([^>]*)>/gi;

// Images live inside SVG <foreignObject>, where native lazy loading is
// unreliable; markmap only renders nodes that are expanded anyway.
function normalizeImages(html: string) {
  return html.replace(IMAGE_TAG, (_tag, attributes: string) => {
    let next = attributes.replace(/\s+loading="[^"]*"/i, '');
    if (!/\sdecoding=/i.test(next)) next += ' decoding="async"';
    return `<img${next}>`;
  });
}

function compactNode(node: MindMapNode): MindMapNode {
  const payload = node.payload ? { ...node.payload } : undefined;
  if (payload) delete payload.lines;

  return {
    content: normalizeImages(restoreEntities(node.content)).trim(),
    children: node.children.map(compactNode),
    ...(payload && Object.keys(payload).length > 0 ? { payload } : {}),
  };
}

/** Convert mind-map Markdown into markmap's node tree (build time). */
export function transformMindMapMarkdown(markdown: string): MindMapNode {
  const { root } = getTransformer().transform(markdown.trim());
  return compactNode(root);
}
