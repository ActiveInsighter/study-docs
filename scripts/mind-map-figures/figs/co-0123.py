from common import bitfield
LABEL = '无符号数：n 位全部是数值位'
F = Fig(560, 170)
p = bitfield(F, 30, 34, ['x_{0}', 'x_{1}', 'x_{2}', '…', 'x_{n}'], [70, 70, 70, 210, 70], {i: 'blue' for i in range(5)}, 15)
F.brace(30, 520, 82, '全部为数值部分（无符号位）')
F.text(275, 152, '表示范围：0 ~ 2^{n} − 1', 13, color=INK2)
