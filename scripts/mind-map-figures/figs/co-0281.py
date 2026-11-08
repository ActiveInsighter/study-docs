LABEL = '高位交叉编址：高位 2 bit为体号'
F = Fig(720, 380, '高位交叉编址的多体存储器')
tone = 'blue'
LAB = [[(0, '0'), (1, '1'), (5, 'n−1')], [(0, 'n'), (1, 'n+1'), (5, '2n−1')], [(0, '2n'), (1, '2n+1'), (5, '3n−1')], [(0, '3n'), (1, '3n+1'), (5, '4n−1')]]
for m in range(4):
    x = 90 + m * 160
    F.text(x + 35, 66, 'M_{%d}' % m, 14, color=INK, weight=700)
    for r in range(6):
        y = 76 + r * 30
        F.rect(x, y, 70, 30, 'white' if r not in (2, 3) else '#fafafa', INK2, 1.2, 0)
        if r in (2, 3): F.text(x + 35, y + 15, '⋮', 12, color=MUTED, valign='middle')
    for r, t in LAB[m]:
        F.text(x - 8, 91 + r * 30, t, 12, 'end', ACCENT[tone] if r == 0 else INK2, mono=True, valign='middle')
    F.line(x + 35, 300, x + 35, 258, INK2, 1.2, dash='4 3', arrow='end')
F.line(125, 300, 605, 300, INK2, 1.2, dash='4 3')
F.box(300, 304, 100, 28, '地址译码', 'white', 12.5, 4)
F.cells(250, 344, ['体号', '体内地址'], 100, 28, {0: 'blue'}, size=12.5, mono=False)
F.poly([(300, 344), (300, 280), (60, 280), (60, 190), (88, 190)], ACCENT['blue'], 1.3, arrow='end')
for m in range(1, 4): F.poly([(60 + m * 160, 280), (60 + m * 160, 190), (88 + m * 160, 190)], ACCENT['blue'], 1.3, arrow='end')
F.text(580, 360, '连续地址落在同一个体中', 12, color=MUTED)
