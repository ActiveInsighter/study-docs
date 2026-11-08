from svgkit import *
MST_N = {'V1': (150, 40), 'V2': (60, 104), 'V3': (150, 112), 'V4': (240, 104), 'V5': (90, 192), 'V6': (210, 192)}
MST_E = [('V1','V2','6'), ('V1','V3','1'), ('V1','V4','5'), ('V2','V3','5'), ('V3','V4','5'), ('V2','V5','3'), ('V3','V5','6'), ('V3','V6','4'), ('V4','V6','2'), ('V5','V6','6')]
def mst_panel(F, ox, oy, edges, cap, s=0.8, full=False):
    N = {k: (ox + x * s, oy + y * s) for k, (x, y) in MST_N.items()}
    if full:
        E = [(a, b, w) for a, b, w in MST_E]
        hl = set()
    else:
        E = [(a, b, w) for a, b, w in MST_E if (a, b) in edges]
        hl = {(a, b) for a, b in edges if edges[(a, b)] == 'new'}
    F.graph(N, E, r=14, directed=False, size=11, esize=11, hl=hl, hl_color='red', labels={k: k for k in N})
    F.text(ox + 150 * s, oy + 228 * s, cap, 12, color=INK2)
def adj_matrix(F, x, y, names, M, cw=28, ch=26, size=12, hl=None):
    rows = [[''] + names] + [[n] + r for n, r in zip(names, M)]
    tones = {}
    for (r, c) in (hl or []): tones[(r + 1, c + 1)] = 'amber'
    F.table(x, y, rows, [cw + 6] + [cw] * len(names), ch, size=size, mono_cols=range(1, len(names) + 1), tones=tones, head_tone='gray', zebra=False)
