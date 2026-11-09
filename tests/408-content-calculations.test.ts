import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';

function section(chapter: string, number: number) {
  const dir = join(process.cwd(), 'content/docs/408/mind-maps', chapter);
  const prefix = chapter.split('/').at(-1)!.slice(0, 2) + '-' + number + '-';
  const file = readdirSync(dir).find((name) => name.startsWith(prefix) && name.endsWith('.mdx'))!;
  return readFileSync(join(dir, file), 'utf8');
}

describe('408 documented calculation examples', () => {
  it('recalculates the UDP checksum from the actual documented 16-bit words', () => {
    const text = section('computer-networks/05-transport-layer', 6);
    const words = /校验分组依次：`([^`]+)`/.exec(text)![1].split(' ').map((word) => parseInt(word, 16));
    let sum = words.reduce((a, b) => a + b, 0);
    while (sum > 0xffff) sum = (sum & 0xffff) + (sum >>> 16);
    const checksum = (sum ^ 0xffff).toString(16).toUpperCase().padStart(4, '0');
    expect(text).toContain('`0x' + sum.toString(16).toUpperCase() + '`');
    expect(text).toContain('**`0x' + checksum + '`**');
  });

  it('verifies CRC remainder and divisibility of the transmitted codeword', () => {
    const text = section('computer-networks/03-data-link-layer', 3);
    const data = /D=([01]+)/.exec(text)![1];
    const generator = /除数比特`([01]+)`/.exec(text)![1];
    const divide = (value: number) => {
      const divisor = parseInt(generator, 2);
      while (value >= 2 ** (generator.length - 1)) {
        const shift = Math.floor(Math.log2(value)) - generator.length + 1;
        value ^= divisor << shift;
      }
      return value;
    };
    const padded = parseInt(data, 2) << (generator.length - 1);
    const remainder = divide(padded);
    expect(text).toContain('异或除法余数：`' + remainder.toString(2).padStart(generator.length - 1, '0') + '`');
    expect(divide(padded ^ remainder)).toBe(0);
  });

  it('simulates the exact FIFO reference string for both documented frame counts', () => {
    const text = section('operating-systems/03-memory', 16);
    const references = /引用串：\$([^$]+)\$/.exec(text)![1].split(',').map(Number);
    for (const capacity of [3, 4]) {
      const frames: number[] = [];
      let faults = 0;
      for (const page of references) {
        if (frames.includes(page)) continue;
        faults++;
        if (frames.length === capacity) frames.shift();
        frames.push(page);
      }
      expect(text).toContain(`${capacity}个页框：**${faults}次缺页**`);
    }
  });

  it('checks tridiagonal packing and inverse mapping for every band entry through n=20', () => {
    const text = section('data-structures/03-stacks-queues-arrays', 9);
    const [, factor, offset] = /k=(\d+)i\+j-(\d+)/.exec(text)!;
    expect(text).toContain('i=\\left\\lfloor\\frac{k+1}{3}\\right\\rfloor+1');
    for (let n = 2; n <= 20; n++) {
      let index = 0;
      for (let i = 1; i <= n; i++) {
        for (let j = Math.max(1, i - 1); j <= Math.min(n, i + 1); j++) {
          const k = Number(factor) * i + j - Number(offset);
          expect(k).toBe(index++);
          const row = Math.floor((k + 1) / 3) + 1;
          expect([row, k - 2 * row + 3]).toEqual([i, j]);
        }
      }
      expect(index).toBe(3 * n - 2);
    }
  });

  it('validates the printed Bankers safe sequence against Allocation and Need', () => {
    const text = section('operating-systems/02-processes', 20);
    const processes = new Map([...text.matchAll(/P(\d)：`\(([^)]+)\) \/ \(([^)]+)\)`/g)].map((m) => [Number(m[1]), { allocation: m[2].split(',').map(Number), need: m[3].split(',').map(Number) }]));
    expect(processes.size).toBe(5);
    const work = /Available=\(([^)]+)\)/.exec(text)![1].split(',').map(Number);
    const sequence = /安全序列 \*\*([^*]+)\*\*/.exec(text)![1].match(/P\d/g)!.map((p) => Number(p.slice(1)));
    expect(new Set(sequence).size).toBe(5);
    for (const id of sequence) {
      const process = processes.get(id)!;
      expect(process.need.every((need, j) => need <= work[j]), 'P' + id).toBe(true);
      process.allocation.forEach((allocation, j) => { work[j] += allocation; });
    }
    expect(work).toEqual([10, 5, 7]);
  });

  it('checks the documented interleaved-memory throughput example', () => {
    const text = section('computer-organization/03-memory-system', 7);
    const [, cycle, interval, banks, reads, duration] = /T=(\d+)\\,\\mathrm\{ns\},\\ r=(\d+)\\,\\mathrm\{ns\}\$，至少(\d+)体；连续(\d+)字耗(\d+)ns/.exec(text)!;
    expect(Math.ceil(Number(cycle) / Number(interval))).toBe(Number(banks));
    expect(Number(cycle) + (Number(reads) - 1) * Number(interval)).toBe(Number(duration));
  });
});
