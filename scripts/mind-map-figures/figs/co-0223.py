from common import alu_shape, bus_slash
LABEL = 'ALU 的基本结构：加法器 + ALUop 控制信号'
F = Fig(500, 340)
a = alu_shape(F, 230, 130, 240, 90, 'ALU', 'red', 18)
for lab, x in (('OF', 160), ('SF', 195), ('F', 230), ('ZF', 265), ('CF', 300)):
    top = 40 if lab == 'F' else 72
    F.line(x, 130, x, top, INK2, 1.6 if lab == 'F' else 1.4, arrow='end'); F.text(x, top - 12, lab, 13, color=INK, weight=600, mono=True)
bus_slash(F, 230, 100)
F.line(a['left'][0], a['left'][1], 24, a['left'][1], INK2, 1.5, arrow='end'); F.text(24, a['left'][1] - 14, 'Cout', 13, 'start', INK, mono=True)
F.line(430, a['right'][1] - 12, a['right'][0] - 4, a['right'][1] - 12, INK2, 1.5, arrow='end'); F.text(434, a['right'][1] - 12, 'Cin', 13, 'start', INK, mono=True, valign='middle')
F.line(430, a['right'][1] + 18, a['right'][0] + 10, a['right'][1] + 18, ACCENT['red'], 1.4, dash='5 4', arrow='end'); F.text(434, a['right'][1] + 18, 'ALUop', 13, 'start', ACCENT['red'], mono=True, valign='middle')
for k in ('A', 'B'):
    x, y = a[k]; F.line(x, y + 80, x, y, INK2, 1.6, arrow='end'); bus_slash(F, x, y + 44); F.text(x, y + 96, k, 14, color=INK, weight=600, mono=True)
