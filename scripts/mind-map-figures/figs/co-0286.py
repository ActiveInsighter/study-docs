LABEL = '解决数据冲突③：数据旁路（转发）'
F = Fig(780, 370, '③ 数据旁路技术（转发）')
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
for r, i in ((1, 2), (2, 2), (3, 2)):
    F.curve(152 + (2 + r - 1) * 64 + 40, 90 + (r - 1) * 52 + 14 + (r - 1) * 0, 152 + (r + i) * 64 + 16, 90 + r * 52 + 14, 0.15, ACCENT['violet'], 1.4)
F.text(350, 370 - 14, 'ALU 的输出直接送回 ALU 的输入，后续指令不必等写回就能使用 r1', 11.5, color=MUTED)
