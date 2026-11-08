LABEL = '链式基数排序：第二趟（十位）'
HL = lambda v: v[:1] + '[[red:' + v[1] + ']]' + v[1+1:]
F = Fig(760, 340, '链式基数排序 · 第二趟（十位）')
B = {0: ['505', '008', '109'], 3: ['930'], 6: ['063', '269'], 7: ['278'], 8: ['083', '184', '589']}
for q in range(10):
    x = 50 + q * 70
    F.text(x, 82, 'q[%d]' % q, 12.5, color=INK2, mono=True, weight=600)
    F.line(x, 88, x, 102, LINE, 1.2, arrow='end')
    for j, v in enumerate(B.get(q, [])):
        F.box(x - 25, 104 + j * 40, 50, 26, HL(v), 'blue', 12.5, 5, mono=True)
        if j: F.line(x, 104 + j * 40 - 14, x, 104 + j * 40 - 2, INK2, 1.2, arrow='end')
F.text(380, 246, '(a) 分配：按十位放入队列', 12.5, color=MUTED)
C = ['505', '008', '109', '930', '063', '269', '278', '083', '184', '589']
F.line(16, 279, 26, 279, INK2, 1.2, arrow='end')
for i, v in enumerate(C):
    F.box(28 + i * 72, 266, 52, 26, v, 'white', 12.5, 5, mono=True)
    if i < 9: F.line(80 + i * 72, 279, 98 + i * 72, 279, INK2, 1.2, arrow='end')
F.text(380, 318, '(b) 收集：按 q[0]…q[9] 依次首尾相接', 12.5, color=MUTED)
