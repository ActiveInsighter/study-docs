LABEL = '低位交叉编址：流水线方式访问四个体，耗时 T + 4r'
F = Fig(640, 304, '低位交叉：轮流访问 M₀~M₃，耗时 T + 4r')
for i, m in enumerate(('M₀', 'M₁', 'M₂', 'M₃')):
    F.text(70, 204 - i * 36, m, 13, 'end', INK, valign='middle')
F.line(80, 230, 80, 56, INK2, 1.4, arrow='end'); F.line(80, 230, 600, 230, INK2, 1.4, arrow='end'); F.text(608, 230, 't', 13, 'start', INK, valign='middle')
T, r = 240, 60
for k in range(5):
    m = k % 4
    x = 84 + k * r
    F.box(x, 188 - m * 36, T, 30, f'取 {k}', 'blue' if k < 4 else 'green', 12, 0)
F.line(84 + 4 * r + T, 60, 84 + 4 * r + T, 232, ACCENT['red'], 1.4, dash='5 4')
F.brace(84, 84 + r, 232, 'r', color=ACCENT['red'])
F.text(84 + T / 2, 268, 'T', 13, color=INK, weight=700)
F.text(600, 290, 'T：存取周期　r：总线传送周期　流水线要求模块数 m ≥ T / r', 12, 'end', INK2)
