from svgkit import *

def aoe(F, ox, oy, hl=(), s=1.0):
    P = {'v1': (0, 95), 'v2': (120, 20), 'v3': (120, 170), 'v4': (240, 95), 'v5': (360, 20), 'v6': (480, 95)}
    nodes = {k: (ox + x * s, oy + y * s) for k, (x, y) in P.items()}
    E = [('v1','v2','a₁=3'), ('v1','v3','a₂=2',{'side':-1}), ('v2','v5','a₄=3'), ('v2','v4','a₃=2'),
         ('v3','v4','a₅=4',{'side':-1}), ('v3','v6','a₆=3',{'side':-1}), ('v4','v6','a₇=2'), ('v5','v6','a₈=1')]
    labels = {k: 'v' + k[1] for k in P}
    F.graph(nodes, E, r=19, hl=hl, labels={k: f'v_{{{k[1]}}}' for k in P},
            tones={k: ('red' if any(k in e for e in hl) else 'white') for k in P}, size=15)
    return nodes

CRIT = {('v1','v3'), ('v3','v4'), ('v4','v6')}

def record(F, x, y, fields, cw=34, ch=30, tones=None, size=14, ptr_dot=True):
    """Pointer record like [● | A | ^]. '●' draws a dot, '^' a null mark. Returns centres."""
    tones = tones or {}
    cs = []
    for i, v in enumerate(fields):
        cx = x + i * cw
        t = tones.get(i, 'white')
        F.rect(cx, y, cw, ch, TONES[t][0], 'none', 0, 0)
    F.rect(x, y, cw * len(fields), ch, 'none', INK2, 1.4, 4)
    for i in range(1, len(fields)):
        F.line(x + i * cw, y, x + i * cw, y + ch, INK2, 1)
    for i, v in enumerate(fields):
        cx, cy = x + i * cw + cw / 2, y + ch / 2
        if v == '●':
            F.circle(cx, cy, 3.6, '', 'dark', sw=0)
        elif v == '^':
            F.text(cx, cy, '∧', size - 1, color=LINE, valign='middle')
        else:
            F.text(cx, cy, v, size, color=TONES[tones.get(i, 'white')][2], valign='middle', weight=500)
        cs.append((cx, cy))
    return cs

def bnode(F, cx, y, keys, slots=None, kw=32, h=30, tone='blue', size=13, empty_tone='light'):
    """B-tree node centred at cx: key cells; returns child pointer anchors (len(keys)+1) on bottom edge."""
    slots = slots or len(keys)
    W = slots * kw
    x = cx - W / 2
    F.rect(x - 4, y - 4, W + 8, h + 8, '#fafafa', '#a1a1aa', 1.2, 8)
    for i in range(slots):
        if i < len(keys):
            F.box(x + i * kw + 2, y, kw - 4, h, keys[i], tone, size, 5, mono=True)
        else:
            F.rect(x + i * kw + 2, y, kw - 4, h, '#ffffff', '#d4d4d8', 1, 5, dash='3 3')
    anchors = []
    for i in range(slots + 1):
        ax = x + i * kw
        ax = min(max(ax, x + 1), x + W - 1)
        anchors.append((ax, y + h + 4))
    for i in range(len(keys) + 1):
        F.circle(anchors[i][0], anchors[i][1], 3.2, '', 'dark', sw=0)
    return anchors

def code(F, x, y, src, size=13, lh=1.45, color=INK2, comment='#8b8b94'):
    """Monospace code block; '//' comments are greyed."""
    for i, l in enumerate(src.split('\n')):
        yy = y + i * size * lh
        if '//' in l:
            a, b = l.split('//', 1)
            F.text(x, yy, a.rstrip() and a, size, 'start', color, mono=True)
            F.text(x + len(a) * size * 0.6, yy, '//' + b, size, 'start', comment, mono=True)
        else:
            F.text(x, yy, l, size, 'start', color, mono=True)

def bnode2(F, cx, y, keys, slots=4, kw=30, h=28, size=13, minline=None, hl=None, tone='blue'):
    """keys: '!k' accent red, '~k' ghost (removed). hl: 'red'|'green' dashed outline."""
    n = max(slots, len(keys))
    W = n * kw
    x = cx - W / 2
    if hl:
        F.rect(x - 9, y - 9, W + 18, h + 18, 'none', ACCENT[hl], 1.4, 11, dash='5 4')
    F.rect(x - 4, y - 4, W + 8, h + 8, '#f4f4f5', '#a1a1aa', 1.2, 8)
    for i in range(n):
        if i < len(keys):
            k = keys[i]
            if k.startswith('!'):
                F.box(x + i * kw + 2, y, kw - 4, h, k[1:], 'red', size, 5, mono=True, weight=700)
            elif k.startswith('~'):
                F.box(x + i * kw + 2, y, kw - 4, h, k[1:], 'white', size, 5, mono=True, dash='3 3', color=LINE)
            else:
                F.box(x + i * kw + 2, y, kw - 4, h, k, tone, size, 5, mono=True)
    if minline:
        lx = x + minline * kw
        F.line(lx, y - 2, lx, y + h + 2, ACCENT['green'], 1.4, dash='2 3')
    anchors = [(x + i * kw, y + h + 4) for i in range(n + 1)]
    anchors[0] = (x + 3, anchors[0][1]); anchors[-1] = (x + W - 3, anchors[-1][1])
    real = len([k for k in keys if not k.startswith('~')]) if keys else 0
    for i in range(len(keys) + 1 if keys else 1):
        F.circle(anchors[i][0], anchors[i][1], 2.8, '', 'dark', sw=0)
    return anchors

