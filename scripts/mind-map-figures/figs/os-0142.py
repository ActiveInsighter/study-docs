LABEL = '文件系统的层次结构'
F = Fig(300, 420, '文件系统结构')
labs = ['应用程序', '逻辑文件系统', '文件组织模块', '基本文件系统', 'I/O 控制']
for i, t in enumerate(labs):
    y = 60 + i * 62
    F.box(60, y, 180, 34, t, 'white' if i == 0 else 'blue', 13, 4)
    if i: F.line(140, y - 4, 140, y - 24, INK2, 1.3, arrow='end'); F.line(160, y - 26, 160, y - 6, INK2, 1.3, arrow='end')
F.ellipse(150, 384, 60, 22, '设备', 'gray', 13)
F.line(140, 360, 140, 344, INK2, 1.3, arrow='end'); F.line(160, 344, 160, 360, INK2, 1.3, arrow='end')
