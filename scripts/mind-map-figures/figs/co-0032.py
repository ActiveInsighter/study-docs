from common import bitfield
LABEL = '定点小数：小数点隐含在符号位之后'
F = Fig(620, 190)
bitfield(F, 30, 50, ['x_{0}'], [70], {0: 'green'}, 15)
bitfield(F, 130, 50, ['x_{1}', 'x_{2}', '…', 'x_{n}'], [70, 70, 210, 70], {0: 'red', 1: 'blue', 2: 'blue', 3: 'blue'}, 15)
F.circle(115, 86, 3, '', 'dark', sw=0); F.line(115, 126, 115, 96, INK2, 1.3, arrow='end'); F.text(115, 144, '小数点（隐含）', 12, color=MUTED)
F.text(65, 114, '符号位', 12.5, color=TONES['green'][2]); F.text(165, 40, '最高有效位', 12, color=ACCENT['red'])
F.brace(130, 550, 98, '数值部分')
F.text(340, 176, '纯小数：|x| < 1', 12.5, color=INK2)
