import clsx from 'clsx';
import { ArrowUpRight } from 'lucide-react';
import type { ReactNode } from 'react';
import { IntentLink as Link } from '@/components/intent-link';
import type { StudyHomeData } from '@/lib/home/catalog.server';
import { specimens } from '@/lib/home/content';
import { BinarySearch } from './binary-search';
import home from './home.module.css';
import { RecallList } from './recall-list';
import styles from './specimens.module.css';
import { TaylorPlot } from './taylor-plot';
import { WordDeck } from './word-deck';

/*
 * One live sample of each kind of material the notes contain, each taken from
 * a real page and linking back to it. Tiles differ in shape on purpose: each
 * is sized for its specimen, not stamped from one card template.
 */

function Tile({
  data,
  module,
  area,
  title,
  links,
  children,
}: {
  data: StudyHomeData;
  module: string;
  area: string;
  title: string;
  links: { href: string; label: string }[];
  children: ReactNode;
}) {
  const owner = data.modules.find((candidate) => candidate.key === module);
  return (
    <article className={clsx(home.tone, styles.tile)} data-tone={owner?.tone ?? 'blue'} data-area={area}>
      <header className={styles.tileHead}>
        <span className={styles.tag}>{owner?.name ?? module}</span>
        <h3 className={styles.tileTitle}>{title}</h3>
      </header>
      <div className={styles.tileBody}>{children}</div>
      <footer className={styles.tileFoot}>
        {links.map((link) => (
          <Link key={link.href + link.label} href={link.href} className={styles.tileLink}>
            {link.label}
            <ArrowUpRight aria-hidden="true" />
          </Link>
        ))}
      </footer>
    </article>
  );
}

export function Specimens({ data }: { data: StudyHomeData }) {
  return (
    <section className={styles.section} aria-labelledby="specimens-title">
      <div className={home.sectionHead}>
        <h2 id="specimens-title" className={home.sectionTitle}>
          笔记里不只有文字
        </h2>
        <p className={home.sectionNote}>公式能拖动，词卡能翻面，答案能遮住，算法能单步执行。下面每一块都取自站内真实页面。</p>
      </div>
      <div className={styles.grid}>
        <Tile
          data={data}
          module={specimens.math.module}
          area="math"
          title={specimens.math.title}
          links={[
            { href: data.links.formulas, label: '公式手册' },
            { href: data.links.plots, label: '数学图像' },
          ]}
        >
          <TaylorPlot formulaHtml={data.formulaHtml} />
        </Tile>
        {data.words.length > 0 && (
          <Tile
            data={data}
            module={specimens.english.module}
            area="english"
            title={specimens.english.title}
            links={[{ href: data.links.vocabulary, label: '考研词卡' }]}
          >
            <WordDeck words={data.words} />
          </Tile>
        )}
        <Tile
          data={data}
          module={specimens.politics.module}
          area="politics"
          title={specimens.politics.title}
          links={[{ href: data.links.recall, label: '帽子题背诵版' }]}
        >
          <RecallList items={specimens.politics.items} />
        </Tile>
        <Tile
          data={data}
          module={specimens.algorithm.module}
          area="algorithm"
          title={specimens.algorithm.title}
          links={[{ href: data.links.algorithm, label: '二分查找' }]}
        >
          <BinarySearch nums={specimens.algorithm.nums} target={specimens.algorithm.target} />
        </Tile>
      </div>
    </section>
  );
}
