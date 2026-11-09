import { getMDXComponents } from '@/components/mdx';
import { MindMap, type MindMapProps } from '@/components/mdx/mind-map';
import { MindMapPageHeader } from '@/components/mdx/mind-map-page-header';
import { getPageMDXComponents } from '@/components/mdx/page-components';
import { WordCardsProvider } from '@/components/vocabulary/word-cards';
import { getContentSourceUrl } from '@/lib/site-config';
import { toCanonicalPagePath, toMarkdownPath } from '@/lib/site-url';
import { source } from '@/lib/source';
import { compareMindMapPaths } from '@/lib/mind-map/navigation';
import { shardStaticDocParams } from '@/lib/static-doc-shards';
import { statSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { createRelativeLink } from 'fumadocs-ui/mdx';
import {
  DocsBody,
  DocsDescription,
  DocsPage,
  DocsTitle,
  MarkdownCopyButton,
  PageLastUpdate,
  ViewOptionsPopover,
} from 'fumadocs-ui/layouts/spacious/page';

type PageParameters = {
  params: Promise<{
    slug?: string[];
  }>;
};

export const dynamicParams = false;

// https://nextjs.org/docs/app/api-reference/functions/generate-static-params
function getStaticDocBuildWeight(param: { slug?: string[] }) {
  const page = source.getPage(param.slug);
  if (!page) return 1;

  try {
    return statSync(resolve(process.cwd(), 'content/docs', page.path)).size;
  } catch {
    return 1;
  }
}

export function generateStaticParams() {
  const shardCount = Number.parseInt(process.env.STATIC_DOCS_SHARD_COUNT ?? '1', 10);
  const shardIndex = Number.parseInt(process.env.STATIC_DOCS_SHARD_INDEX ?? '0', 10);
  return shardStaticDocParams(
    source.generateParams(),
    shardCount,
    shardIndex,
    getStaticDocBuildWeight,
  );
}

type DocPage = NonNullable<ReturnType<typeof source.getPage>>;

/**
 * Where a mind-map page sits: its subject and chapter overviews, every map of
 * the chapter in reading order (overview first), the subject's chapters, and
 * the adjacent maps.
 */
function getMindMapNavigation(page: DocPage) {
  const pages = source.getPages();
  const folder = dirname(page.path);
  const toLink = (entry?: DocPage) =>
    entry ? { title: entry.data.title, url: entry.url } : undefined;
  const indexOf = (dir: string) =>
    pages.find((entry) => entry.path === `${dir}/index.mdx` || entry.path === `${dir}/index.md`);

  const siblings = pages
    .filter((entry) => dirname(entry.path) === folder && entry.data.layout === 'mind-map')
    .sort((a, b) => compareMindMapPaths(a.path, b.path));
  const index = siblings.findIndex((entry) => entry.url === page.url);
  const chapter = indexOf(folder);
  const chapterIsMap = chapter?.data.layout === 'mind-map';

  // A chapter folder's parent is the subject; its sibling folders are the other chapters.
  const subjectFolder = dirname(folder);
  const subject = subjectFolder !== '.' ? indexOf(subjectFolder) : undefined;
  const chapters = chapterIsMap
    ? pages
        .filter(
          (entry) =>
            entry.data.layout === 'mind-map' &&
            /(^|\/)index\.mdx?$/u.test(entry.path) &&
            dirname(dirname(entry.path)) === subjectFolder,
        )
        .sort((a, b) => compareMindMapPaths(a.path, b.path))
    : [];

  return {
    subject: toLink(chapterIsMap ? subject : chapter),
    chapter: chapterIsMap ? toLink(chapter) : undefined,
    sections: siblings.map((entry) => ({ title: entry.data.title, url: entry.url })),
    chapters: chapters.map((entry) => ({ title: entry.data.title, url: entry.url })),
    previous: toLink(siblings[index - 1]),
    next: toLink(siblings[index + 1]),
    position: index >= 0 && siblings.length > 1 ? { index: index + 1, total: siblings.length } : undefined,
  };
}

export default async function Page({ params }: PageParameters) {
  const { slug } = await params;
  const page = source.getPage(slug);
  if (!page) notFound();

  const data = await page.data.load();
  const MDX = data.body;
  const markdownUrl = toMarkdownPath(page.url);
  const isVocabularyPage = page.path.startsWith('english/vocabulary/');
  const isMindMapPage = page.data.layout === 'mind-map';
  const pageComponents = getPageMDXComponents(page.path);

  if (isMindMapPage) {
    const header = (
      <MindMapPageHeader title={page.data.title} {...getMindMapNavigation(page)} />
    );
    const PageMindMap = (props: MindMapProps) => (
      <MindMap {...props} variant="page" title={`${page.data.title}思维导图`} header={header} />
    );

    // The map is the page: no title block, table of contents or footer.
    return (
      <DocsPage
        toc={[]}
        full
        tableOfContent={{ enabled: false }}
        tableOfContentPopover={{ enabled: false }}
        footer={{ enabled: false }}
        className="mind-map-article"
      >
        <DocsBody id="docs-body" className="mind-map-page-body">
          <MDX
            components={getMDXComponents({
              ...pageComponents,
              a: createRelativeLink(source, page),
              MindMap: PageMindMap,
            })}
          />
        </DocsBody>
      </DocsPage>
    );
  }

  const useFullPage = Boolean(page.data.full) || isVocabularyPage;

  return (
    <DocsPage toc={data.toc} full={useFullPage}>
      <DocsTitle className="docs-page-title font-medium">{page.data.title}</DocsTitle>
      <DocsDescription className="mb-1 font-normal">
        {page.data.description}
      </DocsDescription>
      {data.lastModified && (
        <PageLastUpdate date={data.lastModified} className="mb-3 mt-1" />
      )}
      <div id="docs-page-actions" className="flex items-center gap-2 pb-4 pt-2">
        <MarkdownCopyButton
          markdownUrl={markdownUrl}
          className="docs-page-action"
        />
        <ViewOptionsPopover
          markdownUrl={markdownUrl}
          githubUrl={getContentSourceUrl(page.path)}
          className="docs-page-action"
        />
      </div>
      <WordCardsProvider>
        <DocsBody
          id="docs-body"
          className={`pb-10 pt-4${isVocabularyPage ? ' vocabulary-docs-body' : ''}`}
        >
          <MDX
            components={getMDXComponents({
              ...pageComponents,
              a: createRelativeLink(source, page),
            })}
          />
        </DocsBody>
      </WordCardsProvider>
    </DocsPage>
  );
}

export async function generateMetadata({
  params,
}: PageParameters): Promise<Metadata> {
  const { slug } = await params;
  const page = source.getPage(slug);
  if (!page) notFound();

  const canonical = toCanonicalPagePath(page.url);

  return {
    title: page.data.title,
    description: page.data.description,
    alternates: {
      canonical,
      types: { 'text/markdown': toMarkdownPath(page.url) },
    },
    openGraph: {
      type: 'article',
      url: canonical,
      title: page.data.title,
      description: page.data.description,
    },
  };
}
