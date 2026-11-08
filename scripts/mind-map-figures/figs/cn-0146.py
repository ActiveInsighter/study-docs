LABEL = '多模光纤（阶跃折射率、渐变折射率）与单模光纤'
F = Fig(640, 340, '多模光纤 / 单模光纤')
for k, (t, y) in enumerate((('阶跃折射率 · 多模', 70), ('渐变折射率 · 多模', 170), ('单模', 270))):
    F.rect(40, y, 440, 50 if k < 2 else 30, '#fafafa', '#71717a', 1.2, 0)
    F.text(496, y + (25 if k < 2 else 15), t, 12, 'start', INK, 600, valign='middle')
F.path('M40 95L110 72L180 118L250 72L320 118L390 72L460 100', ACCENT['blue'], 1.2); F.path('M40 95L150 78L260 112L370 78L470 96', ACCENT['red'], 1.2); F.line(40, 95, 476, 95, INK2, 1, arrow='end')
import math
for amp, c in ((18, ACCENT['blue']), (10, ACCENT['red'])):
    F.path('M' + 'L'.join(f'{x:.1f} {195 + amp * math.sin((x - 40) / 70 * math.pi):.1f}' for x in range(40, 470, 4)), c, 1.2)
F.line(30, 285, 486, 285, ACCENT['blue'], 1.6, arrow='end')
F.text(260, 156, '高阶振型与低阶振型路径不同 → 色散（模间色散）', 11, color=MUTED)
F.text(260, 326, '单模光纤只有一条传播路径，无模间色散，适合远距离传输', 11, color=MUTED)
