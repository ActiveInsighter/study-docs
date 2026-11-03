'use client';

import { useState } from 'react';
import styles from './specimens.module.css';

/** Recitation drill: answers sit under a highlighter strip until tapped. */
export function RecallList({ items }: { items: readonly { prompt: string; answer: string }[] }) {
  const [shown, setShown] = useState<ReadonlySet<number>>(() => new Set());
  const allShown = shown.size === items.length;
  const toggle = (index: number) =>
    setShown((current) => {
      const next = new Set(current);
      if (next.has(index)) next.delete(index);
      else next.add(index);
      return next;
    });

  return (
    <div className={styles.recall}>
      <ol className={styles.recallList}>
        {items.map((item, index) => {
          const open = shown.has(index);
          return (
            <li key={item.prompt}>
              <p className={styles.recallPrompt}>{item.prompt}</p>
              <button
                type="button"
                className={styles.recallAnswer}
                data-open={open ? '' : undefined}
                aria-expanded={open}
                onClick={() => toggle(index)}
              >
                <span aria-hidden={!open}>{item.answer}</span>
                {!open && <span className={styles.srOnly}>揭开答案</span>}
              </button>
            </li>
          );
        })}
      </ol>
      <button
        type="button"
        className={styles.textButton}
        onClick={() => setShown(allShown ? new Set() : new Set(items.map((_, index) => index)))}
      >
        {allShown ? '全部遮住' : '全部揭开'}
      </button>
    </div>
  );
}
