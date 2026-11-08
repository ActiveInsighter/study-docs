LABEL = '循环队列的入队与出队'
F = Fig(760, 330, '循环队列的入队与出队')
W, H = 44, 36
x = 70 + 40
vals = ['', '', '', '', '']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.poly([(x + W / 2, 250), (x + W / 2, 264), (x + W + 14, 264), (x + W + 14, 64), (x + W / 2, 64), (x + W / 2, 70)], LINE, 1.2, arrow='end')
F.text(x + W / 2, 292, '空队', 12.5, color=INK2)
yy = 250 - 0 * H - H / 2 + (6 if 0 == 0 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 0 * H - H / 2 + (-6 if 0 == 0 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 250 + 40
vals = ['a', 'b', 'c', 'd', '']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.poly([(x + W / 2, 250), (x + W / 2, 264), (x + W + 14, 264), (x + W + 14, 64), (x + W / 2, 64), (x + W / 2, 70)], LINE, 1.2, arrow='end')
F.text(x + W / 2, 292, '4 个元素入队（队满）', 12.5, color=INK2)
yy = 250 - 0 * H - H / 2 + (6 if 0 == 4 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 4 * H - H / 2 + (-6 if 0 == 4 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 430 + 40
vals = ['', '', '', 'd', '']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.poly([(x + W / 2, 250), (x + W / 2, 264), (x + W + 14, 264), (x + W + 14, 64), (x + W / 2, 64), (x + W / 2, 70)], LINE, 1.2, arrow='end')
F.text(x + W / 2, 292, '出队 3 次', 12.5, color=INK2)
yy = 250 - 3 * H - H / 2 + (6 if 3 == 4 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 4 * H - H / 2 + (-6 if 3 == 4 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 610 + 40
vals = ['f', 'g', '', 'd', 'e']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.poly([(x + W / 2, 250), (x + W / 2, 264), (x + W + 14, 264), (x + W + 14, 64), (x + W / 2, 64), (x + W / 2, 70)], LINE, 1.2, arrow='end')
F.text(x + W / 2, 292, '3 个元素入队（队满）', 12.5, color=INK2)
yy = 250 - 3 * H - H / 2 + (6 if 3 == 2 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 2 * H - H / 2 + (-6 if 3 == 2 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
F.text(380, 318, '牺牲一个单元区分队空与队满：队满 (rear+1) % MaxSize == front', 12.5, color=MUTED)
