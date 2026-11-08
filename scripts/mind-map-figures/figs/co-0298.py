from common import tlb_part, cache_part
LABEL = 'TLB + Cache 的多级存储系统全图'
F = Fig(1100, 500, 'TLB + Cache 的多级存储系统')
tlb_part(F, 0, 40)
cache_part(F, 500, 0)
F.poly([(400, 410), (460, 410), (460, 466), (680, 466)], ACCENT['blue'], 1.6, arrow='end', dash='5 4')
