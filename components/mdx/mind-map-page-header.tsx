'use client';

import { cn } from '@/lib/utils';
import {
  ChevronDown,
  ChevronLeft,
  ChevronRight,
  ListTree,
  Search,
  X,
} from 'lucide-react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useId, useMemo, useRef, useState } from 'react';

export interface MindMapNavLink {
  title: string;
  url: string;
}

export interface MindMapPageHeaderProps {
  title: string;
  /** The subject overview (操作系统). */
  subject?: MindMapNavLink;
  /** The chapter overview this page belongs to (or is). */
  chapter?: MindMapNavLink;
  /** Every map of the chapter, overview first, in reading order. */
  sections?: MindMapNavLink[];
  /** The subject's chapters, for jumping across chapters. */
  chapters?: MindMapNavLink[];
  previous?: MindMapNavLink;
  next?: MindMapNavLink;
  position?: { index: number; total: number };
}

/** "1.8 系统调用…" → ["1.8", "系统调用…"]; titles without a number keep it empty. */
function splitNumber(title: string): [string, string] {
  const match = /^(\d+(?:\.\d+)*)\s+(.+)$/u.exec(title.trim());
  return match ? [match[1], match[2]] : ['', title.trim()];
}

/** "第一章 操作系统概述 · 16节双侧导图导航" → "第一章 操作系统概述". */
export function shortChapterTitle(title: string) {
  return title.replace(/\s*[·•|｜].*$/u, '').replace(/思维导图$/u, '').trim();
}

/** "第一章 操作系统概述" → ["第一章", "操作系统概述"]. */
function splitChapter(title: string): [string, string] {
  const match = /^(第[一二三四五六七八九十百\d]+章)\s*(.*)$/u.exec(shortChapterTitle(title));
  return match ? [match[1], match[2] || match[1]] : ['', shortChapterTitle(title)];
}

/**
 * Floating navigator for dedicated mind-map pages: where the page sits
 * (subject › chapter), its title and progress through the chapter,
 * previous / next, and a directory of the chapter's sections and the
 * subject's chapters, filterable, to jump anywhere in two clicks.
 */
