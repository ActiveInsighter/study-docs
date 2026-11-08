from common import datapath5
LABEL = '无条件转移指令：EX 段写回 PC，M、WB 为空段'
F = Fig(720, 340)
datapath5(F, idle=(3, 4), wrpc=2)
