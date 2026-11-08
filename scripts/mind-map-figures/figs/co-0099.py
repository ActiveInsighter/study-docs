from common import bitfield
LABEL = 'IEEE 754：数符、移码阶码、隐含最高位 1 的尾数；三种精度'
F = Fig(760, 430, 'IEEE 754 浮点数格式')
bitfield(F, 60, 80, ['m_{s}', 'E', 'M'], [60, 180, 360], {0: 'red', 1: 'blue', 2: 'green'}, 15, 40)
F.text(90, 140, '数符', 12.5, color=INK2); F.text(210, 140, '阶码：移码表示', 12.5, color=INK2); F.text(480, 140, '尾数数值位：原码表示', 12.5, color=INK2)
F.text(480, 68, '规格化后最高位恒为 1，隐藏不存 → 尾数表示 1.M', 12, color=ACCENT['green'], weight=600)
rows = [['类型', '数符', '阶码', '尾数数值', '总位数', '偏置值（十六）', '偏置值（十）'], ['短浮点数 float', '1', '8', '23', '32', '7FH', '127'],
        ['长浮点数 double', '1', '11', '52', '64', '3FFH', '1023'], ['临时浮点数', '1', '15', '64', '80', '3FFFH', '16383']]
F.table(40, 170, rows, [140, 70, 70, 90, 80, 120, 110], 34, size=13, mono_cols=(1, 2, 3, 4, 5, 6))
F.text(380, 330, 'float 真值：(−1)^{s} × 1.M × 2^{E−127}', 14, color=INK, mono=True)
F.text(380, 358, 'double 真值：(−1)^{s} × 1.M × 2^{E−1023}', 14, color=INK, mono=True)
F.text(380, 398, 'E 全 0 / 全 1 有特殊含义：非规格化数、±0、±∞、NaN', 12.5, color=MUTED)
