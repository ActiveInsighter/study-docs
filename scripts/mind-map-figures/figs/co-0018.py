LABEL = '解决数据冲突①：硬件阻塞，插入气泡'
F = Fig(780, 370, '① 硬件阻塞（stall），插入气泡')
st = ['Im', 'Reg', 'ALU', 'Dm', 'Reg']
F.line(150, 50, 760, 50, INK2, 1.2, arrow='end'); F.text(760, 40, '时间（时钟周期）', 11, 'end', MUTED)
for i, s in enumerate(['IF', 'ID', 'EX', 'M', 'WB']): F.text(180 + i * 64, 70, s, 12.5, color=ACCENT['red'], weight=700)
rows = [('add r1,r2,r3', ''), ('stall', 'bubble'), ('stall', 'bubble'), ('stall', 'bubble'), ('sub r4,r1,r3', '')]
for r, (name, kind) in enumerate(rows):
    y = 90 + r * 52
    F.text(140, y + 14, name, 12.5, 'end', INK, 600, valign='middle', mono=True)
    for i in range(5):
        x = 152 + (r + i) * 64
        lab = st[i]
        tone = 'white'
        if kind == 'bubble' and i >= 1:
            F.ellipse(x + 26, y + 14, 26, 12, 'bubble', 'green', 10); continue
        if i == 2:
            F.items.append(f'<path d="M{x + 14} {y - 4}L{x + 40} {y + 6}V{y + 22}L{x + 14} {y + 32}V{y + 18}L{x + 20} {y + 14}L{x + 14} {y + 10}Z" fill="#fff" stroke="#3f3f46" stroke-width="1.2"/>')
            continue
        hl = {(0, 4): 'red', (4, 1): 'blue'}.get((r, i))
        F.box(x, y, 52, 28, lab, hl or 'white', 11.5, 3)
F.line(152 + 4 * 64 + 40, 104, 152 + 5 * 64 + 26, 90 + 4 * 52 + 2, ACCENT['blue'], 1.2); F.items.insert(1, F.items.pop())
F.text(350, 370 - 14, '硬件检测到相关后插入 3 个气泡，sub 等 r1 写回后再读', 11.5, color=MUTED)