def btree(F, root, x0, y0, unit=140, dy=90, minline=2, slots=4, kw=30, stub=False):
    """root = (keys, [children], opts). Leaves are evenly spaced by `unit` from x0."""
    cnt = [0]
    def lay(n, d):
        keys, kids = n[0], n[1] if len(n) > 1 else []
        o = n[2] if len(n) > 2 else {}
        if kids:
            cs = [lay(k, d + 1) for k in kids]
            cx = (cs[0][0] + cs[-1][0]) / 2 + o.get('dx', 0)
        else:
            cx = x0 + cnt[0] * unit + unit / 2
            cnt[0] += 1
            cs = []
        y = y0 + d * dy
        a = bnode2(F, cx, y, keys, slots, kw, minline=minline, hl=o.get('hl'))
        for i, (ccx, cy) in enumerate(cs):
            pi = o.get('ptr', list(range(len(cs))))[i]
            F.line(a[pi][0], a[pi][1], ccx, cy - 5, INK2, 1.3, arrow='end')
        return (cx, y)
    cx, y = lay(root, 0)
    if stub:
        F.line(cx + 30, y - 46, cx + 10, y - 7, INK2, 1.3, arrow='end')
    return cx

def bt_legend(F, x, y, extra=()):
    F.line(x, y - 9, x, y + 5, ACCENT['green'], 1.4, dash='2 3')
    F.text(x + 10, y + 1, '下限 ⌈m/2⌉−1 = 2（m = 5）', 13, 'start', INK2)
    xx = x + 200
    for tone, lab in extra:
        if tone == 'hl':
            F.rect(xx, y - 10, 18, 14, 'none', ACCENT['red'], 1.3, 4, dash='4 3')
        else:
            F.rect(xx, y - 10, 14, 14, TONES[tone][0], TONES[tone][1], 1.3, 3)
        F.text(xx + 24, y + 1, lab, 13, 'start', INK2)
        xx += 34 + text_width(lab, 13) + 16

def chain(F, x, y, nodes, cw=30, ch=28, gap=26, data_tone='amber', tail='NULL', size=13, head=None):
    """Singly linked chain; nodes = list of lists of data cells. Returns end x."""
    if head:
        F.text(x - 8, y + ch / 2, head, 13, 'end', INK2, mono=True, valign='middle')
        F.line(x - 4, y + ch / 2, x + gap - 4, y + ch / 2, INK2, 1.3, arrow='end')
        x += gap
    for i, cells in enumerate(nodes):
        n = len(cells)
        for j, v in enumerate(cells):
            t = 'white' if v in ('', '#') else data_tone
            F.rect(x + j * cw, y, cw, ch, TONES[t][0], 'none', 0, 0)
            F.text(x + j * cw + cw / 2, y + ch / 2, v, size, color=TONES[t][2], mono=True, valign='middle')
        pw = 14
        F.rect(x + n * cw, y, pw, ch, '#f4f4f5', 'none', 0, 0)
        F.rect(x, y, n * cw + pw, ch, 'none', INK2, 1.3, 4)
        for j in range(1, n + 1):
            F.line(x + j * cw, y, x + j * cw, y + ch, INK2, 1)
        px = x + n * cw + pw / 2
        F.circle(px, y + ch / 2, 2.6, '', 'dark', sw=0)
        nx = x + n * cw + pw + gap
        F.line(px, y + ch / 2, nx - 2, y + ch / 2, INK2, 1.3, arrow='end')
        x = nx
    if tail:
        F.text(x + 2, y + ch / 2, tail, 12, 'start', MUTED, mono=True, valign='middle')
    return x

def count_slots(n):
    if n is None or isinstance(n, str):
        return 1
    return sum(count_slots(k) for k in n[1])

def merge_tree(F, x, y, tree, unit=56, levelh=72, r=20, root_tone='red'):
    if x is None:
        x = (F.w - count_slots(tree) * unit) / 2
    tones = {}
    def walk(n, d):
        if isinstance(n, str):
            tones[n] = 'green'; return
        tones[n[0]] = root_tone if d == 0 else 'blue'
        for k in n[1]: walk(k, d + 1)
    walk(tree, 0)
    return F.tree(x, y, tree, unit=unit, levelh=levelh, r=r, tones=tones, size=14)

RUNS8 = [['27', '30', '46'], ['12', '36', '40'], ['1', '6', '7'], ['17', '22', '27'], ['2', '3', '88'], ['9', '15', '19'], ['11', '13', '53'], ['4', '31', '77']]

def loser_tree(F, ox, oy, inner=None, champ='', winners=None, leaves=None, runs=RUNS8, W=760, hl_nodes=(), hl_path=(), leaf_tone='green', note_runs=True):
    """8-way loser tree. inner: {1..7: label}; winners: {node: red label}; leaves: 8 head values."""
    inner = inner or {}
    winners = winners or {}
    unit = W / 8
    pos = {}
    for i in range(8):
        pos[8 + i] = (ox + unit * i + unit / 2, oy + 4 * 62)
    for lvl, ids in ((3, range(4, 8)), (2, range(2, 4)), (1, range(1, 2))):
        for n in ids:
            pos[n] = ((pos[2 * n][0] + pos[2 * n + 1][0]) / 2, oy + lvl * 62)
    pos[0] = (pos[1][0], oy)
    for n in range(1, 16):
        if n >= 2:
            p = n // 2
            hot = (n, p) in hl_path
            F.line(pos[n][0], pos[n][1], pos[p][0], pos[p][1], ACCENT['red'] if hot else INK2, 2.2 if hot else 1.4, gap=16, gap2=16)
    F.line(pos[1][0], pos[1][1], pos[0][0], pos[0][1], INK2, 1.4, gap=16, gap2=16)
    for n in range(1, 8):
        x, y = pos[n]
        F.circle(x, y, 16, inner.get(n, ''), 'dark', 13, weight=600, mono=True)
        if n in hl_nodes:
            F.circle(x, y, 21, '', 'none', sw=1.5)
            F.items[-1] = F.items[-1].replace('stroke="none"', f'stroke="{ACCENT["red"]}"')
        if n in winners:
            F.text(x + 22, y - 12, winners[n], 12.5, 'start', ACCENT['red'], 700, mono=True)
    F.circle(*pos[0], 16, champ, 'blue', 13, weight=700, mono=True)
    if 1 in winners:
        pass
    for i in range(8):
        x, y = pos[8 + i]
        lv = leaves[i] if leaves else runs[i][0]
        F.circle(x, y, 16, lv, leaf_tone, 13, mono=True, weight=600)
        rest = runs[i][1:] if leaves is None else runs[i][len(runs[i]) - 2:]
        F.rect(x - 17, y + 26, 34, 14 + 22 * len(rest), '#fafafa', '#a1a1aa', 1.2, 6)
        for j, v in enumerate(rest):
            F.text(x, y + 44 + j * 22, v, 13, color=INK2, mono=True)
        F.text(x, y + 56 + 22 * len(rest), f'R{i + 1}', 12, color=MUTED, weight=600)
    return pos

