from common import datapath
LABEL = '32 位除法运算的逻辑结构图'
F = Fig(780, 346, '32 位除法运算的逻辑结构')
datapath(F, '除数寄存器 Y', '余数寄存器 R', '余数/商寄存器 Q', op='加 / 减', shift='左移')
F.text(400, 334, '每轮：加 / 减除数 → 根据余数符号上商 → 左移', 12.5, color=MUTED)
