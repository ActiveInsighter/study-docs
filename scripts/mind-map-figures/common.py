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
