LABEL = '两机通信使用双缓冲：可以实现双向传输'
F = Fig(460, 260, '双缓冲：可以双向传输')
for x, t in ((40, 'A 机'), (260, 'B 机')):
    F.text(x + 80, 56, t, 14, color=INK, weight=700); F.rect(x, 66, 160, 150, 'none', INK2, 1.2, 4, dash='6 4')
F.text(100, 105, '发送\n缓冲区', 12, 'middle', INK2, lh=1.3, valign='middle'); F.box(140, 88, 30, 34, '', 'teal', rx=0)
F.text(100, 175, '接收\n缓冲区', 12, 'middle', INK2, lh=1.3, valign='middle'); F.box(140, 158, 30, 34, '', 'violet', rx=0)
F.box(290, 88, 30, 34, '', 'violet', rx=0); F.text(360, 105, '接收\n缓冲区', 12, 'middle', INK2, lh=1.3, valign='middle')
F.box(290, 158, 30, 34, '', 'teal', rx=0); F.text(360, 175, '发送\n缓冲区', 12, 'middle', INK2, lh=1.3, valign='middle')
F.line(172, 105, 288, 105, INK2, 1.6, arrow='end'); F.line(288, 175, 172, 175, INK2, 1.6, arrow='end')
F.text(230, 246, '双方各有发送、接收缓冲区，可同时双向通信', 11.5, color=MUTED)
