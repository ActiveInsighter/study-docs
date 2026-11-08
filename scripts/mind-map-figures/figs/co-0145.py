from common import block
LABEL = '一位全加器的逻辑符号'
F = Fig(460, 250)
block(F, 150, 80, 160, 70, 'FA', top='S_{i}', bottoms=('A_{i}', 'B_{i}'), left='C_{i}', right='C_{i−1}', L=44, size=18, lsize=15)
