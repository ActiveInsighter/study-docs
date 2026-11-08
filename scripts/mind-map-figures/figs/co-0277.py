LABEL = '周期窃取：DMA 需要时窃取一个存取周期'
F = Fig(660, 230, '周期窃取')
F.text(120, 76, '主存工作时间', 12.5, 'end', INK, valign='middle'); F.line(130, 76, 640, 76, INK2, 1.4)
F.line(130, 60, 130, 210, INK2, 1.4)
F.text(120, 130, 'CPU 控制\n并使用主存', 12, 'end', ACCENT['green'], valign='middle', lh=1.3); F.text(120, 186, 'DMA 控制\n并使用主存', 12, 'end', ACCENT['red'], valign='middle', lh=1.3)
for a, b in [(130, 170), (200, 350), (380, 470), (500, 540)]: F.line(a, 130, b, 130, ACCENT['green'], 2.4)
for a, b in [(170, 200), (350, 380), (470, 500)]: F.line(a, 186, b, 186, ACCENT['red'], 2.4)
for x in sorted(set([p for seg in [(130, 170), (200, 350), (380, 470), (500, 540)] + [(170, 200), (350, 380), (470, 500)] for p in seg])): F.line(x, 80, x, 200, LINE, 0.8, dash='3 3')
F.text(390, 222, 'DMA 请求时，CPU 让出一个存取周期；同时请求时 DMA 优先', 11.5, color=MUTED)
