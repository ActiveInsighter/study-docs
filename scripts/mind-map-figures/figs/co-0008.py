from common import datapath
LABEL = '定点小数除法：被除数放在高位，低位补 0'
F = Fig(780, 320, '定点小数：被除数在高 4 位')
ry = datapath(F, '除数 Y（4 bit）', '被除数 X（4 bit）', '0 0 0 0', '4 位 ALU', 4, '加 / 减', 150, left_tone='blue', right_tone='white', shift='左移')
F.box(30, ry + 70, 170, 26, '小数点隐含在高位前', 'red', 11.5, 5)
