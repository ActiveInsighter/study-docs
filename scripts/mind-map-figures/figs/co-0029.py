from common import pipe_row, STG
LABEL = '指令执行过程图：用于分析指令执行过程及影响流水线的因素'
F = Fig(720, 300, '指令执行过程图')
labs = ['第 k 条指令 I_{k}', '第 k+1 条指令 I_{k+1}', '第 k+2 条指令 I_{k+2}']
for k in range(3):
    y = 210 - k * 34
    pipe_row(F, 180 + k * 70, y, [(f'{a} k' + (f'+{k}' if k else ''), t) for a, t in STG], w=70, h=28)
    F.text(170, y + 14, labs[k], 12, 'end', INK2, valign='middle')
pipe_row(F, 180 + 4 * 70, 210 - 4 * 34 - 6, [('', t) for a, t in STG], w=70, h=28)
pipe_row(F, 180 + 4 * 70, 210 - 3 * 34 - 0, [('', t) for a, t in STG], w=70, h=28) if False else None
F.text(140, 120, '……', 12, color=MUTED); F.text(460, 126, '……', 12, color=MUTED)
F.line(176, 242, 680, 242, INK2, 1.3, arrow='end'); F.line(176, 242, 176, 70, INK2, 1.3, arrow='end'); F.text(184, 72, '指令序列', 11.5, 'start', INK2)
F.text(430, 280, '横轴为时间，纵轴为指令序列', 11.5, color=MUTED)
