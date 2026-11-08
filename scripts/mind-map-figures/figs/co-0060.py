LABEL = '多重中断与屏蔽字：高优先级中断可以打断低优先级的中断服务'
F = Fig(640, 300, '多重中断：优先级高的可打断低的')
for i in range(4):
    y = 86 + i * 30
    F.text(90, y, f'程序 {i + 1}', 12, 'end', INK, valign='middle'); F.line(100, y, 600, y, LINE, 0.8, dash='2 4')
F.line(120, 240, 620, 240, INK2, 1.3, arrow='end'); F.line(120, 240, 120, 66, INK2, 1.3, arrow='end')
F.path('M140 240V86H200V146H300V86H400V240H430V146H450V176H470V146H490V116H560V240', ACCENT['blue'], 2)
F.text(200, 64, '先请求了 1', 12, 'start', ACCENT['red']); F.line(196, 64, 146, 80, ACCENT['red'], 1.1, arrow='end')
F.text(320, 196, '3 的处理次序更高，打断 1，执行 3', 12, 'middle', ACCENT['red']); F.line(240, 186, 208, 152, ACCENT['red'], 1.1, arrow='end')
F.text(180, 274, '1、2、3、4 同时请求中断', 12, 'start', INK2); F.line(176, 268, 142, 244, INK2, 1.1, arrow='end')
