LABEL = '异步传输：以字符为单位，每个字符加起始位和终止位'
F = Fig(620, 280, '异步传输')
F.line(40, 150, 580, 150, ACCENT['blue'], 1.4, arrow='end'); F.text(588, 150, 't', 12, 'start', INK, valign='middle')
for i in range(5):
    x = 70 + i * 100
    F.box(x, 90, 40, 60, '', 'green' if i != 2 else 'dark', rx=0); F.text(x + 20, 80, f'字节 {5 - i}', 11.5, color=INK2)
F.cells(130, 190, ['', 'b7', 'b6', 'b5', 'b4', 'b3', 'b2', 'b1', 'b0', ''], 34, 30, {i: 'green' for i in range(1, 9)}, size=12)
F.text(147, 240, '终止位', 11.5, color=INK2); F.text(453, 240, '起始位', 11.5, color=INK2)
F.text(310, 268, '发送方可在任何时刻发送；收方不知道它们何时到达，靠起止位识别', 11, color=MUTED)
