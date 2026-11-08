LABEL = 'DMA 请求：I/O 设备向 DMA 控制器请求，DMA 控制器再向 CPU 请求总线'
F = Fig(600, 170)
F.box(20, 40, 130, 48, 'I/O 设备', 'blue', 15, 8); F.box(235, 40, 130, 48, 'DMA 控制器', 'blue', 15, 8); F.box(450, 40, 130, 48, 'CPU', 'blue', 15, 8)
F.line(150, 64, 233, 64, INK2, 1.5, arrow='end'); F.text(192, 54, 'DMA 请求', 12.5, color=INK2)
F.line(365, 64, 448, 64, INK2, 1.5, arrow='end'); F.text(406, 54, '总线请求', 12.5, color=INK2)
F.brace(85, 515, 100, '整个过程称为 DMA 请求', size=13)
