LABEL = '按行优先存放的二维数组：按行访问空间局部性好，按列访问需要跳跃'
F = Fig(460, 560, '二维数组 a[1024][1024] 在内存中按行存放')
labs = ['a[0][0]', 'a[0][1]', 'a[0][2]', '⋮', 'a[0][1023]', 'a[1][0]', 'a[1][1]', 'a[1][2]', '⋮', 'a[1][1023]', 'a[2][0]', 'a[2][1]', '⋮']
for i, l in enumerate(labs):
    y = 66 + i * 36
    F.box(60, y, 130, 36, l, 'red' if l.endswith('[0]') else ('white' if l != '⋮' else 'light'), 13, 0, True)
for i in (0, 1, 5, 6):
    y = 84 + i * 36
    F.curve(192, y, 192, y + 36, -0.6, ACCENT['blue'], 1.3)
F.curve(192, 84, 192, 84 + 5 * 36, -0.45, ACCENT['green'], 1.6)
F.curve(192, 84 + 5 * 36, 192, 84 + 10 * 36, -0.45, ACCENT['green'], 1.6)
F.text(300, 200, '按行访问 a[i][j]：\n相邻元素连续存放\n空间局部性好 👍', 12.5, 'start', ACCENT['blue'], lh=1.5)
F.text(300, 400, '按列访问 a[j][i]：\n每次跳过 1024 个元素\n空间局部性差 👎', 12.5, 'start', ACCENT['green'], lh=1.5)
F.text(125, 548, '内存', 13, color=INK2)
