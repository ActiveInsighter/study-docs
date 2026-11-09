'use client';

import {
  Modal,
  ModalBody,
  ModalContent,
  ModalHeader,
  ModalTag,
  ModalTags,
  ModalTitle,
  ModalToolbar,
} from '@/components/ui/modal';
import type { MindMapImagePreview } from '@/components/mdx/mind-map-hook';
import {
  Download,
  ExternalLink,
  Expand,
  Shrink,
  Minus,
  Plus,
  Scan,
} from 'lucide-react';
import {
  useCallback,
  useEffect,
  useLayoutEffect,
  useRef,
  useState,
  useSyncExternalStore,
  type PointerEvent as ReactPointerEvent,
} from 'react';

const MIN_SCALE = 0.1;
const MAX_SCALE = 8;
const ZOOM_STEP = 1.25;
/** Space kept around the picture when it is fitted, in px. */
const FIT_PADDING = 32;

type View = { scale: number; x: number; y: number };

function clampScale(scale: number) {
  return Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale));
}

function fileName(src: string) {
  try {
    const path = new URL(src, window.location.href).pathname;
    return decodeURIComponent(path.split('/').pop() || 'image');
  } catch {
    return 'image';
  }
}

function subscribeFullscreen(callback: () => void) {
  document.addEventListener('fullscreenchange', callback);
  return () => document.removeEventListener('fullscreenchange', callback);
}

export interface MindMapImageModalProps {
  image: MindMapImagePreview | null;
  onClose: () => void;
  /** Portal target: the map while it is fullscreen, so the modal shows on top of it. */
  container?: HTMLElement | null;
}

/** A mind-map figure on the general Modal, with pan, zoom, fullscreen and download. */
export function MindMapImageModal({ image, onClose, container }: MindMapImageModalProps) {
  // Keep the last image while the sheet slides away.
  const [shown, setShown] = useState(image);
  if (image && image !== shown) setShown(image);

  return (
    <Modal
      open={Boolean(image)}
      onOpenChange={(open) => {
        if (!open) onClose();
      }}
    >
      <ModalContent
        size="xl"
        height="fixed"
        container={container ?? undefined}
        data-mind-map-image-modal=""
      >
        {shown ? <ImageViewer key={shown.src} image={shown} /> : null}
      </ModalContent>
    </Modal>
  );
}

