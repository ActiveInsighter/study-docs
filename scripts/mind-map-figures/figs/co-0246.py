LABEL = '标记项组成的二维标记阵列（2 路组相联）'
F = Fig(560, 260, '标记阵列：有效位 + 脏位 + 计数位 + 标记 = 23 bit')
for r in range(4):
    for c in range(2):
        t = 'green' if (r, c) == (1, 0) else ('red' if (r, c) == (1, 1) else 'gray')
        F.box(40 + c * 240, 70 + r * 40, 240, 40, '标记项', t, 13.5, 0)
    F.text(30, 90 + r * 40, f'{r}', 12, 'end', MUTED, valign='middle')
F.text(280, 248, '查找 Cache 就是在对应组的标记项中比对标记是否符合', 12, color=MUTED)
