LABEL = '数据冲突：后续指令要用 add 写回的 r1'
F = Fig(780, 370, '数据冲突（数据相关）')
st = ['Im', 'Reg', 'ALU', 'Dm', 'Reg']
F.line(150, 50, 760, 50, INK2, 1.2, arrow='end'); F.text(760, 40, '时间（时钟周期）', 11, 'end', MUTED)
for i, s in enumerate(['IF', 'ID', 'EX', 'M', 'WB']): F.text(180 + i * 64, 70, s, 12.5, color=ACCENT['red'], weight=700)
rows = [('add r1,r2,r3', ''), ('sub r4,r1,r3', ''), ('and r6,r1,r7', ''), ('or r8,r1,r9', ''), ('xor r10,r1,r11', '')]
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
        hl = {(0, 4): 'red', (1, 1): 'red', (2, 1): 'red', (3, 1): 'red', (4, 1): 'blue'}.get((r, i))
        F.box(x, y, 52, 28, lab, hl or 'white', 11.5, 3)
for r in (1, 2, 3):
    F.line(152 + 4 * 64 + 26, 104, 152 + (r + 1) * 64 + 26, 90 + r * 52 + 2, ACCENT['red'], 1.2)
F.text(350, 370 - 14, 'add 在 WB 段才写回 r1，而后续指令在 ID 段就要读 r1：红色为冲突，蓝色可正常读取', 11.5, color=MUTED)
