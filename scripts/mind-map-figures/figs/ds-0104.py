from common import bp_node, records
LABEL = 'B+ 树的叶结点：包含全部关键字与记录指针，相邻叶子互相链接'
F = Fig(860, 220, 'B+ 树的叶结点层')
L = [['1', '3'], ['6', '8', '9'], ['13', '15'], ['30', '35'], ['40', '42'], ['47', '48', '50', '56']]
xs = [60, 170, 300, 410, 520, 630]
F.text(32, 92, 'p', 13, 'end', ACCENT['red'], mono=True, valign='middle'); F.line(36, 92, 58, 92, ACCENT['red'], 1.3, arrow='end')
for i, (x, ks) in enumerate(zip(xs, L)):
    cs = bp_node(F, x, 80, ks)
    F.line(cs[-1][0], 50, cs[-1][0], 78, LINE, 1.2, dash='3 3', arrow='end')
    for c in cs: records(F, c[0], 104)
    if i < 5: F.line(x + 26 * len(ks), 92, xs[i + 1] - 2, 92, ACCENT['green'], 1.3, arrow='end')
F.text(430, 200, '每个关键字对应一条记录的指针；叶结点链表支持顺序查找与范围查询', 12.5, color=MUTED)
