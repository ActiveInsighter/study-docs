from common import pipe_row, STG
LABEL = '顺序执行方式：总耗时 T = 3nt'
F = Fig(640, 170, '① 顺序执行：T = n × 3t = 3nt')
pipe_row(F, 70, 86, [(f'{a} k', t) for a, t in STG] + [(f'{a} k+1', t) for a, t in STG])
F.line(30, 116, 610, 116, INK2, 1.3, arrow='end')
