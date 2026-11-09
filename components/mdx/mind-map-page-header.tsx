import { ChevronLeft, ChevronRight } from 'lucide-react';
import Link from 'next/link';

interface ChapterLink {
  title: string;
  url: string;
}

export interface MindMapPageHeaderProps {
  title: string;
  course?: ChapterLink;
  previous?: ChapterLink;
  next?: ChapterLink;
  position?: { index: number; total: number };
}

/** Floating title card for dedicated mind-map pages. */
export function MindMapPageHeader({
  title,
  course,
  previous,
  next,
  position,
}: MindMapPageHeaderProps) {
  return (
    <div className="mind-map-page-header">
      <div className="mind-map-page-heading">
        {course ? (
          <Link href={course.url} className="mind-map-page-course">
            {course.title}
            {position ? (
              <span className="mind-map-page-position">
                {position.index} / {position.total}
              </span>
            ) : null}
          </Link>
        ) : null}
        <h1 className="mind-map-page-title">{title}</h1>
      </div>
      {previous || next ? (
        <nav className="mind-map-page-nav" aria-label="章节导航">
          {previous ? (
            <Link
              href={previous.url}
              className="mind-map-page-nav-link"
              title={`上一页：${previous.title}`}
              aria-label={`上一页：${previous.title}`}
            >
              <ChevronLeft aria-hidden="true" />
            </Link>
          ) : (
            <span className="mind-map-page-nav-link" aria-hidden="true" data-disabled="true">
              <ChevronLeft />
            </span>
          )}
          {next ? (
            <Link
              href={next.url}
              className="mind-map-page-nav-link"
              title={`下一页：${next.title}`}
              aria-label={`下一页：${next.title}`}
            >
              <ChevronRight aria-hidden="true" />
            </Link>
          ) : (
            <span className="mind-map-page-nav-link" aria-hidden="true" data-disabled="true">
              <ChevronRight />
            </span>
          )}
        </nav>
      ) : null}
    </div>
  );
}
