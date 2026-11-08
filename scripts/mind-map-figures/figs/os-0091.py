LABEL = '成组链接法示意：内存中的超级块与磁盘中各组的 s.free 链'
F = Fig(760, 380, '成组链接法')
def grp(x, y, n, vals, tone='white'):
    F.text(x - 6, y + 12, 'N', 10.5, 'end', INK2, valign='middle'); F.box(x, y, 34, 22, str(n), tone, 10.5, 0, True)
    for i, v in enumerate(vals):
        F.text(x - 6, y + 34 + i * 22, f's.free[{i if v != "…" else "…"}]' if v != '…' else '…', 10, 'end', INK2, valign='middle'); F.box(x, y + 22 + i * 22, 34, 22, v, tone, 10.5, 0, True)
F.rect(20, 140, 120, 180, 'none', INK2, 1.2, 10); F.text(80, 158, '内存', 11.5, color=INK2)
grp(90, 170, 3, ['2', '3', '4', '…', ''], 'blue')
grp(230, 60, 2, ['5', '6', '…', '', '', ''])
grp(380, 60, 4, ['7', '8', '9', '10', '…', ''])
grp(530, 60, 1, ['−1', '11', '', '', '', ''])
F.poly([(124, 203), (160, 203), (160, 80), (228, 80)], INK2, 1.1, arrow='end')
for (x, y, t) in ((160, 250, '3'), (160, 290, '4')):
    F.box(x + 30, y, 34, 20, '', 'blue', rx=0); F.text(x + 47, y + 32, t, 10.5, color=INK2)
F.line(124, 225, 188, 260, INK2, 1, arrow='end'); F.line(124, 247, 188, 300, INK2, 1, arrow='end')
F.poly([(264, 104), (300, 104), (300, 80), (378, 80)], INK2, 1.1, arrow='end')
F.poly([(414, 104), (450, 104), (450, 80), (528, 80)], INK2, 1.1, arrow='end')
F.text(380, 370, '超级块中 N 为本组空闲块数，s.free[0] 指向的盘块保存下一组的 N 与块号', 11, color=MUTED)