function ImageViewer({ image }: { image: MindMapImagePreview }) {
  const stageRef = useRef<HTMLDivElement>(null);
  const panelRef = useRef<HTMLElement | null>(null);
  const [natural, setNatural] = useState<{ width: number; height: number } | null>(null);
  const [view, setView] = useState<View | null>(null);
  const [fitScale, setFitScale] = useState(1);
  const [dragging, setDragging] = useState(false);
  const pointers = useRef(new Map<number, { x: number; y: number }>());
  const gesture = useRef<{ distance: number; scale: number } | null>(null);
  const userMoved = useRef(false);

  const fullscreen = useSyncExternalStore(
    subscribeFullscreen,
    () => Boolean(panelRef.current) && document.fullscreenElement === panelRef.current,
    () => false,
  );
  const fullscreenSupported = useSyncExternalStore(
    subscribeFullscreen,
    () => typeof document.documentElement.requestFullscreen === 'function',
    () => false,
  );

  const computeFit = useCallback(() => {
    const stage = stageRef.current;
    if (!stage || !natural) return null;
    const { width, height } = stage.getBoundingClientRect();
    // The glass header floats over the stage: fit the picture below it.
    const header =
      stage.closest('[data-slot="modal-page"]')?.querySelector<HTMLElement>('[data-slot="modal-header"]')
        ?.offsetHeight ?? 0;
    const availableHeight = height - header;
    const scale = clampScale(
      Math.min((width - FIT_PADDING * 2) / natural.width, (availableHeight - FIT_PADDING * 2) / natural.height, 3),
    );
    return {
      scale,
      x: (width - natural.width * scale) / 2,
      y: header + (availableHeight - natural.height * scale) / 2,
    };
  }, [natural]);

  const fit = useCallback(() => {
    const next = computeFit();
    if (!next) return;
    userMoved.current = false;
    setFitScale(next.scale);
    setView(next);
  }, [computeFit]);

  // Fit on load and whenever the stage changes size (sheet opening, fullscreen, rotation).
  useLayoutEffect(() => {
    const stage = stageRef.current;
    if (!stage || !natural) return;
    fit();
    const observer = new ResizeObserver(() => {
      const next = computeFit();
      if (!next) return;
      setFitScale(next.scale);
      if (!userMoved.current) setView(next);
    });
    observer.observe(stage);
    return () => observer.disconnect();
  }, [natural, fit, computeFit]);

  useEffect(() => {
    panelRef.current = stageRef.current?.closest<HTMLElement>('[data-slot="modal-content"]') ?? null;
  }, []);

  /** Zoom by `factor` keeping the stage point (cx, cy) still; the centre by default. */
  const zoomBy = useCallback((factor: number, cx?: number, cy?: number) => {
    const stage = stageRef.current;
    if (!stage) return;
    userMoved.current = true;
    setView((current) => {
      if (!current) return current;
      const box = stage.getBoundingClientRect();
      const px = cx ?? box.width / 2;
      const py = cy ?? box.height / 2;
      const scale = clampScale(current.scale * factor);
      const ratio = scale / current.scale;
      return { scale, x: px - (px - current.x) * ratio, y: py - (py - current.y) * ratio };
    });
  }, []);

  const actualSize = useCallback(() => {
    const stage = stageRef.current;
    if (!stage || !view) return;
    zoomBy(1 / view.scale);
  }, [view, zoomBy]);

  // Wheel and trackpad pinch zoom around the pointer (non-passive, so the page does not scroll).
  useEffect(() => {
    const stage = stageRef.current;
    if (!stage) return;
    const onWheel = (event: WheelEvent) => {
      event.preventDefault();
      const box = stage.getBoundingClientRect();
      const delta = event.deltaMode === 1 ? event.deltaY * 16 : event.deltaY;
      zoomBy(Math.exp(-delta * (event.ctrlKey ? 0.01 : 0.0025)), event.clientX - box.x, event.clientY - box.y);
    };
    stage.addEventListener('wheel', onWheel, { passive: false });
    return () => stage.removeEventListener('wheel', onWheel);
  }, [zoomBy]);

  // Keyboard: + / - zoom, 0 fits, 1 shows actual size.
  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.metaKey || event.ctrlKey || event.altKey) return;
      if (event.target instanceof HTMLInputElement) return;
      if (event.key === '+' || event.key === '=') zoomBy(ZOOM_STEP);
      else if (event.key === '-' || event.key === '_') zoomBy(1 / ZOOM_STEP);
      else if (event.key === '0') fit();
      else if (event.key === '1') actualSize();
      else return;
      event.preventDefault();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [zoomBy, fit, actualSize]);

  const onPointerDown = (event: ReactPointerEvent<HTMLDivElement>) => {
    if (event.button !== 0) return;
    event.currentTarget.setPointerCapture(event.pointerId);
    pointers.current.set(event.pointerId, { x: event.clientX, y: event.clientY });
    if (pointers.current.size === 2) {
      const [a, b] = [...pointers.current.values()];
      gesture.current = { distance: Math.hypot(a.x - b.x, a.y - b.y), scale: view?.scale ?? 1 };
    }
    setDragging(true);
  };

  const onPointerMove = (event: ReactPointerEvent<HTMLDivElement>) => {
    const previous = pointers.current.get(event.pointerId);
    if (!previous) return;
    const point = { x: event.clientX, y: event.clientY };
    pointers.current.set(event.pointerId, point);
    const stage = stageRef.current;
    if (!stage) return;

    if (pointers.current.size === 2 && gesture.current) {
      const [a, b] = [...pointers.current.values()];
      const box = stage.getBoundingClientRect();
      const distance = Math.hypot(a.x - b.x, a.y - b.y);
      const target = clampScale(gesture.current.scale * (distance / gesture.current.distance));
      setView((current) => {
        if (!current) return current;
        const cx = (a.x + b.x) / 2 - box.x;
        const cy = (a.y + b.y) / 2 - box.y;
        const ratio = target / current.scale;
        return { scale: target, x: cx - (cx - current.x) * ratio, y: cy - (cy - current.y) * ratio };
      });
    } else {
      setView((current) =>
        current ? { ...current, x: current.x + point.x - previous.x, y: current.y + point.y - previous.y } : current,
      );
    }
    userMoved.current = true;
  };

  const onPointerUp = (event: ReactPointerEvent<HTMLDivElement>) => {
    pointers.current.delete(event.pointerId);
    if (pointers.current.size < 2) gesture.current = null;
    if (pointers.current.size === 0) setDragging(false);
  };

  const toggleFullscreen = () => {
    const panel = panelRef.current;
    if (!panel) return;
    const request = document.fullscreenElement === panel ? document.exitFullscreen() : panel.requestFullscreen();
    request.catch(() => {
      // Fullscreen can be denied by the browser or an embedding host.
    });
  };

  const name = fileName(image.src);
  const extension = name.includes('.') ? name.split('.').pop()?.toUpperCase() : undefined;
  const percent = view ? Math.round(view.scale * 100) : 100;

  return (
    <>
      <ModalHeader>
        <ModalTitle className="mind-map-image-title">{image.alt}</ModalTitle>
        <ModalTags>
          {extension ? <ModalTag>{extension}</ModalTag> : null}
          {natural ? (
            <ModalTag>
              {natural.width} × {natural.height}
            </ModalTag>
          ) : null}
        </ModalTags>
        <ModalToolbar aria-label="图片操作">
          <button
            type="button"
            data-slot="mind-map-image-action"
            title="缩小 (-)"
            aria-label="缩小"
            disabled={!view || view.scale <= MIN_SCALE}
            onClick={() => zoomBy(1 / ZOOM_STEP)}
          >
            <Minus aria-hidden="true" />
          </button>
          <button
            type="button"
            data-slot="mind-map-image-scale"
            title="原始大小 (1)"
            aria-label={`当前缩放 ${percent}%，点击切换到原始大小`}
            onClick={actualSize}
          >
            {percent}%
          </button>
          <button
            type="button"
            data-slot="mind-map-image-action"
            title="放大 (+)"
            aria-label="放大"
            disabled={!view || view.scale >= MAX_SCALE}
            onClick={() => zoomBy(ZOOM_STEP)}
          >
            <Plus aria-hidden="true" />
          </button>
          <button
            type="button"
            data-slot="mind-map-image-action"
            title="适应窗口 (0)"
            aria-label="适应窗口"
            onClick={fit}
          >
            <Scan aria-hidden="true" />
          </button>
          <span data-slot="mind-map-image-divider" aria-hidden="true" />
          {fullscreenSupported ? (
            <button
              type="button"
              data-slot="mind-map-image-action"
              title={fullscreen ? '退出全屏' : '全屏查看'}
              aria-label={fullscreen ? '退出全屏' : '全屏查看'}
              aria-pressed={fullscreen}
              onClick={toggleFullscreen}
            >
              {fullscreen ? <Shrink aria-hidden="true" /> : <Expand aria-hidden="true" />}
            </button>
          ) : null}
          <a
            data-slot="mind-map-image-action"
            href={image.src}
            download={name}
            title="下载图片"
            aria-label="下载图片"
          >
            <Download aria-hidden="true" />
          </a>
          <a
            data-slot="mind-map-image-action"
            href={image.src}
            target="_blank"
            rel="noopener noreferrer"
            title="在新标签页打开原图"
            aria-label="在新标签页打开原图"
          >
            <ExternalLink aria-hidden="true" />
          </a>
        </ModalToolbar>
      </ModalHeader>
      <ModalBody className="mind-map-image-body">
        <div
          ref={stageRef}
          className="mind-map-image-stage"
          data-dragging={dragging ? '' : undefined}
          onPointerDown={onPointerDown}
          onPointerMove={onPointerMove}
          onPointerUp={onPointerUp}
          onPointerCancel={onPointerUp}
          onDoubleClick={(event) => {
            const box = event.currentTarget.getBoundingClientRect();
            if (view && view.scale > fitScale * 1.05) fit();
            else zoomBy(2, event.clientX - box.x, event.clientY - box.y);
          }}
        >
          {/* eslint-disable-next-line @next/next/no-img-element -- static SVG asset preview */}
          <img
            src={image.src}
            alt={image.alt}
            draggable={false}
            className="mind-map-image"
            data-ready={view ? '' : undefined}
            onLoad={(event) => {
              const img = event.currentTarget;
              setNatural({ width: img.naturalWidth || 800, height: img.naturalHeight || 600 });
            }}
            style={
              view && natural
                ? {
                    width: natural.width,
                    height: natural.height,
                    transform: `translate(${view.x}px, ${view.y}px) scale(${view.scale})`,
                  }
                : undefined
            }
          />
          <p className="mind-map-image-hint" aria-hidden="true">
            滚轮或双指缩放 · 拖动平移 · 双击放大
          </p>
        </div>
      </ModalBody>
    </>
  );
}
