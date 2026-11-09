from common import flow
LABEL = '程序查询方式的流程'
F = Fig(420, 560, '程序查询方式')
cs = flow(F, 120, 64, [('预置传送参数', 'box'), ('启动外设', 'box'), ('取外设状态', 'box'), ('外设准备就绪？', 'diamond'), ('传送一次数据', 'box'), ('修改传送参数', 'box'), ('传送完否？', 'diamond'), ('结束', 'dark')], gap=26)
F.rect(90, cs[2][2] - 12, 230, cs[3][3] - cs[2][2] + 24, 'amber', ACCENT['amber'], 1.2, 8, dash='5 4'); F.items.insert(4, F.items.pop())
F.poly([(300, cs[3][1]), (340, cs[3][1]), (340, cs[2][1]), (292, cs[2][1])], INK2, 1.3, arrow='end'); F.text(346, cs[3][1] - 6, 'N', 12, 'start', INK2)
F.poly([(110, cs[6][1]), (60, cs[6][1]), (60, cs[2][1]), (118, cs[2][1])], INK2, 1.3, arrow='end'); F.text(66, cs[6][1] - 6, 'N', 12, 'start', INK2)
F.text(213, cs[3][3] + 23, 'Y', 11, 'start', INK2); F.text(213, cs[6][3] + 20, 'Y', 11, 'start', INK2)
F.text(330, cs[2][2] + 4, '查询等待（踏步）', 11, 'start', ACCENT['amber'])
