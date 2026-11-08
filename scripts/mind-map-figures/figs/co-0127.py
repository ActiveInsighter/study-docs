LABEL = 'CPU 的三总线结构：数据总线 DB、地址总线 AB、控制总线 CB'
F = Fig(800, 380, 'CPU 与三总线')
F.rect(150, 50, 400, 150, 'none', INK2, 1.2, 8, dash='5 4'); F.text(160, 68, '控制器部件', 11.5, 'start', MUTED)
F.box(170, 80, 70, 26, '步骤标记', 'white', 11, 4); F.box(170, 140, 70, 26, '指令寄存器 IR', 'amber', 10, 4)
F.box(290, 80, 110, 100, '控制信号\n产生电路', 'violet', 12, 4)
F.box(440, 140, 80, 30, '程序计数器 PC', 'green', 10.5, 4)
F.line(240, 93, 288, 93, INK2, 1.2, arrow='end'); F.line(240, 153, 288, 153, INK2, 1.2, arrow='end')
F.box(620, 70, 120, 100, '运算器部件', 'red', 13, 4)
F.poly([(480, 138), (480, 64), (680, 64), (680, 68)], INK2, 1.1); F.text(420, 98, '条件', 10.5, 'start', INK2); F.line(440, 98, 402, 98, INK2, 1.1, arrow='end')
for i, (n, y) in enumerate((('数据总线 DB', 230), ('地址总线 AB', 250), ('控制总线 CB', 270))):
    F.line(140, y, 780, y, INK, 2.4); F.text(132, y, n, 11, 'end', INK2, valign='middle')
for x in (310, 330, 350, 370, 390): F.line(x, 182, x, 270, INK2, 1)
F.line(480, 172, 480, 250, INK2, 1.2, arrow='end')
F.line(660, 172, 660, 230, INK2, 1.2, arrow='both'); F.line(700, 270, 700, 172, INK2, 1.2, arrow='end')
for x, lab in ((180, '接口\n输入设备'), (380, '接口\n输出设备'), (580, '内存储器')):
    F.box(x, 300, 90, 54, lab, 'blue', 11.5, 4)
    for dx in (20, 45, 70): F.line(x + dx, 232 if dx == 20 else (252 if dx == 45 else 272), x + dx, 298, INK2, 1)
