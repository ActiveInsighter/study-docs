LABEL = '二级页表结构示意图：页目录表的每项指向一个二级页表'
F = Fig(700, 450, '二级页表结构')
F.text(100, 92, '第 0 块', 11, color=INK2)
top = ['第 3 块', '第 4 块', '第 325 块', '第 2 块', '第 23 块', '…']
for i, t in enumerate(top): F.box(60, 100 + i * 22, 80, 22, t, 'blue' if i < 5 else 'white', 10.5, 0)
F.box(60, 232, 80, 90, '…', 'white', 11, 0)
mids = [(90, '第 2 块', ['第 1 块', '第 5 块', '…']), (200, '第 3 块', ['第 6 块', '第 55 块', '…']), (300, '第 4 块', ['第 24 块', '第 234 块', '…'])]
for (y, lab, rows), src in zip(mids, (0, 1, 2)):
    F.text(280, y - 8, lab, 11, color=INK2)
    for j, r in enumerate(rows): F.box(240, y + j * 22, 80, 22, r, 'blue' if r != '…' else 'white', 10.5, 0)
    F.line(140, 111 + src * 22, 238, y + 11, INK2, 1.1, arrow='end')
F.brace(60, 320, 376, '页表块（页目录表 + 二级页表）')
for j, (lab, y) in enumerate((('第 1 块', 90), ('第 5 块', 170), ('第 6 块', 250))):
    F.text(410, y - 8, lab, 11, color=INK2); F.box(380, y, 70, 50, '…', 'amber', 11, 0)
F.line(322, 101, 378, 112, INK2, 1.1, arrow='end'); F.line(322, 123, 378, 195, INK2, 1.1, arrow='end'); F.line(322, 211, 378, 275, INK2, 1.1, arrow='end')
F.text(415, 320, '数据块', 11.5, color=INK2)
F.text(610, 72, '00000000H', 10.5, color=INK2, mono=True)
mem = ['第 3 块', '第 4 块', '第 325 块', '…', '…', '第 1 块', '第 5 块', '…', '第 6 块', '第 55 块', '…', '…']
for i, t in enumerate(mem): F.box(570, 80 + i * 24, 80, 24, t, 'blue' if '块' in t else 'white', 10.5, 0)
for i, lab in enumerate(('第 0 块\n（页表）', '第 1 块\n（数据）', '第 2 块\n（页表）', '第 3 块\n（页表）')):
    F.text(560, 104 + i * 72, lab, 10.5, 'end', INK2, lh=1.2, valign='middle')
F.text(610, 382, 'FFFFFFFFH', 10.5, color=INK2, mono=True)
