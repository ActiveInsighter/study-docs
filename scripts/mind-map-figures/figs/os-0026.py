LABEL = '两级目录结构：主文件目录 MFD + 用户文件目录 UFD'
F = Fig(720, 220, '两级目录结构')
for i in range(4): F.box(200 + i * 80, 50, 80, 28, f'User{i + 1}', 'blue', 12, 0)
F.text(530, 64, '主文件目录', 12, 'start', INK2, valign='middle')
groups = [['CAT', 'BO', 'A', 'TEST'], ['A', 'TEST'], ['A', 'DATA'], ['X', 'DATA', 'A']]
x = 30
for g, files in enumerate(groups):
    F.line(240 + g * 80, 80, x + 20, 118, INK2, 1.1, arrow='end')
    for j, f in enumerate(files):
        F.box(x + j * 44, 120, 44, 28, f, 'amber', 11, 0, True)
        F.circle(x + j * 44 + 22, 182, 9, '', 'white'); F.line(x + j * 44 + 22, 148, x + j * 44 + 22, 172, INK2, 1)
    x += len(files) * 44 + 20
F.text(x, 134, '用户文件目录', 12, 'start', INK2, valign='middle'); F.text(x, 182, '文件', 12, 'start', INK2, valign='middle')
