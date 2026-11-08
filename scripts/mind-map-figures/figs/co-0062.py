LABEL = '主存中的页表：有效位、脏位、引用位、物理页号或磁盘地址'
F = Fig(760, 400, '页表：⟨有效位, 脏位, 引用位, 物理页号 / 磁盘地址⟩')
F.box(30, 92, 70, 24, '虚页号', 'white', 12, 4); F.poly([(65, 116), (65, 220), (128, 220)], INK2, 1.2, arrow='end')
rows = ['101', '100', '100', '101', '000', '101', '101', '000', '111', '111', '000', '111']
F.text(150, 76, '有效 脏 引用', 10.5, color=MUTED); F.text(250, 76, '物理页 或 磁盘地址', 11, color=MUTED); F.text(220, 62, '页表', 12.5, color=INK, weight=700)
for i, r in enumerate(rows):
    y = 86 + i * 24
    valid = r[0] == '1'
    F.cells(130, y, list(r), 22, 24, size=11)
    F.box(196, y, 110, 24, '', 'amber' if valid else 'blue', rx=0)
    F.circle(250, y + 12, 3, '', 'dark', sw=0)
for i in range(10):
    F.box(480, 74 + i * 22, 120, 22, '', 'amber', rx=0)
F.text(540, 62, '物理存储器', 12, color=INK2)
F.ellipse(560, 340, 60, 14, '', 'gray'); F.rect(500, 340, 120, 34, '#f4f4f5', 'none', 0, 0); F.path('M500 340V374M620 340V374', INK2, 1.2); F.ellipse(560, 374, 60, 14, '', 'gray')
F.text(560, 316, '磁盘存储', 12, color=INK2)
import random
targets = [3, 7, 1, 9, None, 0, 5, None, 2, 8, None, 4]
for i, t in enumerate(targets):
    y = 98 + i * 24
    if t is None:
        F.line(252, y, 506, 352, INK2, 1, arrow='end')
    else:
        F.line(252, y, 478, 85 + t * 22, ACCENT['amber'], 1, arrow='end')
F.text(380, 394, '有效位 = 1：存放主存物理页号；有效位 = 0：存放磁盘地址（缺页）', 12, color=MUTED)
