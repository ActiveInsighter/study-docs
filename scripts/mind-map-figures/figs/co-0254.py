from common import bitfield
LABEL = '直接映射：主存地址的划分'
F = Fig(620, 230, '④ 直接映射：28 位主存地址的划分')
bitfield(F, 96, 80, ['标记 19 bit', '行号 3 bit', '块内 6 bit'], [228, 80, 120], {0: 'blue', 1: 'amber', 2: 'gray'}, 13.5, 40)
F.brace(96, 96 + 308, 128, '块号 22 bit')
F.text(310, 200, '块号 22 bit = 标记 19 bit + 行号 3 bit（2³ 行）', 12.5, color=INK2)
