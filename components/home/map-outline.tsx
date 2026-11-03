import clsx from 'clsx';
import { IntentLink as Link } from '@/components/intent-link';
import type { MindMapLayout } from '@/lib/home/mind-map-layout';
import home from './home.module.css';
import styles from './mind-map.module.css';

/**
 * The same map as an outline (a mind-map app's outline view), for screens too
 * narrow to draw branches. Plain server-rendered links in source order.
 */
export function MapOutline({ layout, rootLabel }: { layout: MindMapLayout; rootLabel: string }) {
  return (
    <nav className={styles.outline} aria-label="学习目录">
      <span className={styles.outlineRoot}>{rootLabel}</span>
      <ul className={styles.outlineModules}>
        {layout.branches.map((branch) => (
          <li key={branch.key} className={home.tone} data-tone={branch.tone}>
            <Link href={branch.href} className={styles.outlineModule}>
              {branch.name}
              <span className={styles.count}>{branch.pages}</span>
            </Link>
            <ul className={styles.outlineLeaves}>
              {branch.leaves.map((leaf) => (
                <li key={leaf.href + leaf.name}>
                  <Link href={leaf.href} className={clsx(styles.outlineLeaf)} data-more={leaf.more ? '' : undefined}>
                    <span className={styles.label}>{leaf.name}</span>
                    {leaf.pages !== null && <span className={styles.count}>{leaf.pages}</span>}
                  </Link>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </nav>
  );
}
