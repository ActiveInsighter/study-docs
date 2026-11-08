from common import record
LABEL = '孩子兄弟表示法：左指针指向第一个孩子，右指针指向右兄弟'
F = Fig(760, 520, '孩子兄弟表示法（二叉链表）')
# original tree
t = F.tree(30, 120, ('R', [('A', ['D', 'E']), 'B', ('C', [('F', ['G', 'H', 'K'])])]), unit=34, levelh=62, r=14, size=13)
F.text(118, 92, '原树', 13, color=MUTED)
F.line(214, 250, 244, 250, LINE, 1.5, arrow='end')
# record layout: (name, col, row)
cw, ch = 30, 28
P = {'R': (4, 0), 'A': (2, 1), 'D': (0, 2), 'E': (1.4, 3), 'B': (3.6, 2), 'C': (5, 3), 'F': (4, 4), 'G': (3, 5), 'H': (4.4, 6), 'K': (5.8, 7)}
fc = {'R': 'A', 'A': 'D', 'C': 'F', 'F': 'G'}
ns = {'A': 'B', 'D': 'E', 'B': 'C', 'G': 'H', 'H': 'K'}
X0, Y0, DX, DY = 262, 70, 62, 52
cent = {}
for k, (c, r) in P.items():
    x, y = X0 + c * DX, Y0 + r * DY
    fields = ['●' if k in fc else '^', k, '●' if k in ns else '^']
    cs = record(F, x, y, fields, cw, ch, {1: 'gray'})
    cent[k] = (x, y, cs)
for a, b in fc.items():
    (_, _, cs), (bx, by, _) = cent[a], cent[b]
    F.line(cs[0][0], cs[0][1], bx + 1.5 * cw, by, ACCENT['blue'], 1.5, arrow='end')
for a, b in ns.items():
    (_, _, cs), (bx, by, _) = cent[a], cent[b]
    F.line(cs[2][0], cs[2][1], bx + 1.5 * cw, by, ACCENT['amber'], 1.5, arrow='end')
F.legend(40, 492, [('blue', '左指针 firstchild：第一个孩子'), ('amber', '右指针 nextsibling：右兄弟')])
