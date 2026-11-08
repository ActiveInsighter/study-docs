from common import aoe, CRIT
LABEL = 'AOE 网：求事件的最早发生时间 ve 与最迟发生时间 vl'
F = Fig(640, 470, '求事件 v_{i} 的 ve(i) 与 vl(i)')
aoe(F, 80, 80, CRIT)
F.legend(80, 300, [('red', '关键路径 v₁→v₃→v₄→v₆（长度 8）')])
rows = [['事件', 'v₁', 'v₂', 'v₃', 'v₄', 'v₅', 'v₆'],
        ['ve(i)  拓扑正序取 max', '0', '3', '2', '6', '6', '8'],
        ['vl(i)  逆拓扑序取 min', '0', '4', '2', '6', '7', '8']]
crit_cols = [1, 3, 4, 6]
tones = {(r, c): 'red' for r in (1, 2) for c in crit_cols}
F.table(40, 322, rows, [200] + [60] * 6, 34, tones=tones, mono_cols=range(1, 7), align=['start'] + ['middle'] * 6)
F.text(40, 450, 've(4) = max{ve(2)+2, ve(3)+4} = 6：v₄ 要等所有前驱活动都完成；ve = vl 的事件在关键路径上', 12.5, 'start', MUTED)
