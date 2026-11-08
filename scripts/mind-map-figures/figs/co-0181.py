import math
LABEL = '磁盘的概念：磁道、扇区、磁道间隙、扇区间隙'
F = Fig(560, 380, '磁道 · 扇区 · 间隙')
cx, cy = 200, 205
for k, r in enumerate((150, 122, 94, 66)):
    F.circle(cx, cy, r, '', 'gray' if k % 2 == 0 else 'white', sw=1.2)
F.circle(cx, cy, 40, '', 'white', sw=1.4)
for i in range(8):
    a = i * math.pi / 4
    F.line(cx + 40 * math.cos(a), cy + 40 * math.sin(a), cx + 150 * math.cos(a), cy + 150 * math.sin(a), '#ffffff', 5)
a1, a2 = -math.pi / 2 + 0.06, -math.pi / 4 - 0.06
r = 136
F.path(f'M{cx + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f}A{r} {r} 0 0 1 {cx + r * math.cos(a2):.1f} {cy + r * math.sin(a2):.1f}', ACCENT['green'], 14)
F.line(400, 80, cx + 136 * math.cos(-1.2), cy + 136 * math.sin(-1.2), INK2, 1.2); F.text(408, 80, '扇区（磁盘块）', 12.5, 'start', ACCENT['green'], 600, valign='middle')
F.line(400, 130, cx + 108 * math.cos(-0.5), cy + 108 * math.sin(-0.5), INK2, 1.2); F.text(408, 130, '磁道', 12.5, 'start', INK, 600, valign='middle')
F.line(400, 180, cx + 136 * math.cos(0), cy + 136 * math.sin(0) - 0, INK2, 1.2); F.text(408, 180, '扇区间隙', 12.5, 'start', INK, 600, valign='middle')
F.line(400, 230, cx + 80 * math.cos(0.5), cy + 80 * math.sin(0.5), INK2, 1.2); F.text(408, 230, '磁道间隙', 12.5, 'start', INK, 600, valign='middle')
F.text(408, 290, '每条磁道划分为若干扇区；\n各扇区存储的数据量相同', 12, 'start', MUTED, lh=1.5)
