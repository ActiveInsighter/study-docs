from common import ADDR_C
LABEL = '74LS138 译码器：三个使能端 G1、G2A、G2B'
F = Fig(560, 360, '74LS138：多个“使能”')
F.box(180, 70, 120, 240, '', 'white', rx=4); F.text(260, 200, '译\n码\n器', 15, color=INK, valign='middle')
for j, (n, v, neg) in enumerate((('G₁', '1', False), ('G̅₂A', '0', True), ('G̅₂B', '0', True))):
    y = 92 + j * 28
    F.line(100, y, 178 - (9 if neg else 0), y, ACCENT['blue'], 1.5)
    if neg: F.circle(173, y, 4.5, '', 'white', sw=1.2)
    F.text(94, y, v, 14, 'end', ACCENT['blue'], 700, valign='middle'); F.text(188, y, n, 13, 'start', ACCENT['blue'], 700, valign='middle')
for j, (n, v) in enumerate((('C', '1'), ('B', '0'), ('A', '1'))):
    y = 244 + j * 22; F.line(110, y, 178, y, ADDR_C, 1.3); F.text(104, y, f'{v} {n}', 13, 'end', ADDR_C, valign='middle')
for i in range(8):
    y = 84 + i * 28; idx = 7 - i; on = idx == 5
    F.circle(306, y, 4.5, '', 'white', sw=1.2); F.line(311, y, 360, y, ADDR_C, 1.3)
    F.text(368, y, f'Ȳ_{{{idx}}}  {"0" if on else "1"}', 13, 'start', ACCENT['red'] if on else INK2, 600 if on else 400, valign='middle')
F.text(280, 342, '仅当 G₁ = 1、G̅₂A = G̅₂B = 0 时才译码', 12.5, color=MUTED)
