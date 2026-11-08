LABEL = '单缓冲工作示意图'
F = Fig(560, 320, '单缓冲工作示意图')
F.box(30, 70, 130, 70, '', 'white', rx=4); F.text(95, 88, '处理（C）', 12, color=INK2); F.box(50, 100, 90, 28, '工作区', 'blue', 12, 3)
F.text(60, 62, '用户进程', 12, color=INK2)
F.box(240, 100, 80, 28, '缓冲区', 'amber', 12, 3); F.box(420, 100, 100, 28, 'I/O 设备', 'gray', 12, 3)
F.line(238, 114, 142, 114, INK2, 1.4, arrow='end'); F.text(190, 104, '传送（M）', 11.5, color=INK2)
F.line(418, 114, 322, 114, INK2, 1.4, arrow='end'); F.text(370, 104, '输入（T）', 11.5, color=INK2)
F.text(280, 162, '(a)', 12, color=INK2)
for k in range(4):
    x = 40 + k * 120
    F.path(f'M{x} 190H{x + 40}V214H{x + 70}V238H{x + 100}', INK, 1.5)
    F.text(x + 20, 182, f'T_{{{k + 1}}}', 11.5, color=INK, mono=True); F.text(x + 55, 208, f'M_{{{k + 1}}}', 11.5, color=INK, mono=True); F.text(x + 85, 232, f'C_{{{k + 1}}}', 11.5, color=INK, mono=True)
F.line(30, 262, 530, 262, INK2, 1.3, arrow='end'); F.text(536, 262, 't', 12, 'start', INK, valign='middle')
F.text(280, 290, '(b)　默认用户空间可以放得下一个缓冲区的数据', 12, color=INK2)
