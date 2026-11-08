LABEL = '双总线结构：主存总线 + I/O 总线，通道连接两者'
F = Fig(600, 320, '双总线结构')
F.line(30, 70, 570, 70, INK2, 2.6, arrow='both'); F.text(300, 58, '主存总线', 12.5, color=INK2)
F.box(70, 130, 80, 30, 'CPU', 'blue', 12.5, 5); F.box(190, 130, 80, 30, '主存', 'blue', 12.5, 5); F.box(310, 130, 80, 30, '通道', 'amber', 12.5, 5)
for x in (110, 230, 350): F.line(x, 74, x, 128, INK2, 1.6, arrow='both')
F.line(150, 220, 570, 220, INK2, 2.6, arrow='both'); F.text(450, 208, 'I/O 总线', 12.5, color=INK2)
F.line(350, 162, 350, 216, ACCENT['amber'], 1.6, arrow='both')
for x in (250, 400): F.line(x, 224, x, 268, INK2, 1.6, arrow='both'); F.box(x - 40, 270, 80, 30, 'I/O 接口', 'white', 12, 5)
F.text(325, 285, '…', 14, color=MUTED, valign='middle')
