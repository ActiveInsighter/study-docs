LABEL = '设备分配的数据结构：SDT → DCT → COCT → CHCT'
F = Fig(560, 330, '设备分配的数据结构')
F.box(220, 40, 120, 44, 'CHCT', 'amber', 16, 8)
F.box(100, 130, 120, 44, 'COCT', 'blue', 16, 8); F.box(340, 130, 120, 44, 'COCT', 'blue', 16, 8)
F.rect(60, 220, 480, 96, 'none', INK2, 1.3, 12); F.text(50, 268, 'SDT', 14, 'end', INK, 700, valign='middle')
for i in range(5):
    x = 76 + i * 92
    F.box(x, 232, 74, 72, 'DCT', 'green', 14, 8)
    F.line(x + 37, 230, 160 if i < 3 else 400, 176, INK2, 1.2, arrow='end')
F.line(160, 128, 250, 86, INK2, 1.2, arrow='end'); F.line(400, 128, 310, 86, INK2, 1.2, arrow='end')
F.poly([(218, 50), (70, 50), (70, 150), (98, 150)], INK2, 1.2, arrow='end')
F.text(380, 46, 'SDT：系统设备表\nDCT：设备控制表\nCOCT：控制器控制表\nCHCT：通道控制表', 11, 'start', MUTED, lh=1.4)
