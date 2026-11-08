LABEL = '双端口 RAM：两个独立端口分别连接两个 CPU'
F = Fig(640, 280, '双端口 RAM')
F.box(30, 60, 110, 190, 'CPU₁', 'blue', 16, 8, weight=700); F.box(500, 60, 110, 190, 'CPU₂', 'blue', 16, 8, weight=700)
F.box(265, 60, 110, 190, '双端口\nRAM', 'red', 15, 8, weight=700)
for i, (lab, both) in enumerate((('数据线', True), ('地址线', False), ('控制线', False))):
    y = 98 + i * 58
    F.line(142 if not both else 144, y, 262, y, INK2, 2.4, arrow='both' if both else 'end'); F.text(202, y - 10, lab, 12, color=INK2)
    F.line(498 if not both else 496, y, 378, y, INK2, 2.4, arrow='both' if both else 'end'); F.text(438, y - 10, lab, 12, color=INK2)
F.text(320, 270, '同时访问同一地址且有写操作会冲突：置 busy 信号，暂时关闭一个端口', 12, color=MUTED)
