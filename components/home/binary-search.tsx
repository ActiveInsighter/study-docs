'use client';

import { useMemo, useState, type CSSProperties } from 'react';
import styles from './specimens.module.css';

/*
 * Binary search in the closed-interval form the algorithm notes teach
 * (`[left, right]`, `while (left <= right)`), one press per step.
 */

type Step = {
  left: number;
  right: number;
  mid: number | null;
  /** Highlighted line of the code listing. */
  line: number;
  found: boolean;
  text: string;
};

const CODE = [
  'while (left <= right) {',
  '  int mid = left + (right - left) / 2;',
  '  if (nums[mid] > target) right = mid - 1;',
  '  else if (nums[mid] < target) left = mid + 1;',
  '  else return mid;',
  '}',
];

function trace(nums: readonly number[], target: number): Step[] {
  let left = 0;
  let right = nums.length - 1;
  const steps: Step[] = [
    { left, right, mid: null, line: 0, found: false, text: `在 [${left}, ${right}] 里找 ${target}。区间两端都能取到，所以循环条件是 left <= right。` },
  ];
  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);
    const value = nums[mid] ?? 0;
    if (value > target) {
      steps.push({ left, right, mid, line: 2, found: false, text: `nums[${mid}] = ${value} > ${target}，答案在左半边：right = mid - 1 = ${mid - 1}。` });
      right = mid - 1;
    } else if (value < target) {
      steps.push({ left, right, mid, line: 3, found: false, text: `nums[${mid}] = ${value} < ${target}，答案在右半边：left = mid + 1 = ${mid + 1}。` });
      left = mid + 1;
    } else {
      steps.push({ left, right, mid, line: 4, found: true, text: `nums[${mid}] = ${value}，找到了，返回 ${mid}。共比较 ${steps.length} 次。` });
      return steps;
    }
  }
  steps.push({ left, right, mid: null, line: 0, found: false, text: `left > right，区间为空：${target} 不在数组里。` });
  return steps;
}

export function BinarySearch({ nums, target }: { nums: readonly number[]; target: number }) {
  const steps = useMemo(() => trace(nums, target), [nums, target]);
  const [at, setAt] = useState(0);
  const step = steps[at] ?? steps[0]!;
  const done = at === steps.length - 1;
  // Each step shows the interval being compared; the next step shows it narrowed.
  const pointerStyle = (index: number) => ({ '--at': index, '--count': nums.length }) as CSSProperties;

  return (
    <div className={styles.search}>
      <div className={styles.track} style={{ '--count': nums.length } as CSSProperties}>
        <div className={styles.pointers} aria-hidden="true">
          <span className={styles.pointer} style={pointerStyle(step.left)}>
            left
          </span>
          {step.mid !== null && (
            <span className={styles.pointerMid} style={pointerStyle(step.mid)}>
              mid
            </span>
          )}
          <span className={styles.pointer} style={pointerStyle(Math.max(step.right, 0))}>
            right
          </span>
        </div>
        <ol className={styles.cells} aria-label={`有序数组，目标 ${target}`}>
          {nums.map((value, index) => (
            <li
              key={index}
              className={styles.cellItem}
              data-out={index < step.left || index > step.right ? '' : undefined}
              data-mid={index === step.mid ? '' : undefined}
              data-found={step.found && index === step.mid ? '' : undefined}
            >
              <span className={styles.cellValue}>{value}</span>
              <span className={styles.cellIndex}>{index}</span>
            </li>
          ))}
        </ol>
      </div>
      <pre className={styles.code} aria-hidden="true">
        {CODE.map((line, index) => (
          <span key={index} data-active={step.mid !== null && index === step.line ? '' : undefined}>
            {line}
          </span>
        ))}
      </pre>
      <p className={styles.searchNote} aria-live="polite">
        {step.text}
      </p>
      <div className={styles.searchBar}>
        <button type="button" className={styles.stepButton} onClick={() => setAt((value) => value + 1)} disabled={done}>
          下一步
        </button>
        <button type="button" className={styles.textButton} onClick={() => setAt(0)} disabled={at === 0}>
          重来
        </button>
      </div>
    </div>
  );
}
