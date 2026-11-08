LABEL = '多级先行进位加法器：单级（组内并行、组间串行）与两级（组内并行、组间并行）'
F = Fig(860, 470, '16 位先行进位加法器的两种组织方式')
def grp(x, y, i):
    F.box(x, y, 92, 44, '4 位 CLA\n加法器', 'blue', 12, 6)
    hi, lo = 4 * i + 4, 4 * i + 1
    F.line(x + 46, y, x + 46, y - 18, INK2, 1.2, arrow='end'); F.text(x + 46, y - 26, f'S_{{{hi}}}~S_{{{lo}}}', 11, color=INK)
    F.line(x + 30, y + 64, x + 30, y + 46, INK2, 1.2, arrow='end'); F.line(x + 62, y + 64, x + 62, y + 46, INK2, 1.2, arrow='end')
    F.text(x + 46, y + 76, f'A、B {hi}~{lo}', 11, color=MUTED)
F.text(30, 76, '① 单级先行进位：组内并行、组间串行', 13.5, 'start', INK, 700)
for i in range(4):
    x = 640 - i * 180
    grp(x, 110, i)
    F.line(x - 2, 132, x - 46, 132, ACCENT['red'], 1.5, arrow='end')
    F.text(x - 24, 124, ['C_{4}', 'C_{8}', 'C_{12}', 'C_{16}'][i], 11, color=ACCENT['red'])
F.line(780, 132, 734, 132, INK2, 1.3, arrow='end'); F.text(786, 132, 'C_{0}', 12, 'start', INK, valign='middle')
F.text(30, 256, '② 两级先行进位：组内并行、组间也并行', 13.5, 'start', INK, 700)
F.box(80, 274, 680, 28, 'CLA 电路（产生组间进位 C_{4}、C_{8}、C_{12}、C_{16}）', 'green', 12.5, 6)
for i in range(4):
    x = 640 - i * 180
    grp(x, 350, i)
    F.line(x + 14, 348, x + 14, 304, INK2, 1.2, arrow='end'); F.text(x + 8, 326, f'G*_{{{i + 1}}}P*_{{{i + 1}}}', 10.5, 'end', INK2)
    if i:
        F.line(x + 140, 304, x + 140, 368, ACCENT['green'], 1.2, arrow='end')
F.poly([(800, 372), (800, 288), (762, 288)], INK2, 1.2, arrow='end'); F.line(800, 372, 734, 372, INK2, 1.2, arrow='end'); F.text(806, 372, 'C_{0}', 12, 'start', INK, valign='middle')
F.line(78, 288, 40, 288, INK2, 1.2, arrow='end'); F.text(34, 288, 'C_{16}', 12, 'end', INK, valign='middle')
