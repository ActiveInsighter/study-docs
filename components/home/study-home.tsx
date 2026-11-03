import { IntentLink as Link } from '@/components/intent-link';
import { getStudyHomeData } from '@/lib/home/catalog.server';
import { siteConfig } from '@/lib/site-config';
import { Hero } from './hero';
import home from './home.module.css';
import { Specimens } from './specimens';
import { TearCalendar } from './tear-calendar';

/*
 * Home page, composed on the server from build-time data:
 *
 *   Hero          headline + the study modules drawn as a mind map (outline on phones)
 *   Specimens     one live sample per kind of material, each from a real page
 *   TearCalendar  exam countdown as a tear-off calendar (client clock)
 */
export function StudyHome() {
  const data = getStudyHomeData();

  return (
    <div className={home.page}>
      <Hero data={data} />
      <Specimens data={data} />
      <TearCalendar />
      <footer className={home.footer}>
        <span className={home.footerBrand}>{siteConfig.name}</span>
        <nav aria-label="更多资源">
          <Link href="/blog/">博客</Link>
          <a href="/llms.txt">全部文档目录</a>
          <a href={siteConfig.repository.url} target="_blank" rel="noreferrer">
            GitHub
          </a>
        </nav>
      </footer>
    </div>
  );
}
