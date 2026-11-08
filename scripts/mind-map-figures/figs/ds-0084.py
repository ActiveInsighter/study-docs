LABEL = '有序顺序表上的顺序查找判定树'
F = Fig(720, 420, '有序表顺序查找判定树（10, 20, 30, 40, 50, 60）')
vals = [10, 20, 30, 40, 50, 60]
fails = ['(−∞,10)', '(10,20)', '(20,30)', '(30,40)', '(40,50)', '(50,60)']
for i, v in enumerate(vals):
    x, y = 110 + i * 86, 84 + i * 46
    F.circle(x, y, 18, str(v), 'blue' if v == 40 else 'white', 14, mono=True)
    if i < 5:
        F.line(x, y, x + 86, y + 46, INK2, 1.4, gap=18, gap2=18)
        F.text(x + 52, y + 18, '>', 12, color=MUTED)
    fx, fy = x - 66, y + 46
    F.line(x, y, fx + 30, fy - 10, INK2, 1.2, gap=18, gap2=0)
    F.box(fx - 4, fy - 10, 72, 24, fails[i], 'light', 12, 4, mono=True)
F.line(540, 314, 580, 348, INK2, 1.2, gap=18); F.box(560, 350, 64, 24, '(60,∞)', 'light', 12, 4, mono=True)
F.text(420, 116, '查找 25：25>10, 25>20, 25<30 → 失败于 (20,30)', 12.5, 'start', ACCENT['red'])
F.text(420, 84, '查找 40：40>10, 40>20, 40>30, 40=40 → 成功', 12.5, 'start', ACCENT['blue'])
F.text(360, 406, '有序表中查找失败不必比到表尾：遇到比 key 大的元素即可停止', 12.5, color=MUTED)
