LABEL = '双绞线的结构：外护套、编织屏蔽层、铝箔、地线、PVC 胶料、四对铜芯对绞'
F = Fig(640, 300, '双绞线（屏蔽双绞线）的结构')
F.rect(380, 120, 240, 60, 'amber', ACCENT['amber'], 1.4, 30)
F.rect(300, 128, 90, 44, '#d4d4d8', '#71717a', 1.2, 10)
import math
cols = [('#2f8f57', '#e3f4e8'), ('#c98a12', '#fdf1d8'), ('#3b6fd4', '#e8effc'), ('#8a5a2b', '#f2e6d8')]
for k, (c1, c2) in enumerate(cols):
    y0 = 70 + k * 50
    d1 = 'M' + 'L'.join(f'{x:.1f} {y0 + 6 * math.sin(x / 8):.1f}' for x in range(60, 300, 4))
    d2 = 'M' + 'L'.join(f'{x:.1f} {y0 - 6 * math.sin(x / 8):.1f}' for x in range(60, 300, 4))
    F.path(d1, c1, 3); F.path(d2, c2, 3)
    F.path(f'M300 {y0}Q330 {y0} 340 150', c1, 2)
    F.circle(52, y0, 8, str(2 * k + 1), 'amber', 9)
labs = [('进口环保外被', 500, 120), ('96 股编织对绞加密', 360, 126), ('金属铝箔包覆', 320, 176), ('金属地线', 290, 200), ('高密度聚乙烯 PVC 胶料', 250, 226), ('8 股无氧铜线芯对绞', 180, 250)]
for i, (t, x, y) in enumerate(labs):
    ly = 50 + i * 40 if i < 2 else 196 + (i - 2) * 24
    F.text(630, ly, t, 11, 'end', INK2, valign='middle'); F.circle(616 - 0, ly, 0.1, '', 'none', sw=0)
