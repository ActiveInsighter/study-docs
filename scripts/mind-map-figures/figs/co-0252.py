from common import instr
LABEL = '立即寻址：形式地址 A 就是操作数本身'
F = Fig(460, 220, '立即寻址')
instr(F, 60, 90, 'OP', '#', 'A', (110, 110, 110), 44)
F.brace(280, 390, 138, '立即数（补码）', size=12.5)
F.text(230, 206, '不访存：取指即得操作数，范围受 A 的位数限制', 12, color=MUTED)
