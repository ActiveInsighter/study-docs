from common import ADDR_C
LABEL = '位扩展：8 块 8K×1 位芯片并联成 8K×8 位'
F = Fig(760, 360, '位扩展：8 块 8K × 1 位 → 8K × 8 位')
F.box(30, 70, 100, 250, '中央处理器\nCPU', 'green', 13, 8)
for i in reversed(range(8)):
    x, y = 260 + i * 30, 160 - i * 14
    F.box(x, y, 120, 70, '8K × 1 位' if i == 0 else '', 'blue', 12, 4)
    F.text(x + 112, y + 12, str(i + 1), 11, 'end', MUTED, valign='middle')
for k in range(8):
    y = 250 + k * 8
    F.line(130, y, 620, y, INK2, 1)
for i in range(8):
    x = 260 + i * 30 + 100
    y = 160 - i * 14 + 70
    F.line(x, y, x, 250 + i * 8, INK2, 1.1); F.circle(x, 250 + i * 8, 2, '', 'dark', sw=0)
F.text(136, 246, 'D₀', 11, 'start', INK2); F.text(136, 316, 'D₇', 11, 'start', INK2); F.text(640, 280, '数据总线', 12, 'start', INK2, valign='middle')
F.line(130, 150, 258, 150, ADDR_C if False else '#d1493a', 1.6, arrow='end'); F.line(130, 170, 258, 170, '#d1493a', 1.6, arrow='end')
F.text(136, 140, '地址总线 A₁₂~A₀', 11.5, 'start', '#d1493a')
F.text(380, 346, '所有芯片共用地址线、片选和读写线；每块芯片的 I/O 各接一根数据线', 12, color=MUTED)
