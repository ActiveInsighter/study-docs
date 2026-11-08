from common import pipe_row, STG
LABEL = '一次重叠执行方式：T = 3t + (n−1)·2t = (1+2n)t'
F = Fig(640, 230, '② 一次重叠：T = 3t + (n−1)·2t = (1 + 2n)t')
for k in range(3):
    pipe_row(F, 60 + k * 168, 150 - k * 34, [(f'{a} k' + (f'+{k}' if k else ''), t) for a, t in STG])
F.line(30, 180, 620, 180, INK2, 1.3, arrow='end')
F.text(320, 214, '上一条指令的“执行”与下一条指令的“取指”重叠', 11.5, color=MUTED)
