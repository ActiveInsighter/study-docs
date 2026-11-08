from common import gate, wire
LABEL = 'SRAM 存储元：双稳态触发器（6 个 MOS 管）'
F = Fig(700, 330, 'SRAM 存储元：6 管双稳态触发器')
F.line(60, 70, 640, 70, ACCENT['red'], 2); F.text(70, 60, '字选择线 WL', 12, 'start', ACCENT['red'], 600)
F.line(80, 90, 80, 280, ACCENT['green'], 2); F.text(80, 298, 'BL', 13, color=ACCENT['green'], weight=700, mono=True)
F.line(620, 90, 620, 280, ACCENT['green'], 2); F.text(620, 298, 'BLX', 13, color=ACCENT['green'], weight=700, mono=True)
F.rect(220, 110, 260, 140, '#fafafa', '#a1a1aa', 1.2, 12, dash='5 4'); F.text(350, 270, '双稳态触发器（M1~M4，两个交叉耦合的反相器）', 12, color=MUTED)
ai, ao = gate(F, 300, 130, 'not', 1, tone='white'); bi, bo = gate(F, 360, 194, 'not', 1, tone='white')
F.text(318, 120, '', 1)
wire(F, [(250, ai[0][1]), ai[0]]); wire(F, [ao, (450, ao[1])], dot=[(450, ao[1])])
wire(F, [(450, ao[1]), (450, bi[0][1] + 0)]); wire(F, [(450, 208), (bi[0][0] + 100, 208)])
wire(F, [(450, 208), (bi[0][0] + 0, 208)])
wire(F, [bo, (250, bo[1])]) if False else None
wire(F, [(bi[0][0], bi[0][1]), (bi[0][0] - 0, bi[0][1])])
wire(F, [(bo[0], bo[1]), (bo[0] + 40, bo[1]), (bo[0] + 40, 236), (250, 236), (250, ai[0][1])], dot=[(250, ai[0][1])])
F.text(244, ai[0][1] - 10, 'A', 13, 'end', INK, 700, mono=True); F.text(456, ao[1] - 10, 'B', 13, 'start', INK, 700, mono=True)
for x, name, nx in ((150, 'M5', 250), (550, 'M6', 450)):
    F.box(x - 22, 128, 44, 26, name, 'blue', 12, 4, True)
    F.line(x, 70, x, 128, INK2, 1.3)
    F.line(80 if x < 300 else 620, 141, x - 22 if x < 300 else x + 22, 141, INK2, 1.3)
wire(F, [(172, 141), (250, 141), (250, ai[0][1])]); wire(F, [(528, 141), (450, 141), (450, ao[1])])
F.box(240, 296, 220, 26, 'A 高 B 低 → “1”；A 低 B 高 → “0”', 'red', 11.5, 5)
F.text(100, 232, '读出 0 时\nBL 为低电平', 11, 'start', ACCENT['green'], lh=1.4); F.text(600, 232, '读出 1 时\nBLX 为低电平', 11, 'end', ACCENT['green'], lh=1.4)
