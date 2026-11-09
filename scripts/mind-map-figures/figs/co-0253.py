LABEL = '低位交叉编址：低位 2 bit为体号'
F = Fig(720, 380, '低位交叉编址的多体存储器')
tone = 'amber'
LAB = [[(0, '0'), (1, '4'), (5, '4n−4')], [(0, '1'), (1, '5'), (5, '4n−3')], [(0, '2'), (1, '6'), (5, '4n−2')], [(0, '3'), (1, '7'), (5, '4n−1')]]
for m in range(4):
    x = 90 + m * 160
    F.text(x + 35, 66, 'M_{%d}' % m, 14, color=INK, weight=700)
    for r in range(6):
        y = 76 + r * 30
        F.rect(x, y, 70, 30, 'white' if r not in (2, 3) else '#fafafa', INK2, 1.2, 0)
        if r in (2, 3): F.text(x + 35, y + 15, '⋮', 12, color=MUTED, valign='middle')
    for r, t in LAB[m]:
        F.text(x + 78, 91 + r * 30, t, 12, 'start', ACCENT[tone] if r == 0 else INK2, mono=True, valign='middle')
    F.line(x + 35, 300, x + 35, 258, INK2, 1.2, dash='4 3', arrow='end')
F.line(125, 300, 605, 300, INK2, 1.2, dash='4 3')
F.box(300, 304, 100, 28, '地址译码', 'white', 12.5, 4)
F.cells(250, 344, ['体内地址', '体号'], 100, 28, {1: 'amber'}, size=12.5, mono=False)
F.poly([(400, 344), (400, 280), (60, 280), (60, 120), (88, 120)], ACCENT['amber'], 1.3, arrow='end')
for m in range(1, 4): F.poly([(60 + m * 160, 280), (60 + m * 160, 120), (88 + m * 160, 120)], ACCENT['amber'], 1.3, arrow='end')
F.text(580, 360, '连续地址依次落在不同的体中', 12, color=MUTED)
