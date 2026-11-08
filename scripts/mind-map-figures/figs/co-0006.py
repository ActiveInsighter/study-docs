LABEL = '停止 CPU 访存：DMA 传送期间 CPU 不访问主存'
F = Fig(660, 230, '停止 CPU 访存')
F.text(120, 76, '主存工作时间', 12.5, 'end', INK, valign='middle'); F.line(130, 76, 640, 76, INK2, 1.4)
F.line(130, 60, 130, 210, INK2, 1.4)
F.text(120, 130, 'CPU 控制\n并使用主存', 12, 'end', ACCENT['green'], valign='middle', lh=1.3); F.text(120, 186, 'DMA 控制\n并使用主存', 12, 'end', ACCENT['red'], valign='middle', lh=1.3)
for a, b in [(130, 260), (380, 500)]: F.line(a, 130, b, 130, ACCENT['green'], 2.4)
for a, b in [(260, 380), (500, 630)]: F.line(a, 186, b, 186, ACCENT['red'], 2.4)
for x in sorted(set([p for seg in [(130, 260), (380, 500)] + [(260, 380), (500, 630)] for p in seg])): F.line(x, 80, x, 200, LINE, 0.8, dash='3 3')
F.text(390, 222, 'DMA 传送一批数据时独占主存，CPU 处于不工作或保持状态', 11.5, color=MUTED)
