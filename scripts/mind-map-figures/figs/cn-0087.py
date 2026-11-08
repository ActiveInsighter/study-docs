LABEL = '光纤通信：利用光导纤维传递光脉冲，有光脉冲表示 1，无光脉冲表示 0'
F = Fig(560, 240, '光纤（光缆）')
F.rect(40, 90, 280, 60, '#e4e4e7', '#71717a', 1.4, 30)
cols = ['#2f8f57', '#d1493a', '#3b6fd4', '#c98a12', '#7856c9', '#23877c']
import math
for i, c in enumerate(cols):
    a = i * math.pi / 3
    cx, cy = 320 + 14 * math.cos(a), 120 + 14 * math.sin(a)
    F.circle(cx, cy, 8, '', 'white', sw=2); F.items[-1] = F.items[-1].replace('stroke="#52525b"', f'stroke="{c}"')
    F.path(f'M{cx + 8:.1f} {cy:.1f}L{500:.1f} {60 + i * 24}', c, 1.6)
    F.circle(500, 60 + i * 24, 3, '', 'blue', sw=0)
F.text(280, 220, '光脉冲有表示 1、无表示 0；损耗小、带宽大、抗电磁干扰', 11, color=MUTED)
