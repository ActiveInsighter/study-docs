LABEL = '数据平面：根据转发表进行分组转发，这是路由器的本地动作'
F = Fig(600, 280, '数据平面：根据转发表转发')
F.text(300, 60, '数据平面执行的主要功能是根据转发表进行转发，这是路由器的本地动作', 12, color=INK2)
F.ellipse(310, 120, 50, 22, '⇄', 'blue', 15)
F.line(160, 100, 262, 116, ACCENT['green'], 2, arrow='end'); F.text(170, 90, '分组', 12, 'start', ACCENT['green'], 600)
for i, (dx, dy, c) in enumerate(((150, -30, 'amber'), (160, 0, 'violet'), (150, 40, 'blue'))): F.line(360, 120, 360 + dx, 120 + dy, ACCENT[c], 1.6, arrow='end')
F.text(170, 150, '本地转发表', 11.5, color=ACCENT['blue'])
F.table(110, 160, [['首部', '输出'], ['0100', '3'], ['0110', '2'], ['0111', '2'], ['1001', '1']], [60, 60], 22, size=11, head_tone='blue', mono_cols=(0, 1))
F.text(420, 220, '转发表基于路由表生成', 12, color=INK2)