def disk_blocks(F, x, y, rows, cw=26, ch=24, gap=8, tones=None, group=3, rgap=8):
    """rows: list of lists of blocks (each block a list of values)."""
    tones = tones or {}
    for r, row in enumerate(rows):
        cx = x
        for b, blk in enumerate(row):
            t = tones.get((r, b), 'violet')
            F.cells(cx, y + r * (ch + rgap), blk, cw, ch, {i: t for i in range(len(blk))}, size=12, rx=4)
            cx += len(blk) * cw + gap

def trace(F, x, y, rows, cw=44, ch=30, lw=86, gap=10, size=13, mono=True):
    """rows: [(label, values, tones{idx:tone}, extra)] ; '_' = hole (dashed)."""
    for r, row in enumerate(rows):
        lab, vals = row[0], row[1]
        tones = row[2] if len(row) > 2 else {}
        yy = y + r * (ch + gap)
        F.text(x + lw - 12, yy + ch / 2, lab, 12.5, 'end', INK2, 500, valign='middle')
        shown = ['' if v == '_' else v for v in vals]
        F.cells(x + lw, yy, shown, cw, ch, tones, size=size, mono=mono)
        for i, v in enumerate(vals):
            if v == '_':
                F.rect(x + lw + i * cw + 4, yy + 4, cw - 8, ch - 8, 'none', LINE, 1, 4, dash='3 3')
    return y + len(rows) * (ch + gap)

def groups_row(F, x, y, groups, cw=40, ch=30, ggap=14, tone='white', size=13):
    cx = x
    for g in groups:
        F.cells(cx, y, g, cw, ch, {i: tone for i in range(len(g))}, size=size, rx=5)
        cx += len(g) * cw + ggap

def heap_tree(F, x, y, arr, unit=40, levelh=50, r=15, tones=None, size=12, cut=0):
    """Complete binary tree from array (1-based semantics). cut: last `cut` items drawn ghosted."""
    n = len(arr)
    def build(i):
        if i > n:
            return None
        l, rr = build(2 * i), build(2 * i + 1)
        key = f'{arr[i - 1]}#{i}'
        if l is None and rr is None:
            return key
        return (key, [l, rr] if rr is not None else [l, None])
    tones = tones or {}
    tk = {f'{arr[i - 1]}#{i}': t for i, t in tones.items()}
    return F.tree(x, y, build(1), unit=unit, levelh=levelh, r=r, size=size, tones=tk, mono=True)

def bp_node(F, x, y, keys, tone='green', kw=26, h=24, size=12):
    """B+ tree node: contiguous key cells. Returns (x, y, w, h) and centres."""
    cs = F.cells(x, y, keys, kw, h, {i: tone for i in range(len(keys))}, size=size, rx=3)
    return cs

def records(F, cx, y, n=1, w=18, h=34):
    F.line(cx, y, cx, y + 12, INK2, 1.1, arrow='end')
    F.rect(cx - w / 2, y + 14, w, h, '#fafafa', '#a1a1aa', 1, 3)
    F.text(cx, y + 14 + h / 2, '记\n录', 9.5, color=MUTED, valign='middle', lh=1.15)

def rb(F, x, y, t, unit=44, levelh=58, r=16, nil=True, size=13, labels=None):
    """t = (key, 'R'|'B', left, right) or None. Draws NIL leaves as small boxes when nil=True."""
    tones = {}
    cnt = [0]
    def conv(n):
        if n is None:
            cnt[0] += 1
            return f'□NIL#{cnt[0]}' if nil else None
        k, c, l, rr = n
        key = str(k)
        tones[key] = 'rbred' if c == 'R' else 'rbblack'
        kids = [conv(l), conv(rr)]
        if all(kk is None for kk in kids):
            return key
        return (key, kids)
    pos = F.tree(x, y, conv(t), unit=unit, levelh=levelh, r=r, size=size, tones=tones, mono=True)
    return pos

def subtree(F, cx, y, label, h='H', tone='gray', w=40, hh=34, hot=False):
    """Triangle-ish subtree box with height label below."""
    t = 'red' if hot else tone
    F.items.append(f'<path d="M{cx} {y}L{cx + w / 2} {y + hh}H{cx - w / 2}Z" fill="{TONES[t][0]}" stroke="{TONES[t][1]}" stroke-width="1.3" stroke-linejoin="round"/>')
    F.text(cx, y + hh - 9, label, 11.5, color=TONES[t][2], weight=600)
    F.text(cx, y + hh + 15, h, 11.5, color=ACCENT['red'] if hot else MUTED, mono=True)

def avl_node(F, x, y, k, bf=None, tone='blue'):
    F.circle(x, y, 16, k, tone, 14, weight=600)
    if bf is not None:
        F.text(x + 22, y - 10, bf, 12, 'start', ACCENT['red'] if bf in ('2', '-2') else MUTED, 700, mono=True)

def edge(F, a, b, r1=16, r2=0):
    F.line(a[0], a[1], b[0], b[1], INK2, 1.4, gap=r1, gap2=r2)

