from common import bitfield
LABEL = '浮点数的一般格式：阶码 E（阶符 + 阶码数值）与尾数 M（数符 + 尾数数值）'
F = Fig(620, 200)
bitfield(F, 30, 70, ['J_{f}', 'J_{1}J_{2}…J_{m}', 'S_{f}', 'S_{1}S_{2}…S_{n}'], [60, 190, 60, 250], {0: 'green', 1: 'green', 2: 'blue', 3: 'blue'}, 15, 44)
F.brace(30, 280, 62, '', down=False); F.pill(155, 20, '阶码 E', 'green', 13, anchor='middle')
F.brace(280, 590, 62, '', down=False); F.pill(435, 20, '尾数 M', 'blue', 13, anchor='middle')
for x, t in ((60, '阶符'), (185, '阶码数值部分'), (370, '数符'), (465, '尾数数值部分')):
    F.text(x, 140, t, 12.5, color=INK2)
F.text(310, 180, 'N = r^{E} × M：阶码决定范围，尾数决定精度，数符决定正负', 12.5, color=MUTED)
