from common import aoe, CRIT
LABEL = 'AOE 网：求活动的最早开始时间 e、最迟开始时间 l 与时间余量'
F = Fig(640, 490, '求活动 a_{i} 的 e(i)、l(i) 与 d(i) = l(i) − e(i)')
aoe(F, 80, 80, CRIT)
F.legend(80, 300, [('red', 'd(i) = 0 的活动即关键活动：a₂、a₅、a₇')])
rows = [['活动', 'a₁', 'a₂', 'a₃', 'a₄', 'a₅', 'a₆', 'a₇', 'a₈'],
        ['e(i) = ve(起点)', '0', '0', '3', '3', '2', '2', '6', '6'],
        ['l(i) = vl(终点) − 权', '1', '0', '4', '4', '2', '5', '6', '7'],
        ['d(i) = l − e', '1', '0', '1', '1', '0', '3', '0', '1']]
tones = {(r, c): 'red' for r in (1, 2, 3) for c in (2, 5, 7)}
F.table(30, 322, rows, [180] + [50] * 8, 34, tones=tones, mono_cols=range(1, 9), align=['start'] + ['middle'] * 8)
F.text(30, 474, '先求各事件的 ve、vl，再由活动 ⟨v_{j}, v_{k}⟩ 得 e(i) = ve(j)，l(i) = vl(k) − 权值', 12.5, 'start', MUTED)
