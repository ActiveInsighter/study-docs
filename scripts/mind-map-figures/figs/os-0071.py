from common import xlate
LABEL = '基本分页存储的地址变换机构'
F = Fig(640, 340, '基本地址变换机构')
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
F.text(320, 330, '① 页号与页表长度比较（越界检查）② 页表始址 + 页号 × 页表项长度 → 块号 b ③ E = b × 页大小 + W', 10.5, color=MUTED)