def sysbus(F, hl_paths=(), notes=None):
    """Bus-structured computer: CPU, IO bridge, memory, IO bus with USB/display/disk controllers.
    hl_paths: list of (tone, [points]) polylines to highlight data flow."""
    F.rect(24, 64, 300, 140, 'none', ACCENT['blue'], 1.3, 12, dash='5 4')
    F.pill(36, 54, 'CPU', 'blue', 11.5)
    F.box(40, 84, 70, 26, '控制器', 'white', 12, 5)
    F.box(120, 80, 70, 56, '寄存器组', 'gray', 12, 5)
    F.items.append('<path d="M226 80L262 94V128L226 142L226 120L236 111L226 102Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>')
    F.text(246, 112, 'ALU', 11, color='#7f1d1d', weight=700, valign='middle')
    F.box(40, 160, 110, 28, '总线接口', 'white', 12, 5)
    F.box(380, 140, 90, 44, 'I/O 桥接器', 'gray', 12, 6)
    F.box(600, 140, 100, 44, '主存储器', 'green', 13, 6)
    F.line(150, 174, 378, 162, INK2, 2, arrow='both'); F.text(260, 158, '处理器总线', 11, color=MUTED, halo=True)
    F.line(470, 162, 598, 162, INK2, 2, arrow='both'); F.text(534, 152, '存储器总线', 11, color=MUTED, halo=True)
    F.rect(40, 236, 640, 12, '#e4e4e7', '#71717a', 1.2, 6); F.text(50, 228, 'I/O 总线', 11.5, 'start', MUTED)
    F.line(425, 184, 425, 234, INK2, 2, arrow='both')
    for x, lab in ((130, 'USB\n控制器'), (330, '显示\n适配卡'), (560, '磁盘\n控制器')):
        F.line(x, 248, x, 278, INK2, 1.6, arrow='end')
        F.box(x - 42, 280, 84, 44, lab, 'white', 12, 6)
    F.text(105, 364, '鼠标', 12, color=INK2); F.text(155, 364, '键盘', 12, color=INK2)
    F.line(105, 350, 105, 326, INK2, 1.3, arrow='end'); F.line(155, 350, 155, 326, INK2, 1.3, arrow='end')
    F.line(330, 324, 330, 350, INK2, 1.3, arrow='end'); F.text(330, 364, '显示器', 12, color=INK2)
    F.line(560, 324, 560, 344, INK2, 1.3, arrow='both')
    F.ellipse(560, 350, 26, 7, '', 'white'); F.rect(534, 350, 52, 18, '#fff', 'none', 0, 0)
    F.path('M534 350V368M586 350V368', INK2, 1.3); F.ellipse(560, 368, 26, 7, '', 'white'); F.text(560, 388, '磁盘', 12, color=INK2)
    for tone, pts in hl_paths:
        F.poly(pts, ACCENT[tone], 2.4, arrow='end')

GATE_SYM = {'and': '&', 'or': '≥1', 'xor': '=1', 'not': '1', 'nand': '&', 'nor': '≥1', 'xnor': '=', 'buf': '1'}

def gate(F, x, y, kind, n=2, w=34, label=None, tone='white', pitch=14):
    """IEC-style gate box at top-left (x, y). Returns (inputs[], output)."""
    h = max(28, pitch * (n + 1))
    F.box(x, y, w, h, GATE_SYM.get(kind, kind) if label is None else label, tone, 12.5, 3, weight=600)
    ins = [(x, y + h * (i + 1) / (n + 1)) for i in range(n)]
    neg = kind in ('nand', 'nor', 'not', 'xnor') and kind != 'xnor'
    out = (x + w + (7 if neg else 0), y + h / 2)
    if neg:
        F.circle(x + w + 3.5, y + h / 2, 3.5, '', 'white', sw=1.3)
    return ins, out

def wire(F, pts, color=INK2, sw=1.3, dot=None, arrow=None):
    F.poly(pts, color, sw, arrow=arrow, r=0.01)
    for p in (dot or []):
        F.circle(p[0], p[1], 2.6, '', 'dark', sw=0)

def bitfield(F, x, y, cells, widths, tones=None, size=14, h=40, mono=False):
    tones = tones or {}
    cx = x
    pos = []
    for i, (c, w) in enumerate(zip(cells, widths)):
        F.box(cx, y, w, h, c, tones.get(i, 'white'), size, 0, mono)
        pos.append((cx, cx + w))
        cx += w
    return pos

def block(F, x, y, w, h, label, tone='blue', size=14, top=None, bottoms=(), left=None, right=None, lsize=13, L=30):
    """Block with labelled signal arrows: top = output up, bottoms = inputs from below, left = output to the left, right = input from the right."""
    F.box(x, y, w, h, label, tone, size, 8, weight=600)
    if top:
        F.line(x + w / 2, y, x + w / 2, y - L, INK2, 1.4, arrow='end'); F.text(x + w / 2, y - L - 8, top, lsize, color=INK, valign='middle')
    n = len(bottoms)
    for i, b in enumerate(bottoms):
        bx = x + w * (i + 1) / (n + 1)
        F.line(bx, y + h + L, bx, y + h, INK2, 1.4, arrow='end'); F.text(bx, y + h + L + 12, b, lsize, color=INK, valign='middle')
    if left:
        F.line(x, y + h / 2, x - L, y + h / 2, INK2, 1.4, arrow='end'); F.text(x - L - 6, y + h / 2, left, lsize, 'end', INK, valign='middle')
    if right:
        F.line(x + w + L, y + h / 2, x + w, y + h / 2, INK2, 1.4, arrow='end'); F.text(x + w + L + 6, y + h / 2, right, lsize, 'start', INK, valign='middle')

def alu_shape(F, cx, top, w=220, h=90, label='加法器', tone='red', size=16, vertical=False):
    """ALU/adder trapezoid with notch; inputs enter at bottom. Returns dict of anchor points."""
    f, s, t = TONES[tone]
    x0, x1 = cx - w / 2, cx + w / 2
    k = w * 0.2
    d = (f'M{x0 + k} {top}H{x1 - k}L{x1} {top + h}H{cx + w * 0.16}L{cx} {top + h - h * 0.35}L{cx - w * 0.16} {top + h}H{x0}Z')
    F.items.append(f'<path d="{d}" fill="{f}" stroke="{s}" stroke-width="1.5" stroke-linejoin="round"/>')
    F.text(cx, top + h * 0.42, label, size, color=t, weight=700, valign='middle')
    return {'A': (cx - w * 0.3, top + h), 'B': (cx + w * 0.3, top + h), 'left': (x0 + k / 2, top + h / 2), 'right': (x1 - k / 2, top + h / 2), 'top': (cx, top)}

def bus_slash(F, x, y, label='n', vertical=True):
    if vertical:
        F.line(x - 6, y + 6, x + 6, y - 6, INK2, 1.3); F.text(x + 9, y + 9, label, 11, 'start', INK2)
    else:
        F.line(x - 6, y + 6, x + 6, y - 6, INK2, 1.3); F.text(x + 2, y - 10, label, 11, 'middle', INK2)

