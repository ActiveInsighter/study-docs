'use client';

import clsx from 'clsx';
import { IntentLink as Link } from '@/components/intent-link';
import { Fragment, useState, type CSSProperties } from 'react';
import type { MindMapLayout } from '@/lib/home/mind-map-layout';
import home from './home.module.css';
import styles from './mind-map.module.css';

/*
 * The hero mind map. Geometry comes precomputed from the server
 * (lib/home/mind-map-layout.ts); this component only adds the focus state:
 * pointing at or tabbing into a module brings its branch forward and fades
 * the rest. Branches grow out from the centre once on load (CSS only).
 */
export function MindMap({ layout, rootLabel }: { layout: MindMapLayout; rootLabel: string }) {
  const [active, setActive] = useState<string | null>(null);
  const dim = (key: string) => (active !== null && active !== key ? '' : undefined);
  const focusProps = (key: string) => ({
    onPointerEnter: () => setActive(key),
    onFocus: () => setActive(key),
  });

  return (
    <nav
      className={styles.map}
      style={{ height: layout.height }}
      aria-label="学习目录"
      onPointerLeave={() => setActive(null)}
      onBlur={(event) => {
        if (!event.currentTarget.contains(event.relatedTarget as Node | null)) setActive(null);
      }}
    >
      <svg className={styles.edges} viewBox={`0 0 100 ${layout.height}`} preserveAspectRatio="none" aria-hidden="true">
        {layout.branches.map((branch) => (
          <g key={branch.key} className={clsx(home.tone, styles.branch)} data-tone={branch.tone} data-dim={dim(branch.key)}>
            <path d={branch.trunk} className={styles.trunk} vectorEffect="non-scaling-stroke" />
            {branch.twigs.map((twig, index) => (
              <path key={index} d={twig} className={styles.twig} vectorEffect="non-scaling-stroke" />
            ))}
          </g>
        ))}
      </svg>

      <span className={styles.root} style={{ left: `${layout.root.x}%`, top: layout.root.y }}>
        {rootLabel}
      </span>

      {layout.branches.map((branch, branchIndex) => (
        <Fragment key={branch.key}>
          <Link
            href={branch.href}
            className={clsx(home.tone, styles.module)}
            data-tone={branch.tone}
            data-dim={dim(branch.key)}
            style={{ left: `${branch.x}%`, top: branch.y, '--delay': `${180 + branchIndex * 70}ms` } as CSSProperties}
            {...focusProps(branch.key)}
          >
            {branch.name}
            <span className={styles.count}>{branch.pages}</span>
          </Link>
          {branch.leaves.map((leaf, leafIndex) => (
            <Link
              key={leaf.href + leaf.name}
              href={leaf.href}
              className={clsx(home.tone, styles.leaf)}
              data-tone={branch.tone}
              data-side={branch.side}
              data-more={leaf.more ? '' : undefined}
              data-dim={dim(branch.key)}
              style={{ left: `${leaf.x}%`, top: leaf.y, '--delay': `${420 + branchIndex * 70 + leafIndex * 35}ms` } as CSSProperties}
              {...focusProps(branch.key)}
            >
              <span className={styles.label}>{leaf.name}</span>
              {leaf.pages !== null && <span className={styles.count}>{leaf.pages}</span>}
            </Link>
          ))}
        </Fragment>
      ))}
    </nav>
  );
}
