LABEL = '内存中的一个进程：程序运行时的内存映像与地址空间'
F = Fig(700, 460, '程序运行的内存映像（虚拟地址空间）')
segs = [('操作系统内核区', 'blue', 34), ('用户栈（运行时创建）', 'green', 40), ('', 'green', 34), ('共享库的存储映射区', 'violet', 36), ('', 'amber', 30), ('动态生成的堆（运行时由 malloc 创建）', 'amber', 40), ('读 / 写数据段（.data、.bss）', 'red', 34), ('只读代码段（.init、.text、.rodata）', 'red', 40), ('未使用区', 'gray', 26)]
y = 60
pos = []
for t, tone, h in segs:
    F.box(260, y, 220, h, t, tone, 11, 0); pos.append((y, y + h)); y += h
F.text(370, pos[2][0] + 18, '↓', 14, color=INK2, valign='middle'); F.text(370, pos[4][0] + 15, '↑', 14, color=INK2, valign='middle')
for (y0, y1), lab in ((pos[0], '0xFFFFFFFF'), (pos[1], '0xC0000000'), (pos[4], '0x40000000'), (pos[8], '0x08048000')):
    F.text(252, y0, lab, 10.5, 'end', INK2, mono=True, valign='middle')
F.text(252, pos[8][1], '0', 10.5, 'end', INK2, mono=True, valign='middle')
F.text(490, pos[0][0] + 17, '用户代码不可见区', 11, 'start', INK2, valign='middle')
F.line(530, pos[1][0] + 20, 484, pos[1][0] + 20, INK2, 1.1, arrow='end'); F.text(534, pos[1][0] + 20, '%esp（栈指针）', 11, 'start', INK2, valign='middle')
F.text(490, pos[3][0] + 18, '共享函数库代码所在区域', 11, 'start', INK2, valign='middle')
F.vbrace(484, pos[6][0], pos[7][1], '从可执行文件装入\n的数据及代码', size=11)
F.line(150, 400, 150, 70, INK2, 1.4, arrow='end'); F.text(140, 230, '地址从低到高\n从下到上\n（虚拟地址）', 11.5, 'end', INK2, lh=1.4, valign='middle')
F.text(370, 446, 'printf() 等共享库函数放在共享库映射区；.bss 是未初始化及初始化为 0 的全局 / 静态变量', 10.5, color=MUTED)
