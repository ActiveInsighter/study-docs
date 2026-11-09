'use client';

import { cn } from '@/lib/utils';
import {
  useMindMap,
  type MindMapImagePreview,
} from '@/components/mdx/mind-map-hook';
import { MindMapImageModal } from '@/components/mdx/mind-map-image-modal';
import { MindMapToolbar } from '@/components/mdx/mind-map-toolbar';
import { useTheme } from 'next-themes';
import { useRouter } from 'next/navigation';
import {
  useCallback,
  useId,
  useRef,
  useState,
  type CSSProperties,
  type ReactNode,
} from 'react';

export interface MindMapProps {
  /** Build-time Markmap tree as JSON; produced from ```mindmap fences. */
  data?: string;
  /** Serialized Markmap frontmatter; validated by the view before use. */
  documentOptions?: string;
  /** Markdown headings and list items, parsed in the browser. */
  markdown?: string;
  /** Visible label used by assistive technologies. */
  title?: string;
  /** CSS height, or a number interpreted as pixels (embedded variant only). */
  height?: number | string;
  /**
   * Levels shown on first render, counting the root as level 1 (Markmap 0.18
   * semantics). `-1` expands every level. Omit to pick from the map's size.
   */
  initialExpandLevel?: number;
  /** Width at which labels and images wrap, in px. */
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

function toFoldLevel(initialExpandLevel: number | undefined) {
  if (initialExpandLevel === undefined) return undefined;
  // 0.18 expanded `level` levels including the root; 1.0 folds from a depth.
  return initialExpandLevel < 0 ? Number.POSITIVE_INFINITY : Math.max(initialExpandLevel - 1, 0);
}

export function MindMap({
  data,
  documentOptions,
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
  const { resolvedTheme } = useTheme();
  const containerRef = useRef<HTMLElement>(null);
  const [preview, setPreview] = useState<{ image: MindMapImagePreview; container: HTMLElement | null } | null>(null);
  const rawId = useId();
  const id = rawId.replaceAll(':', '');
  const descriptionId = `mind-map-description-${id}`;

  const onNavigate = useCallback((href: string) => router.push(href), [router]);
  // While the map is fullscreen, the modal opens inside it (or it would be hidden).
  const onPreviewImage = useCallback((image: MindMapImagePreview) => {
    const fullscreenElement = document.fullscreenElement;
    const container =
      fullscreenElement instanceof HTMLElement && fullscreenElement === containerRef.current ? fullscreenElement : null;
    setPreview({ image, container });
  }, []);
  const { errorMessage, status, surfaceRef, markmap, initialLevel } = useMindMap({
    data,
    documentOptions,
    markdown,
    foldLevel: toFoldLevel(initialExpandLevel),
    wrapWidth: maxWidth,
    fitPadding: variant === 'page' ? 72 : 24,
    colorScheme: resolvedTheme === 'dark' ? 'dark' : 'light',
    onNavigate,
    onPreviewImage,
  });

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
        {/* The hook mounts Markmap's <svg> here. */}
        <div ref={surfaceRef} className="mind-map-surface-host" aria-label={title} />

        {header ? <div className="mind-map-header">{header}</div> : null}

        {status === 'loading' && (
          <div className="mind-map-status" role="status">
            
            正在生成思维导图…
          </div>
        )}
        {status === 'error' && (
          <div className="mind-map-status mind-map-status-error" role="alert">
            {errorMessage}
          </div>
        )}

        <div className="mind-map-toolbar-host">
          <MindMapToolbar markmap={markmap} initialLevel={initialLevel} fullscreenTargetRef={containerRef} />
        </div>
      </div>

      <p id={descriptionId} className="mind-map-sr-only">
        滚轮或双指缩放，拖动平移，点击节点圆点展开或收起分支，点击节点旁的小圆点查看代码、表格等注释；右下角工具栏可放大、缩小、适应窗口、按层级展开、全部展开或收起和全屏查看。点击配图在弹窗中查看，可缩放、全屏和下载。
      </p>

      <MindMapImageModal
        image={preview?.image ?? null}
        container={preview?.container}
        onClose={() => setPreview(null)}
      />
    </figure>
  );
}
