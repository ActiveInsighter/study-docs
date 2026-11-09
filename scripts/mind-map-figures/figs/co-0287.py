LABEL = '字段间接编码方式：一个字段的译码结果还要受另一字段控制'
F = Fig(620, 320, '字段间接编码方式')
labs = ['字段 1', '字段 2', '…', '字段 n']
for i, l in enumerate(labs):
    F.box(30 + i * 100, 220, 100, 36, l, 'white', 12, 0)
F.box(430, 220, 150, 36, '下地址', 'amber', 12, 0)
for i in (0, 1, 3):
    x = 30 + i * 100
    F.box(x + 15, 150, 70, 30, '译码', 'blue', 12, 4); F.line(x + 50, 218, x + 50, 182, INK2, 1.2, arrow='end')
for i in (0, 3):
    x = 30 + i * 100
    F.box(x + 10, 80, 80, 36, '', 'white', rx=4)
    F.line(x + 35, 148, x + 35, 118, ACCENT['blue'], 1.1, arrow='end'); F.line(x + 50, 148, x + 50, 118, ACCENT['blue'], 1.1, arrow='end'); F.line(x + 70, 148, x + 70, 118, ACCENT['blue'], 1.1, arrow='end')
    for dx in (25, 40, 70): F.line(x + dx, 78, x + dx, 56, INK2, 1.2, arrow='end')
    F.text(x + 108, 64, '控制信号', 11.5, 'start', INK2)
F.poly([(130 + 50, 148), (180, 130), (140, 130), (140, 98), (122, 98)], ACCENT['blue'], 1.2, arrow='end')
F.poly([(180, 130), (300, 130), (300, 98), (338, 98)], ACCENT['blue'], 1.2, arrow='end')
F.line(30, 276, 430, 276, INK2, 1.2, arrow='both'); F.text(230, 290, '操作控制', 12, color=INK2, halo=True)
F.text(310, 312, '字段 2 的译码结果参与决定其他字段的微命令：可进一步缩短字长，但速度更慢', 11, color=MUTED)
