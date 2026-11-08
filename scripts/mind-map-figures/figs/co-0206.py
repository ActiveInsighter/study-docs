LABEL = 'GB2312-80：区位码 → 国标码 → 汉字内码'
F = Fig(700, 420, 'GB2312-80：汉字 + 各种符号共 7445 个')
rows = [('区位码', '16', '01', '例：“啊”'), ('（十六进制）', '10H', '01H', ''), ('国标码', '30H', '21H', ''), ('汉字内码', 'B0H', 'A1H', '')]
ys = [90, 150, 230, 310]
for (lab, a, b, note), y in zip(rows, ys):
    F.text(330, y, lab, 13.5, 'end', INK2, 600, valign='middle')
    F.box(350, y - 16, 70, 32, a, 'white', 14, 6, True); F.box(440, y - 16, 70, 32, b, 'white', 14, 6, True)
    if note: F.text(530, y, note, 12, 'start', MUTED, valign='middle')
for x in (385, 475):
    F.line(x, 106, x, 132, LINE, 1.3, arrow='end')
    F.line(x, 166, x, 212, INK2, 1.4, arrow='end'); F.line(x, 246, x, 292, INK2, 1.4, arrow='end')
F.text(520, 190, '+20H', 13, 'start', ACCENT['green'], 600, mono=True); F.text(520, 270, '+80H', 13, 'start', ACCENT['amber'], 600, mono=True)
F.box(40, 72, 200, 40, '区位码：直观，方便人类理解', 'blue', 12.5, 8)
F.box(40, 168, 200, 44, '+20H：避开 ASCII 的控制 /\n通信字符（00H~1FH）', 'green', 12, 8)
F.box(40, 248, 200, 44, '+80H：最高位置 1，\n与 ASCII 码区分', 'amber', 12, 8)
F.line(430, 330, 430, 362, INK2, 1.4, arrow='end'); F.box(370, 364, 120, 34, '计算机内部处理', 'dark', 13, 8)
