from common import datapath5
LABEL = '条件转移指令：M 段把目标 PC 写回 PC，WB 为空段'
F = Fig(720, 340)
datapath5(F, idle=(4,), wrpc=3)
