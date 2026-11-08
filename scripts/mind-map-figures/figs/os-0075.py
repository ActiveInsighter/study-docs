LABEL = '该打开文件来自 FAT 文件系统：vnode 的函数功能指针指向 FAT 提供的函数'
F = Fig(560, 280, 'vnode（v 结点）')
for i, t in enumerate(('文件名', '文件大小', '创建者', '文件格式', '……', '函数功能指针')):
    F.box(40, 56 + i * 28, 140, 28, t, 'red' if i == 5 else 'white', 12, 0)
F.text(110, 236, 'vnode（v 结点）', 12, color=ACCENT['red']); F.text(110, 258, '该打开文件来自 FAT 文件系统', 11, color=INK2)
for i, t in enumerate(('open', 'read', 'write', '…')):
    F.box(330, 110 + i * 26, 120, 26, t, 'teal', 12, 0, t != '…')
F.text(390, 238, 'FAT 文件系统提供的函数功能', 11.5, color=INK2)
F.line(182, 210, 328, 156, INK2, 1.4, arrow='end')
