LABEL = 'CM 中的微指令序列：取指、间址、中断周期为公共微程序，各指令有自己的执行周期微程序'
F = Fig(620, 540, 'CM 中的微指令序列')
F.text(70, 66, '微指令\n存放地址', 11.5, 'middle', INK2, lh=1.2); F.text(250, 72, '微指令操作码', 12, color=INK2); F.text(380, 72, '下地址', 12, color=INK2)
rows = [('0', '', '1'), ('1', '', '2'), ('2', '', '3'), ('3…7', '…\n转执行周期', ''), ('8…12', '…\n转取指周期', ''), ('13', '', '14'), ('14', '', '15'), ('15', '', '0'), ('16', '', '17'), ('17', '', '18'), ('18', '', '0')]
groups = [(0, 3, '取指周期 微程序', 'green'), (3, 4, '间址周期 微程序', 'amber'), (4, 5, '中断周期 微程序', 'violet'), (5, 8, 'LDA 指令的执行周期微程序', 'blue'), (8, 11, 'STA 指令的执行周期微程序', 'blue')]
y = 90
ys = []
for a, b, c in rows:
    h = 54 if '\n' in b else 34
    F.box(110, y, 210, h, b, 'white', 11.5, 0); F.box(320, y, 120, h, c, 'white', 12, 0, True)
    F.text(80, y + h / 2, a, 11.5, 'middle', ACCENT['blue'], mono=True, valign='middle')
    ys.append((y, y + h)); y += h
for a, b, lab, t in groups:
    y1, y2 = ys[a][0], ys[b - 1][1]
    F.line(110, y2, 440, y2, ACCENT[t], 2)
    F.vbrace(446, y1 + 2, y2 - 2, lab, color=ACCENT[t], size=11.5)
F.box(110, y, 330, 26, '⋮', 'light', 12, 0)