def mux_shape(F, x, y, w, h, label='MUX', tone='blue', size=14, vertical=False):
    """Horizontal MUX: wide bottom (inputs), narrow top (output) when vertical=False means inputs bottom."""
    f, s, t = TONES[tone]
    if not vertical:
        k = w * 0.14
        F.items.append(f'<path d="M{x + k} {y}H{x + w - k}L{x + w} {y + h}H{x}Z" fill="{f}" stroke="{s}" stroke-width="1.5" stroke-linejoin="round"/>')
        F.text(x + w / 2, y + h / 2, label, size, color=t, weight=700, valign='middle')
    else:
        k = h * 0.16
        F.items.append(f'<path d="M{x} {y}L{x + w} {y + k}V{y + h - k}L{x} {y + h}Z" fill="{f}" stroke="{s}" stroke-width="1.5" stroke-linejoin="round"/>')
        F.text(x + w / 2, y + h / 2, label, size, color=t, weight=700, valign='middle', rotate=90)

def datapath(F, top_reg, left_reg, right_reg, alu='32 位 ALU', w=32, op='加', reg_w=150, y0=60, left_tone='amber', right_tone='amber', shift='右移', note=None):
    """Shared multiplier/divider datapath: top register, ALU, 2w-bit register pair, control counter."""
    F.box(150, y0, 170, 30, top_reg, 'blue', 12.5, 5)
    ax = 120
    F.items.append(f'<path d="M{ax} {y0 + 70}H{ax + 160}L{ax + 144} {y0 + 110}H{ax + 120}L{ax + 80} {y0 + 92}L{ax + 40} {y0 + 110}H{ax + 16}Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.4"/>')
    F.text(ax + 80, y0 + 84, alu, 12, color='#7f1d1d', weight=700, valign='middle')
    F.line(ax + 120, y0 + 32, ax + 120, y0 + 68, INK2, 1.3, arrow='end'); F.text(ax + 128, y0 + 50, str(w), 11, 'start', INK2)
    F.line(ax + 80, y0 + 110, ax + 80, y0 + 154, INK2, 1.3, arrow='end'); F.text(ax + 88, y0 + 136, str(w), 11, 'start', INK2)
    ry = y0 + 156
    F.box(100, ry, reg_w, 30, left_reg, left_tone, 12.5, 0); F.box(100 + reg_w, ry, reg_w, 30, right_reg, right_tone, 12.5, 0)
    F.text(100 + reg_w, ry - 10, f'{2 * w} 位', 11, color=MUTED)
    F.poly([(130, ry + 32), (130, ry + 60), (60, ry + 60), (60, y0 + 56), (ax + 40, y0 + 56), (ax + 40, y0 + 68)], INK2, 1.2, arrow='end')
    cx = 100 + 2 * reg_w + 110
    F.ellipse(cx, ry + 15, 74, 30, '控制逻辑\n计数器 C_{n}', 'violet', 12)
    F.line(cx - 74, ry + 8, 100 + 2 * reg_w + 2, ry + 8, INK2, 1.2, dash='4 3', arrow='end'); F.text(cx - 54, ry - 2, shift, 11, color=INK2)
    F.line(cx - 74, ry + 22, 100 + 2 * reg_w + 2, ry + 22, INK2, 1.2, dash='4 3', arrow='end'); F.text(cx - 54, ry + 40, '写使能', 11, color=INK2)
    F.poly([(cx, ry - 15), (cx, y0 + 90), (ax + 154, y0 + 90)], INK2, 1.2, dash='4 3', arrow='end'); F.text(ax + 200, y0 + 82, op, 11, color=INK2)
    F.line(cx, ry + 80, cx, ry + 46, INK2, 1.2, arrow='end'); F.text(cx + 8, ry + 78, '时钟', 11, 'start', INK2)
    return ry

ADDR_C, CTRL_C, DATA_C = '#d1493a', '#c98a12', '#2f8f57'

def cpu_box(F, x=30, y=60, w=86, h=300, pins=()):
    """pins: [(label, y, color)] drawn on the right edge."""
    F.box(x, y, w, h, '', 'white', rx=6)
    F.text(x + w / 2 - 14, y + h / 2, 'CPU', 14, color=INK, weight=700, valign='middle')
    for lab, py, col in pins:
        F.text(x + w - 6, py, lab, 11.5, 'end', col, valign='middle')
    return x + w

def chip(F, x, y, label, num=None, w=118, h=84, cs='CS̄', data='D₀', data_col=DATA_C):
    F.box(x, y, w, h, label, 'blue', 12.5, 4, weight=600)
    F.text(x + 6, y + 16, 'A₁₂~A₀', 10.5, 'start', ADDR_C, valign='middle')
    F.text(x + w - 34, y + 14, cs, 10.5, 'middle', CTRL_C, valign='middle')
    F.text(x + 6, y + h - 12, 'WĒ', 10.5, 'start', CTRL_C, valign='middle')
    F.text(x + w - 6, y + h - 12, data, 10.5, 'end', data_col, valign='middle')
    if num is not None:
        F.text(x + w - 6, y + 34, str(num), 11, 'end', MUTED, valign='middle')
    return {'addr': (x, y + 16), 'cs': (x + w - 34, y), 'we': (x + 24, y + h), 'data': (x + w - 18, y + h)}

