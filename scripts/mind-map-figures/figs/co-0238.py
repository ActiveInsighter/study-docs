LABEL = '增加中断屏蔽功能：MASK 为该中断的中断屏蔽字'
F = Fig(640, 340, '中断屏蔽：INTRᵢ 与 MASK̄ᵢ 相与')
xs = [60, 190, 320, 450]
for i, x in enumerate(xs):
    F.text(x + 20, 62, f'INTP_{{{i + 1}}}', 12, color=INK, mono=True)
    F.line(x + 20, 116, x + 20, 76, INK2, 1.2, arrow='end'); F.text(x + 28, 96, '1' if i == 0 else '0', 10.5, 'start', ACCENT['red'])
    F.box(x, 116, 40, 28, '1', 'white', 12, 3); F.box(x, 186, 40, 28, '&', 'white', 12, 3)
    F.line(x + 20, 146, x + 20, 184, INK2, 1.2); F.circle(x + 20, 164, 2.5, '', 'dark', sw=0)
    F.line(x + 12, 216, x + 12, 262, INK2, 1.2); F.line(x + 28, 216, x + 28, 262, INK2, 1.2)
    F.text(x + 20, 278 + (i % 2) * 18, f'INTR_{{{i + 1}}}  M̄ASK_{{{i + 1}}}', 11, color=ACCENT['red'], mono=True)
    for j in range(i):
        F.poly([(xs[j] + 20, 164), (xs[j] + 34, 164), (xs[j] + 34, 232 + j * 5), (x + 34, 232 + j * 5), (x + 34, 216)], INK2, 1)
F.box(160, 312, 320, 24, '增加中断屏蔽功能', 'red', 11.5, 4)
