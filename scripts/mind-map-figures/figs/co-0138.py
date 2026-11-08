from common import cpu_box, chip, ADDR_C, CTRL_C, DATA_C, wire, gate
LABEL = '字扩展·译码片选法：高位地址经译码器产生片选，n 根线可选 2^n 块芯片'
F = Fig(860, 400, '字扩展 · 译码片选法（2-4 译码器）')
cx = cpu_box(F, 30, 60, 90, 320, [('A₁₅', 76, ADDR_C), ('A₁₄', 92, ADDR_C), ('A₁₃', 108, ADDR_C), ('A₁₂~A₀', 170, ADDR_C), ('WĒ', 280, CTRL_C), ('D₇~D₀', 350, DATA_C)])
F.box(170, 66, 50, 64, '译码器', 'amber', 11, 4)
wire(F, [(cx, 92), (168, 92)], ADDR_C); wire(F, [(cx, 108), (168, 108)], ADDR_C); F.line(cx, 76, cx + 30, 76, ADDR_C, 1.2, dash='3 3')
for i in range(4):
    x = 250 + i * 150
    a = chip(F, x, 154, '8K × 8 位', i, w=112, data='D₇~D₀')
    yy = 74 + i * 14
    wire(F, [(220, yy), (a['cs'][0], yy), (a['cs'][0], 154)], CTRL_C)
    F.text(a['cs'][0] + 6, yy - 6, ['00', '01', '10', '11'][i], 10, 'start', MUTED, mono=True)
    wire(F, [(cx, 170), (x, 170)], ADDR_C)
    wire(F, [a['we'], (a['we'][0], 280), (cx, 280)], CTRL_C)
    wire(F, [a['data'], (a['data'][0], 350), (cx, 350)], DATA_C)
F.text(500, 388, 'A₁₄A₁₃ 经 2-4 译码器选中 4 块芯片：4 块 8K × 8 位 → 32K × 8 位，地址连续', 12, color=MUTED)
