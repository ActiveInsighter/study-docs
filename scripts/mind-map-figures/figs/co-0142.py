from common import datapath
LABEL = '定点整数除法：被除数放在低位，高位补 0'
F = Fig(780, 320, '定点整数：被除数在低 4 位')
ry = datapath(F, '除数 Y（4 bit）', '0 0 0 0', '被除数 X（4 bit）', '4 位 ALU', 4, '加 / 减', 150, left_tone='white', right_tone='green', shift='左移')
F.box(30, ry + 70, 170, 26, '小数点隐含在最低位后', 'red', 11.5, 5)
