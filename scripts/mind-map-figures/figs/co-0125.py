from common import cpu_box, chip, ADDR_C, CTRL_C, DATA_C, wire, gate
LABEL = '字位扩展：两块 16K×4 位芯片一组做位扩展，四组再做字扩展得 64K×8 位'
F = Fig(860, 380, '字位同时扩展：8 块 16K × 4 位 → 64K × 8 位')
cx = cpu_box(F, 30, 60, 90, 300, [('A₁₅', 80, ADDR_C), ('A₁₄', 96, ADDR_C), ('A₁₃~A₀', 160, ADDR_C), ('WĒ', 270, CTRL_C), ('D₇~D₀', 330, DATA_C)])
F.box(150, 62, 52, 50, '2-4\n译码器', 'amber', 10.5, 4)
wire(F, [(cx, 80), (148, 80)], ADDR_C); wire(F, [(cx, 96), (148, 96)], ADDR_C)
for g in range(4):
    for k in range(2):
        x = 230 + g * 156 + k * 72
        F.box(x, 140, 66, 70, '16K\n× 4 位', 'blue', 11, 4)
        F.line(cx, 160, x, 160, ADDR_C, 1) if False else None
        wire(F, [(x + 33, 210), (x + 33, 330)], DATA_C if k else '#23877c')
        wire(F, [(x + 10, 210), (x + 10, 270)], CTRL_C)
    yy = 70 + g * 12
    wire(F, [(202, yy), (230 + g * 156 + 100, yy), (230 + g * 156 + 100, 132), (230 + g * 156 + 33, 132), (230 + g * 156 + 33, 140)], CTRL_C)
    wire(F, [(230 + g * 156 + 100, 132), (230 + g * 156 + 105, 132), (230 + g * 156 + 105, 140)], CTRL_C)
    F.text(230 + g * 156 + 69, 226, '组 ' + str(g), 11, color=MUTED)
wire(F, [(cx, 160), (220, 160)], ADDR_C); F.text(170, 176, '并联到每块芯片', 10.5, 'middle', ADDR_C)
wire(F, [(cx, 270), (840, 270)], CTRL_C); wire(F, [(cx, 330), (840, 330)], DATA_C)
F.text(540, 352, '同组两块分接 D₇~D₄、D₃~D₀（位扩展）；A₁₅A₁₄ 译码选组（字扩展）', 12, color=MUTED)
