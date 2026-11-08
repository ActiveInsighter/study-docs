LABEL = '硬链接：多个目录项指向同一个 inode'
F = Fig(680, 330, '硬链接：文件指向同一个 inode')
for k, (x, d, name) in enumerate(((60, '/home/xiaolin', 'file'), (260, '/home/jay', 'hardlink1'), (460, '/tmp', 'hardlink2'))):
    F.text(x + 80, 56, d, 11.5, color=INK2)
    for i in range(4):
        if i == 2: F.box(x, 64 + i * 22, 80, 22, name, 'green' if k == 0 else 'violet', 10.5, 0); F.box(x + 80, 64 + i * 22, 80, 22, 'inode 100', 'blue', 10.5, 0)
        else: F.box(x, 64 + i * 22, 160, 22, '', 'white', rx=0)
F.text(54, 120, '目录项', 11, 'end', INK2)
F.box(270, 200, 110, 32, 'inode 100', 'blue', 12, 4)
F.poly([(220, 119), (232, 119), (232, 216), (268, 216)], INK2, 1.2, arrow='end'); F.poly([(420, 119), (430, 119), (430, 176), (325, 176), (325, 198)], INK2, 1.2, arrow='end'); F.text(380, 170, '硬链接', 11, color=INK2)
F.poly([(620, 119), (640, 119), (640, 216), (382, 216)], INK2, 1.2, arrow='end'); F.text(520, 208, '硬链接', 11, color=INK2)
for i, x in enumerate((180, 280, 380)): F.box(x, 280, 70, 28, '数据块', 'amber', 11, 4); F.line(325, 234, x + 35, 278, INK2, 1.1, arrow='end')
