from common import bitfield
LABEL = '定点整数：小数点隐含在最低位之后'
F = Fig(620, 190)
bitfield(F, 30, 50, ['x_{0}'], [70], {0: 'green'}, 15)
bitfield(F, 110, 50, ['x_{1}', 'x_{2}', '…', 'x_{n}'], [70, 70, 210, 70], {0: 'blue', 1: 'blue', 2: 'blue', 3: 'amber'}, 15)
F.circle(538, 86, 3, '', 'dark', sw=0); F.line(560, 126, 541, 96, INK2, 1.3, arrow='end'); F.text(570, 144, '小数点（隐含）', 12, color=MUTED)
F.text(65, 114, '符号位', 12.5, color=TONES['green'][2]); F.text(495, 40, '最低有效位', 12, color=TONES['amber'][2])
F.brace(110, 530, 98, '数值部分')
F.text(320, 176, '纯整数', 12.5, color=INK2)
