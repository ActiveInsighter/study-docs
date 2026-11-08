LABEL = '文件系统的层次结构（教材版）：用户调用接口 → 文件目录系统 → 存取控制验证 → 逻辑文件系统 → 物理文件系统'
F = Fig(420, 470, '文件系统的层次结构')
labs = [('用户调用接口', '第 0 级'), ('文件目录系统', '第 1 级'), ('存取控制验证模块', '第 2 级'), ('逻辑文件系统与\n文件信息缓冲区', '第 3 级'), ('物理文件系统', '第 4 级')]
F.text(170, 54, '用户', 12, color=INK2); F.line(160, 60, 160, 78, INK2, 1.2, arrow='end'); F.line(180, 78, 180, 60, INK2, 1.2, arrow='end')
for i, (t, lv) in enumerate(labs):
    h = 46 if '\n' in t else 32
    y = 80 + i * 58
    F.box(90, y, 160, h, t, 'blue', 12.5, 4); F.text(268, y + h / 2, lv, 12, 'start', INK2, 600, valign='middle')
    if i: F.line(170, y - 24, 170, y - 2, INK2, 1.2, arrow='end')
F.box(30, 380, 120, 32, '辅助分配模块', 'white', 12, 4); F.box(190, 380, 160, 32, '设备管理程序模块', 'white', 12, 4)
F.line(150, 346, 100, 378, INK2, 1.2, arrow='end'); F.line(190, 346, 260, 378, INK2, 1.2, arrow='end')
F.ellipse(270, 446, 34, 16, '设备', 'gray', 12); F.line(270, 414, 270, 428, INK2, 1.2, arrow='both')
