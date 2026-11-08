LABEL = '单体多字存储器：一个存储单元存 m 个字，一次读一整行'
F = Fig(560, 300, '单体多字存储器')
for c in range(4):
    F.box(40 + c * 120, 64, 120, 34, '1 个字', 'red', 13, 0)
for r in range(1, 6):
    for c in range(4):
        if r == 3: continue
        F.rect(40 + c * 120, 64 + r * 34, 120, 34, '#ffffff', INK2, 1.1, 0)
F.rect(40, 166, 480, 34, '#fafafa', INK2, 1.1, 0); F.text(280, 183, '⋮', 14, color=MUTED, valign='middle')
F.text(280, 290, '共用控制电路与寄存器；一次存取一整行（m 个字），可能读到多余的信息', 12, color=MUTED)
