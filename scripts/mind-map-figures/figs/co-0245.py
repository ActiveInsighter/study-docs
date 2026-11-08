from common import alu_shape, mux_shape, bus_slash, gate, wire
LABEL = '补码加减运算电路：Sub 控制 MUX 选择 Y 或 ¬Y，并作为 Cin'
F = Fig(720, 320, '加减运算电路')
F.text(30, 110, 'X', 15, 'start', INK, 700, mono=True, valign='middle'); F.line(50, 110, 486, 110, INK2, 1.5, arrow='end'); bus_slash(F, 420, 110)
F.text(30, 200, 'Y', 15, 'start', INK, 700, mono=True, valign='middle'); wire(F, [(50, 200), (330, 200)], dot=[(100, 200)])
wire(F, [(100, 200), (100, 250), (170, 250)]); gi, go = gate(F, 172, 236, 'not', 1, tone='green')
wire(F, [go, (330, go[1])]); F.text(240, 270, '¬Y', 13, 'start', INK2, mono=True)
mux_shape(F, 330, 180, 36, 90, 'MUX', 'violet', 11, vertical=True)
F.text(338, 200, '0', 10, 'start', ACCENT['red'], mono=True, valign='middle'); F.text(338, go[1], '1', 10, 'start', ACCENT['red'], mono=True, valign='middle')
wire(F, [(366, 225), (486, 225)], arrow='end'); bus_slash(F, 430, 225)
F.items.append('<path d="M488 70L580 110V136L556 168L580 200V226L488 266Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.5" stroke-linejoin="round"/>')
F.text(526, 168, '加法器', 15, color='#7f1d1d', weight=700, valign='middle')
F.text(348, 40, 'Sub', 13, 'start', ACCENT['blue'], 600, mono=True); wire(F, [(348, 48), (348, 186)], ACCENT['blue'], dot=[(348, 60)])
F.poly([(348, 60), (534, 60), (534, 86)], ACCENT['blue'], 1.3); F.text(540, 80, 'Cin', 12, 'start', INK2, mono=True)
F.line(534, 250, 534, 300, INK2, 1.3, arrow='end'); F.text(542, 296, 'Cout', 12, 'start', INK2, mono=True)
for i, f in enumerate(('ZF', 'OF', 'SF', 'CF')):
    y = (118, 140, 196, 218)[i]
    F.line(580, y, 630, y, INK2, 1.2, arrow='end'); F.text(636, y, f, 12, 'start', INK, mono=True, valign='middle')
F.text(690, 168, 'F', 15, 'start', INK, 700, mono=True, valign='middle'); F.line(580, 168, 680, 168, INK2, 1.6, arrow='end')
F.text(30, 300, 'Sub = 0：X + Y；Sub = 1：X + ¬Y + 1 = X − Y', 12.5, 'start', MUTED)
