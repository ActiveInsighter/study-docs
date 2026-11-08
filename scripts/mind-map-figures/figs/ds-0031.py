from common import bnode
LABEL = 'B 树：终端结点与叶结点（失败结点）'
F = Fig(860, 390, 'm 阶 B 树（m = 5）')
r = bnode(F, 430, 76, ['22'], 1, kw=36)
L = bnode(F, 220, 170, ['5', '11'], 2, kw=34)
R = bnode(F, 640, 170, ['36', '45'], 2, kw=34)
F.line(r[0][0], r[0][1], 220, 164, INK2, 1.3, arrow='end'); F.line(r[1][0], r[1][1], 640, 164, INK2, 1.3, arrow='end')
leaves = [(70, ['1', '3'], L, 0), (200, ['6', '8', '9'], L, 1), (330, ['13', '15'], L, 2), (470, ['30', '35'], R, 0), (590, ['40', '42'], R, 1), (740, ['47', '48', '50', '56'], R, 2)]
for cx, ks, par, i in leaves:
    a = bnode(F, cx, 262, ks, len(ks), kw=30, size=12)
    F.line(par[i][0], par[i][1], cx, 256, INK2, 1.3, arrow='end')
    for j in range(len(ks) + 1):
        F.line(a[j][0], a[j][1] + 3, a[j][0], a[j][1] + 22, LINE, 1.1, arrow='end')
        F.rect(a[j][0] - 7, a[j][1] + 24, 14, 16, 'violet', ACCENT['violet'], 1, 3, dash='2 2')
F.legend(40, 340, [('blue', '终端结点（最底层的非叶结点）'), ('violet', '叶结点 = 失败结点，实际不存在')])
F.text(430, 374, '所有叶结点都在同一层；n 个关键字的 B 树有 n + 1 个叶结点', 12.5, color=MUTED)
