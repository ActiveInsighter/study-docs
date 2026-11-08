LABEL = '5 位无符号阵列乘法器：同时得到多位乘积'
F = Fig(820, 410, '5 位无符号阵列乘法器')
for j in range(5):
    for i in range(5):
        x, y = 640 - i * 64 - j * 64 + 64 * 0, 80 + j * 52
        x = 700 - (i + j) * 64 + j * 0
        F.box(x - 26, y - 13, 52, 26, f'x_{{{i}}}y_{{{j}}}', 'blue' if j == 0 else 'white', 11.5, 4)
        if j > 0:
            F.circle(x - 32, y + 22, 7, '', 'green', sw=1.2)
            F.text(x - 32, y + 22, '+', 10, color=TONES['green'][2], valign='middle', weight=700)
for k in range(10):
    x = 700 - k * 64
    F.line(x, 330, x, 352, INK2, 1.2, arrow='end'); F.text(x, 368, f'P_{{{k}}}', 12, color=INK, mono=True)
F.text(60, 90, '每个 x_{i}y_{j} 是一个与门；', 12.5, 'start', INK2)
F.text(60, 112, '绿色为全加器，逐行累加部分积', 12.5, 'start', INK2)
F.text(60, 134, '所有部分积同时产生，速度快', 12.5, 'start', ACCENT['green'])
F.text(410, 400, '第 j 行是 X 与 y_{j} 的部分积，左移 j 位后与上一行相加，得到乘积 P_{9} ~ P_{0}', 12, color=MUTED)
