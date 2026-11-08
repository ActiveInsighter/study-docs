LABEL = '异步定时 · 全互锁方式'
F = Fig(520, 300, '异步定时 · 全互锁方式')
F.text(60, 110, '请求', 15, 'start', ACCENT['red'], 700, valign='middle'); F.text(60, 230, '回答', 15, 'start', ACCENT['blue'], 700, valign='middle')
from common import wave_level
wave_level(F, [(140, 130), (180, 80), (260, 130), (460, 130)], ACCENT['red'], 2.2)
wave_level(F, [(140, 250), (220, 200), (300, 250), (460, 250)], ACCENT['blue'], 2.2)
F.curve(188, 86, 218, 196, 0.12, ACCENT['red'], 1.6, '3 3')
F.curve(228, 196, 256, 130, 0.12, ACCENT['blue'], 1.6, '3 3')
F.curve(266, 134, 296, 246, 0.12, ACCENT['red'], 1.6, '3 3')
F.text(260, 286, '双方都互锁：从设备确认请求撤销后才撤销回答：最慢、最可靠', 11.5, color=MUTED)
