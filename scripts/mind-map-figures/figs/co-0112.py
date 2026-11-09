from common import gate, mux_shape, wire
LABEL = '一位 ALU：与、或、加三种操作，由 ALUop 经 MUX 选择'
F = Fig(640, 320, '一位 ALU（与 / 或 / 加）')
F.text(40, 90, 'A', 14, 'end', INK, 600, valign='middle', mono=True); F.text(40, 230, 'B', 14, 'end', INK, 600, valign='middle', mono=True)
ai, ao = gate(F, 200, 70, 'and'); oi, oo = gate(F, 200, 130, 'or')
F.box(200, 196, 100, 44, '一位全加器', 'blue', 12.5, 6)
wire(F, [(46, 90), (120, 90), (120, ai[0][1]), ai[0]], dot=[(120, 90)])
wire(F, [(120, 90), (120, oi[0][1]), oi[0]], dot=[(120, oi[0][1])]); wire(F, [(120, oi[0][1]), (120, 208), (198, 208)])
wire(F, [(46, 230), (150, 230), (150, ai[1][1]), ai[1]], dot=[(150, 230)])
wire(F, [(150, oi[1][1]), oi[1]], dot=[(150, oi[1][1])]); wire(F, [(150, 230), (198, 230)])
mux_shape(F, 440, 60, 40, 200, '', 'violet', 13, vertical=True); F.text(466, 184, 'MUX', 12, color=TONES['violet'][2], weight=700, valign='middle', rotate=90)
for (src, lab, y) in ((ao, 'and', 90), (oo, 'or', 150), ((300, 218), 'add', 218)):
    wire(F, [src, (400, src[1]), (400, y), (440, y)]); F.text(420, y - 6, lab, 11, color=MUTED)
for y, c in ((90, '00'), (150, '01'), (218, '10')): F.text(448, y, c, 11, 'start', ACCENT['red'], mono=True, valign='middle')
F.line(480, 160, 560, 160, INK2, 1.6, arrow='end'); F.text(566, 160, 'F', 14, 'start', INK, 600, valign='middle', mono=True)
F.line(460, 30, 460, 66, ACCENT['red'], 1.4, dash='5 4', arrow='end'); F.text(468, 30, 'ALUop（2 bit）', 12, 'start', ACCENT['red'], valign='middle')
F.line(250, 50, 250, 194, INK2, 1.3, arrow='end'); F.text(258, 50, 'Cin', 12, 'start', INK2, mono=True)
F.line(250, 242, 250, 290, INK2, 1.3, arrow='end'); F.text(258, 290, 'Cout', 12, 'start', INK2, mono=True)
