LABEL = 'B 树每个关键字都带有对应记录的指针'
F = Fig(640, 270, 'B 树：每个关键字都直接指向记录')
def node(cx, y, ks):
    w = 44 * len(ks)
    F.cells(cx - w / 2, y, ks, 44, 34, {i: 'blue' for i in range(len(ks))}, size=15)
    return cx - w / 2, w
x, w = node(260, 66, ['22'])
F.box(350, 70, 76, 26, '记录', 'light', 13, 5); F.line(282, 83, 348, 83, INK2, 1.3, arrow='end')
lx, lw = node(140, 160, ['5', '11'])
rx, rw = node(400, 160, ['36', '45'])
F.line(240, 100, 160, 158, INK2, 1.3, arrow='end'); F.line(280, 100, 380, 158, INK2, 1.3, arrow='end')
F.box(240, 164, 76, 26, '记录', 'light', 13, 5); F.line(378, 177, 318, 177, INK2, 1.3, arrow='end')
F.box(508, 164, 76, 26, '记录', 'light', 13, 5); F.line(444, 177, 506, 177, INK2, 1.3, arrow='end')
for bx in (lx, lx + 44, lx + 88, rx, rx + 44, rx + 88):
    F.line(bx, 194, bx + (-14 if bx in (lx, rx) else 0 if bx in (lx + 44, rx + 44) else 14), 228, LINE, 1.2, arrow='end')
F.text(560, 248, '查到关键字即可取到记录，不必走到叶子', 12.5, 'end', MUTED)
