LABEL = '四位全先行进位加法器：CLA 部件 + 4 个全加器'
F = Fig(800, 330, '4 位全先行进位加法器')
F.box(60, 60, 660, 34, '4 位 CLA 部件', 'green', 14, 6)
for i in range(4):
    x = 570 - i * 160
    F.box(x, 190, 90, 50, 'FA', 'blue', 14, 6, weight=600)
    F.line(x + 18, 188, x + 18, 96, INK2, 1.2, arrow='end'); F.line(x + 32, 188, x + 32, 96, INK2, 1.2, arrow='end')
    F.text(x + 25, 112, f'G_{{{i + 1}}} P_{{{i + 1}}}', 11.5, 'end', INK2, halo=True)
    F.line(x + 60, 188, x + 60, 164, INK2, 1.2, arrow='end'); F.text(x + 60, 156, f'S_{{{i + 1}}}', 12, color=INK)
    if i < 3:
        F.poly([(x - 20, 96), (x - 20, 215), (x - 2, 215)], ACCENT['violet'], 1.2, arrow='end'); F.text(x - 26, 140, f'C_{{{i + 1}}}', 11.5, 'end', ACCENT['violet'])
    for j, s in enumerate(('A', 'B')):
        F.line(x + 30 + j * 30, 280, x + 30 + j * 30, 242, INK2, 1.2, arrow='end'); F.text(x + 30 + j * 30, 294, f'{s}_{{{i + 1}}}', 12, color=INK)
F.poly([(770, 215), (740, 215), (662, 215)], INK2, 1.2, arrow='end'); F.poly([(740, 215), (740, 77), (722, 77)], INK2, 1.2, arrow='end'); F.text(776, 215, 'C_{0}', 12.5, 'start', INK, valign='middle')
F.line(58, 77, 30, 77, INK2, 1.2, arrow='end'); F.text(24, 77, 'C_{4}', 12.5, 'end', INK, valign='middle')
