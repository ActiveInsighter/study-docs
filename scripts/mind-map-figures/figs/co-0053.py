LABEL = '三总线结构：主存总线、I/O 总线、DMA 总线'
F = Fig(620, 320, '三总线结构')
F.box(40, 60, 80, 36, 'CPU', 'blue', 13, 5); F.box(40, 180, 80, 32, '主存', 'blue', 13, 5)
F.line(122, 78, 600, 78, ACCENT['red'], 2, arrow='both'); F.text(360, 66, 'I/O 总线', 12.5, color=ACCENT['red'])
F.line(80, 98, 80, 178, ACCENT['red'], 1.6, arrow='both'); F.text(90, 140, '主存总线', 12, 'start', ACCENT['red'])
for i, dev in enumerate(('磁盘机', '打印机', '显示器')):
    x = 220 + i * 130
    F.line(x + 40, 82, x + 40, 178, INK2, 1.6, arrow='both')
    F.box(x, 180, 80, 32, 'I/O 接口', 'white', 12, 5)
    F.line(x + 40, 214, x + 40, 256, INK2, 1.6, arrow='both')
    F.box(x, 258, 80, 32, dev, 'gray', 12, 5)
F.line(122, 196, 218, 196, ACCENT['red'], 1.6, arrow='both'); F.text(170, 222, 'DMA 总线', 12, color=ACCENT['red'])
F.text(310, 312, '高速外设经 DMA 总线直接与主存交换数据', 11.5, color=MUTED)
