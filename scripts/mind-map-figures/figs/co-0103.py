LABEL = 'CPU 内部单总线方式（含主存接口与通用寄存器组）'
F = Fig(600, 700)
F.items.append('<path d="M520 60L560 100H540V660H560L520 690L480 660H500V100H480Z" fill="#e8effc" stroke="#3b6fd4" stroke-width="1.4"/>')
F.text(520, 380, 'BUS', 13, color='#1e3a8a', weight=700, valign='middle', rotate=-90)
regs = [('CU', 'amber', None, None, 70), ('IR', 'amber', 'IRin', None, 120), ('PC', 'blue', 'PCin', 'PCout', 180), ('MAR', 'green', 'MARin', None, 250), ('MDR', 'green', 'MDRin', 'MDRout', 320),
        ('R₀', 'violet', 'R0in', 'R0out', 400), ('Rₙ₋₁', 'violet', 'Rn-1in', 'Rn-1out', 470), ('Y', 'red', 'Yin', None, 540), ('ALU', 'red', 'ALUin', None, 590), ('Z', 'red', None, 'Zout', 640)]
for r, t, i_, o_, y in regs:
    F.box(260, y, 80, 30, r, t, 13, 4, True)
    if i_: F.poly([(498, y - 6), (380, y - 6), (380, y + 15), (342, y + 15)], INK2, 1.1, arrow='end'); F.text(390, y - 12, i_, 10.5, 'start', INK2)
    if o_: F.poly([(340, y + 24), (498, y + 24)], INK2, 1.1, arrow='end'); F.text(400, y + 18, o_, 10.5, 'start', INK2)
F.line(300, 118, 300, 102, INK2, 1.1, arrow='end'); F.line(300, 68, 300, 52, INK2, 1.1, arrow='end'); F.text(300, 44, '控制信号', 11, color=INK2)
F.line(300, 572, 300, 588, INK2, 1.1, arrow='end'); F.line(300, 622, 300, 638, INK2, 1.1, arrow='end')
F.line(220, 195, 258, 195, INK2, 1.1, arrow='end'); F.text(214, 195, '+1', 12, 'end', INK2, valign='middle')
F.text(300, 444, '⋮', 14, color=MUTED, valign='middle')
F.rect(220, 386, 140, 128, 'none', ACCENT['red'], 1.3, 10, dash='5 4'); F.text(214, 450, '通用\n寄存器组', 11, 'end', ACCENT['red'], lh=1.3, valign='middle')
F.rect(30, 236, 216, 128, 'none', ACCENT['blue'], 1.3, 10, dash='5 4')
F.box(110, 250, 50, 100, '主\n存', 'amber', 13, 4)
F.line(258, 265, 162, 265, INK2, 1.2, arrow='end'); F.text(212, 258, 'MARout', 10, color=INK2)
F.line(162, 326, 258, 326, INK2, 1.2, arrow='end'); F.text(212, 320, 'MDRinE', 10, color=INK2)
F.line(258, 342, 162, 342, INK2, 1.2, arrow='end'); F.text(212, 356, 'MDRoutE', 10, color=INK2)
F.line(50, 270, 108, 270, INK2, 1.2, arrow='end'); F.text(44, 262, 'MemR', 10.5, 'start', INK2)
F.line(50, 330, 108, 330, INK2, 1.2, arrow='end'); F.text(44, 322, 'MemW', 10.5, 'start', INK2)
F.line(176, 605, 258, 605, INK2, 1.2, arrow='end'); F.text(170, 605, '控制信号', 11, 'end', INK2, valign='middle')
