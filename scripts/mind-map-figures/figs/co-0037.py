LABEL = 'CPU 用 MREQ 控制译码器使能端，从而控制片选信号生效的时间'
F = Fig(760, 330, 'MREQ̄ 接译码器使能端')
F.box(30, 120, 140, 160, '', 'white', rx=18); F.text(90, 210, 'CPU', 14, color=INK, weight=700, valign='middle')
F.text(100, 140, 'MREQ̄', 12, 'middle', CTRL_C := '#c98a12', 600)
for i, p in enumerate(('A₁₅', 'A₁₄', 'A₁₃', 'A₁₂~A₀')): F.text(162, 170 + i * 22, p, 11.5, 'end', '#d1493a', valign='middle')
F.box(400, 60, 90, 150, '', 'white', rx=4); F.text(445, 150, '译\n码\n器', 13, color=INK, valign='middle')
F.poly([(100, 120), (100, 104), (398, 104)], CTRL_C, 1.4)
F.text(404, 76, 'G₁ ← 1', 11, 'start', ACCENT['blue']); F.text(404, 92, 'G̅₂A ← 0', 11, 'start', ACCENT['blue']); F.text(404, 108, 'G̅₂B', 11, 'start', ACCENT['blue'])
for i, p in enumerate(('C', 'B', 'A')):
    F.poly([(170, 170 + i * 22), (300 + i * 14, 170 + i * 22), (300 + i * 14, 160 + i * 16), (398, 160 + i * 16)], '#d1493a', 1.2)
for i in range(8):
    F.line(490, 72 + i * 17, 530, 72 + i * 17, '#d1493a', 1.1)
F.box(560, 210, 140, 80, '8K × 8 位', 'blue', 12.5, 4)
F.poly([(530, 157), (640, 157), (640, 208)], CTRL_C, 1.4, arrow='end'); F.text(648, 198, 'CS̄（低电平有效）', 11, 'start', CTRL_C)
F.poly([(170, 236), (540, 236), (558, 236)], '#d1493a', 1.2, arrow='end')
F.box(200, 280, 160, 34, '先送出地址信号', 'blue', 12, 6); F.line(362, 297, 420, 297, ACCENT['blue'], 2, arrow='end')
F.text(560, 60, '地址稳定后 CPU 才使 MREQ̄ = 0，\n译码器开始工作，片选信号生效', 12, 'start', INK2, lh=1.5)
