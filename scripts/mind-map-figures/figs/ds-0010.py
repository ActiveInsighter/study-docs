from common import bnode, code
LABEL = '5 叉查找树：每个结点最多 4 个关键字、5 个分叉'
F = Fig(900, 520, '5 叉查找树')
code(F, 30, 84, '//5 叉排序树结点定义\nstruct Node {\n  ElemType keys[4];     //最多 4 个关键字\n  struct Node *child[5];//最多 5 个孩子\n  int num;              //结点中有几个关键字\n};', 12.5)
F.box(640, 90, 230, 56, '最少 1 个关键字、2 个分叉\n最多 4 个关键字、5 个分叉', 'amber', 13, 10)
r = bnode(F, 520, 120, ['22'], 4)
L = bnode(F, 260, 240, ['5', '11'], 4)
R = bnode(F, 700, 240, ['36', '45'], 4)
F.line(r[0][0], r[0][1], 260, 234, INK2, 1.4, arrow='end')
F.line(r[1][0], r[1][1], 700, 234, INK2, 1.4, arrow='end')
leaves = [(95, ['1', '3'], L, 0), (245, ['6', '8', '9'], L, 1), (395, ['13', '15'], L, 2),
          (545, ['30', '35'], R, 0), (690, ['40', '42'], R, 1), (818, ['47', '48', '50', '56'], R, 2)]
for cx, ks, par, i in leaves:
    a = bnode(F, cx, 360, ks, 4, kw=30, size=12)
    F.line(par[i][0], par[i][1], cx, 354, INK2, 1.4, arrow='end')
    for j in range(len(ks) + 1):
        F.line(a[j][0], a[j][1] + 4, a[j][0], a[j][1] + 30, LINE, 1.2, arrow='end')
        F.rect(a[j][0] - 7, a[j][1] + 32, 14, 16, 'violet', ACCENT['violet'], 1, 3, dash='2 2')
F.legend(30, 498, [('blue', '关键字'), ('violet', '失败结点（查找到此即失败）')])
