from common import ADDR_C
LABEL = '3-8 译码器：输出高电平有效与低电平有效'
F = Fig(760, 330, '3-8 译码器：高电平有效 vs 低电平有效')
for k, (x, low) in enumerate(((60, False), (440, True))):
    F.box(x + 60, 70, 80, 170, '译\n码\n器', 'white', 14, 4)
    for j, (n, v) in enumerate((('C', '1'), ('B', '0'), ('A', '1'))):
        y = 186 + j * 20; F.line(x + 20, y, x + 58, y, ADDR_C, 1.3); F.text(x + 14, y, f'{v} {n}', 12, 'end', ADDR_C, valign='middle')
    for i in range(8):
        y = 82 + i * 20; idx = 7 - i
        on = idx == 5
        val = ('0' if on else '1') if low else ('1' if on else '0')
        if low: F.circle(x + 145, y, 4, '', 'white', sw=1.2)
        F.line(x + 140 + (9 if low else 0), y, x + 180, y, ADDR_C, 1.3)
        F.text(x + 186, y, ('Ȳ' if low else 'Y') + f'_{{{idx}}}  {val}', 12, 'start', ACCENT['red'] if on else INK2, 600 if on else 400, valign='middle')
    F.text(x + 100, 270, '高电平有效：选中的输出为 1' if not low else '低电平有效：选中的输出为 0', 13, color=INK, weight=600)
F.text(380, 310, 'CBA = 101 → 选中第 5 路；芯片的 CS 为高有效时接高有效译码器，CS̄ 为低有效时接低有效译码器', 11.5, color=MUTED)
