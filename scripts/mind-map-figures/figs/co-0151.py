LABEL = '微操作的确定：由指令 OP、所处机器周期、节拍号与 PSW 状态共同决定'
F = Fig(820, 380, '一条指令 → 若干机器周期 → 若干节拍 → 微操作')
F.box(20, 150, 90, 50, '高级语言\n代码', 'white', 12, 6, dash='4 3')
for i in range(6):
    F.box(150, 66 + i * 44, 70, 30, f'指令 {i + 1}', 'amber' if i == 1 else 'white', 11.5, 4)
F.line(110, 175, 148, 125, LINE, 1.1); F.line(110, 175, 148, 300, LINE, 1.1)
cyc = [('取指周期\n(FE = 1)', 'green'), ('间址周期\n(IND = 1)', 'amber'), ('执行周期\n(EX = 1)', 'violet'), ('中断周期\n(INT = 1)', 'blue')]
for i, (l, t) in enumerate(cyc):
    F.box(270, 66 + i * 70, 90, 50, l, t, 11, 4)
F.line(222, 125, 268, 91, LINE, 1.1); F.line(222, 125, 268, 300, LINE, 1.1)
mos = [('T₀：微操作 1、微操作 2\nT₁：微操作 3\nT₂：微操作 4', 'green'), ('T₀：微操作 5、微操作 2\nT₁：微操作 6\nT₂：微操作 7', 'amber'),
       ('T₀：\nT₁：微操作 8\nT₂：微操作 9、微操作 6', 'violet'), ('T₀：\nT₁：微操作 10\nT₂：微操作 11', 'blue')]
for i, (l, t) in enumerate(mos):
    F.box(410, 62 + i * 70, 170, 58, l, t, 10.5, 4, align='start')
    F.line(360, 91 + i * 70, 408, 91 + i * 70, LINE, 1.1)
notes = ['① 一个节拍内可并行完成\n多个“相容”的操作', '② 同一个微操作可在\n不同指令中被使用', '③ 选择定长的机器周期，\n以最大节拍数为准', '④ 所需节拍较少时，可将\n微操作放在后几个节拍']
for i, n in enumerate(notes):
    F.box(600, 66 + i * 70, 210, 44, n, 'red', 10.5, 4)
