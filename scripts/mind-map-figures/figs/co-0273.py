LABEL = 'CPU 内部单总线方式：所有寄存器的输入、输出端都连到一条内部总线'
F = Fig(560, 600, 'CPU 内部单总线方式')
F.items.append('<path d="M470 60L510 100H490V560H510L470 590L430 560H450V100H430Z" fill="#e8effc" stroke="#3b6fd4" stroke-width="1.4"/>')
F.text(470, 330, 'CPU 内部总线 BUS', 12, color='#1e3a8a', weight=700, valign='middle', rotate=-90)
regs = [('CU', 'amber', None, None), ('IR', 'amber', 'IRin', None), ('PC', 'blue', 'PCin', 'PCout'), ('MAR', 'green', 'MARin', None), ('MDR', 'green', 'MDRin', 'MDRout'),
        ('ACC', 'violet', 'ACCin', 'ACCout'), ('Y', 'red', 'Yin', None), ('ALU', 'red', 'ALUin', None), ('Z', 'red', None, 'Zout')]
for i, (r, t, i_, o_) in enumerate(regs):
    y = 80 + i * 56
    F.box(220, y, 80, 30, r, t, 13, 4, True)
    if i_:
        F.poly([(450, y - 8), (330, y - 8), (330, y + 15), (302, y + 15)], INK2, 1.1, arrow='end'); F.text(340, y - 14, i_, 10.5, 'start', INK2)
    if o_:
        F.poly([(300, y + 22), (360, y + 22), (448, y + 22)], INK2, 1.1, arrow='end'); F.text(370, y + 16, o_, 10.5, 'start', INK2)
    if i:
        F.line(260, y - 26, 260, y - 2, INK2, 1.1, arrow='end') if r in ('CU',) else None
F.line(260, 136, 260, 112, INK2, 1.2, arrow='end'); F.text(258, 60, '控制信号', 11.5, 'middle', INK2); F.line(260, 78, 260, 66, INK2, 1.1, arrow='end')
F.line(260, 448, 260, 470, INK2, 1.1, arrow='end'); F.line(260, 504, 260, 526, INK2, 1.1, arrow='end')
F.text(150, 263, '地址线', 12, 'end', INK2, valign='middle'); F.line(218, 319, 160, 319, INK2, 1.3, arrow='both'); F.text(150, 319, '数据线', 12, 'end', INK2, valign='middle'); F.line(218, 263, 160, 263, INK2, 1.3, arrow='end')
F.line(180, 207, 218, 207, INK2, 1.2, arrow='end'); F.text(176, 207, '+1', 12, 'end', INK2, valign='middle')
F.text(150, 487, '控制信号', 12, 'end', INK2, valign='middle'); F.line(160, 487, 218, 487, INK2, 1.2, arrow='end')
F.text(280, 592, '同一时刻总线上只能有一个寄存器输出（单总线），结构简单但速度慢', 11.5, color=MUTED)
