LABEL = '边界不对齐：数据紧密存放，一个半字或字可能跨两个存储字'
F = Fig(620, 252, '边界不对齐方式（紧密存放）')
rows = [[('字节1', 1, 'blue'), ('字节2', 1, 'blue'), ('字节3', 1, 'blue'), ('半字1-1', 1, 'teal')], [('半字1-2', 1, 'teal'), ('半字2', 2, 'teal'), ('半字3-1', 1, 'teal')],
        [('半字3-2', 1, 'teal'), ('字1-1', 3, 'violet')], [('字1-2', 1, 'violet'), ('字节1', 1, 'blue'), ('半字1', 2, 'teal')], [('字2', 4, 'violet')]]
for r, row in enumerate(rows):
    x = 110
    for lab, n, t in row:
        hot = '-' in lab
        F.box(x, 64 + r * 30, 100 * n, 30, lab, 'red' if hot else t, 13, 0)
        x += 100 * n
F.text(310, 240, '红色：跨越两个存储字，读一个半字也可能需要 2 次访存', 12.5, color=MUTED)
