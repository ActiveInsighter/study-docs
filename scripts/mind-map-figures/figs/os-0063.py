LABEL = '两级页表的地址变换（含快表）'
F = Fig(760, 360, '两级页表的地址变换')
F.text(130, 86, '页表寄存器', 11.5, color=INK2); F.box(30, 94, 110, 26, '页表始址 F', 'white', 11, 0); F.box(140, 94, 100, 26, '页表长度 M', 'white', 11, 0)
F.circle(300, 107, 13, '>', 'white', 13); F.line(300, 94, 300, 60, INK2, 1.2, arrow='end'); F.text(300, 52, '越界中断', 11.5, color=ACCENT['red']); F.line(242, 107, 286, 107, INK2, 1.2, arrow='end')
F.text(560, 82, '逻辑地址 A', 11.5, color=INK2)
F.box(440, 94, 70, 26, '一级 P1', 'amber', 11, 0); F.box(510, 94, 70, 26, '二级 P2', 'green', 11, 0); F.box(580, 94, 110, 26, '页内偏移量 W', 'gray', 11, 0)
F.poly([(475, 122), (475, 140), (300, 140), (300, 122)], ACCENT['amber'], 1.2, arrow='end'); F.poly([(300, 140), (70, 140), (70, 157)], ACCENT['amber'], 1.2, arrow='end')
F.circle(70, 170, 13, '+', 'white', 14); F.line(70, 122, 70, 128, INK2, 1)
for k, (x, lab, hl) in enumerate(((200, '一级页表', 'b'), (370, '二级页表', 'c'))):
    F.text(x + 30, 214, '页号　块号', 10.5, 'start', INK2)
    for i, (p, b) in enumerate((('0', '…'), ('…', '…'), ('P1' if k == 0 else 'P2', hl), ('…', '…'))):
        F.text(x + 24, 236 + i * 22, p, 10.5, 'end', INK2, mono=True, valign='middle'); F.box(x + 30, 225 + i * 22, 60, 22, b, ('amber' if k == 0 else 'green') if b == hl else 'white', 10.5, 0, True)
    F.text(x + 60, 326, lab, 11.5, color=INK2)
F.poly([(70, 184), (70, 280), (228, 280)], ACCENT['amber'], 1.2, arrow='end')
F.poly([(292, 280), (330, 280), (330, 240), (398, 240)], ACCENT['green'], 1.2, arrow='end'); F.poly([(545, 122), (545, 200), (360, 200), (360, 280), (398, 280)], ACCENT['green'], 1.2, arrow='end')
F.box(600, 266, 60, 26, 'c', 'blue', 12, 0, True); F.box(660, 266, 80, 26, 'W', 'gray', 12, 0, True); F.text(670, 308, '物理地址 E', 11.5, color=INK2)
F.line(462, 280, 598, 280, ACCENT['red'], 1.2, arrow='end'); F.poly([(700, 122), (700, 264)], INK2, 1.2, arrow='end')
F.text(560, 146, '一级　二级　块号', 10, 'start', INK2)
for i, row in enumerate((('…', '…', '…'), ('P1', 'P2', 'c'), ('…', '…', '…'))):
    for j, v in enumerate(row): F.box(560 + j * 40, 154 + i * 18, 40, 18, v, 'blue' if v not in ('…',) and i == 1 else 'white', 10, 0, True)
F.text(620, 222, '快表', 11, color=ACCENT['blue'])
F.text(380, 350, '先查快表（P1、P2 一起作关键字）；未命中则 F + P1 查一级页表 → 二级页表地址 + P2 → 块号 c', 10.5, color=MUTED)
