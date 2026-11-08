from common import disk_grid
LABEL = '空闲链表法：空闲盘块链与空闲盘区链'
F = Fig(700, 340, '空闲链表法')
free = [0, 5, 6, 7, 10, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23]
hl = {b: ('green' if b in free else 'amber', str(b)) for b in range(24)}
cs = disk_grid(F, 20, 60, 24, 4, hl, labels=False, cw=36, ch=22, dx=50, dy=36)
F.text(130, 52, '空闲盘块链', 12.5, color=INK, weight=600)
for a, b in zip(free, free[1:]): F.line(*cs[a], *cs[b], ACCENT['red'], 1, arrow='end', gap=8, gap2=10)
cs2 = disk_grid(F, 360, 60, 24, 4, hl, labels=False, cw=36, ch=22, dx=50, dy=36)
F.text(470, 52, '空闲盘区链', 12.5, color=INK, weight=600)
for grp in ([0], [5, 6, 7], [10, 11], [13, 14, 15], [17, 18, 19], [20, 21, 22, 23]):
    x1, y1 = cs2[grp[0]]; x2, y2 = cs2[grp[-1]]
    F.rect(x1 - 22, y1 - 15, x2 - x1 + 44, 30, 'none', ACCENT['red'], 1.2, 6, dash='3 3')
F.text(350, 330, '盘块链：每个空闲块存指向下一个空闲块的指针；盘区链：以连续空闲区为单位链接，并记录盘区长度', 10.5, color=MUTED)
