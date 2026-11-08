from common import bitfield
LABEL = '2 路组相联映射：主存地址的划分'
F = Fig(620, 230, '④ 2 路组相联映射：28 位主存地址的划分')
bitfield(F, 96, 80, ['标记 20 bit', '组号 2 bit', '块内 6 bit'], [248, 60, 120], {0: 'blue', 1: 'amber', 2: 'gray'}, 13.5, 40)
F.brace(96, 96 + 308, 128, '块号 22 bit')
F.text(310, 200, '8 行、2 路一组 → 4 = 2² 组：块号 = 标记 20 bit + 组号 2 bit', 12.5, color=INK2)
