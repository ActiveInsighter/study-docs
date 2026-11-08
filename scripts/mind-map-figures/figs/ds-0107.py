LABEL = '顺序队列的入队与出队'
F = Fig(760, 330, '顺序队列的入队与出队')
W, H = 44, 36
x = 70 + 40
vals = ['', '', '', '', '']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.text(x + W / 2, 292, '空队', 12.5, color=INK2)
yy = 250 - 0 * H - H / 2 + (6 if 0 == 0 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 0 * H - H / 2 + (-6 if 0 == 0 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 250 + 40
vals = ['a', 'b', 'c', 'd', 'e']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.text(x + W / 2, 292, '5 个元素入队', 12.5, color=INK2)
yy = 250 - 0 * H - H / 2 + (6 if 0 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 4.6 * H - H / 2 + (-6 if 0 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 430 + 40
vals = ['', 'b', 'c', 'd', 'e']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.text(x + W / 2, 292, '出队 1 次', 12.5, color=INK2)
yy = 250 - 1 * H - H / 2 + (6 if 1 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 4.6 * H - H / 2 + (-6 if 1 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
x = 610 + 40
vals = ['', '', '', '', 'e']
for i in range(5):
    y = 250 - (i + 1) * H
    F.box(x, y, W, H, vals[i], 'blue' if vals[i] else 'white', 14, 0, True)
F.text(x + W / 2, 292, '出队 3 次', 12.5, color=INK2)
yy = 250 - 4 * H - H / 2 + (6 if 4 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['green'], 1.3, arrow='end')
F.text(x - 44, yy, 'front', 11, 'end', ACCENT['green'], mono=True, valign='middle')
yy = 250 - 4.6 * H - H / 2 + (-6 if 4 == 5 else 0)
F.line(x - 40, yy, x - 4, yy, ACCENT['red'], 1.3, arrow='end')
F.text(x - 44, yy, 'rear', 11, 'end', ACCENT['red'], mono=True, valign='middle')
F.text(380, 318, '队空 front == rear；rear 指向队尾的下一位置。出队后前面空出的单元无法再用（假溢出）', 12.5, color=MUTED)
