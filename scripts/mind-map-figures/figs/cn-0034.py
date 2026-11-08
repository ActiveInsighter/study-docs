LABEL = '虚电路方式：建立 → 数据传输 → 拆除，各分组沿同一条虚电路传送'
F = Fig(700, 470, '虚电路方式')
N = {'A': (130, 80), 'E': (200, 40), 'C': (280, 80), 'F': (380, 40), 'D': (450, 80), 'B': (200, 120), 'G': (380, 120)}
for a, b in (('A', 'E'), ('A', 'B'), ('E', 'C'), ('B', 'C'), ('C', 'F'), ('C', 'G'), ('F', 'D'), ('G', 'D')): F.line(*N[a], *N[b], INK2, 1.1)
for k, (x, y) in N.items(): F.circle(x, y, 10, '', 'blue', sw=1)
F.text(130, 104, '结点 A', 9.5, color=INK2); F.text(450, 104, '结点 D', 9.5, color=INK2)
for (a, b) in (('A', 'B'), ('B', 'C'), ('C', 'F'), ('F', 'D')): F.line(*N[a], *N[b], ACCENT['amber'], 2.4, gap=12, gap2=12)
F.box(30, 64, 44, 32, '主机 A', 'violet', 9.5, 4); F.box(530, 64, 44, 32, '主机 B', 'violet', 9.5, 4)
F.line(76, 80, 116, 80, ACCENT['amber'], 1.4, arrow='end'); F.line(462, 80, 528, 80, ACCENT['amber'], 1.4, arrow='end')
xs = [140, 260, 380, 500]
for x in xs: F.line(x, 160, x, 460, INK2, 1.2)
def msg(y, lab, back=False, step=6):
    for i in range(3):
        a, b = (xs[i], xs[i + 1]) if not back else (xs[3 - i], xs[2 - i])
        F.line(a, y + i * step, b, y + i * step + step * 2, INK2, 1, arrow='end')
    F.text(xs[0] + 30 if not back else xs[3] - 30, y - 6, lab, 10.5, 'start' if not back else 'end', INK2)
msg(176, '呼叫请求'); msg(220, '呼叫应答', True)
for i, p in enumerate(('P1', 'P2')): msg(266 + i * 22, p)
msg(330, 'ACK', True)
msg(380, '释放请求'); msg(420, '释放应答', True)
F.vbrace(130, 170, 246, '虚电路建立', right=False, size=11); F.vbrace(130, 260, 356, '数据传输', right=False, size=11); F.vbrace(130, 372, 450, '虚电路拆除', right=False, size=11)
