LABEL = '多级存储器结构：越往上速度越快、容量越小、价格越高'
F = Fig(640, 330, '多级存储器结构')
levels = [('CPU 寄存器', 'dark'), ('Cache', 'red'), ('主存', 'amber'), ('磁盘', 'blue'), ('磁带 / 光盘', 'gray')]
for i, (lab, t) in enumerate(levels):
    y = 64 + i * 46
    half = 66 + i * 38
    cx = 220
    f, s, c = TONES[t]
    F.items.append(f'<path d="M{cx - half + 21} {y}H{cx + half - 21}L{cx + half} {y + 42}H{cx - half}Z" fill="{f}" stroke="{s}" stroke-width="1.3"/>')
    F.text(cx, y + 22, lab, 13.5, color=c, weight=600, valign='middle')
for x, (a, b, up) in zip((480, 540, 600), (('速度', '快 → 慢', True), ('容量', '小 → 大', False), ('价格', '高 → 低', True))):
    F.text(x, 74, a, 13, color=INK, weight=700)
    F.line(x, 90, x, 280, ACCENT['blue'] if up else ACCENT['green'], 1.6, arrow='start' if up else 'end')
    F.text(x, 300, {'速度': '最慢', '容量': '最大', '价格': '最低'}[a], 12, color=MUTED)
    F.text(x + 0, 108 - 0, '', 1)
F.text(220, 312, 'Cache—主存层解决速度问题；主存—辅存层解决容量问题', 12, color=MUTED)
