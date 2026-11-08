LABEL = '三总线结构：DMA 总线使 I/O 与主机并行工作'
F = Fig(560, 200, 'DMA 总线：I/O 与主机并行')
F.box(30, 60, 90, 34, 'CPU', 'gray', 13, 4); F.box(30, 140, 90, 34, '主存', 'blue', 13, 4)
F.line(122, 77, 540, 77, INK2, 1.6, arrow='both'); F.text(330, 66, 'I/O 总线', 11.5, color=INK2)
F.line(75, 96, 75, 138, INK2, 1.6, arrow='both'); F.text(84, 120, '主存总线', 11, 'start', INK2)
for i, (t, tone) in enumerate((('DMA 接口', 'amber'), ('IO 接口', 'amber'), ('IO 接口', 'amber'))):
    x = 200 + i * 120
    F.line(x + 45, 80, x + 45, 138, '#c98a12', 2.6, arrow='both'); F.box(x, 140, 90, 34, t, tone, 12, 4)
F.line(122, 157, 198, 157, INK2, 1.6, arrow='both'); F.text(160, 186, 'DMA 总线', 11, color=INK2)
