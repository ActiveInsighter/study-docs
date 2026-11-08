LABEL = '希尔排序示例：增量 5、3、1'
F = Fig(640, 360, '希尔排序（d = 5 → 3 → 1）')
pal = ['blue', 'green', 'amber', 'violet', 'red']
rows = [('初始 d=5', '49 38 65 97 76 13 27 49* 55 04', 5), ('一趟后 d=3', '13 27 49* 55 04 49 38 65 97 76', 3),
        ('二趟后 d=1', '13 04 49* 38 27 49 55 65 97 76', 1), ('三趟后', '04 13 27 38 49* 49 55 65 76 97', 0)]
for r, (lab, s, d) in enumerate(rows):
    y = 72 + r * 64
    v = s.split()
    t = {i: pal[i % d] for i in range(10)} if d > 1 else ({} if d == 1 else {i: 'gray' for i in range(10)})
    F.text(112, y + 15, lab, 12.5, 'end', INK2, 500, valign='middle')
    F.cells(124, y, v, 48, 30, t, size=13)
    note = {5: '同色为一组（间隔 5），组内直接插入排序', 3: '间隔 3 分组', 1: '最后对整体做一次直接插入排序', 0: ''}[d]
    if note: F.text(124, y + 48, note, 12, 'start', MUTED)
F.text(320, 344, '希尔排序不稳定：49 与 49* 的相对次序发生了变化', 12.5, color=ACCENT['red'])
