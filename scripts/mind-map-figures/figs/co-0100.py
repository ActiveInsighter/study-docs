from common import datapath
LABEL = '补码一位乘法的逻辑结构图'
F = Fig(780, 346, '补码一位乘法的逻辑结构')
ry = datapath(F, '被乘数寄存器 X', '乘积寄存器 P', '乘数寄存器 Y', op='加 / 减')
F.box(398, ry, 22, 30, '', 'red', rx=0); F.text(409, ry - 10, '辅助位', 10.5, color=ACCENT['red'])
F.box(510, 60, 240, 70, '辅助位 − 最低位：\n−1：+[−x]_{补}　0：+0　1：+[x]_{补}', 'violet', 12, 8)
F.box(40, 290 - 0, 0, 0, '', 'none')
F.text(400, 334, '溢出判断：P 的 n 位 + Y 的最高位不全为 0 或 1', 12.5, color=INK2)
