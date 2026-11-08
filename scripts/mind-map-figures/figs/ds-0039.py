from common import bp_node, records
LABEL = 'B+ 树：根结点是叶子时可以只有一个子树，非叶根至少两棵子树'
F = Fig(860, 300, 'B+ 树的根结点：非叶根至少有两棵子树')
def ptr(x, y):
    F.text(x - 34, y + 12, 'p', 13, 'end', ACCENT['red'], mono=True, valign='middle'); F.line(x - 30, y + 12, x - 2, y + 12, ACCENT['red'], 1.3, arrow='end')
# case 1
ptr(80, 120); cs = bp_node(F, 80, 120, ['15', '56']); [records(F, c[0], 132) for c in cs]
F.text(106, 74, '根结点就是叶子', 12.5, color=INK2); F.text(106, 252, '✓ 合法', 15, color=ACCENT['green'], weight=700)
# case 2
cs = bp_node(F, 390, 80, ['15', '56'], 'blue')
ptr(330, 140); c2 = bp_node(F, 330, 140, ['13', '15'])
F.line(cs[0][0] - 6, 92, c2[1][0], 140, INK2, 1.3, arrow='end')
[records(F, c[0], 152) for c in c2]
F.text(416, 66, '非叶根只有 1 棵子树', 12.5, color=INK2); F.text(390, 252, '✗ 不合法', 15, color=ACCENT['red'], weight=700)
# case 3
cs = bp_node(F, 680, 80, ['15', '56'], 'blue')
ptr(610, 140); a = bp_node(F, 610, 140, ['13', '15']); b = bp_node(F, 680, 140, ['47', '48', '50', '56'])
F.line(a[-1][0] + 14, 152, 678, 152, INK2, 1.2, arrow='end')
F.line(cs[0][0], 92, a[1][0], 140, INK2, 1.3, arrow='end'); F.line(cs[1][0], 92, b[-1][0], 140, INK2, 1.3, arrow='end')
[records(F, c[0], 152) for c in a + b]
F.text(706, 66, '非叶根有 2 棵子树', 12.5, color=INK2); F.text(706, 252, '✓ 合法', 15, color=ACCENT['green'], weight=700)
F.legend(40, 284, [('blue', '分支结点'), ('green', '叶结点'), ('light', 'p：头指针，指向第一个叶结点')])
