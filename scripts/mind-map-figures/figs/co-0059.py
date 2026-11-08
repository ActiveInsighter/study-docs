LABEL = 'CPU 专用数据通路方式：寄存器之间有专门的通路，由控制信号 Ci 控制'
F = Fig(820, 380, '专用数据通路方式')
B = {'MDR': (60, 60, 50, 70, 'green'), 'MAR': (60, 250, 50, 70, 'green'), 'PC': (240, 160, 70, 30, 'blue'), 'IR': (380, 160, 70, 30, 'amber'), 'CU': (380, 260, 70, 30, 'amber'),
     'AC': (560, 80, 70, 30, 'red'), 'ALU': (560, 180, 70, 30, 'red')}
for k, (x, y, w, h, t) in B.items():
    F.box(x, y, w, h, k, t, 12.5, 4, True)
def ctl(x, y, lab):
    F.circle(x, y, 4, '', 'white', sw=1.2); F.text(x + 8, y - 8, lab, 10, 'start', INK2)
F.line(110, 80, 600, 80, INK2, 1.2); ctl(560, 80, 'C₁₁')
F.poly([(275, 80), (275, 158)], INK2, 1.2, arrow='end'); ctl(275, 130, 'C₆')
F.poly([(415, 80), (415, 158)], INK2, 1.2, arrow='end'); ctl(415, 130, 'C₇')
F.poly([(415, 190), (415, 258)], INK2, 1.2, arrow='end'); ctl(415, 226, 'C₄')
F.poly([(275, 190), (275, 285), (112, 285)], INK2, 1.2, arrow='end'); ctl(220, 285, 'C₀')
F.poly([(595, 110), (595, 178)], INK2, 1.2, arrow='end'); ctl(595, 144, 'C₉')
F.poly([(630, 195), (680, 195), (680, 95), (632, 95)], INK2, 1.2, arrow='end'); ctl(680, 140, 'C₈')
F.poly([(110, 110), (520, 110), (520, 190), (558, 190)], INK2, 1.2, arrow='end'); ctl(520, 150, 'C₅')
F.line(30, 70, 58, 70, INK2, 1.2, arrow='end'); ctl(40, 70, 'C₂'); F.line(58, 110, 30, 110, INK2, 1.2, arrow='end'); ctl(40, 110, 'C₁₃')
F.line(58, 290, 26, 290, INK2, 1.2, arrow='end'); ctl(40, 290, 'C₁')
F.box(330, 330, 50, 24, '时钟', 'violet', 11, 4); F.line(380, 342, 412, 342, INK2, 1.1); F.line(412, 342, 412, 292, INK2, 1.1, arrow='end')
F.text(470, 275, '标志', 11, 'start', INK2); F.text(415, 312, '控制信号', 10.5, color=MUTED)
F.rect(560, 230, 240, 130, 'white', '#a1a1aa', 1.2, 8)
F.text(574, 252, '举例（取指周期）：', 12, 'start', INK, 600)
for i, (a, b) in enumerate((('(PC) → MAR', 'C₀ 有效'), ('(MAR) → 主存', 'C₁ 有效'), ('1 → R', '控制单元向主存发读命令'), ('M(MAR) → MDR', 'C₂ 有效'), ('(MDR) → IR', 'C₃ 有效'), ('OP(IR) → CU', 'C₄ 有效'))):
    F.text(574, 272 + i * 15, a, 10.5, 'start', INK2, mono=True); F.text(690, 272 + i * 15, b, 10.5, 'start', ACCENT['blue'])
