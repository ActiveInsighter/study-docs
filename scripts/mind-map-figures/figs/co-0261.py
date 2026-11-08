LABEL = '高位交叉编址：连续访问同一个体，耗时 5T'
F = Fig(640, 260, '高位交叉：连续地址都在 M₀，耗时 5T')
for i, m in enumerate(('M₀', 'M₁', 'M₂', 'M₃')):
    F.text(70, 194 - i * 34, m, 13, 'end', INK, valign='middle')
F.line(80, 216, 80, 60, INK2, 1.4, arrow='end'); F.line(80, 216, 600, 216, INK2, 1.4, arrow='end'); F.text(608, 216, 't', 13, 'start', INK, valign='middle')
for k in range(5):
    F.box(84 + k * 96, 178, 96, 32, f'取 {k}', 'blue', 12, 0)
    F.text(84 + (k + 1) * 96, 234, f'{k + 1}T', 12, color=INK2, mono=True)
F.text(330, 254, '每次都要等同一个存储体存取（含恢复）完成后才能访问下一个', 11.5, color=MUTED)
