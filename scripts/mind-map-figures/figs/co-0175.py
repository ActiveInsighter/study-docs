from common import ADDR_C
LABEL = '带使能端 EN 的译码器：EN 有效时才译码'
F = Fig(540, 330, '使能端 EN：类似于片选 CS')
F.box(170, 70, 110, 200, '', 'white', rx=4); F.text(225, 160, '译\n码\n器', 15, color=INK, valign='middle')
F.line(90, 96, 168, 96, ACCENT['blue'], 1.5); F.text(84, 96, '1', 14, 'end', ACCENT['blue'], 700, valign='middle'); F.text(180, 96, 'EN', 13, 'start', ACCENT['blue'], 700, valign='middle')
for j, (n, v) in enumerate((('C', '1'), ('B', '0'), ('A', '1'))):
    y = 210 + j * 22; F.line(100, y, 168, y, ADDR_C, 1.3); F.text(94, y, f'{v} {n}', 13, 'end', ADDR_C, valign='middle')
for i in range(8):
    y = 86 + i * 24; idx = 7 - i; on = idx == 5
    F.circle(286, y, 4.5, '', 'white', sw=1.2); F.line(291, y, 340, y, ADDR_C, 1.3)
    F.text(348, y, f'Ȳ_{{{idx}}}  {"0" if on else "1"}', 13, 'start', ACCENT['red'] if on else INK2, 600 if on else 400, valign='middle')
F.text(270, 314, 'EN = 1 时按 CBA 译码；EN 无效时所有输出都无效（全为 1）', 12, color=MUTED)
