from common import bitfield
LABEL = '全相联映射：主存地址的划分'
F = Fig(620, 230, '④ 全相联映射：28 位主存地址的划分')
bitfield(F, 96, 80, ['标记 22 bit', '块内 6 bit'], [308, 120], {0: 'blue', 1: 'gray'}, 13.5, 40)
F.brace(96, 96 + 308, 128, '块号 22 bit')
F.text(310, 200, '主存块可放入任意 Cache 行：整个块号都作为标记', 12.5, color=INK2)
