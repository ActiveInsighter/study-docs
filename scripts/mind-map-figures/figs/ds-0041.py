LABEL = '稀疏矩阵的十字链表存储'
F = Fig(860, 380, '稀疏矩阵的压缩存储：十字链表法')
M = [['0','0','4','0','0','5'], ['0','3','0','9','0','0'], ['0','0','0','0','7','0'], ['0','2','0','0','0','0'], ['0','0','0','0','0','0']]
for c in range(6): F.text(64 + c * 30, 78, str(c + 1), 12, color=ACCENT['red'], mono=True)
for r, row in enumerate(M):
    F.text(40, 100 + r * 28, str(r + 1), 12, color=ACCENT['green'], mono=True, valign='middle')
    for c, v in enumerate(row):
        F.text(64 + c * 30, 100 + r * 28, v, 13, color=INK if v != '0' else LINE, mono=True, weight=600 if v != '0' else 400, valign='middle')
F.text(30, 270, '非零结点：', 12.5, 'start', INK2)
F.cells(100, 256, ['行', '列', '值'], 40, 24, size=11.5, mono=False)
F.cells(100, 280, ['down', '', 'right'], 40, 24, {0: 'green', 2: 'amber'}, size=10.5, mono=False)
F.text(100, 326, 'down：同列下一个元素　right：同行下一个元素', 11.5, 'start', MUTED)
X0, Y0, cw, rh = 330, 66, 82, 56
for c in range(6):
    F.box(X0 + 40 + c * cw, Y0, 60, 22, str(c + 1), 'amber', 12, 3, True)
for r in range(5):
    F.box(X0, Y0 + 40 + r * rh, 30, 26, str(r + 1), 'green', 12, 3, True)
nz = [(1, 3, 4), (1, 6, 5), (2, 2, 3), (2, 4, 9), (3, 5, 7), (4, 2, 2)]
pos = {}
for (r, c, v) in nz:
    x, y = X0 + 40 + (c - 1) * cw, Y0 + 40 + (r - 1) * rh
    F.cells(x, y, [str(r), str(c), v], 20, 26, {2: 'blue'}, size=11)
    pos[(r, c)] = (x, y)
for r in range(1, 6):
    row = sorted(c for (rr, c, v) in nz if rr == r)
    px, py = X0 + 30, Y0 + 53 + (r - 1) * rh
    for c in row:
        x, y = pos[(r, c)]
        F.line(px, py, x - 2, y + 13, ACCENT['green'], 1.2, arrow='end')
        px = x + 60
for c in range(1, 7):
    col = sorted(r for (r, cc, v) in nz if cc == c)
    px, py = X0 + 70 + (c - 1) * cw, Y0 + 22
    for r in col:
        x, y = pos[(r, c)]
        F.line(px, py, x + 30, y - 2, ACCENT['amber'], 1.2, arrow='end')
        px, py = x + 30, y + 26
F.text(600, 364, '行头指针（绿）串起同一行的非零元，列头指针（橙）串起同一列的非零元', 12, color=MUTED)
