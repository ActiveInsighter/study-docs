LABEL = 'RAM 的读周期时序：地址有效 → 片选有效 → 数据稳定'
F = Fig(760, 300, 'RAM 的读周期')
def bus(y, x1, x2, tone, h=24):
    f, s, _ = TONES[tone]
    F.items.append(f'<path d="M{x1} {y}L{x1 + 12} {y - h / 2}H{x2 - 12}L{x2} {y}L{x2 - 12} {y + h / 2}H{x1 + 12}Z" fill="{f}" stroke="{s}" stroke-width="1.3"/>')
F.text(90, 140, '地址', 13, 'end', INK, valign='middle'); bus(140, 100, 160, 'green'); bus(140, 160, 560, 'green'); bus(140, 560, 720, 'green')
F.text(90, 200, 'CS̄', 13, 'end', INK, valign='middle')
F.path('M100 188H230L246 212H430L446 188H720', TONES['red'][1], 1.6)
F.text(90, 256, 'D_{OUT}', 13, 'end', INK, valign='middle'); F.path('M100 256H330', LINE, 1.6); bus(256, 330, 600, 'blue'); F.path('M600 256H720', LINE, 1.6)
for x in (160, 560): F.line(x, 80, x, 280, LINE, 1, dash='3 3')
F.line(162, 84, 558, 84, INK2, 1.2, arrow='both'); F.text(360, 76, 't_{RC}：读周期', 12, color=INK2)
F.line(162, 108, 330, 108, INK2, 1.2, arrow='both'); F.text(246, 102, 't_{A}', 12, color=INK2)
F.line(246, 176, 330, 176, INK2, 1.2, arrow='both'); F.text(290, 170, 't_{CO}', 12, color=INK2)
F.line(330, 80, 330, 280, ACCENT['blue'], 1, dash='3 3')
F.text(160, 288, '地址有效', 11.5, color=MUTED); F.text(330, 288, '数据有效', 11.5, color=MUTED); F.text(560, 288, '地址失效', 11.5, color=MUTED)
