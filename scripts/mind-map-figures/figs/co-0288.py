from common import flow
LABEL = '中断处理流程：关中断、保存断点、寻址由硬件完成，其余由中断服务程序完成；多重中断时提前开中断'
F = Fig(560, 640, '中断处理流程')
items = [('关中断', 'box'), ('保存断点', 'box'), ('中断服务程序寻址', 'box'), ('保存现场和屏蔽字', 'box'), ('开中断', 'red'), ('执行中断服务程序', 'box'), ('关中断', 'red'), ('恢复现场和屏蔽字', 'box'), ('开中断', 'box'), ('中断返回', 'box')]
cs = flow(F, 180, 60, items, w=170, h=38, gap=20)
F.vbrace(362, cs[0][2], cs[2][3], '硬件完成（中断隐指令）')
F.vbrace(362, cs[3][2], cs[9][3], '中断服务程序完成')
F.text(100, (cs[4][1] + cs[6][1]) / 2, '多重中断', 13, 'middle', ACCENT['red'], 600, valign='middle')
F.line(130, (cs[4][1] + cs[6][1]) / 2 - 10, 178, cs[4][1], ACCENT['red'], 1.2, arrow='end'); F.line(130, (cs[4][1] + cs[6][1]) / 2 + 10, 178, cs[6][1], ACCENT['red'], 1.2, arrow='end')
