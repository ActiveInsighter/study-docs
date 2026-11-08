LABEL = '字段直接编码方式：操作控制字段分为若干段，每段经译码发出微命令'
F = Fig(620, 300, '字段直接编码方式')
for i in range(3):
    x = 40 + i * 130
    F.box(x, 190, 130, 40, '', 'white', rx=0)
    F.brace(x + 4, x + 126, 186, '', down=False)
    F.box(x + 25, 110, 80, 40, '译码', 'blue', 12.5, 4)
    F.line(x + 65, 168, x + 65, 152, INK2, 1.2, arrow='end')
    for dx in (40, 55, 90): F.line(x + dx, 108, x + dx, 80, INK2, 1.2, arrow='end')
    F.text(x + 72, 90, '…', 11, color=MUTED)
F.box(430, 190, 140, 40, '下地址', 'amber', 12.5, 0)
F.text(220, 64, '控制信号', 12.5, color=INK2)
F.line(40, 250, 430, 250, INK2, 1.2, arrow='both'); F.text(235, 266, '操作控制', 12, color=INK2, halo=True)
F.text(310, 292, '互斥的微命令放在同一字段；每个字段留一个状态表示“不操作”', 11.5, color=MUTED)
