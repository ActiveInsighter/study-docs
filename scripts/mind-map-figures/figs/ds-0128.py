LABEL = '链式基数排序：第三趟（百位）'
HL = lambda v: v[:0] + '[[red:' + v[0] + ']]' + v[0+1:]
F = Fig(760, 340, '链式基数排序 · 第三趟（百位）')
B = {0: ['008', '063', '083'], 1: ['109', '184'], 2: ['269', '278'], 5: ['505', '589'], 9: ['930']}
for q in range(10):
    x = 50 + q * 70
    F.text(x, 82, 'q[%d]' % q, 12.5, color=INK2, mono=True, weight=600)
    F.line(x, 88, x, 102, LINE, 1.2, arrow='end')
    for j, v in enumerate(B.get(q, [])):
        F.box(x - 25, 104 + j * 40, 50, 26, HL(v), 'blue', 12.5, 5, mono=True)
        if j: F.line(x, 104 + j * 40 - 14, x, 104 + j * 40 - 2, INK2, 1.2, arrow='end')
F.text(380, 246, '(a) 分配：按百位放入队列', 12.5, color=MUTED)
C = ['008', '063', '083', '109', '184', '269', '278', '505', '589', '930']
F.line(16, 279, 26, 279, INK2, 1.2, arrow='end')
for i, v in enumerate(C):
    F.box(28 + i * 72, 266, 52, 26, v, 'white', 12.5, 5, mono=True)
    if i < 9: F.line(80 + i * 72, 279, 98 + i * 72, 279, INK2, 1.2, arrow='end')
F.text(380, 318, '(b) 收集：按 q[0]…q[9] 依次首尾相接', 12.5, color=MUTED)
