LABEL = '简单图：不存在重复边，不存在顶点到自身的边'
F = Fig(560, 380, '哪些是简单图？')
F.text(150, 76, '有向图', 14, color=INK, weight=700); F.text(410, 76, '无向图', 14, color=INK, weight=700)
def pair(cx, y, kind, d):
    a, b = (cx - 60, y), (cx + 60, y)
    for p in (a, b) if kind != 'loop' else (a, b):
        pass
    if kind == 'two':
        F.curve(a[0] + 14, a[1] - 8, b[0] - 15, b[1] - 8, -0.25, INK2, 1.5, arrow='end' if d else None)
        F.curve(b[0] - 14, b[1] + 8, a[0] + 15, a[1] + 8, -0.25, INK2, 1.5, arrow='end' if d else None)
        F.circle(*a, 16); F.circle(*b, 16)
    elif kind == 'none':
        pass
    elif kind == 'multi':
        F.curve(a[0] + 14, a[1] - 8, b[0] - 15, b[1] - 8, -0.25, INK2, 1.5, arrow='end' if d else None)
        F.curve(a[0] + 14, a[1] + 8, b[0] - 15, b[1] + 8, 0.25, INK2, 1.5, arrow='end' if d else None)
        F.circle(*a, 16); F.circle(*b, 16)
    else:
        F.path(f'M{a[0] + 10} {a[1] - 12}C{a[0] + 40} {a[1] - 50} {a[0] + 70} {a[1] + 30} {a[0] + 15} {a[1] + 8}', INK2, 1.5, arrow='end' if d else None)
        F.circle(*a, 16)

pair(150, 130, 'two', True); F.text(150, 168, '✓ 方向相反的两条弧', 12.5, color=ACCENT['green'])
pair(410, 130, 'multi', False); F.text(410, 168, '✗ 两条重复边', 12.5, color=ACCENT['red'])
pair(150, 230, 'multi', True); F.text(150, 268, '✗ 同方向的重复弧', 12.5, color=ACCENT['red'])
pair(410, 230, 'none', False); F.line(350, 230, 470, 230, INK2, 1.5, gap=16, gap2=16); F.circle(350, 230, 16); F.circle(470, 230, 16); F.text(410, 268, '✓ 一条边', 12.5, color=ACCENT['green'])
pair(150, 320, 'loop', True); F.text(210, 350, '✗ 自环', 12.5, color=ACCENT['red'])
pair(410, 320, 'loop', False); F.text(470, 350, '✗ 自环', 12.5, color=ACCENT['red'])
