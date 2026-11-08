LABEL = '控制器图标'
F = Fig(48, 48, bg=False)
F.rect(2, 2, 44, 44, '#f4f4f5', '#d4d4d8', 1, 11)
F.rect(11, 15, 26, 18, 'white', INK2, 1.8, 3)
for x in (16, 22, 28): F.path(f'M{x} 33V38M{x} 10V15', INK2, 1.6)
F.circle(31, 24, 2, '', 'dark', sw=0)
