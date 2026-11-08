'use client';

import { cn } from '@/lib/utils';
import {
  useMindMap,
  type MindMapImagePreview,
} from '@/components/mdx/mind-map-hook';
import { ExternalLink, X } from 'lucide-react';
import { useRouter } from 'next/navigation';
import {
  useCallback,
  useEffect,
  useId,
  useRef,
  useState,
  type CSSProperties,
  type ReactNode,
} from 'react';

export interface MindMapProps {
  /** Build-time markmap tree as JSON; produced from ```mindmap fences. */
  data?: string;
  /** Markdown headings and list items, transformed in the browser. */
  markdown?: string;
  /** Visible label used by assistive technologies. */
  title?: string;
  /** CSS height, or a number interpreted as pixels (embedded variant only). */
  height?: number | string;
  /** Heading depth shown on first render. `-1` expands every level. */
  initialExpandLevel?: number;
  /** Maximum width of a plain-text node label before it wraps. */
  maxWidth?: number;
  /**
   * `embedded` sits in the article flow; `page` fills the docs panel as a
   * canvas (dedicated mind-map pages).
   */
  variant?: 'embedded' | 'page';
  /** Overlay shown in the top-left corner of the canvas (page variant). */
  header?: ReactNode;
  className?: string;
}

export function MindMap({
  data,
  markdown,
  title = '思维导图',
  height = 'clamp(22rem, 62vh, 38rem)',
  initialExpandLevel,
  maxWidth = 300,
  variant = 'embedded',
  header,
  className,
}: MindMapProps) {
  const router = useRouter();
  const containerRef = useRef<HTMLElement>(null);
  const dialogRef = useRef<HTMLDialogElement>(null);
  const [preview, setPreview] = useState<MindMapImagePreview | null>(null);
  const rawId = useId();
  const id = rawId.replaceAll(':', '');
  const descriptionId = `mind-map-description-${id}`;

  const onNavigate = useCallback((href: string) => router.push(href), [router]);
  const { errorMessage, status, svgRef, toolbarHostRef } = useMindMap({
    data,
    markdown,
    initialExpandLevel: initialExpandLevel ?? 3,
    adaptiveExpand: initialExpandLevel === undefined,
    maxWidth,
    fullscreenTargetRef: containerRef,
    onNavigate,
    onPreviewImage: setPreview,
  });

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    if (preview && !dialog.open) dialog.showModal();
    if (!preview && dialog.open) dialog.close();
  }, [preview]);

  const heightValue = typeof height === 'number' ? `${height}px` : height;

  return (
    <figure
      ref={containerRef}
      className={cn('mind-map not-prose', className)}
      data-mind-map="true"
      data-variant={variant}
      data-status={status}
      style={
        variant === 'embedded'
          ? ({ '--mind-map-height': heightValue } as CSSProperties)
          : undefined
      }
    >
      <div
        className="mind-map-stage"
        role="region"
        aria-label={title}
        aria-describedby={descriptionId}
        aria-busy={status === 'loading'}
      >
        <svg
          ref={svgRef}
          id={`mind-map-svg-${id}`}
          className="mind-map-svg"
          role="img"
          aria-label={title}
        />

        {header ? <div className="mind-map-header">{header}</div> : null}

        {status === 'loading' && (
          <div className="mind-map-status" role="status">
            <span className="mind-map-spinner" aria-hidden="true" />
            正在生成思维导图…
          </div>
        )}
        {status === 'error' && (
          <div className="mind-map-status mind-map-status-error" role="alert">
            {errorMessage}
          </div>
        )}

        <div ref={toolbarHostRef} className="mind-map-toolbar-host" />
      </div>

      <p id={descriptionId} className="mind-map-sr-only">
        滚轮或双指缩放，拖动平移，点击节点圆点展开或收起分支；右下角工具栏可放大、缩小、适应窗口、联动子分支、全部展开、折叠、恢复初始视图和全屏查看。点击配图可放大查看。
      </p>

      <dialog
        ref={dialogRef}
        className="mind-map-lightbox"
        aria-label={preview?.alt || '配图预览'}
        onClose={() => setPreview(null)}
        onClick={(event) => {
          if (event.target === event.currentTarget) setPreview(null);
        }}
      >
        {preview ? (
          <>
            <div className="mind-map-lightbox-actions">
              <a
                href={preview.href}
                target="_blank"
                rel="noopener noreferrer"
                className="mind-map-lightbox-button"
                title="在新标签页打开原图"
                aria-label="在新标签页打开原图"
              >
                <ExternalLink aria-hidden="true" />
              </a>
              <button
                type="button"
                className="mind-map-lightbox-button"
                onClick={() => setPreview(null)}
                title="关闭"
                aria-label="关闭"
              >
                <X aria-hidden="true" />
              </button>
            </div>
            {/* eslint-disable-next-line @next/next/no-img-element -- static SVG asset preview */}
            <img src={preview.src} alt={preview.alt} className="mind-map-lightbox-image" />
          </>
        ) : null}
      </dialog>
    </figure>
  );
}
