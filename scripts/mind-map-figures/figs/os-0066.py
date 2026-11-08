from common import disk_grid
LABEL = '空闲表法：记录每个连续空闲区的第一个盘块号和盘块数'
F = Fig(700, 330, '空闲表法')
free = [0, 1, 5, 10, 11, 12, 13, 14, 18, 19, 20, 23]
hl = {b: ('green' if b in free else 'amber', str(b)) for b in range(24)}
disk_grid(F, 20, 50, 24, 4, hl, labels=False, cw=40, ch=24, dx=52, dy=38)
F.table(330, 70, [['第一个空闲盘块号', '空闲盘块数'], ['0', '2'], ['5', '1'], ['10', '5'], ['18', '3'], ['23', '1']], [130, 100], 28, size=12, head_tone='amber', mono_cols=(0, 1))
F.text(445, 252, '空闲盘块表', 12, color=INK2)
F.line(270, 160, 326, 160, ACCENT['blue'], 2, arrow='end')
F.legend(330, 290, [('green', '空闲块'), ('amber', '非空闲块')])
F.text(445, 318, '分配：可采用首次适应等算法；回收时注意合并相邻空闲区', 11, color=MUTED)
