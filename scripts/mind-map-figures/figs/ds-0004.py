LABEL = '共享栈：两个顺序栈共享一段存储空间'
F = Fig(720, 280, '共享栈 · 两个顺序栈共享存储空间')
n = 14; cw = 44; x0 = 52; y = 108
vals = ['a₀','a₁','a₂','a₃','','','','','','','b₃','b₂','b₁','b₀']
tones = {i: 'blue' for i in range(4)}
tones.update({i: 'green' for i in range(10, 14)})
F.cells(x0, y, vals, cw, 40, tones, size=14)
F.text(x0, y - 12, '0', 12, 'start', MUTED, mono=True)
F.text(x0 + n * cw, y - 12, 'MaxSize−1', 12, 'end', MUTED, mono=True)
# growth arrows
F.line(x0 + 4 * cw + 10, y + 20, x0 + 6 * cw, y + 20, ACCENT['blue'], 1.5, dash='4 4', arrow='end')
F.line(x0 + 10 * cw - 10, y + 20, x0 + 8 * cw, y + 20, ACCENT['green'], 1.5, dash='4 4', arrow='end')
def ptr(i, label, tone, sub):
    cx = x0 + i * cw + cw / 2
    F.line(cx, y + 92, cx, y + 46, ACCENT[tone], 1.5, arrow='end')
    F.text(cx, y + 110, label, 14, color=TONES[tone][2], weight=600, mono=True)
    F.text(cx, y + 128, sub, 12, color=MUTED)
ptr(0, '栈底', 'blue', '0 号栈')
ptr(3, 'top0', 'blue', '0 号栈顶')
ptr(10, 'top1', 'green', '1 号栈顶')
ptr(13, '栈底', 'green', '1 号栈')
F.text(360, 262, '栈满：top1 − top0 = 1　　入栈：0 号 ++top0，1 号 −−top1', 13, color=INK2)
