'use client';

import type { MarkmapNode } from '@markmap/core';
import type { Markmap } from '@markmap/view';
import {
  Expand,
  Shrink,
  Minus,
  Plus,
  Scan,
} from 'lucide-react';
import { useCallback, useEffect, useRef, useState, useSyncExternalStore } from 'react';

/** Depth of the deepest node with children: folding deeper than that does nothing. */
function deepestParent(node: MarkmapNode | undefined, depth = 0): number {
  if (!node?.children.length) return 0;
  return Math.max(depth, ...node.children.map((child) => deepestParent(child, depth + 1)));
}

/** Scales only reach a limit once animations and floats are done with them. */
const atLimit = (scale: number, limit: number) => Math.abs(scale / limit - 1) < 1e-3;

/** Levels offered as buttons; deeper levels are reached with 全部. */
const MAX_LEVEL_BUTTONS = 4;

function subscribeFullscreen(callback: () => void) {
  document.addEventListener('fullscreenchange', callback);
  return () => document.removeEventListener('fullscreenchange', callback);
}

export interface MindMapToolbarProps {
  markmap: Markmap | null;
  /** Fold level the map opened with, highlighted until the reader folds by hand. */
  initialLevel: number | null;
  fullscreenTargetRef: React.RefObject<HTMLElement | null>;
}

/**
 * Controls for a Markmap view: zoom (with the current scale), fit, show the
 * map to a level or in full, and fullscreen, on one frosted capsule.
 * Uses the view's public API and follows its zoom, fold and render events.
 */
export function MindMapToolbar({ markmap, initialLevel, fullscreenTargetRef }: MindMapToolbarProps) {
  const [scale, setScale] = useState(1);
  const [limits, setLimits] = useState<[number, number]>([0, Infinity]);
  const [depth, setDepth] = useState(0);
  const [folded, setFolded] = useState(0);
  const [level, setLevel] = useState<number | null>(initialLevel);
  // Fold events caused by our own buttons keep the highlighted level.
  const ownFold = useRef(false);

  const fullscreen = useSyncExternalStore(
    subscribeFullscreen,
    () => Boolean(fullscreenTargetRef.current) && document.fullscreenElement === fullscreenTargetRef.current,
    () => false,
  );
  const fullscreenSupported = useSyncExternalStore(
    subscribeFullscreen,
    () => typeof document.documentElement.requestFullscreen === 'function',
    () => false,
  );

  useEffect(() => setLevel(initialLevel), [initialLevel]);

  useEffect(() => {
    if (!markmap) return;
    const sync = () => {
      setScale(markmap.transform.k);
      setLimits(markmap.scaleLimits);
    };
    const syncTree = () => {
      setDepth(deepestParent(markmap.tree));
      setFolded(markmap.foldedIds.size);
      sync();
    };
    syncTree();
    const stops = [
      markmap.on('zoom', sync),
      markmap.on('render', syncTree),
      markmap.on('fold', (ids) => {
        setFolded(ids.size);
        if (ownFold.current) ownFold.current = false;
        else setLevel(null);
      }),
    ];
    return () => stops.forEach((stop) => stop());
  }, [markmap]);

  const foldTo = useCallback(
    (next: number | 'all') => {
      if (!markmap) return;
      ownFold.current = true;
      if (next === 'all') {
        markmap.expandAll();
        setLevel(Infinity);
      } else {
        markmap.foldToLevel(next);
        setLevel(next);
      }
    },
    [markmap],
  );

  const toggleFullscreen = useCallback(() => {
    const target = fullscreenTargetRef.current;
    if (!target) return;
    const request = document.fullscreenElement === target ? document.exitFullscreen() : target.requestFullscreen();
    request.catch(() => {
      // Fullscreen can be denied by the browser or an embedding host.
    });
  }, [fullscreenTargetRef]);

  const ready = Boolean(markmap);
  const levels = Array.from({ length: Math.min(depth, MAX_LEVEL_BUTTONS) }, (_, index) => index + 1);
  const allExpanded = ready && folded === 0;

  return (
    <div className="mind-map-toolbar" role="toolbar" aria-label="思维导图工具">
      <div className="mind-map-toolbar-group">
        <button
          type="button"
          className="mind-map-tool"
          title="缩小"
          aria-label="缩小"
          disabled={!ready || atLimit(scale, limits[0])}
          onClick={() => markmap?.zoomOut()}
        >
          <Minus aria-hidden="true" />
        </button>
        <output className="mind-map-toolbar-scale" aria-label="当前缩放">
          {Math.round(scale * 100)}%
        </output>
        <button
          type="button"
          className="mind-map-tool"
          title="放大"
          aria-label="放大"
          disabled={!ready || atLimit(scale, limits[1])}
          onClick={() => markmap?.zoomIn()}
        >
          <Plus aria-hidden="true" />
        </button>
      </div>

      <span className="mind-map-toolbar-divider" aria-hidden="true" />

      <button
        type="button"
        className="mind-map-tool"
        title="适应窗口"
        aria-label="适应窗口"
        disabled={!ready}
        onClick={() => markmap?.fit()}
      >
        <Scan aria-hidden="true" />
      </button>

      {levels.length > 0 ? (
        <>
          <span className="mind-map-toolbar-divider" aria-hidden="true" />
          <div className="mind-map-toolbar-levels" role="group" aria-label="展开到层级">
            <span className="mind-map-toolbar-label" aria-hidden="true">
              层级
            </span>
            {levels.map((value) => (
              <button
                key={value}
                type="button"
                className="mind-map-tool mind-map-tool-level"
                title={`只展开到第 ${value} 层`}
                aria-label={`只展开到第 ${value} 层`}
                aria-pressed={!allExpanded && level === value}
                disabled={!ready}
                onClick={() => foldTo(value)}
              >
                {value}
              </button>
            ))}
            <button
              type="button"
              className="mind-map-tool mind-map-tool-level mind-map-tool-all"
              title="全部展开"
              aria-label="全部展开"
              aria-pressed={allExpanded}
              disabled={!ready}
              onClick={() => foldTo('all')}
            >
              全部
            </button>
          </div>
        </>
      ) : null}

      <span className="mind-map-toolbar-divider" aria-hidden="true" />

      {fullscreenSupported ? (
        <button
          type="button"
          className="mind-map-tool"
          title={fullscreen ? '退出全屏' : '全屏查看'}
          aria-label={fullscreen ? '退出全屏' : '全屏查看'}
          aria-pressed={fullscreen}
          onClick={toggleFullscreen}
        >
          {fullscreen ? <Shrink aria-hidden="true" /> : <Expand aria-hidden="true" />}
        </button>
      ) : null}
    </div>
  );
}
