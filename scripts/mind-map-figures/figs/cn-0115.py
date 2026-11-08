LABEL = '码元：固定时长的信号波形；M 进制码元可携带 log2(M) 比特信息'
F = Fig(700, 200, '码元')
F.box(40, 60, 70, 50, 'A', 'white', 13, 4); F.box(590, 60, 70, 50, 'B', 'white', 13, 4)
F.line(112, 85, 588, 85, ACCENT['blue'], 1.6)
from common import wave_digital
wave_digital(F, 470, 78, [1, 0, 1, 0, 1, 0, 1, 1], 26, 12, INK, 1.4)
F.text(522, 56, '1 0 1 0 1 0 1', 10.5, color=INK2, mono=True)
F.text(350, 140, 'K 进制码元：如 4 进制码元 → 码元的离散状态有 4 个 → 4 种高低不同的信号波形 00、01、10、11', 11.5, color=INK2)
F.text(350, 168, '1 个码元可以携带多个比特的信息量（二进制码元只携带 1 bit）', 11.5, color=MUTED)