export function MindMapPageHeader({
  title,
  subject,
  chapter,
  sections = [],
  chapters = [],
  previous,
  next,
  position,
}: MindMapPageHeaderProps) {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const rootRef = useRef<HTMLDivElement>(null);
  const listRef = useRef<HTMLOListElement>(null);
  const panelId = useId();
  const [number, name] = splitNumber(title);
  const isOverview = chapter ? normalize(chapter.url) === normalize(pathname) : false;

  // Close on navigation.
  const [lastPath, setLastPath] = useState(pathname);
  if (pathname !== lastPath) {
    setLastPath(pathname);
    setOpen(false);
    setQuery('');
  }

  // Outside click and Esc close the directory.
  useEffect(() => {
    if (!open) return;
    const onPointer = (event: PointerEvent) => {
      if (!rootRef.current?.contains(event.target as Node)) setOpen(false);
    };
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        event.stopPropagation();
        setOpen(false);
      }
    };
    document.addEventListener('pointerdown', onPointer, true);
    document.addEventListener('keydown', onKey, true);
    return () => {
      document.removeEventListener('pointerdown', onPointer, true);
      document.removeEventListener('keydown', onKey, true);
    };
  }, [open]);

  // Bring the current section into view when the directory opens.
  useEffect(() => {
    if (!open) return;
    listRef.current
      ?.querySelector<HTMLElement>('[aria-current="page"]')
      ?.scrollIntoView({ block: 'center' });
  }, [open]);

  const filtered = useMemo(() => {
    const needle = query.trim().toLowerCase();
    if (!needle) return sections;
    return sections.filter((section) => section.title.toLowerCase().includes(needle));
  }, [query, sections]);

  const progress = position ? (position.index / position.total) * 100 : 0;
  const chapterLabel = chapter ? shortChapterTitle(chapter.title) : undefined;

  return (
    <div ref={rootRef} className="mind-map-nav" data-open={open ? '' : undefined}>
      <div className="mind-map-nav-card">
        <div className="mind-map-nav-main">
          <button
            type="button"
            className="mind-map-nav-toggle"
            aria-expanded={open}
            aria-controls={panelId}
            title={open ? '收起目录' : '打开本章目录'}
            onClick={() => setOpen((value) => !value)}
          >
            <ListTree aria-hidden="true" />
            <span className="sr-only">本章目录</span>
          </button>

          <div className="mind-map-nav-heading">
            {subject || chapter ? (
              <nav className="mind-map-nav-trail" aria-label="所在位置">
                {subject ? (
                  <Link href={subject.url} className="mind-map-nav-crumb">
                    {shortChapterTitle(subject.title)}
                  </Link>
                ) : null}
                {subject && chapter && !isOverview ? (
                  <ChevronRight className="mind-map-nav-crumb-sep" aria-hidden="true" />
                ) : null}
                {chapter && !isOverview ? (
                  <Link href={chapter.url} className="mind-map-nav-crumb">
                    {chapterLabel}
                  </Link>
                ) : null}
              </nav>
            ) : null}
            <h1 className="mind-map-page-title">
              <button
                type="button"
                className="mind-map-nav-title"
                aria-expanded={open}
                aria-controls={panelId}
                onClick={() => setOpen((value) => !value)}
              >
                {number ? <span className="mind-map-nav-number">{number}</span> : null}
                <span className="mind-map-nav-title-text">
                  {isOverview ? `${chapterLabel ?? name} · 导览` : name}
                </span>
                <ChevronDown className="mind-map-nav-caret" aria-hidden="true" />
              </button>
            </h1>
          </div>
        </div>

        {previous || next || position ? (
          <div className="mind-map-nav-steps">
            <StepLink link={previous} direction="previous" />
            {position ? (
              <div
                className="mind-map-nav-progress"
                role="progressbar"
                aria-label="本章进度"
                aria-valuemin={1}
                aria-valuemax={position.total}
                aria-valuenow={position.index}
              >
                <span className="mind-map-nav-progress-bar" style={{ width: `${progress}%` }} />
                <span className="mind-map-nav-progress-text">
                  {position.index}
                  <span aria-hidden="true"> / </span>
                  <span className="sr-only">共</span>
                  {position.total}
                </span>
              </div>
            ) : null}
            <StepLink link={next} direction="next" />
          </div>
        ) : null}
      </div>

      {open ? (
        <div id={panelId} className="mind-map-nav-panel" role="dialog" aria-label="思维导图目录">
          <div className="mind-map-nav-panel-head">
            <div className="mind-map-nav-panel-title">
              <span>{chapterLabel ?? '本章'}</span>
              <span className="mind-map-nav-panel-count">{sections.length} 张导图</span>
            </div>
            <button
              type="button"
              className="mind-map-nav-icon"
              onClick={() => setOpen(false)}
              title="关闭目录"
              aria-label="关闭目录"
            >
              <X aria-hidden="true" />
            </button>
          </div>

          {sections.length > 6 ? (
            <label className="mind-map-nav-search">
              <Search aria-hidden="true" />
              <input
                type="search"
                value={query}
                placeholder="筛选本章小节"
                aria-label="筛选本章小节"
                onChange={(event) => setQuery(event.target.value)}
                // eslint-disable-next-line jsx-a11y/no-autofocus -- the directory is opened to search it
                autoFocus
              />
            </label>
          ) : null}

          <ol ref={listRef} className="mind-map-nav-list">
            {filtered.map((section) => {
              const current = normalize(section.url) === normalize(pathname);
              const overview = chapter ? normalize(section.url) === normalize(chapter.url) : false;
              const [sectionNumber, sectionName] = splitNumber(section.title);
              return (
                <li key={section.url}>
                  <Link
                    href={section.url}
                    className="mind-map-nav-item"
                    aria-current={current ? 'page' : undefined}
                    data-overview={overview ? '' : undefined}
                  >
                    <span className="mind-map-nav-item-number">
                      {overview ? <ListTree aria-hidden="true" /> : sectionNumber || '·'}
                    </span>
                    <span className="mind-map-nav-item-title">{overview ? '本章导览' : sectionName}</span>
                  </Link>
                </li>
              );
            })}
            {filtered.length === 0 ? <li className="mind-map-nav-empty">没有匹配的小节</li> : null}
          </ol>

          {chapters.length > 1 ? (
            <div className="mind-map-nav-chapters">
              <div className="mind-map-nav-chapters-label">
                <span>切换章节</span>
                {subject ? (
                  <Link href={subject.url} className="mind-map-nav-chapters-all">
                    {shortChapterTitle(subject.title)}总览
                    <ChevronRight aria-hidden="true" />
                  </Link>
                ) : null}
              </div>
              <div className="mind-map-nav-chapter-grid">
                {chapters.map((entry) => {
                  const current = chapter ? normalize(entry.url) === normalize(chapter.url) : false;
                  const [order, label] = splitChapter(entry.title);
                  return (
                    <Link
                      key={entry.url}
                      href={entry.url}
                      className="mind-map-nav-chapter"
                      aria-current={current ? 'true' : undefined}
                      title={shortChapterTitle(entry.title)}
                    >
                      {order ? <span className="mind-map-nav-chapter-order">{order}</span> : null}
                      <span className="mind-map-nav-chapter-name">{label}</span>
                    </Link>
                  );
                })}
              </div>
            </div>
          ) : null}
        </div>
      ) : null}
    </div>
  );
}

function normalize(url: string) {
  return url.replace(/\/+$/u, '') || '/';
}

function StepLink({ link, direction }: { link?: MindMapNavLink; direction: 'previous' | 'next' }) {
  const label = direction === 'previous' ? '上一张' : '下一张';
  const Icon = direction === 'previous' ? ChevronLeft : ChevronRight;
  if (!link) {
    return (
      <span className={cn('mind-map-nav-step', `mind-map-nav-step-${direction}`)} data-disabled="" aria-hidden="true">
        <Icon />
        <span className="mind-map-nav-step-text">{direction === 'previous' ? '已是第一张' : '已是最后一张'}</span>
      </span>
    );
  }
  const [number, name] = splitNumber(link.title);
  const text = number ? `${number} ${name}` : shortChapterTitle(link.title);
  return (
    <Link
      href={link.url}
      className={cn('mind-map-nav-step', `mind-map-nav-step-${direction}`)}
      title={`${label}：${link.title}`}
      aria-label={`${label}：${link.title}`}
    >
      <Icon aria-hidden="true" />
      <span className="mind-map-nav-step-text">{text}</span>
    </Link>
  );
}
