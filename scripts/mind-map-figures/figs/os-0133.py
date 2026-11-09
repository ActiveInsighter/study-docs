LABEL = '软链接（符号链接）：创建一个 LINK 类型的新文件，内容是被链接文件的路径'
F = Fig(680, 348, '软链接：创建 LINK 类新文件')
_n0 = len(F.items)
for k, (x, d, name, tone) in enumerate(((60, '/home/xiaolin', 'file', 'green'), (400, '/home/jay', 'symlink1', 'violet'))):
    F.text(x + 80, 56, d, 11.5, color=INK2)
    for i in range(4):
        if i == 2: F.box(x, 64 + i * 22, 80, 22, name, tone, 10.5, 0); F.box(x + 80, 64 + i * 22, 80, 22, 'inode 100' if k == 0 else 'inode 200', 'blue' if k == 0 else 'red', 10.5, 0)
        else: F.box(x, 64 + i * 22, 160, 22, '', 'white', rx=0)
F.box(150, 180, 110, 32, 'inode 100', 'blue', 12, 4); F.line(200, 132, 205, 178, INK2, 1.2, arrow='end')
for i, x in enumerate((70, 170, 270)): F.box(x, 270, 70, 28, '数据块', 'amber', 11, 4); F.line(205, 214, x + 35, 268, INK2, 1.1, arrow='end')
F.box(500, 180, 110, 32, 'inode 200', 'red', 12, 4); F.line(540, 132, 555, 178, INK2, 1.2, arrow='end'); F.text(560, 158, '软链接', 11, 'start', INK2)
F.box(500, 270, 110, 28, '/home/xiaolin', 'amber', 11, 4); F.line(555, 214, 555, 268, INK2, 1.1, arrow='end'); F.text(562, 246, '数据块', 10.5, 'start', INK2)
F.poly([(612, 196), (650, 196), (650, 36), (40, 36), (40, 108), (58, 108)], INK2, 1.1, dash='4 3', arrow='end')
F.text(340, 318, '通过路径名再找到原文件：原文件删除后软链接失效', 11.5, color=MUTED)
F.items[_n0:] = ['<g transform="translate(0 18)">'] + F.items[_n0:] + ['</g>']
