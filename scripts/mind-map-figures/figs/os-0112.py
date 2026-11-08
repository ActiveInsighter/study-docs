LABEL = '双缓冲工作示意图'
F = Fig(640, 320, '双缓冲')
F.rect(160, 50, 260, 130, 'blue', ACCENT['blue'], 1.2, 6, opacity=0.6)
F.box(40, 92, 60, 40, 'CPU', 'violet', 12, 4); F.box(200, 96, 100, 36, '用户进程的\n工作区', 'violet', 11, 6)
F.box(330, 64, 70, 28, '缓冲区 1', 'amber', 11, 4); F.box(330, 140, 70, 28, '缓冲区 2', 'amber', 11, 4)
F.box(520, 96, 70, 36, '块设备', 'green', 11.5, 4)
F.line(198, 112, 102, 112, INK2, 1.3, arrow='end'); F.text(150, 102, '处理（C）', 11, color=INK2)
F.line(328, 78, 302, 104, INK2, 1.2, arrow='end'); F.line(328, 154, 302, 124, INK2, 1.2, arrow='end'); F.text(300, 66, '传送（M）', 10.5, 'end', INK2)
F.line(518, 106, 402, 78, INK2, 1.2, arrow='end'); F.line(518, 122, 402, 154, INK2, 1.2, arrow='end'); F.text(470, 80, '输入（T）', 10.5, color=INK2)
F.text(290, 196, '内存', 11, color=INK2)
F.line(20, 218, 620, 218, LINE, 1)
for k in range(4):
    x = 40 + k * 150
    F.path(f'M{x} 230H{x + 50}V254H{x + 80}V278H{x + 110}', INK, 1.5)
    F.text(x + 25, 226, f'T_{{{k + 1}}}（缓冲 {k % 2 + 1}）', 10.5, color=INK, mono=True); F.text(x + 65, 250, f'M_{{{k + 1}}}', 11, color=INK, mono=True); F.text(x + 95, 274, f'C_{{{k + 1}}}', 11, color=INK, mono=True)
