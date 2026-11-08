from common import flow
LABEL = 'DMA 方式'
F = Fig(560, 306, 'DMA 方式')
cs = flow(F, 60, 70, [('给 I/O 控制器发出读块命令', 'box'), ('读 DMA 控制器的状态', 'box'), ('下一条指令', 'gray')], w=190, h=40, gap=22)
F.text(276, cs[0][1], 'CPU → DMA；CPU 去做其他事情', 12, 'start', ACCENT['red'], 600 if 'red' == 'red' else 400, valign='middle', lh=1.3)
F.text(276, cs[1][1], 'DMA 控制器发出中断\nDMA → CPU', 12, 'start', ACCENT['red'], 600 if 'red' == 'red' else 400, valign='middle', lh=1.3)
F.text(280, 286, '以块为单位传送，只在一块开始和结束时需要 CPU 干预', 11.5, color=MUTED)
