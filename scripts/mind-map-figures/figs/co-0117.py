LABEL = '不同指令的指令周期：取指、执行、间址、中断周期的组合'
F = Fig(700, 360, '指令周期 = 若干机器周期')
rows = [('空指令 NOP', [('取指周期', 'blue', 120)]), ('加法指令 ADD', [('取指周期', 'blue', 120), ('执行周期', 'green', 120)]),
        ('乘法指令 MUL', [('取指周期', 'blue', 120), ('执行周期（多个）', 'green', 220)]),
        ('间接寻址指令', [('取指周期', 'blue', 120), ('间址周期', 'amber', 120), ('执行周期', 'green', 120)]),
        ('有中断的间址指令', [('取指周期', 'blue', 120), ('间址周期', 'amber', 120), ('执行周期', 'green', 120), ('中断周期', 'red', 120)])]
for i, (name, segs) in enumerate(rows):
    y = 70 + i * 52
    F.text(140, y + 14, name, 12.5, 'end', INK, 600, valign='middle')
    x = 160
    for lab, t, w in segs:
        F.box(x, y, w, 28, lab, t, 12, 0); x += w
    F.line(160, y + 38, x, y + 38, LINE, 1.1, arrow='both'); F.text((160 + x) / 2, y + 38, '指令周期', 10.5, color=MUTED, valign='middle', chip=True)
F.text(350, 348, '只有检测到中断请求才进入中断周期（在执行周期末尾检测）', 12, color=MUTED)
