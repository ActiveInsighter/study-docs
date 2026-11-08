LABEL = 'SDN 方法中控制平面与数据平面分离：路由器不再运行路由选择协议'
F = Fig(380, 520, 'SDN：控制平面与数据平面分离')
F.box(40, 60, 300, 140, '', 'white', rx=4); F.text(190, 86, '路由选择处理机', 16, color=INK, weight=600)
F.box(70, 104, 240, 36, '路由选择协议', 'white', 14, 2); F.box(130, 150, 120, 32, '路由表', 'white', 14, 2)
F.line(10, 226, 370, 226, INK2, 1.2, dash='8 6')
F.line(190, 202, 190, 252, INK2, 1.6, arrow='both'); F.text(190, 228, '✕', 40, color=ACCENT['red'], weight=700, valign='middle')
F.box(40, 260, 300, 220, '', 'white', rx=4)
F.box(90, 286, 200, 100, '', 'white', rx=2); F.text(190, 316, '分组处理', 16, color=INK, weight=600); F.box(130, 336, 120, 32, '转发表', 'blue', 14, 2)
F.text(190, 430, '交换结构', 16, color=INK, weight=600)
