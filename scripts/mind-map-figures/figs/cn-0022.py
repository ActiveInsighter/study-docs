LABEL = '带宽（数字设备中）：单位时间内通过链路的数据量，单位 bit/s'
F = Fig(640, 260, '带宽：最高数据率（bit/s）')
for k, n in enumerate((1, 2)):
    y = 70 + k * 80
    F.rect(40, y, 400, 26 + (n - 1) * 30, 'amber', 'none', 0, 2)
    for r in range(n):
        for i in range(5): F.box(56 + i * 80, y + 6 + r * 30, 30, 14, '', 'blue', rx=5); F.circle(63 + i * 80, y + 21 + r * 30, 3, '', 'dark', sw=0); F.circle(79 + i * 80, y + 21 + r * 30, 3, '', 'dark', sw=0)
F.box(470, 110, 140, 60, '拥有更宽的宽带，\n也就是拥有更大的\n信息运送能力', 'green', 11, 4)
F.text(320, 240, '“道路”更宽，单位时间能通过的“车”（比特）就更多', 11.5, color=MUTED)
