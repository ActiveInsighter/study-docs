LABEL = '4 路平衡归并：增加输入缓冲区数目实现多路归并'
F = Fig(620, 284, '4 路平衡归并的排序过程')
xs = [50 + i * 74 for i in range(8)]
for i, x in enumerate(xs):
    F.box(x - 26, 70, 52, 30, f'R{i + 1}', 'violet', 13, mono=True)
for g, x in ((0, 161), (1, 457)):
    for i in range(4):
        F.line(xs[g * 4 + i], 100, x, 146, INK2, 1.3, arrow='end')
    F.box(x - 30, 148, 60, 30, f"R{g + 1}'", 'blue', 13, mono=True)
    F.line(x, 178, 309, 206, INK2, 1.3, arrow='end')
F.box(249, 208, 120, 32, '有序文件', 'green', 14)
F.text(40, 128, '第 1 趟', 12, 'start', MUTED); F.text(40, 198, '第 2 趟', 12, 'start', MUTED)
F.text(310, 270, '4 路归并需 4 个输入缓冲区 + 1 个输出缓冲区', 12.5, 'middle', MUTED)
