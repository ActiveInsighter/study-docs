LABEL = 'Unix 系统的 inode 结构：直接块 + 一级、二级、三级间接块'
F = Fig(760, 470, 'Unix 的 inode 结构（混合索引）')
rows = [('模式', 'teal'), ('所有者(2)', 'teal'), ('时间戳(3)', 'teal'), ('块大小', 'teal'), ('计数', 'teal')]
for i, (t, tone) in enumerate(rows): F.box(30, 60 + i * 28, 130, 28, t, tone, 11.5, 0)
F.box(30, 200, 130, 130, '直接块', 'amber', 12, 0)
for i, t in enumerate(('一级间址', '二级间址', '三级间址')): F.box(30, 330 + i * 28, 130, 28, t, 'amber', 11.5, 0)
for i, y in enumerate((214, 238, 262, 310)):
    F.box(270, y - 10, 70, 22, '数据', 'red', 10.5, 3); F.poly([(160, 210 + i * 30), (230, 210 + i * 30), (230, y), (268, y)], INK2, 1, arrow='end')
F.text(305, 290, '…', 12, color=MUTED)
def ind(x, y, h=50):
    F.box(x, y, 24, h, '⋮', 'red', 10, 3)
    return (x + 24, y)
ind(200, 330); F.line(160, 344, 198, 344, INK2, 1, arrow='end')
for k, y in enumerate((336, 368)): F.box(270, y, 70, 22, '数据', 'red', 10.5, 3); F.line(224, 346 + k * 20, 268, y + 11, INK2, 1, arrow='end')
ind(380, 370); F.poly([(160, 372), (180, 372), (180, 400), (378, 400)], INK2, 1, arrow='end')
for k, (y) in enumerate((330, 400)):
    ind(460, y, 44); F.line(404, 382 + k * 26, 458, y + 22, INK2, 1, arrow='end')
    for j in range(2): F.box(530, y + j * 24, 60, 20, '数据', 'red', 10, 3); F.line(484, y + 10 + j * 24, 528, y + 10 + j * 24, INK2, 1, arrow='end')
F.text(380, 458, '三级间址同理再多一层', 11, color=MUTED)
F.text(540, 120, '直接块指向数据块；\n一级间址指向索引块，\n索引块再指向数据块……', 12, 'middle', INK2, lh=1.5)
