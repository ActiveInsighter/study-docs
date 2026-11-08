LABEL = '控制存储器 CM：由 ROM 组成，按地址存放各条指令的微程序'
F = Fig(560, 260, '控制存储器 CM（按地址寻访）')
rows = ['…', '指令 1 的微程序', '指令 2 的微程序', '…']
for i, r in enumerate(rows):
    h = 26 if r == '…' else 50
    y = [60, 86, 136, 186][i]
    F.box(200, y, 160, h, r, 'violet' if r != '…' else 'light', 12, 0)
F.line(80, 100, 198, 100, INK2, 1.3, arrow='end'); F.text(74, 100, 'P', 13, 'end', INK, mono=True, valign='middle')
F.line(80, 150, 198, 150, INK2, 1.3, arrow='end'); F.text(74, 150, 'K', 13, 'end', INK, mono=True, valign='middle')
F.text(60, 70, '地址', 12, 'start', MUTED)
F.text(380, 136, '每段由若干微指令\n顺序组成', 12, 'start', INK2, lh=1.5)
F.text(280, 238, '微程序就像存在主存中的程序；P、K 为微程序的入口地址', 11.5, color=MUTED)
