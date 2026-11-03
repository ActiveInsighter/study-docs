'use client';

import { useMemo, useState, useSyncExternalStore } from 'react';
import { calendarSheets, examSchedule } from '@/lib/home/content';
import styles from './tear-calendar.module.css';

/*
 * A 考研倒计时 tear-off calendar. The top sheet is today: days left to the
 * initial exam, a reminder and the almanac's 宜 / 忌. Tearing it shows
 * tomorrow's sheet (one day fewer, the next reminder); "回到今天" restores.
 * The static page cannot know today, so the date fills in after hydration.
 */

const WEEKDAYS = ['日', '一', '二', '三', '四', '五', '六'];
const RELATIVE = ['今天', '明天', '后天'];
const DAY = 86_400_000;
const noop = () => () => {};

interface Sheet {
  offset: number;
  dateLabel: string;
  weekday: string;
  relative: string;
  days: number;
  quote: string;
  good: string;
  avoid: string;
}

function examDayUtc(): number {
  const [year, month, day] = examSchedule.startsAt.slice(0, 10).split('-').map(Number);
  return Date.UTC(year ?? 1970, (month ?? 1) - 1, day ?? 1);
}

function sheetFor(today: Date | null, offset: number): Sheet {
  const content = calendarSheets[offset % calendarSheets.length]!;
  if (!today) {
    return { offset, dateLabel: '', weekday: '', relative: '', days: -1, ...content };
  }
  const date = new Date(today.getFullYear(), today.getMonth(), today.getDate() + offset);
  const todayUtc = Date.UTC(today.getFullYear(), today.getMonth(), today.getDate());
  const days = Math.max(0, Math.round((examDayUtc() - todayUtc) / DAY) - offset);
  return {
    offset,
    dateLabel: `${date.getFullYear()} 年 ${date.getMonth() + 1} 月 ${date.getDate()} 日`,
    weekday: `星期${WEEKDAYS[date.getDay()]}`,
    relative: RELATIVE[offset] ?? `${offset} 天后`,
    days,
    ...content,
  };
}

function SheetFace({ sheet, className, onAnimationEnd }: { sheet: Sheet; className?: string; onAnimationEnd?: () => void }) {
  return (
    <div className={className} onAnimationEnd={onAnimationEnd}>
      <div className={styles.sheetHead}>
        <span>{sheet.dateLabel || ' '}</span>
        <span>{sheet.weekday}</span>
      </div>
      <p className={styles.caption}>{sheet.relative ? `${sheet.relative}，距初试还有` : '距初试还有'}</p>
      <p className={styles.days}>
        <span>{sheet.days < 0 ? '--' : sheet.days}</span>
        <small>天</small>
      </p>
      <p className={styles.quote}>{sheet.quote}</p>
      <dl className={styles.almanac}>
        <div>
          <dt>宜</dt>
          <dd>{sheet.good}</dd>
        </div>
        <div>
          <dt>忌</dt>
          <dd>{sheet.avoid}</dd>
        </div>
      </dl>
    </div>
  );
}

export function TearCalendar() {
  const mounted = useSyncExternalStore(noop, () => true, () => false);
  const today = useMemo(() => (mounted ? new Date() : null), [mounted]);
  const [offset, setOffset] = useState(0);
  const [leaving, setLeaving] = useState<Sheet | null>(null);
  const current = sheetFor(today, offset);

  const tear = () => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reduced) setLeaving(current);
    setOffset((value) => value + 1);
  };

  return (
    <section className={styles.section} aria-labelledby="calendar-title">
      <div className={styles.stand}>
        <div className={styles.binding} aria-hidden="true">
          <i />
          <i />
        </div>
        <div className={styles.pad} aria-live="polite" aria-atomic="true">
          <SheetFace sheet={current} className={styles.sheet} />
          {leaving && (
            <SheetFace
              key={leaving.offset}
              sheet={leaving}
              className={`${styles.sheet} ${styles.leaving}`}
              onAnimationEnd={() => setLeaving(null)}
            />
          )}
        </div>
      </div>

      <div className={styles.copy}>
        <h2 id="calendar-title" className={styles.title}>
          倒计时，一天一页
        </h2>
        <p className={styles.text}>每天撕下一页：看看还剩几天，读一句写给自己的提醒，按黄历的样子定一件今天宜做的事。</p>
        <div className={styles.actions}>
          <button type="button" className={styles.tear} onClick={tear}>
            {offset === 0 ? '撕下今天，看看明天' : '再撕一页'}
          </button>
          {offset > 0 && (
            <button type="button" className={styles.back} onClick={() => setOffset(0)}>
              回到今天
            </button>
          )}
        </div>
        <p className={styles.note}>{examSchedule.note}</p>
      </div>
    </section>
  );
}
