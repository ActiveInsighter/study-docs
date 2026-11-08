from common import block
LABEL = '4 位 CLA 加法器：两个 4 位二进制数相加，同时产生 4 位和'
F = Fig(460, 262)
block(F, 120, 80, 220, 70, '4 位 CLA 加法器', top='S_{3} ~ S_{0}', bottoms=('A_{3} ~ A_{0}', 'B_{3} ~ B_{0}'), left='C_{4}', right='C_{0}', L=40, size=16)
F.text(230, 248, '两个 4 位数相加，同时产生 4 位和', 12.5, color=MUTED)
