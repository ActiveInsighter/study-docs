import clsx from 'clsx';
import { ArrowRight } from 'lucide-react';
import { IntentLink as Link } from '@/components/intent-link';
import type { StudyHomeData } from '@/lib/home/catalog.server';
import styles from './hero.module.css';
import home from './home.module.css';
import { MindMap } from './mind-map';
import { MapOutline } from './map-outline';
import { SearchButton } from './search-button';

const numberFormat = new Intl.NumberFormat('zh-CN');

export function Hero({ data }: { data: StudyHomeData }) {
  const start = data.modules[0]?.href ?? '/docs/';

  return (
    <section className={styles.hero} aria-labelledby="home-title">
      <div className={styles.intro}>
        <h1 id="home-title" className={styles.title}>
          把零散的知识，
          <br />
          画成一张图。
        </h1>
        <div className={styles.side}>
          <p className={styles.lead}>
            政治、英语、数学、408 和算法的笔记、公式、词卡与思维导图，按章节整理在一处。下面这张图就是目录，点任意一支直接进入。
          </p>
          <div className={styles.actions}>
            <Link href={start} className={clsx(home.button, home.buttonPrimary)}>
              开始复习
              <ArrowRight aria-hidden="true" />
            </Link>
            <SearchButton className={clsx(home.button, home.buttonGhost)} kbdClassName={home.kbd} />
          </div>
        </div>
      </div>

      <div className={styles.board}>
        <div className={styles.boardBar}>
          <span className={styles.boardTitle}>学习目录</span>
          <dl className={styles.stats}>
            <div>
              <dt>科目</dt>
              <dd>{data.modules.length}</dd>
            </div>
            <div>
              <dt>专题</dt>
              <dd>{numberFormat.format(data.totals.sections)}</dd>
            </div>
            <div>
              <dt>篇笔记</dt>
              <dd>{numberFormat.format(data.totals.pages)}</dd>
            </div>
          </dl>
        </div>
        <MindMap layout={data.map} rootLabel="考研学习" />
        <MapOutline layout={data.map} rootLabel="考研学习" />
      </div>
    </section>
  );
}
