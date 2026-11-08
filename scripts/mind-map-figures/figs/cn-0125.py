LABEL = 'IP 地址的分类：A、B、C、D、E 类'
F = Fig(720, 330, '分类的 IP 地址')
X, U = 150, 16.5
for t, b in (('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('8', 8), ('16', 16), ('24', 24), ('32', 32)): F.text(X + b * U, 60, t, 10.5, color=MUTED, mono=True)
rows = [('A 类（1~126）', '0', 8, '网络号', '主机号', '7 bit'), ('B 类（128~191）', '10', 16, '网络号', '主机号', '14 bit'), ('C 类（192~223）', '110', 24, '网络号', '主机号', '21 bit'),
        ('D 类（224~239）', '1110', None, '多播地址', '', ''), ('E 类（240~255）', '1111', None, '保留为今后使用', '', '')]
for i, (name, pre, nb, a, b, note) in enumerate(rows):
    y = 72 + i * 48
    F.text(X - 10, y + 16, name, 11.5, 'end', INK, valign='middle')
    for j, c in enumerate(pre): F.box(X + j * U, y, U, 32, c, 'blue', 11, 0, True)
    p = len(pre)
    if nb:
        F.box(X + p * U, y, (nb - p) * U, 32, a, 'blue', 11.5, 0); F.box(X + nb * U, y, (32 - nb) * U, 32, b, 'amber', 11.5, 0)
        F.text(X + nb * U - 4, y - 4, note, 9.5, 'end', INK2)
    else:
        F.box(X + p * U, y, (32 - p) * U, 32, a, 'amber', 11.5, 0)