def tlb_part(F, ox=0, oy=0):
    X = lambda x: x + ox
    Y = lambda y: y + oy
    F.box(X(160), Y(60), 100, 30, 'CPU', 'violet', 13, 5)
    F.text(X(40), Y(110), '虚拟地址', 12, 'start', INK2)
    F.box(X(60), Y(116), 180, 30, '虚页号（20 位）', 'amber', 12, 0); F.box(X(240), Y(116), 130, 30, '页内地址（12 位）', 'gray', 12, 0)
    F.line(X(210), Y(92), X(210), Y(114), INK2, 1.3, arrow='end')
    F.rect(X(40), Y(166), 320, 140, 'none', INK2, 1.2, 8, dash='5 4'); F.text(X(50), Y(184), 'TLB', 12.5, 'start', INK, 700)
    F.table(X(140), Y(190), [['Tag', '有效位', '实页号'], ['0008CH', '1', '0040H'], ['', '', ''], ['⋮', '⋮', '⋮']], [80, 60, 80], 26, size=11.5, head_tone='gray', tones={(1, 0): 'blue', (1, 1): 'blue', (1, 2): 'blue'}, zebra=False)
    for i in range(3):
        F.circle(X(112), Y(229 + i * 26), 8, '=', 'white', 11)
    F.text(X(112), Y(298), '比较器', 11, color=MUTED)
    F.poly([(X(80), Y(146)), (X(80), Y(229)), (X(102), Y(229))], INK2, 1.2, arrow='end')
    F.text(X(42), Y(330), 'TLB 缺失', 11.5, 'start', ACCENT['red'])
    F.poly([(X(80), Y(229)), (X(80), Y(342))], ACCENT['red'], 1.2, arrow='end')
    F.cells(X(40), Y(344), ['10 位', '10 位'], 60, 26, size=11.5, mono=False); F.text(X(70), Y(386), '查页表', 11, color=ACCENT['red'])
    F.text(X(270), Y(330), '物理地址', 12, 'middle', INK2)
    F.box(X(180), Y(344), 160, 26, '实页号', 'blue', 12, 0); F.box(X(340), Y(344), 120, 26, '页内地址（12 位）', 'gray', 11.5, 0)
    F.line(X(300), Y(296), X(300), Y(342), INK2, 1.3, arrow='end')
    F.poly([(X(320), Y(146)), (X(400), Y(146)), (X(400), Y(342))], INK2, 1.3, arrow='end')

def cache_part(F, ox=0, oy=0):
    X = lambda x: x + ox
    Y = lambda y: y + oy
    F.box(X(240), Y(60), 90, 28, 'CPU', 'violet', 12.5, 5); F.box(X(240), Y(104), 90, 28, '数据', 'white', 12, 5)
    F.line(X(285), Y(104), X(285), Y(90), INK2, 1.2, arrow='end')
    F.rect(X(30), Y(150), 520, 210, 'none', INK2, 1.2, 8, dash='5 4'); F.text(X(42), Y(168), 'Cache（2 路组相联）', 12, 'start', INK, 700)
    F.items.append(f'<path d="M{X(230)} {Y(172)}H{X(340)}L{X(325)} {Y(190)}H{X(245)}Z" fill="#f4f4f5" stroke="#52525b" stroke-width="1.2"/>')
    F.text(X(285), Y(181), '多路选择', 11, color=INK, valign='middle'); F.line(X(285), Y(172), X(285), Y(134), INK2, 1.2, arrow='end')
    for k, x0 in enumerate((60, 310)):
        cols = [('有效位', 40), ('Tag', 80), ('Data', 100)] if k == 0 else [('Data', 100), ('Tag', 80), ('有效位', 40)]
        rows = [[c for c, _ in cols], ['1', '00400H', ''] if k == 0 else ['', '', ''], ['⋮', '⋮', '⋮']]
        F.table(X(x0), Y(250), rows, [w for _, w in cols], 26, size=11, head_tone='gray', tones={(1, i): 'blue' for i in range(3)}, zebra=False)
        cx = X(x0 + (100 if k == 0 else 120))
        F.circle(cx, Y(224), 8, '=', 'white', 11); F.text(cx + 14, Y(220), '比较器', 10.5, 'start', MUTED)
        F.box(cx - 14, Y(196), 28, 18, '&', 'white', 11, 3)
        F.line(cx, Y(214), cx, Y(206) + 8, INK2, 1)
        F.text(cx, Y(190) - 0, '', 1)
        F.line(cx + 2, Y(196), X(285) + (-30 if k == 0 else 30), Y(190), INK2, 1.1)
        F.line(cx, Y(250), cx, Y(232), INK2, 1.1, arrow='end')
    F.line(X(282), Y(290), X(308), Y(290), INK2, 1.2, arrow='both')
    F.cells(X(180), Y(384), ['标记', '组号', '块内地址'], 70, 26, size=11.5, mono=False)
    F.line(X(250), Y(384), X(250), Y(312), INK2, 1.2, arrow='end')
    F.poly([(X(215), Y(384)), (X(215), Y(370)), (X(20), Y(370)), (X(20), Y(224)), (X(150), Y(224))], INK2, 1.1)
    F.text(X(320), Y(428), '物理地址 ⇕', 11.5, 'start', MUTED)
    F.cells(X(180), Y(440), ['实页号', '页内地址（12 位）'], [0] and 0, 0) if False else (F.box(X(180), Y(440), 100, 26, '实页号', 'blue', 11.5, 0), F.box(X(280), Y(440), 120, 26, '页内地址（12 位）', 'gray', 11, 0))

def instr(F, x, y, op='OP', mode='', addr='A', w=(70, 50, 60), h=30, label=True):
    F.box(x, y, w[0], h, op, 'teal', 13, 0, True)
    F.box(x + w[0], y, w[1], h, mode, 'dark', 13, 0, True)
    F.box(x + w[0] + w[1], y, w[2], h, addr, 'teal', 13, 0, True)
    if label:
        F.brace(x + w[0], x + w[0] + w[1], y - 4, '寻址特征', down=False, size=11.5)
    return (x + w[0] + w[1] + w[2] / 2, y + h)

def memcol(F, x, y, rows, w=90, rh=30, title='主存', hl=None, labels=None):
    """rows: list of cell texts ('' blank, '⋮'); hl: index to tone."""
    hl = hl or {}
    if title: F.text(x + w / 2, y - 10, title, 12.5, color=INK2, weight=600)
    for i, r in enumerate(rows):
        F.box(x, y + i * rh, w, rh, r, hl.get(i, 'white' if r != '⋮' else 'light'), 12.5, 0)
    if labels:
        for i, l in labels.items():
            F.text(x - 8, y + i * rh + rh / 2, l, 12, 'end', INK2, valign='middle', mono=True)
    return [(x, y + i * rh + rh / 2) for i in range(len(rows))]

