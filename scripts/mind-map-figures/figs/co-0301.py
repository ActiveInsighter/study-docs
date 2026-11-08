from common import cpu_box, chip, ADDR_C, CTRL_C, DATA_C, wire
LABEL = '位扩展：再并联一块芯片接 D₁'
F = Fig(760, 380, '位扩展')
pins = [('A₁₅', 76, ADDR_C), ('A₁₄', 92, ADDR_C), ('A₁₃', 108, ADDR_C), ('A₁₂~A₀', 140, ADDR_C), ('WĒ', 250, CTRL_C), ('D₇~D₂' if 2 > 1 else 'D₇~D₁', 300, DATA_C), ('D₁', 322, DATA_C), ('D₀', 340, DATA_C)]
if 2 == 1: pins = [p for p in pins if p[0] != 'D₁']
cx = cpu_box(F, 30, 60, 90, 300, pins)
for y in (76, 92, 108): F.line(cx, y, cx + 40, y, ADDR_C, 1.2)
for i in range(2):
    x = 220 + i * 190
    a = chip(F, x, 124, '8K × 1 位', i, data='D₀')
    wire(F, [(cx, 140), (x - 20 if i else x, 140), (x, 140)], ADDR_C)
    wire(F, [(a['cs'][0], 96), (a['cs'][0], a['cs'][1])], CTRL_C); F.text(a['cs'][0], 88, '0', 11, color=CTRL_C)
    wire(F, [a['we'], (a['we'][0], 250), (cx, 250)], CTRL_C)
    yy = 340 - i * 18
    wire(F, [a['data'], (a['data'][0], yy), (cx, yy)], DATA_C)
F.text(470, 372, '地址线、片选、读写线并联，数据线各接一位', 12, color=MUTED)
