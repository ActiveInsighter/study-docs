LABEL = '两机通信使用单缓冲：只能单向传输'
F = Fig(460, 260, '单缓冲：只能单向传输')
for x, t in ((40, 'A 机'), (260, 'B 机')):
    F.text(x + 80, 56, t, 14, color=INK, weight=700); F.rect(x, 66, 160, 150, 'none', INK2, 1.2, 4, dash='6 4')
    F.box(x + 50, 90, 60, 90, '', 'teal', rx=0); F.text(x + 80, 200, '缓冲区', 12.5, color=INK2)
F.line(152, 135, 308, 135, INK2, 1.6, arrow='both')
F.text(230, 246, '同一时刻只能一方发送、另一方接收', 11.5, color=MUTED)
