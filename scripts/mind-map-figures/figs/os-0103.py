LABEL = '索引文件：定长记录的顺序文件配合索引表'
F = Fig(640, 280, '索引文件（索引表 + 逻辑文件）')
F.table(30, 70, [['索引号', '长度 m', '指针 ptr'], ['0', 'm₀', '●'], ['1', 'm₁', '●'], ['…', '…', ''], ['i', 'mᵢ', '●'], ['…', '…', '']], [70, 80, 80], 30, size=12, head_tone='gray', zebra=False)
F.text(145, 268, '索引表', 12, color=INK2)
for i, t in enumerate(('R₀', 'R₁', '…', 'Rᵢ', '…')): F.box(420, 70 + i * 36, 170, 36, t, 'blue' if t != '…' else 'white', 12, 0)
F.text(505, 268, '逻辑文件', 12, color=INK2)
for r, tgt in ((1, 0), (2, 1), (4, 3)): F.line(220, 85 + r * 30, 418, 88 + tgt * 36, INK2, 1.1, arrow='end')
