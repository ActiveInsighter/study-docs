LABEL = '两个路由器之间直接相连时，链路上的帧可以是 PPP 帧'
F = Fig(560, 160)
for i, x in enumerate((90, 280, 470)):
    F.circle(x, 70, 26, '⇄', 'blue', 16); F.text(x, 120, f'路由器 {i}', 12.5, color=INK2)
    if i: F.line(x - 164, 70, x - 26, 70, ACCENT['red'], 1.6)
F.text(280, 146, '点对点链路：可使用 PPP 帧', 11, color=MUTED)
