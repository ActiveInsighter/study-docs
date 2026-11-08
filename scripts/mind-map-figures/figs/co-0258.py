LABEL = '存储控制器、存储器总线、内存条和 DRAM 芯片之间的连接'
F = Fig(800, 300, '主存的基本组成')
F.box(30, 70, 110, 44, '存储控制器', 'violet', 13, 6)
F.line(142, 92, 210, 92, INK, 3, arrow='both'); F.text(176, 80, '存储器总线', 11, color=INK2)
for i in range(8):
    F.box(212 + i * 70, 64, 58, 56, f'SIMM\n插槽{i}', 'blue', 11, 4)
F.rect(150, 170, 580, 100, '#e8effc', ACCENT['blue'], 1.3, 8); F.text(440, 190, 'DRAM SIMM 内存条', 12, color=INK2)
F.line(212, 120, 150, 170, LINE, 1); F.line(270, 120, 730, 170, LINE, 1)
for r in range(2):
    for c, x in enumerate((180, 260, 340, 540, 620)):
        if c == 3 - 1 + 0 and False: pass
    for x in (180, 270, 580, 660):
        F.box(x, 204 + r * 32, 66, 24, 'DRAM', 'amber', 11.5, 3)
    F.text(440, 216 + r * 32, '……', 12, color=MUTED, valign='middle')