def wave_clock(F, x0, y, n, T, hi=22, color=INK):
    d = f'M{x0} {y}'
    x = x0
    for i in range(n):
        d += f'H{x + T * 0.15}V{y - hi}H{x + T * 0.65}V{y}H{x + T}'
        x += T
    F.path(d, color, 1.6)

def wave_bus(F, y, segs, tone, h=20, x_end=None):
    """segs: list of (x1, x2, label) valid windows drawn as hexagons, rest as line."""
    f, s, t = TONES[tone]
    for x1, x2, lab in segs:
        F.items.append(f'<path d="M{x1} {y}L{x1 + 8} {y - h / 2}H{x2 - 8}L{x2} {y}L{x2 - 8} {y + h / 2}H{x1 + 8}Z" fill="{f}" stroke="{s}" stroke-width="1.4"/>')
        if lab: F.text((x1 + x2) / 2, y, lab, 11, color=t, valign='middle')

def wave_level(F, pts, color, sw=1.8):
    """pts: [(x, level)] level 0/1; draws step waveform with slanted edges."""
    d = ''
    for i, (x, lv) in enumerate(pts):
        if i == 0:
            d = f'M{x} {lv}'
        else:
            px, pl = pts[i - 1]
            d += f'L{x - 8} {pl}L{x} {lv}' if pl != lv else f'L{x} {lv}'
    F.path(d, color, sw)

