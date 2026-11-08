import math
LABEL = '磁盘读写一个扇区的时间：启动时间 + 寻道时间 + 旋转延迟 + 传输时间'
F = Fig(820, 420, '磁盘的存取时间')
cx, cy = 230, 220
for k, r in enumerate((160, 136, 112, 88, 64)): F.circle(cx, cy, r, '', 'blue' if k % 2 == 0 else 'green', sw=1)
F.circle(cx, cy, 44, '', 'white', sw=1.2)
for i in range(8):
    a = -math.pi / 2 + math.pi / 4 * i + math.pi / 8
    F.line(cx + 44 * math.cos(a), cy + 44 * math.sin(a), cx + 160 * math.cos(a), cy + 160 * math.sin(a), '#ffffff', 4)
for i, n in enumerate(['7', '0', '1', '2', '3', '4', '5', '6']):
    a = -math.pi / 2 + math.pi / 4 * i
    F.text(cx + 178 * math.cos(a), cy + 178 * math.sin(a), n, 13, color=INK, valign='middle')
F.path(f'M{cx + 160} {cy - 2}H{cx + 76}', ACCENT['violet'], 1.8, arrow='end'); F.text(cx + 150, cy - 14, '② 寻道', 11, color=ACCENT['violet'])
a1, a2 = 0.15, 1.2
F.path(f'M{cx + 76 * math.cos(a1):.1f} {cy + 76 * math.sin(a1):.1f}A76 76 0 0 1 {cx + 76 * math.cos(a2):.1f} {cy + 76 * math.sin(a2):.1f}', ACCENT['violet'], 1.8, arrow='end'); F.text(cx + 80, cy + 80, '③ 旋转延迟', 11, color=ACCENT['violet'])
a3, a4 = 1.4, 2.6
F.path(f'M{cx + 76 * math.cos(a3):.1f} {cy + 76 * math.sin(a3):.1f}A76 76 0 0 1 {cx + 76 * math.cos(a4):.1f} {cy + 76 * math.sin(a4):.1f}', ACCENT['red'], 4); F.text(cx - 90, cy + 70, '④ 传输', 11, color=ACCENT['red'])
F.box(cx + 158, cy - 10, 10, 20, '', 'dark', rx=1); F.text(cx + 180, cy, '① 启动', 11, 'start', ACCENT['violet'], valign='middle')
x = 470
lines = ['① 启动时间：s（约 2 ms）', '② 寻找 / 寻道时间：m × n（跨越 n 条磁道，每条 m）',
         '③ 旋转延迟时间 Tᵣ：转速为 r，平均转半圈', '　 Tᵣ = (1/2) × (1/r) = 1/(2r)',
         '　 硬盘 r = 5400 转/min → Tᵣ = 5.55 ms', '　 软盘 r = 300~600 转/min → Tᵣ = 50~100 ms',
         '④ 传输时间 Tₜ：读写 b 字节，每磁道 N 字节', '　 Tₜ = (1/r) × (b/N) = b/(rN)', '', 'Tₐ = s + m×n + 1/(2r) + b/(rN)']
for i, l in enumerate(lines): F.text(x, 76 + i * 30, l, 12.5 if i < 9 else 14, 'start', ACCENT['red'] if i == 9 else INK2, 700 if i == 9 else 400)
