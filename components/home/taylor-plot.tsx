'use client';

import { useId, useMemo, useState } from 'react';
import styles from './specimens.module.css';

/*
 * The Maclaurin formula from the formula handbook, drawn: the slider adds
 * terms and the polynomial closes in on eˣ around x = 0.
 */

const X = [-3.2, 2.4] as const;
const Y = [-1.4, 8] as const;
const WIDTH = 320;
const HEIGHT = 190;
const MAX_TERMS = 6;

const sx = (x: number) => ((x - X[0]) / (X[1] - X[0])) * WIDTH;
const sy = (y: number) => HEIGHT - ((y - Y[0]) / (Y[1] - Y[0])) * HEIGHT;

function factorial(n: number): number {
  return n <= 1 ? 1 : n * factorial(n - 1);
}

function path(fn: (x: number) => number): string {
  const points: string[] = [];
  const steps = 160;
  for (let index = 0; index <= steps; index++) {
    const x = X[0] + ((X[1] - X[0]) * index) / steps;
    // Clamp far outside the view so the clip path trims the curve cleanly.
    const y = Math.max(Y[0] - 4, Math.min(Y[1] + 4, fn(x)));
    points.push(`${index ? 'L' : 'M'}${sx(x).toFixed(1)} ${sy(y).toFixed(1)}`);
  }
  return points.join(' ');
}

const exponential = path(Math.exp);
const SUBSCRIPTS = '₀₁₂₃₄₅₆₇₈₉';

export function TaylorPlot({ formulaHtml }: { formulaHtml: string }) {
  const [terms, setTerms] = useState(2);
  const clipId = useId();
  const polynomial = useMemo(
    () => path((x) => Array.from({ length: terms + 1 }, (_, k) => x ** k / factorial(k)).reduce((sum, value) => sum + value, 0)),
    [terms],
  );
  const error = Math.abs(Math.exp(1) - Array.from({ length: terms + 1 }, (_, k) => 1 / factorial(k)).reduce((a, b) => a + b, 0));

  return (
    <div className={styles.taylor}>
      <div className={styles.formula} dangerouslySetInnerHTML={{ __html: formulaHtml }} />
      <svg className={styles.plot} viewBox={`0 0 ${WIDTH} ${HEIGHT}`} role="img" aria-label={`eˣ 与 ${terms} 阶麦克劳林多项式的图像`}>
        <defs>
          <clipPath id={clipId}>
            <rect width={WIDTH} height={HEIGHT} />
          </clipPath>
        </defs>
        {[-2, -1, 1, 2].map((x) => (
          <line key={`x${x}`} className={styles.gridLine} x1={sx(x)} x2={sx(x)} y1={0} y2={HEIGHT} />
        ))}
        {[2, 4, 6].map((y) => (
          <line key={`y${y}`} className={styles.gridLine} x1={0} x2={WIDTH} y1={sy(y)} y2={sy(y)} />
        ))}
        <line className={styles.axis} x1={0} x2={WIDTH} y1={sy(0)} y2={sy(0)} />
        <line className={styles.axis} x1={sx(0)} x2={sx(0)} y1={0} y2={HEIGHT} />
        <g clipPath={`url(#${clipId})`}>
          <path className={styles.curveExact} d={exponential} />
          <path className={styles.curveApprox} d={polynomial} />
        </g>
        <text className={styles.plotLabel} x={sx(1.55)} y={sy(6.6)}>
          y = eˣ
        </text>
        <text className={styles.plotLabelTone} x={sx(-3.05)} y={sy(7.1)}>
          P{String(terms)
            .split('')
            .map((digit) => SUBSCRIPTS[Number(digit)])
            .join('')}
          (x)
        </text>
      </svg>
      <label className={styles.slider}>
        <span>
          展开到 <strong>n = {terms}</strong>
        </span>
        <input type="range" min={0} max={MAX_TERMS} step={1} value={terms} onChange={(event) => setTerms(Number(event.target.value))} />
        <span className={styles.sliderNote}>x = 1 处误差 {error < 0.001 ? error.toExponential(1) : error.toFixed(3)}</span>
      </label>
    </div>
  );
}
