LABEL = '相邻两层之间的关系：实体、协议、服务访问点 SAP、服务原语'
F = Fig(720, 300, '相邻两层之间的关系')
F.rect(20, 160, 680, 110, 'red', 'none', 0, 4, opacity=0.6); F.line(20, 160, 700, 160, LINE, 1, dash='5 4')
F.text(680, 86, '第 n+1 层', 15, 'end', ACCENT['red'], 700); F.text(680, 200, '第 n 层', 15, 'end', ACCENT['red'], 700)
F.box(150, 60, 100, 30, '实体 (n+1)', 'amber', 12, 4); F.box(420, 60, 100, 30, '实体 (n+1)', 'amber', 12, 4)
F.box(150, 220, 100, 30, '实体 (n)', 'amber', 12, 4); F.box(420, 220, 100, 30, '实体 (n)', 'amber', 12, 4)
F.line(252, 75, 418, 75, INK2, 1.1, dash='3 3', arrow='both'); F.text(335, 68, '协议 (n+1)', 11, color=INK2, halo=True)
F.line(252, 235, 418, 235, INK2, 1.1, dash='3 3', arrow='both'); F.text(335, 228, '协议 (n)', 11, color=INK2, halo=True)
for x in (200, 470):
    F.line(x - 6, 92, x - 6, 218, INK2, 1.4, arrow='both')
    F.text(x + 6, 110, '交换原语', 11, 'start', ACCENT['blue'])
F.circle(470, 182, 14, 'SAP', 'white', 10)
F.text(212, 182, 'SAP', 11, 'start', ACCENT['blue']); F.text(440, 168, '服务访问点', 11, 'end', INK2)
F.text(140, 75, '服务用户', 12, 'end', ACCENT['red'], 600, valign='middle'); F.text(140, 235, '服务提供者', 12, 'end', ACCENT['red'], 600, valign='middle')
