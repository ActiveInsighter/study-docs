LABEL = '循环移位：不带进位位与带进位位'
F = Fig(760, 300, '循环移位')
def panel(x, y, cap, right, withcf):
    F.box(x, y + 6, 34, 22, 'CF', 'amber', 11, 4, mono=True)
    rx = x + 70
    F.rect(rx, y, 200, 34, 'blue', ACCENT['blue'], 1.3, 4)
    F.text(rx, y - 8, '最高位', 11, 'start', MUTED); F.text(rx + 200, y - 8, '最低位', 11, 'end', MUTED)
    if right:
        F.line(rx + 30, y + 17, rx + 170, y + 17, INK2, 1.3, arrow='end')
    else:
        F.line(rx + 170, y + 17, rx + 30, y + 17, INK2, 1.3, arrow='end')
    if withcf:
        if right: F.poly([(rx + 200, y + 17), (rx + 220, y + 17), (rx + 220, y + 52), (x + 17, y + 52), (x + 17, y + 30)], INK2, 1.3); F.line(x + 34, y + 17, rx - 2, y + 17, INK2, 1.3, arrow='end')
        else: F.poly([(rx, y + 17), (x + 52, y + 17)], INK2, 1.3, arrow=None); F.line(x + 52, y + 17, x + 36, y + 17, INK2, 1.3, arrow='end'); F.poly([(x + 17, y + 30), (x + 17, y + 52), (rx + 220, y + 52), (rx + 220, y + 17), (rx + 202, y + 17)], INK2, 1.3)
    else:
        if right: F.poly([(rx + 200, y + 17), (rx + 220, y + 17), (rx + 220, y + 52), (rx - 16, y + 52), (rx - 16, y + 17), (rx - 2, y + 17)], INK2, 1.3); F.poly([(rx + 210, y + 17), (rx + 210, y - 14), (x + 17, y - 14), (x + 17, y + 4)], LINE, 1.2)
        else: F.poly([(rx, y + 17), (rx - 16, y + 17), (rx - 16, y + 52), (rx + 220, y + 52), (rx + 220, y + 17), (rx + 202, y + 17)], INK2, 1.3); F.line(rx - 16, y + 17, x + 36, y + 17, LINE, 1.2, arrow='end')
    F.text(rx + 100, y + 76, cap, 12, color=INK2)
panel(30, 80, '(a) 不带进位位的循环右移', True, False)
panel(400, 80, '(b) 带进位位的循环右移', True, True)
panel(30, 200, '(c) 不带进位位的循环左移', False, False)
panel(400, 200, '(d) 带进位位的循环左移', False, True)
