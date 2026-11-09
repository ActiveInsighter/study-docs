from common import cpu_box, chip, ADDR_C, CTRL_C, DATA_C, wire, gate
LABEL = '字扩展·线选法：每根高位地址线直接作一块芯片的片选'
F = Fig(800, 380, '字扩展 · 线选法')
cx = cpu_box(F, 30, 60, 90, 300, [('A₁₅', 76, ADDR_C), ('A₁₄', 92, ADDR_C), ('A₁₃', 108, ADDR_C), ('A₁₂~A₀', 150, ADDR_C), ('WĒ', 260, CTRL_C), ('D₇~D₀', 330, DATA_C)])
pins = [76, 92, 108][::-1]
for i in range(3):
    x = 200 + i * 200
    a = chip(F, x, 134, '8K × 8 位', i, data='D₇~D₀')
    wire(F, [(cx, pins[i]), (a['cs'][0], pins[i]), (a['cs'][0], 134)], ADDR_C)
    wire(F, [(cx, 150), (x, 150)], ADDR_C)
    wire(F, [a['we'], (a['we'][0], 260), (cx, 260)], CTRL_C)
    wire(F, [a['data'], (a['data'][0], 330), (cx, 330)], DATA_C)
    F.text(a['cs'][0] + 8, 124, ['A₁₃', 'A₁₄', 'A₁₅'][i], 10.5, 'start', ADDR_C)
    F.text(x + 59, 240, ['001 0…0 ~ 001 1…1', '010 0…0 ~ 010 1…1', '100 0…0 ~ 100 1…1'][i], 10.5, color=MUTED, mono=True, chip=True)
F.text(480, 368, 'n 根地址线只能选 n 块芯片，且地址空间不连续', 12, color=MUTED)
