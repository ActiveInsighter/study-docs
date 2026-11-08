from common import alu_shape, bus_slash
LABEL = '带标志加法器：输出 F 与 OF、SF、ZF、CF'
F = Fig(480, 340)
a = alu_shape(F, 240, 130, 240, 90)
for i, (lab, x) in enumerate((('OF', 170), ('SF', 205), ('F', 240), ('ZF', 275), ('CF', 310))):
    top = 40 if lab == 'F' else 72
    F.line(x, 130, x, top, INK2, 1.6 if lab == 'F' else 1.4, arrow='end')
    F.text(x, top - 12, lab, 14 if lab == 'F' else 13, color=INK, weight=700 if lab == 'F' else 600, mono=True)
bus_slash(F, 240, 100)
F.line(a['left'][0], a['left'][1], 30, a['left'][1], INK2, 1.5, arrow='end'); F.text(30, a['left'][1] - 14, 'Cout', 13, 'start', INK, mono=True)
F.line(450, a['right'][1], a['right'][0], a['right'][1], INK2, 1.5, arrow='end'); F.text(450, a['right'][1] - 14, 'Cin', 13, 'end', INK, mono=True)
for k in ('A', 'B'):
    x, y = a[k]; F.line(x, y + 80, x, y, INK2, 1.6, arrow='end'); bus_slash(F, x, y + 44); F.text(x, y + 96, k, 14, color=INK, weight=600, mono=True)
