LABEL = '第一类虚拟机管理程序：直接运行在硬件上，如 Xen、Hyper-V、vSphere'
F = Fig(560, 300, '第一类虚拟机管理程序（裸金属）')
F.box(110, 80, 120, 80, '', 'blue', rx=0); F.box(230, 80, 120, 80, '', 'amber', rx=0); F.box(350, 80, 100, 80, '控制域', 'white', 12.5, 0)
for x, l in ((140, 'Excel'), (200, 'Word'), (260, 'Mplayer'), (320, 'Emacs')):
    F.circle(x, 112, 14, '', 'white'); F.text(x, 66, l, 11, color=INK, weight=600); F.line(x, 72, x, 96, INK2, 1.1, arrow='end')
F.text(170, 148, 'Windows', 12, color=TONES['blue'][2]); F.text(290, 148, 'Linux', 12, color=TONES['amber'][2])
F.box(110, 160, 340, 44, '第一类虚拟机管理程序', 'white', 13, 0); F.box(110, 204, 340, 44, '硬件（CPU、磁盘、网络、中断等）', 'gray', 13, 0)
F.vbrace(100, 80, 248, '', right=False); F.text(60, 164, '普通的\n电脑', 12, 'middle', INK2, lh=1.3, valign='middle')
F.text(280, 282, '虚拟机管理程序直接运行在硬件上，拥有最高特权', 11.5, color=MUTED)
