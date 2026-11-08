from common import pipe_row, STG
LABEL = '二次重叠执行方式：T = 3t + (n−1)·t = (2+n)t'
F = Fig(560, 230, '③ 二次重叠：T = 3t + (n−1)·t = (2 + n)t')
for k in range(3):
    pipe_row(F, 50 + k * 84, 150 - k * 34, [(f'{a} k' + (f'+{k}' if k else ''), t) for a, t in STG])
F.line(30, 180, 540, 180, INK2, 1.3, arrow='end')
F.text(280, 214, '每个时刻都有三条指令在不同阶段执行', 11.5, color=MUTED)
