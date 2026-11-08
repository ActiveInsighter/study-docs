LABEL = '资源冲突（结构相关）：LOAD 的访存与 Instr 3 的取指同时访问存储器'
F = Fig(780, 370, '资源冲突（结构相关）')
st = ['Mem', 'Reg', 'ALU', 'Mem', 'Reg']
F.line(150, 50, 760, 50, INK2, 1.2, arrow='end'); F.text(760, 40, '时间（时钟周期）', 11, 'end', MUTED)
for i, s in enumerate(['IF', 'ID', 'EX', 'M', 'WB']): F.text(180 + i * 64, 70, s, 12.5, color=ACCENT['red'], weight=700)
rows = [('LOAD', ''), ('Instr 1', ''), ('Instr 2', ''), ('Instr 3', ''), ('Instr 4', '')]
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
        hl = {(0, 3): 'red', (0, 4): 'blue', (3, 0): 'red', (3, 1): 'blue'}.get((r, i))
        F.box(x, y, 52, 28, lab, hl or 'white', 11.5, 3)

F.text(350, 370 - 14, '同一时刻两条指令争用同一硬件资源（存储器）：可暂停或把指令 / 数据存储器分开', 11.5, color=MUTED)
