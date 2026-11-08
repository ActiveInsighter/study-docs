LABEL = '数据、数据对象、数据元素、数据项的关系'
F = Fig(700, 420, '数据 ⊃ 数据对象 ⊃ 数据元素 ⊃ 数据项')
F.ellipse(350, 225, 320, 180, '', 'light'); F.text(350, 80, '数据', 16, color=INK, weight=700)
F.ellipse(220, 240, 170, 110, '', 'violet'); F.text(220, 158, '数据对象', 14, color=TONES['violet'][2], weight=700)
F.text(220, 330, '（个人财富的数据元素集合）', 11.5, color=TONES['violet'][2])
for k, x in enumerate((150, 290)):
    F.box(x - 60, 178, 120, 120, '', 'amber', rx=14)
    F.text(x, 198, '数据元素', 13, color=TONES['amber'][2], weight=700)
    for j in range(3):
        F.box(x - 52 + j * 36, 212, 32, 76, '数\n据\n项', 'blue', 12, 6)
F.ellipse(520, 170, 100, 50, '', 'violet'); F.text(520, 164, '数据对象', 14, color=TONES['violet'][2], weight=700); F.text(520, 186, '（微博账号的数据元素集合）', 11, color=TONES['violet'][2])
F.ellipse(520, 300, 100, 50, '', 'violet'); F.text(520, 294, '数据对象', 14, color=TONES['violet'][2], weight=700); F.text(520, 316, '（海底捞排队的数据元素集合）', 11, color=TONES['violet'][2])