def cpu_flow(F, steps, regs=('PC', 'MAR', 'CU', 'IR', 'MDR'), extra=None):
    """CPU (PC, MAR, CU, IR, MDR) + three buses + memory; steps: list of (num, pts) arrows."""
    F.rect(30, 60, 330, 230, 'none', INK2, 1.3, 10); F.pill(38, 50, 'CPU', 'violet', 11.5)
    P = {'PC': (60, 90), 'MAR': (230, 90), 'CU': (230, 160), 'IR': (60, 230), 'MDR': (230, 230), 'SP': (60, 90)}
    tones = {'PC': 'blue', 'MAR': 'green', 'CU': 'amber', 'IR': 'red', 'MDR': 'green', 'SP': 'blue'}
    for r in regs:
        x, y = P[r]
        F.box(x, y, 90, 32, r, tones[r], 13, 4, True)
    for i, lab in enumerate(('地址总线', '数据总线', '控制总线')):
        x = 410 + i * 40
        F.line(x, 60, x, 300, INK, 4)
        F.text(x + 12, 280, lab, 10.5, 'start', MUTED, rotate=-90)
    F.box(560, 140, 100, 70, '存储器', 'violet', 14, 6)
    for num, pts, col in steps:
        F.poly(pts, ACCENT.get(col, col), 1.5, arrow='end')
        mx, my = pts[-2] if len(pts) > 2 else pts[0]
        lx, ly = (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
        F.circle(lx, ly - 10, 8, num, 'white', 10.5, sw=1)

def cu_full(F, hl=None, ox=0, oy=0):
    """Hardwired CU: IR -> OP decoder, CLK -> beat generator, FE/IND/EX/INT, flags -> CU -> C0..Ck.
    hl: one of 'op','cycle','beat','flag','out' to emphasise; others dimmed."""
    X = lambda x: x + ox
    Y = lambda y: y + oy
    op = lambda k: None if hl in (None, k) else 0.28
    F.items.append(f'<g opacity="{op("op") or 1}">')
    F.box(X(240), Y(60), 220, 32, '指令寄存器 IR', 'white', 13, 4)
    F.line(X(350), Y(92), X(350), Y(110), INK2, 1.4, arrow='end'); F.text(X(360), Y(102), 'n 位操作码', 11, 'start', INK2)
    F.box(X(240), Y(112), 220, 30, '操作码译码器', 'blue', 13, 4)
    for x, l in ((X(260), '0'), (X(290), '1'), (X(440), '2ⁿ−1')):
        F.line(x, Y(142), x, Y(168), ACCENT['blue'], 1.4, arrow='end'); F.text(x + 4, Y(156), l, 10.5, 'start', ACCENT['blue'])
    F.text(X(365), Y(156), '……', 11, color=ACCENT['blue'])
    F.items.append('</g>')
    F.box(X(240), Y(170), 220, 160, '控制单元\nCU', 'white', 16, 4, weight=700)
    F.items.append(f'<g opacity="{op("beat") or 1}">')
    F.box(X(40), Y(190), 46, 26, '时钟', 'violet', 11.5, 4)
    F.path(f'M{X(30)} {Y(250)}' + ''.join(f'h6v-14h8v14' for _ in range(5)) + 'h8', ACCENT['violet'], 1.4)
    F.text(X(64), Y(272), 'CLK（主频）', 11, color=INK2)
    F.box(X(130), Y(180), 30, 140, '节\n拍\n发\n生\n器', 'amber', 11, 4)
    F.line(X(108), Y(244), X(128), Y(244), ACCENT['violet'], 1.3, arrow='end')
    for i, t in enumerate(('T₀', 'T₁', 'T₂', '⋮', 'Tₘ')):
        y = Y(190 + i * 28)
        if t != '⋮': F.line(X(160), y, X(238), y, ACCENT['amber'], 1.3, arrow='end')
        F.text(X(200), y - 6, t, 11, color=ACCENT['amber'])
    F.text(X(145), Y(346), '每个时钟周期发出一个节拍信号（循环）', 10.5, color=ACCENT['amber'])
    F.items.append('</g>')
    F.items.append(f'<g opacity="{op("cycle") or 1}">')
    F.line(X(620), Y(186), X(462), Y(186), ACCENT['amber'], 1.4, arrow='end'); F.text(X(560), Y(176), 'FE、IND、EX、INT', 11, color=ACCENT['amber'])
    F.text(X(560), Y(204), '（机器周期标志，集成在 CU 内）', 10, color=MUTED)
    F.items.append('</g>')
    F.items.append(f'<g opacity="{op("flag") or 1}">')
    for i, y in enumerate((240, 262, 300)):
        F.line(X(620), Y(y), X(462), Y(y), ACCENT['green'], 1.3, arrow='end')
    F.text(X(540), Y(286), '⋮', 11, color=ACCENT['green'])
    F.text(X(640), Y(262), '标志（来自执行单元\n的反馈：PSW、ACC、\nI/O 设备、主存等）', 10.5, 'start', ACCENT['green'], lh=1.4)
    F.items.append('</g>')
    F.items.append(f'<g opacity="{op("out") or 1}">')
    for x, l in ((X(270), 'C₀'), (X(300), 'C₁'), (X(430), 'Cₖ')):
        F.line(x, Y(330), x, Y(364), ACCENT['red'], 1.4, arrow='end'); F.text(x, Y(380), l, 12, color=ACCENT['red'])
    F.text(X(365), Y(350), '……', 11, color=ACCENT['red'])
    F.text(X(350), Y(402), '每个输出的控制信号对应一个微命令；如 C₁ 对应 (PC)→MAR，就让 C₁ 接到 PCout 和 MARin 上', 10.5, color=ACCENT['red'])
    F.items.append('</g>')

def pipe_row(F, x, y, segs, w=84, h=30):
    """segs: list of (label, tone)."""
    for i, (lab, t) in enumerate(segs):
        F.box(x + i * w, y, w, h, lab, t, 12, 0)

STG = [('取指', 'violet'), ('分析', 'blue'), ('执行', 'amber')]

def spacetime(F, x0, y0, rows, cols, cw=42, rh=30, fills=None, labels=None, tone=None):
    """Grid space-time diagram: rows from bottom; fills: {(r,c): text}."""
    for (r, c), t in fills.items():
        tt = tone(r, c, t) if tone else 'white'
        F.box(x0 + c * cw, y0 - (r + 1) * rh, cw, rh, t, tt, 12, 0, True)
    if labels:
        for r, l in enumerate(labels):
            F.text(x0 - 10, y0 - r * rh - rh / 2, l, 12, 'end', INK2, valign='middle')
    F.line(x0, y0 + 2, x0 + cols * cw + 30, y0 + 2, INK2, 1.3, arrow='end'); F.text(x0 + cols * cw + 36, y0 + 2, 't', 12, 'start', INK, valign='middle')
    F.line(x0, y0 + 2, x0, y0 - len(labels or []) * rh - 30, INK2, 1.3, arrow='end')

def datapath5(F, idle=(), green=False, wrpc=None, ox=0, oy=0):
    """5-stage pipeline datapath. idle: stages drawn as '空段' arrows; wrpc: stage index writing PC."""
    X = lambda v: v + ox
    Y = lambda v: v + oy
    names = [('IF', 'Fetch'), ('ID', 'Decode'), ('EX', 'Execute'), ('M', 'Memory'), ('WB', 'WriteBack')]
    bx = [40, 170, 300, 430, 560, 690]
    for i, (a, b) in enumerate(names):
        F.text(X((bx[i] + bx[i + 1]) / 2), Y(64), a, 13, color=ACCENT['red'], weight=700); F.text(X((bx[i] + bx[i + 1]) / 2), Y(80), b, 10.5, color=MUTED)
    for x in bx: F.line(X(x), Y(90), X(x), Y(300), LINE, 1, dash='4 4')
    F.box(X(48), Y(110), 18, 150, '', 'white', rx=2); F.text(X(57), Y(185), 'PC', 10, color=INK, valign='middle', rotate=-90)
    F.box(X(80), Y(120), 70, 120, '指令\nCache', 'violet', 11.5, 4)
    for x in (164, 294, 424, 554): F.box(X(x), Y(110), 12, 160, '', 'gray', rx=2)
    F.box(X(190), Y(160), 80, 90, '寄存器堆', 'green', 11.5, 4)
    F.items.append(f'<path d="M{X(330)} {Y(140)}L{X(372)} {Y(162)}V{Y(184)}L{X(362)} {Y(192)}L{X(372)} {Y(200)}V{Y(222)}L{X(330)} {Y(244)}Z" fill="#fde7e4" stroke="#d1493a" stroke-width="1.3"/>')
    F.text(X(354), Y(192), 'ALU', 10.5, color='#7f1d1d', weight=700, valign='middle', rotate=-90)
    F.box(X(460), Y(130), 80, 110, '数据\nCache', 'amber', 11.5, 4)
    for (a, b, y) in ((66, 78, 180), (150, 162, 180), (176, 188, 200), (270, 292, 180), (270, 292, 220), (306, 328, 170), (306, 328, 214), (372, 422, 192), (436, 458, 185), (540, 552, 185), (566, 610, 185)):
        F.line(X(a), Y(y), X(b), Y(y), INK2, 1.2, arrow='end')
    F.poly([(X(610), Y(185)), (X(640), Y(185)), (X(640), Y(290)), (X(230), Y(290)), (X(230), Y(252))], INK2, 1.2, arrow='end')
    if green:
        F.poly([(X(270), Y(230)), (X(282), Y(230)), (X(282), Y(270)), (X(400), Y(270)), (X(400), Y(150)), (X(458), Y(150))], ACCENT['green'], 2, arrow='end')
        F.text(X(400), Y(282), 'B 中的数据送 Store', 10.5, color=ACCENT['green'])
    for s in idle:
        xa, xb = bx[s] + 14, bx[s + 1] - 4
        F.items.append(f'<path d="M{X(xa)} {Y(170)}H{X(xb - 24)}V{Y(156)}L{X(xb)} {Y(190)}L{X(xb - 24)} {Y(224)}V{Y(210)}H{X(xa)}Z" fill="#d4d4d8" fill-opacity="0.85" stroke="#71717a" stroke-width="1.2"/>')
        F.text(X((xa + xb) / 2 - 8), Y(190), '空段', 11.5, color=INK, weight=600, valign='middle')
    if wrpc is not None:
        xs = (bx[wrpc] + bx[wrpc + 1]) / 2
        F.poly([(X(xs), Y(250)), (X(xs), Y(312)), (X(57), Y(312)), (X(57), Y(262))], ACCENT['blue'], 1.6, arrow='end', dash='5 4')
        F.text(X((xs + 57) / 2), Y(326), '目标 PC 值写回 PC', 11, color=ACCENT['blue'])
