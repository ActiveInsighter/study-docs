LABEL = '单总线结构：CPU、主存、I/O 都挂在一组系统总线上'
F = Fig(640, 220, '单总线结构')
F.line(40, 80, 600, 80, INK2, 3, arrow='both'); F.text(320, 66, '系统总线', 12.5, color=INK2)
for i, lab in enumerate(('CPU', '主存', '设备接口', '设备接口')):
    x = 70 + i * 140
    F.line(x + 40, 84, x + 40, 148, INK2, 1.6, arrow='both')
    F.box(x, 150, 80, 34, lab, 'blue' if i < 2 else 'white', 12.5, 6)
F.text(510, 167, '…', 14, color=MUTED, valign='middle')
F.text(320, 206, '结构简单、成本低；但带宽低、多部件争用总线、不支持并行传送', 12, color=MUTED)
