from common import wave_digital, encode
LABEL = '常用编码：非归零、归零、反向不归零、曼彻斯特、差分曼彻斯特'
F = Fig(840, 460, '数字数据 → 数字信号的编码')
bits = [1, 0, 0, 1, 1, 0, 1, 0]
X0, BW = 200, 64
F.text(180, 74, '二进制数据', 13, 'end', INK, 700, valign='middle')
for i, b in enumerate(bits): F.text(X0 + i * BW + BW / 2, 74, str(b), 14, color=INK, mono=True, weight=600, valign='middle')
for i in range(len(bits) + 1): F.line(X0 + i * BW, 60, X0 + i * BW, 420, LINE, 0.8, dash='3 4')
rows = [('非归零编码', 'nrz', '1 是高电平，0 是低电平'), ('归零编码', 'rz', '信号电平在一个码元之内都要恢复到 0'), ('反向不归零编码', 'nrzi', '电平翻转表示 0，不变表示 1'),
        ('曼彻斯特编码', 'man', '1 先高后低，0 先低后高'), ('差分曼彻斯特编码', 'dman', '1 码元开始处不变，0 要变；中间总有跳变')]
for k, (name, kind, note) in enumerate(rows):
    y = 130 + k * 64
    F.text(180, y - 10, name, 12.5, 'end', INK, 600, valign='middle')
    wave_digital(F, X0, y, encode(bits, kind), BW, 24, ACCENT['blue'])
    F.text(X0 + 4 * BW, y + 16, note, 10.5, color=MUTED)
F.box(740, 112, 80, 44, '无自同步\n能力', 'amber', 10.5, 4)
F.box(740, 330, 80, 70, '可以自同步；\n数据传输率\n只有调制\n速率的 1/2', 'amber', 9.5, 4)
