LABEL = '缓冲池：空缓冲队列、输入队列、输出队列与四种工作缓冲区'
F = Fig(700, 380, '缓冲池')
for i, (t, tone) in enumerate((('空缓冲队列', 'green'), ('输入队列', 'amber'), ('输出队列', 'red'))):
    y = 60 + i * 44
    F.text(150, y + 14, t + '：', 12, 'end', INK2, valign='middle')
    for j in range(4):
        F.box(160 + j * 80, y, 60, 28, '', tone, rx=6)
        F.line(222 + j * 80, y + 14, 238 + j * 80, y + 14, INK2, 1.2, arrow='end')
    F.text(490, y + 14, '……', 12, color=MUTED, valign='middle')
F.rect(260, 210, 240, 140, 'none', INK2, 1.2, 4); F.text(380, 226, '缓冲池', 12, color=INK2)
for (x, y, t) in ((290, 240, 'hin'), (400, 240, 'sin'), (290, 300, 'sout'), (400, 300, 'hout')): F.box(x, y, 70, 28, t, 'white', 12, 3, True)
F.box(560, 250, 50, 60, '用户\n程序', 'white', 12, 3)
F.items.append('<path d="M60 246H120L132 258L120 270H60Z" fill="#fdf1d8" stroke="#c98a12" stroke-width="1.2"/>'); F.items.append('<path d="M60 300H120V330L90 322L60 330Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.2"/>')
F.line(134, 254, 288, 254, INK2, 1.2, arrow='end'); F.text(200, 244, '收容输入', 11, color=INK2)
F.line(288, 314, 122, 314, INK2, 1.2, arrow='end'); F.text(200, 304, '提取输出', 11, color=INK2)
F.line(472, 254, 558, 270, INK2, 1.2, arrow='end'); F.text(520, 248, '提取输入', 11, color=INK2)
F.line(558, 294, 472, 314, INK2, 1.2, arrow='end'); F.text(520, 328, '收容输出', 11, color=INK2)
