LABEL = '实例：UNIX 文件系统的目录与索引结点'
F = Fig(900, 380, '实例：UNIX 文件系统的目录 & 索引结点')
F.tree(10, 80, ('□根目录', ['□A', '□B', '□C']), unit=80, levelh=60, size=12)
F.table(20, 170, [['文件名（14B）', 'inode 号（2B）'], ['A', '1'], ['B', '2'], ['C', '4']], [100, 100], 26, size=11.5, head_tone='blue')
F.text(120, 290, '根目录：包含 3 个目录项', 11, color=INK2)
fields = ['所有者', '创建时间', '总块数', '共享计数', '直接索引 0', '直接索引 1', '直接索引 2', '…', '直接索引 9', '一级间接', '二级间接', '三级间接']
vals = {0: {2: '1', 4: '5'}, 1: {2: '2', 4: '6', 5: '7'}, 2: {2: '3', 4: '10', 5: '12', 6: '8'}, 3: {}, 4: {2: '12', 4: '16', 8: '19', 9: '21', 10: 'NULL', 11: 'NULL'}, 5: {}}
notes = ['根目录的 inode', '文件 A 的 inode', '文件 B 的 inode', '暂未使用', '文件 C 的 inode', '暂未使用']
for k in range(6):
    x = 260 + k * 104
    F.box(x, 60, 100, 22, str(k), 'gray', 11, 0, True)
    for i, f in enumerate(fields):
        y = 84 + i * 16
        F.box(x + 2, y, 66, 16, f, 'amber' if i >= 4 else 'white', 8.5, 0); F.box(x + 68, y, 30, 16, vals[k].get(i, ''), 'amber' if i >= 4 else 'white', 9, 0, True)
    F.text(x + 50, 290, notes[k], 9.5, color=ACCENT['green'] if '未' in notes[k] else ACCENT['red'])
segs = [('引导块（开机初始化 OS）', 190, 'gray'), ('超级块', 60, 'gray'), ('空闲空间管理（如位示图）', 150, 'gray'), ('i 结点区', 70, 'amber'), ('根目录', 70, 'blue'), ('其他文件、目录', 280, 'white')]
x = 70
F.text(62, 328, 'UNIX 文件\n系统', 10.5, 'end', INK2, lh=1.2, valign='middle')
for t, w, tone in segs: F.box(x, 312, w, 34, t, tone, 11, 0); x += w
