LABEL = '边界对齐：半字地址为 2 的倍数，字地址为 4 的倍数，不足处填充'
F = Fig(620, 330, '边界对齐方式（32 位字）')
rows = [[('字节1', 1, 'blue'), ('字节2', 1, 'blue'), ('字节3', 1, 'blue'), ('填充', 1, 'white')], [('半字1', 2, 'teal'), ('半字2', 2, 'teal')],
        [('半字3', 2, 'teal'), ('填充', 2, 'white')], [('字1', 4, 'violet')], [('字节4', 1, 'blue'), ('填充', 1, 'white'), ('半字4', 2, 'teal')],
        [('字节5', 1, 'blue'), ('字节6', 1, 'blue'), ('字节7', 1, 'blue'), ('填充', 1, 'white')], [('半字5', 2, 'teal'), ('填充', 2, 'white')], [('字2', 4, 'violet')]]
for r, row in enumerate(rows):
    x = 110
    for lab, n, t in row:
        F.box(x, 64 + r * 30, 100 * n, 30, lab, t, 13, 0)
        x += 100 * n
    F.text(100, 79 + r * 30, f'{r * 4}', 11, 'end', MUTED, mono=True, valign='middle')
F.text(310, 320, '一次访存即可取得一个对齐的字；代价是浪费填充空间', 12.5, color=MUTED)
