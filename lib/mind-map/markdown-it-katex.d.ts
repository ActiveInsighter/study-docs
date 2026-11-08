// The published package points `types` at a file it does not ship.
declare module '@vscode/markdown-it-katex' {
  import type { KatexOptions } from 'katex';

  interface MarkdownItLike {
    use(plugin: unknown, options?: unknown): MarkdownItLike;
  }

  export interface MarkdownItKatexOptions extends KatexOptions {
    enableBareBlocks?: boolean;
    enableMathBlockInHtml?: boolean;
    enableMathInlineInHtml?: boolean;
    enableFencedBlocks?: boolean;
  }

  const markdownItKatex: (md: MarkdownItLike, options?: MarkdownItKatexOptions) => void;
  export default markdownItKatex;
}
