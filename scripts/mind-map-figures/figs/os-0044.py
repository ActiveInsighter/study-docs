from common import xlate
LABEL = '具有快表的地址变换机构'
F = Fig(640, 356, '具有快表的地址变换机构')
xlate(F, 'basic')
F.text(470, 86, '逻辑地址 A', 11.5, color=INK2); F.box(400, 94, 70, 26, '页号 P', 'amber', 11, 0); F.box(470, 94, 110, 26, '页内偏移量 W', 'gray', 11, 0)
F.poly([(435, 122), (435, 140), (300, 140), (300, 122)], INK2, 1.2, arrow='end'); F.poly([(300, 140), (300, 170), (86, 170)], INK2, 1.2, arrow='end')
F.text(250, 214, '页号　块号', 11, 'start', INK2)
for i, (p, b) in enumerate((('0', '…'), ('…', '…'), ('P', 'b'), ('…', '…'))):
    F.text(240, 238 + i * 24, p, 11, 'end', INK2, mono=True, valign='middle'); F.box(250, 226 + i * 24, 70, 24, b, 'blue' if p == 'P' else 'white', 11, 0, True)
F.text(330, 238, '页表', 11.5, 'start', INK2)
F.poly([(70, 184), (70, 274), (248, 274)], INK2, 1.2, arrow='end')
F.box(430, 262, 60, 26, 'b', 'blue', 12, 0, True); F.box(490, 262, 90, 26, 'W', 'gray', 12, 0, True); F.text(505, 304, '物理地址 E', 11.5, color=INK2)
F.line(322, 274, 428, 274, INK2, 1.2, arrow='end'); F.poly([(560, 122), (560, 260)], INK2, 1.2, arrow='end')
F.text(420, 150, '页号　块号', 10.5, 'start', INK2)
for i, (p, b) in enumerate((('…', '…'), ('P', 'b'), ('…', '…'))): F.box(410, 158 + i * 20, 50, 20, p, 'amber' if p == 'P' else 'white', 10.5, 0, True); F.box(460, 158 + i * 20, 50, 20, b, 'blue' if b == 'b' else 'white', 10.5, 0, True)
F.text(460, 230, '快表 TLB', 11, color=ACCENT['blue'])
F.line(447, 122, 447, 156, ACCENT['blue'], 1.2, arrow='end'); F.poly([(512, 188), (520, 188), (520, 236), (460, 236), (460, 260)], ACCENT['blue'], 1.4, arrow='end')
F.text(320, 344, '先查快表：命中则直接得到块号；未命中再查内存中的页表，并把该页表项写入快表', 10.5, color=MUTED)
