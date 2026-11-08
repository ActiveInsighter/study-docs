LABEL = '磁盘的盘面与柱面：所有盘面上相同位置的磁道组成柱面'
F = Fig(640, 360, '盘面与柱面')
for i in range(4):
    y = 90 + i * 64
    F.ellipse(222, y, 150, 30, '', 'blue' if i % 2 == 0 else 'red')
    F.ellipse(222, y, 96, 19, '', 'none', dash='4 3')
    F.items[-1] = F.items[-1].replace('stroke="none"', f'stroke="{ACCENT["green"]}"').replace('stroke-width="1.5"', 'stroke-width="2"')
    F.ellipse(222, y, 18, 6, '', 'white')
    F.text(64, y, f'{i} 号盘面', 12, 'end', INK2, valign='middle')
    F.box(312, y - 24 + 10, 18, 8, '', 'dark', rx=1); F.box(312, y + 6, 18, 8, '', 'dark', rx=1)
F.line(321, 60, 321, 300, INK2, 2); 
F.line(392, 60, 330, 60, ACCENT['red'], 1.6, arrow='both'); F.text(400, 64, '磁头臂整体移动', 12, 'start', ACCENT['red'])
F.text(400, 110, '每个盘面对应一个磁头；', 12, 'start', INK2)
F.text(400, 132, '所有磁头连在同一个磁臂上，', 12, 'start', INK2)
F.text(400, 154, '因此所有磁头“共进退”', 12, 'start', INK2)
F.text(400, 212, '所有盘面中相对位置相同的', 12, 'start', ACCENT['green'], 600)
F.text(400, 234, '磁道（绿色虚线）组成柱面', 12, 'start', ACCENT['green'], 600)
F.text(310, 344, '一个盘片可能有两个盘面；磁盘地址：⟨柱面号, 盘面号, 扇区号⟩', 12, color=MUTED)
