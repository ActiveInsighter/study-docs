import { describe, expect, it } from 'vitest';
import { optimizeStudySidebarTitle } from '@/lib/study-navigation-titles';

describe('Study Docs sidebar labels', () => {
  it('removes redundant subjects while retaining chapter topics', () => {
    expect(optimizeStudySidebarTitle('数据结构 第1章：绪论与算法复杂度', 'file')).toBe('第1章：绪论与算法复杂度');
    expect(optimizeStudySidebarTitle('计算机组成原理 第3章：存储系统', 'file')).toBe('第3章：存储系统');
    expect(optimizeStudySidebarTitle('操作系统 第2章：进程与线程', 'file')).toBe('第2章：进程与线程');
    expect(optimizeStudySidebarTitle('计算机网络 第6章：应用层', 'file')).toBe('第6章：应用层');
    expect(optimizeStudySidebarTitle('第 1 章 计算机系统概述', 'file')).toBe('第1章：计算机系统概述');
    expect(optimizeStudySidebarTitle('第2章：线性表', 'file')).toBe('第2章：线性表');
  });

  it('shortens repeated index and folder titles without touching meaningful names', () => {
    expect(optimizeStudySidebarTitle('408题型总结', 'folder')).toBe('题型总结');
    expect(optimizeStudySidebarTitle('408 知识点总结 2（优化版）', 'folder')).toBe('知识点总结 2');
    expect(optimizeStudySidebarTitle('408题型总结', 'file')).toBe('概览');
    expect(optimizeStudySidebarTitle('数据结构 · 408题型总结', 'file')).toBe('概览');
    expect(optimizeStudySidebarTitle('408 总览', 'file')).toBe('总览');
    expect(optimizeStudySidebarTitle('操作系统', 'folder')).toBe('操作系统');
    expect(optimizeStudySidebarTitle('树与二叉树', 'file')).toBe('树与二叉树');
  });
});
