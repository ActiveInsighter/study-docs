from common import cpu_box, chip, ADDR_C, CTRL_C, DATA_C, wire
LABEL = '字扩展前：一块 8K×8 位芯片，CPU 的 A₁₅~A₁₃ 未用'
F = Fig(620, 360, '字扩展前：A₁₅~A₁₃ 还没有用上')
cx = cpu_box(F, 30, 60, 90, 280, [('A₁₅', 76, ADDR_C), ('A₁₄', 92, ADDR_C), ('A₁₃', 108, ADDR_C), ('A₁₂~A₀', 140, ADDR_C), ('WĒ', 230, CTRL_C), ('D₇~D₀', 310, DATA_C)])
for y in (76, 92, 108): F.line(cx, y, cx + 60, y, ADDR_C, 1.2, dash='3 3')
a = chip(F, 300, 124, '8K × 8 位', data='D₇~D₀')
wire(F, [(cx, 140), (300, 140)], ADDR_C); wire(F, [(a['cs'][0], 96), (a['cs'][0], 124)], CTRL_C)
wire(F, [a['we'], (a['we'][0], 230), (cx, 230)], CTRL_C); wire(F, [a['data'], (a['data'][0], 310), (cx, 310)], DATA_C)
F.text(200, 66, '3 根地址线空闲', 12, 'start', ADDR_C)
F.text(460, 300, '地址范围只有 8K', 12, 'start', MUTED)
