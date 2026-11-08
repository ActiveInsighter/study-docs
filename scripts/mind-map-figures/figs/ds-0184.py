from common import bp_node, records
LABEL = '4 阶 B+ 树：分支结点只含索引，叶结点含全部关键字并相互链接'
F = Fig(860, 360, '4 阶 B+ 树')
root = bp_node(F, 404, 64, ['15', '56'], 'blue')
m1 = bp_node(F, 210, 132, ['3', '9', '15'], 'blue'); m2 = bp_node(F, 560, 132, ['35', '42', '56'], 'blue')
F.line(root[0][0], 88, m1[1][0], 132, INK2, 1.3, arrow='end'); F.line(root[1][0], 88, m2[1][0], 132, INK2, 1.3, arrow='end')
L = [['1', '3'], ['6', '8', '9'], ['13', '15'], ['30', '35'], ['40', '42'], ['47', '48', '50', '56']]
xs = [60, 160, 290, 400, 510, 620]
par = [m1[0], m1[1], m1[2], m2[0], m2[1], m2[2]]
F.text(32, 212, 'p', 13, 'end', ACCENT['red'], mono=True, valign='middle'); F.line(36, 212, 58, 212, ACCENT['red'], 1.3, arrow='end')
for i, (x, ks) in enumerate(zip(xs, L)):
    cs = bp_node(F, x, 200, ks)
    F.line(par[i][0], 156, cs[-1][0], 200, INK2, 1.3, arrow='end')
    for c in cs: records(F, c[0], 224)
    if i < 5: F.line(x + 26 * len(ks), 212, xs[i + 1] - 2, 212, ACCENT['green'], 1.3, arrow='end')
F.legend(40, 312, [('blue', '分支结点：只存各子树的最大关键字'), ('green', '叶结点：全部关键字 + 记录指针')])
F.text(430, 344, '叶结点按关键字递增链接：既可从 p 顺序查找，也可从根做多路查找', 12.5, color=MUTED)
