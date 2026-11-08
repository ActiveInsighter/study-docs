LABEL = '4 位 CLA 部件：由 G、P 与 C0 同时生成 C1~C4'
F = Fig(760, 320, '4 位 CLA 部件（先行进位电路）')
F.box(60, 110, 640, 70, 'CLA 部件（与或两级门电路）', 'green', 15, 10)
for i in range(4):
    x = 610 - i * 160
    for j, s in enumerate(('G', 'P')):
        xx = x + j * 30 - 15
        F.line(xx, 240, xx, 182, INK2, 1.3, arrow='end'); F.text(xx, 254, f'{s}_{{{i + 1}}}', 12.5, color=ACCENT['green'] if s == 'G' else ACCENT['red'], mono=True)
    F.line(x, 108, x, 76, INK2, 1.3, arrow='end'); F.text(x, 68, f'C_{{{i + 1}}}', 13, color=INK, mono=True)
F.poly([(740, 260), (740, 145), (702, 145)], INK2, 1.3); F.text(740, 274, 'C_{0}', 13, color=INK, mono=True)
F.text(380, 304, '每个 C_{i} 都是 G、P、C_{0} 的与或式，只需两级门延迟，4 个进位同时产生', 12.5, color=MUTED)
