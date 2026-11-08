LABEL = '异步定时 · 不互锁方式'
F = Fig(520, 300, '异步定时 · 不互锁方式')
F.text(60, 110, '请求', 15, 'start', ACCENT['red'], 700, valign='middle'); F.text(60, 230, '回答', 15, 'start', ACCENT['blue'], 700, valign='middle')
from common import wave_level
wave_level(F, [(140, 130), (180, 80), (300, 130), (460, 130)], ACCENT['red'], 2.2)
wave_level(F, [(140, 250), (220, 200), (340, 250), (460, 250)], ACCENT['blue'], 2.2)
F.curve(188, 86, 218, 196, 0.12, ACCENT['red'], 1.6, '3 3')
F.text(260, 286, '主设备发出请求后不等回答，过一段时间自行撤销；从设备回答后也自行撤销：最快、最不可靠', 11.5, color=MUTED)
