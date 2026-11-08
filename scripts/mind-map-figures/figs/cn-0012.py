LABEL = '信道利用率：停等、GBN、SR 的时序比较'
F = Fig(820, 360, '信道利用率的推导')
for k, (title, n, x0) in enumerate((('① 停止—等待　W_{T} = W_{R} = 1', 1, 40), ('② GBN　W_{T} = 7，W_{R} = 1', 7, 310))):
    F.text(x0, 60, title, 12.5, 'start', INK, 600)
    F.line(x0 + 20, 76, x0 + 20, 300, INK2, 1.4); F.line(x0 + 220, 76, x0 + 220, 300, INK2, 1.4)
    for i in range(n): F.line(x0 + 20, 86 + i * 6, x0 + 220, 166 + i * 6 - (i * 0), ACCENT['blue'], 1.2)
    F.line(x0 + 220, 170 + n * 6, x0 + 20, 250 + n * 6, ACCENT['green'], 1.4, arrow='end')
    F.vbrace(x0 + 226, 86, 166, 't₁'); F.vbrace(x0 + 226, 170, 250, 't₁')
    F.text(x0 + 120, 330, ['P = t₂ / (2t₁ + t₂ + t₃)', 'P = 7t₂ / (2t₁ + t₂ + t₃)'][k], 13, color=ACCENT['red'], mono=True)
F.text(600, 60, '③ SR　W_{T} = 4，W_{R} = 4', 12.5, 'start', INK, 600)
F.text(690, 170, 'P = 4t₂ / (2t₁ + t₂ + t₃)', 13, color=ACCENT['red'], mono=True)
F.text(690, 210, 't₁：单程传播时延\nt₂：发送一帧的时间\nt₃：确认帧发送时间', 11.5, 'middle', MUTED, lh=1.5)
