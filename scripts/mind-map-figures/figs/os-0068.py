from common import flow
LABEL = '程序直接控制方式'
F = Fig(560, 520, '程序直接控制方式')
cs = flow(F, 60, 70, [('给 I/O 模块发出读命令', 'box'), ('读 I/O 模块的状态', 'box'), ('检查状态', 'diamond'), ('从 I/O 模块中读取字', 'box'), ('往存储器中写入字', 'box'), ('完成？', 'diamond')], w=190, h=40, gap=22)
F.text(276, cs[0][1], 'CPU → I/O', 12, 'start', ACCENT['blue'], 600 if 'blue' == 'red' else 400, valign='middle', lh=1.3)
F.text(276, cs[1][1], 'I/O → CPU（读状态寄存器）', 12, 'start', ACCENT['green'], 600 if 'green' == 'red' else 400, valign='middle', lh=1.3)
F.text(276, cs[2][1], '未准备好：循环查询\n错误：错误条件', 12, 'start', ACCENT['red'], 600 if 'red' == 'red' else 400, valign='middle', lh=1.3)
F.text(276, cs[3][1], 'I/O → CPU', 12, 'start', ACCENT['blue'], 600 if 'blue' == 'red' else 400, valign='middle', lh=1.3)
F.text(276, cs[4][1], 'CPU → 存储器', 12, 'start', ACCENT['blue'], 600 if 'blue' == 'red' else 400, valign='middle', lh=1.3)
F.text(280, 472, '例：scanf("%d", &a)：CPU 一直轮询，最后由 CPU 把数据写到 a 中', 11.5, color=MUTED)
F.poly([(55, cs[5][1]), (36, cs[5][1]), (36, cs[0][1]), (58, cs[0][1])], INK2, 1.2, arrow='end'); F.text(42, cs[5][1] - 8, '否', 10.5, 'start', INK2)
F.poly([(55, cs[2][1]), (44, cs[2][1]), (44, cs[1][1]), (58, cs[1][1])], INK2, 1.2, arrow='end')
F.text(160, cs[5][3] + 22, '是 → 下一条指令', 11, color=INK2)
