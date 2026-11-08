import math
LABEL = '循环缓冲：in 指向下一个可冲入数据的空缓冲区，out 指向下一个可取出数据的满缓冲区'
F = Fig(420, 356, '循环缓冲')
pos = {}
for i in range(6):
    a = -math.pi / 2 + i * math.pi / 3
    pos[i + 1] = (210 + 110 * math.cos(a), 180 + 110 * math.sin(a))
for i in range(1, 7):
    a, b = pos[i], pos[i % 6 + 1]
    F.line(*a, *b, INK2, 1.4, arrow='end', gap=24, gap2=26)
for i, (x, y) in pos.items(): F.box(x - 22, y - 18, 44, 36, str(i), 'blue' if i in (1, 2, 3) else 'amber', 13, 6)
F.text(210, 50, 'in ↓', 12.5, color=ACCENT['blue'], weight=600); F.text(330, 236, '← out', 12.5, 'start', ACCENT['blue'], weight=600)
F.legend(110, 342, [('blue', '装满数据'), ('amber', '空缓冲区')])
