LABEL = '独立编址 I/O：I/O 端口与内存是两个独立的地址空间'
F = Fig(520, 360, '独立编址 I/O：两个地址空间')
F.box(150, 60, 160, 260, '内存', 'blue', 16, 0); F.box(340, 270, 120, 50, 'I/O 端口', 'teal', 14, 0)
F.text(140, 70, '0xFFFF FFFF', 12, 'end', INK2, mono=True); F.text(140, 316, '0', 12, 'end', INK2, mono=True)
F.text(260, 344, '需要专门的 I/O 指令（如 IN、OUT）访问端口', 11.5, color=MUTED)
