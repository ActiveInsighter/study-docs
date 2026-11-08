LABEL = '为什么要把模拟数据编码为数字信号：采样、量化、编码（PCM）'
F = Fig(620, 330, '模拟数据 → 数字信号：采样、量化')
levels = ['0101', '0100', '0011', '0010', '0001', '0000', '1001', '1010', '1011', '1100', '1101']
for i, l in enumerate(levels):
    y = 60 + i * 22
    F.text(70, y, l, 11, 'end', INK, mono=True, valign='middle'); F.line(78, y, 590, y, '#d4d4d8' if l != '0000' else ACCENT['red'], 1)
import math
pts = []
for i in range(0, 501, 4):
    x = 80 + i
    v = 2.2 * math.sin(i / 40) * math.exp(-((i - 40) / 160) ** 2) + 1.5 * math.sin(i / 23 + 1) * 0.8 + 0.6 * math.sin(i / 9)
    pts.append((x, 170 - v * 22))
F.path('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in pts), INK, 1.6)
for x, y in pts[::4]:
    F.line(x, 170, x, y, ACCENT['violet'], 1.4); F.circle(x, round((y - 60) / 22) * 22 + 60, 2.5, '', 'dark', sw=0)
F.text(330, 320, '采样：按固定时间间隔取样；量化：取最接近的离散电平；编码：用二进制码表示电平', 11, color=MUTED)
