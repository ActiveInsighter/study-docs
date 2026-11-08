from common import gate, wire
LABEL = '带标志加法器的逻辑电路：OF、SF、ZF、CF 的产生'
F = Fig(800, 340, '带标志加法器的逻辑电路')
fa = [(560, 'n−1', 'F_{n−1}'), (680, '1', 'F_{1}'), (760, '0', 'F_{0}')]
xs = [150, 450, 600]
for x, (i) in zip(xs, ('n−1', '1', '0')):
    F.box(x, 220, 60, 40, 'FA', 'blue', 13, 6, weight=600)
    F.line(x + 18, 290, x + 18, 262, INK2, 1.2, arrow='end'); F.line(x + 42, 290, x + 42, 262, INK2, 1.2, arrow='end')
    F.text(x + 30, 306, f'A_{{{i}}} B_{{{i}}}', 12, color=INK)
F.text(380, 240, '…', 16, color=MUTED)
F.line(448, 240, 214, 240, ACCENT['violet'], 1.3, arrow='end'); F.line(598, 240, 512, 240, ACCENT['violet'], 1.3, arrow='end'); F.text(555, 232, 'C_{1}', 11, color=ACCENT['violet'])
F.line(740, 240, 662, 240, INK2, 1.3, arrow='end'); F.text(746, 240, 'C_{in}', 12, 'start', INK, valign='middle')
F.line(148, 240, 70, 240, INK2, 1.3, arrow='end'); F.text(64, 240, 'C_{out}', 12, 'end', INK, valign='middle')
# F outputs
for x, lab in ((180, 'F_{n−1}'), (480, 'F_{1}'), (630, 'F_{0}')):
    F.line(x, 218, x, 60, ACCENT['red'], 1.3, arrow='end'); F.text(x + 6, 58, lab, 12, 'start', ACCENT['red'])
oi, oo = gate(F, 80, 104, 'xor', tone='teal'); F.line(oo[0], oo[1], oo[0] + 16, oo[1], INK2, 1.3, arrow='end'); F.text(oo[0] + 22, oo[1], 'OF', 13, 'start', INK, 700, valign='middle')
wire(F, [(165, 218), (165, 200), (60, 200), (60, oi[1][1]), oi[1]]); F.text(158, 208, 'C_{n}', 11, 'end', INK2)
F.text(200, 92, 'SF = F_{n−1}', 12.5, 'start', INK2)
zi, zo = gate(F, 330, 80, 'nor', 3, tone='violet'); F.line(zo[0], zo[1], zo[0] + 16, zo[1], INK2, 1.3, arrow='end'); F.text(zo[0] + 22, zo[1], 'ZF', 13, 'start', INK, 700, valign='middle')
for p, x in zip(zi, (180, 480, 630)):
    wire(F, [(x, p[1] + 40 if False else 150), (300, 150), (300, p[1]), p]) if False else None
wire(F, [(180, 160), (300, 160), (300, zi[0][1]), zi[0]], dot=[(180, 160)]); wire(F, [(480, 170), (310, 170), (310, zi[1][1]), zi[1]], dot=[(480, 170)]); wire(F, [(630, 180), (318, 180), (318, zi[2][1]), zi[2]], dot=[(630, 180)])
ci, co = gate(F, 690, 90, 'xor', tone='amber'); F.line(co[0], co[1], co[0] + 16, co[1], INK2, 1.3, arrow='end'); F.text(co[0] + 4, co[1] - 22, 'CF', 13, 'start', INK, 700)
wire(F, [(70, 240), (70, 200 + 0), (70, 196), (670, 196), (670, ci[0][1]), ci[0]], dot=[(70, 240)]); wire(F, [(740, 240), (740, 140), (680, 140), (680, ci[1][1]), ci[1]], dot=[(740, 240)])
F.text(400, 330, 'OF = C_{n} ⊕ C_{n−1}　SF = F_{n−1}　ZF = ¬(F_{n−1} + … + F_{0})　CF = C_{out} ⊕ C_{in}', 12.5, color=INK2)
