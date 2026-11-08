from common import mux_shape, bus_slash
LABEL = '多路选择器：k 个 n 位输入，m 位控制信号选择一个输出'
F = Fig(520, 300)
mux_shape(F, 60, 120, 280, 70, 'MUX', size=18)
F.line(200, 120, 200, 50, INK2, 1.6, arrow='end'); bus_slash(F, 200, 86); F.text(200, 36, '单个输出（n bit）', 13, color=ACCENT['red'], weight=600)
for x in (90, 130, 310):
    F.line(x, 250, x, 192, INK2, 1.6, arrow='end'); bus_slash(F, x, 222)
F.text(220, 232, '……', 14, color=MUTED)
F.text(200, 282, 'k 个 n bit 输入', 13, color=ACCENT['red'], weight=600)
F.line(470, 155, 330, 155, ACCENT['blue'], 1.4, dash='5 4', arrow='end'); bus_slash(F, 410, 155, 'm', vertical=False)
F.text(470, 132, '控制信号 m bit', 13, 'end', ACCENT['blue'], 600)
F.text(470, 182, 'm ≥ ⌈log₂k⌉', 12.5, 'end', MUTED, mono=True)
