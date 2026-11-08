LABEL = 'I/O 控制器（I/O 接口）的组成'
F = Fig(800, 400, 'I/O 控制器的组成')
F.box(30, 170, 80, 60, 'CPU', 'violet', 14, 8)
F.rect(170, 70, 420, 220, 'blue', ACCENT['blue'], 1.3, 10, opacity=0.6); F.pill(180, 60, 'I/O 控制器', 'blue', 11.5)
F.rect(190, 90, 130, 180, 'white', '#a1a1aa', 1.1, 6)
F.box(200, 100, 110, 30, '数据寄存器', 'white', 11.5, 4); F.box(200, 142, 110, 36, '控制 / 状态\n寄存器', 'white', 11, 4); F.text(255, 200, '⋮（有多个）', 11, color=MUTED)
F.box(350, 160, 80, 70, 'I/O 逻辑', 'red', 12, 4)
F.box(460, 90, 110, 44, '控制器与设备\n的接口 1', 'green', 11, 4); F.box(460, 210, 110, 44, '控制器与设备\n的接口 i', 'green', 11, 4); F.text(515, 172, '⋯', 14, color=MUTED, valign='middle')
for y in (100, 112, 124): F.line(572, y, 640, y, INK2, 1.2, arrow='both')
for y in (220, 232, 244): F.line(572, y, 640, y, INK2, 1.2, arrow='both')
for y, t in ((100, '数据'), (112, '状态'), (124, '控制'), (220, '数据'), (232, '状态'), (244, '控制')): F.text(646, y, t, 10.5, 'start', INK2, valign='middle')
F.poly([(70, 168), (70, 115), (198, 115)], INK2, 1.4, arrow='both'); F.text(80, 106, '数据总线', 11, 'start', INK2)
F.line(112, 190, 348, 190, INK2, 1.4, arrow='end'); F.text(130, 182, '地址线', 11, 'start', INK2)
F.line(112, 215, 348, 215, INK2, 1.4, arrow='both'); F.text(130, 230, '控制线', 11, 'start', INK2)
F.line(312, 160, 348, 175, INK2, 1.1, arrow='both'); F.line(430, 180, 458, 115, INK2, 1.1, arrow='both'); F.line(430, 210, 458, 230, INK2, 1.1, arrow='both')
notes = [('CPU 与控制器的接口：数据线传数据，地址线指明设备与寄存器，控制线发命令', 'amber', 30, 300, 250), ('I/O 逻辑：接收和识别 CPU 的命令（如地址译码），并向设备发出命令', 'red', 300, 300, 230), ('控制器与设备的接口：数据、状态、控制三类信号', 'green', 550, 300, 220)]
for t, tone, x, y, w in notes:
    F.box(x, y, w, 54, '', tone, rx=6); F.text(x + w / 2, y + 27, t[:16] + '\n' + t[16:32] + ('\n' + t[32:] if len(t) > 32 else ''), 10.5, color=TONES[tone][2], valign='middle', lh=1.35)
F.text(400, 386, '一个 I/O 控制器可以控制多个设备；状态寄存器反映设备忙 / 闲等状态', 11, color=MUTED)
