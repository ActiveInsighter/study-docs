LABEL = '成组链接法：超级块中存放第一组空闲盘块号，每组第一块存放下一组的信息'
F = Fig(800, 400, '存储空间管理——成组链接法')
F.text(140, 120, '超级块', 11, color=INK2)
F.box(120, 128, 50, 22, '100', 'blue', 10.5, 0)
for i, v in enumerate(('300', '299', '…', '202', '201')): F.box(120, 150 + i * 22, 50, 22, v, 'amber', 10.5, 0, True)
F.pill(30, 128, '盘块数', 'amber', 11); F.pill(30, 172, '空闲块号', 'amber', 11)
groups = [(300, ['100', '400', '399', '…', '301']), (400, ['100', '7900', '7899', '…', '7801']), (7900, ['99', '−1', '9999', '…', '9901'])]
for k, (num, vals) in enumerate(groups):
    x = 260 + k * 180
    F.text(x + 25, 62, str(num), 10.5, color=INK2, mono=True)
    for i, v in enumerate(vals): F.box(x, 70 + i * 22, 50, 22, v, 'blue' if i == 0 else 'white', 10.5, 0, True)
    blocks = {0: ['299', '…', '202', '201'], 1: ['399', '…', '302', '301'], 2: ['7899', '…', '7802', '7801']}[k]
    for i, b in enumerate(blocks): F.box(x, 200 + i * 44, 50, 26, '', 'amber', rx=0); F.text(x + 25, 196 + i * 44, b, 9.5, color=MUTED, mono=True)
F.line(172, 161, 258, 81, INK2, 1.1, arrow='end')
F.line(312, 103, 438, 81, INK2, 1.1, arrow='end'); F.line(492, 103, 618, 81, INK2, 1.1, arrow='end')
for i, b in enumerate(('9999', '…', '9902', '9901')): F.box(720, 200 + i * 44, 50, 26, '', 'amber', rx=0); F.text(745, 196 + i * 44, b, 9.5, color=MUTED, mono=True)
F.box(600, 190, 190, 0.1, '', 'none')
F.text(400, 390, '注 1：已经没有下一组空闲块时设为特殊值 −1　注 2：一组的块号不需要连续', 11, color=MUTED)
