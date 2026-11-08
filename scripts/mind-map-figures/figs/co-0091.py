LABEL = '统一编址（内存映射 I/O）：I/O 端口占用内存地址空间的一部分'
F = Fig(520, 360, '内存映射 I/O：一个地址空间')
F.box(180, 60, 160, 50, 'I/O 端口', 'teal', 14, 0); F.box(180, 110, 160, 210, '内存', 'blue', 16, 0)
F.text(170, 70, '0xFFFF FFFF', 12, 'end', INK2, mono=True); F.text(170, 316, '0', 12, 'end', INK2, mono=True)
F.text(260, 344, '用普通访存指令即可访问 I/O 端口', 11.5, color=MUTED)
