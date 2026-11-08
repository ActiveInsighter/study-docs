LABEL = '无环图目录结构：允许多个目录项指向同一个共享文件 count'
F = Fig(560, 380, '无环图目录结构')
def dirn(x, y, n): F.cells(x, y, [''] * n, 30, 30, size=10); return [(x + 15 + i * 30, y + 30) for i in range(n)]
r = dirn(240, 50, 2); F.text(312, 66, 'root', 12, 'start', INK2, valign='middle')
d = dirn(60, 120, 4); F.text(184, 136, 'dict', 12, 'start', INK2, valign='middle')
s = dirn(380, 120, 3); F.text(474, 136, 'spell', 12, 'start', INK2, valign='middle')
F.line(*r[0], 120, 118, INK2, 1.2, arrow='end'); F.line(*r[1], 420, 118, INK2, 1.2, arrow='end')
F.circle(75, 200, 14, '', 'white'); F.text(75, 226, 'list', 11.5, color=INK2); F.line(*d[0], 75, 186, INK2, 1.1, arrow='end')
F.circle(270, 200, 14, '', 'blue'); F.text(270, 226, 'count', 11.5, color=ACCENT['blue'], weight=600)
F.rect(246, 176, 48, 58, 'none', ACCENT['blue'], 1.2, 4, dash='3 3')
F.line(*d[2], 258, 190, INK2, 1.1, arrow='end'); F.line(*s[0], 282, 190, INK2, 1.1, arrow='end')
F.circle(460, 200, 14, '', 'white'); F.text(460, 226, 'list', 11.5, color=INK2); F.line(*s[2], 460, 186, INK2, 1.1, arrow='end')
p = dirn(220, 250, 3); F.text(316, 266, 'p', 12, 'start', INK2, valign='middle')
F.line(*d[3], 240, 248, INK2, 1.1, arrow='end'); F.line(*s[1], 280, 248, INK2, 1.1, arrow='end')
for i, (x, t) in enumerate(((220, 'root'), (260, 'rade'), (300, 'W7'))):
    F.circle(x, 330, 14, '', 'white'); F.text(x, 360, t, 11, color=INK2); F.line(p[i][0], p[i][1], x, 316, INK2, 1.1, arrow='end')
F.line(d[1][0], d[1][1], 220, 316, INK2, 1.1, arrow='end')
