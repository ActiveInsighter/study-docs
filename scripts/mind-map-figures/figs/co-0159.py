LABEL = '直接编码（直接控制）方式：每一位对应一个微命令'
F = Fig(620, 210, '直接编码方式：一位对应一个微命令')
bits = ['1'] + ['0'] * 9 + ['1']
F.cells(40, 90, bits, 32, 32, {0: 'blue', 10: 'blue'}, size=13)
F.box(392, 90, 180, 32, '下地址', 'amber', 12.5, 0)
for i in range(11):
    if i in (0, 1, 2, 9, 10): F.line(56 + i * 32, 88, 56 + i * 32, 66, INK2, 1.1, arrow='end')
F.text(56, 56, '(PC)→MAR', 11, color=ACCENT['blue']); F.text(376, 56, '1→R', 11, color=ACCENT['blue']); F.text(216, 56, '控制信号 ……', 11.5, color=INK2)
F.line(40, 140, 392, 140, INK2, 1.2, arrow='both'); F.text(216, 156, '操作控制', 12, color=INK2, halo=True)
F.text(310, 196, '位为 1 则发出该微命令：速度最快，但微指令字长太长', 11.5, color=MUTED)
