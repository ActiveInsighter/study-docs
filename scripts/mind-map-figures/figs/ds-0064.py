LABEL = '二叉树顺序存储的最坏情况：单支树也要 2^h−1 个单元'
F = Fig(860, 330, '顺序存储：结点编号与完全二叉树对应')
on = {1, 3, 7, 15}
def T(i):
    if i > 15: return None
    k = str(i)
    return k if i >= 8 else (k, [T(2 * i), T(2 * i + 1)])
F.tree(20, 80, T(1), unit=34, levelh=54, r=13, size=11, tones={str(i): ('blue' if i in on else 'light') for i in range(1, 16)})
vals = ['^'] + [str(i) if i in on else '^' for i in range(1, 16)]
F.cells(30, 280, vals, 34, 28, {i: 'blue' for i in on}, size=12, index=0)
x = 580
F.text(x, 96, '结点 i（下标从 1 开始）：', 13.5, 'start', INK, 600)
F.text(x, 122, '左孩子 2i，右孩子 2i + 1\n双亲 ⌊i/2⌋', 13.5, 'start', INK2, lh=1.6)
F.text(x, 192, '最坏情况：高度为 h、只有 h 个\n结点的单支树（右斜树），\n也至少需要 2^{h} − 1 个存储单元', 13.5, 'start', ACCENT['red'], lh=1.6)
