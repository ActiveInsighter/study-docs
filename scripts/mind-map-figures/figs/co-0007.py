from mp import machine
LABEL = '多计算机系统：各计算机有独立主存，通过网络消息传递通信'
F = Fig(700, 470, '多计算机系统（MIMD）')
a = machine(F, 235, 50); b = machine(F, 20, 270); c = machine(F, 450, 270)
F.line(300, 222, 200, 268, INK2, 1.3, arrow='both'); F.line(400, 222, 500, 268, INK2, 1.3, arrow='both'); F.line(252, 355, 448, 355, INK2, 1.3, arrow='both')
F.text(220, 240, '网络（消息传递）', 11, 'end', INK2); F.text(480, 240, '网络（消息传递）', 11, 'start', INK2); F.text(350, 345, '网络（消息传递）', 11, color=INK2, halo=True)
