LABEL = '对比清单图标'
F = Fig(48, 48, bg=False)
F.rect(2, 2, 44, 44, '#f4f4f5', '#d4d4d8', 1, 11)
F.rect(13, 10, 22, 28, 'white', INK2, 1.8, 3)
for y in (17, 24, 31): F.path(f'M17 {y}H19M22 {y}H31', INK2, 1.6)
