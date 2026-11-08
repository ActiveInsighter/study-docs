from common import gate
LABEL = '取指周期 T0 节拍一定是 (PC)→MAR：C1 = FE·T0'
F = Fig(480, 220, '取指周期 T₀：(PC) → MAR，C₁ = FE · T₀')
ins, out = gate(F, 200, 80, 'and', 2, w=60, pitch=26)
F.line(360, ins[0][1], 262, ins[0][1], ACCENT['violet'], 1.6, arrow='end'); F.text(366, ins[0][1], 'FE', 15, 'start', ACCENT['violet'], 700, valign='middle')
F.line(360, ins[1][1], 262, ins[1][1], ACCENT['amber'], 1.6, arrow='end'); F.text(366, ins[1][1], 'T₀', 15, 'start', ACCENT['amber'], 700, valign='middle')
F.line(198, out[1], 110, out[1], ACCENT['red'], 1.6, arrow='end'); F.text(100, out[1], 'C₁', 16, 'end', ACCENT['red'], 700, valign='middle')
F.text(240, 200, '所有指令的取指周期 T₀ 都执行 (PC) → MAR，与操作码无关', 12, color=MUTED)
