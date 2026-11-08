LABEL = '片内总线：CPU 内部寄存器与寄存器、寄存器与 ALU 之间的连线（五段流水线数据通路）'
F = Fig(820, 320, '片内总线（CPU 内部数据通路）')
stages = [('IF', '取指', 40), ('ID', '译码', 210), ('EX', '执行', 380), ('M', '访存', 550), ('WB', '写回', 720)]
for s, c, x in stages:
    F.text(x + 50, 70, f'{s}　{c}', 12.5, color=ACCENT['red'], weight=700)
for x in (140, 310, 480, 650):
    F.line(x, 80, x, 290, LINE, 1, dash='4 4'); F.box(x - 6, 100, 12, 170, '', 'gray', rx=2)
F.box(30, 110, 22, 120, '', 'white', rx=2); F.text(41, 170, 'PC', 11, color=INK, valign='middle', rotate=-90)
F.box(66, 120, 66, 100, '指令\nCache', 'violet', 11.5, 4)
F.box(170, 140, 100, 90, '寄存器堆', 'green', 12, 4)
F.items.append('<path d="M360 130L404 152V178L394 186L404 194V220L360 242Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.4"/>'); F.text(386, 186, 'ALU', 11, color='#7f1d1d', weight=700, valign='middle', rotate=-90)
F.box(510, 120, 100, 100, '数据\nCache', 'amber', 11.5, 4)
for (x1, y1, x2, y2) in ((52, 170, 64, 170), (132, 170, 134, 170), (146, 170, 168, 170), (270, 160, 304, 160), (270, 200, 304, 200), (316, 160, 358, 160), (316, 200, 358, 210), (404, 186, 474, 186), (486, 186, 508, 186), (610, 170, 644, 170), (656, 170, 690, 170)):
    F.line(x1, y1, x2, y2, INK2, 1.3, arrow='end')
F.poly([(690, 170), (700, 170), (700, 290), (220, 290), (220, 232)], INK2, 1.3, arrow='end')
F.text(410, 312, '这些连接寄存器、ALU、Cache 的线都属于片内总线', 12, color=MUTED)
