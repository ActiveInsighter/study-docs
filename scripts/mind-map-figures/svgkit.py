"""Tiny SVG authoring kit for the 408 mind-map figures.

One visual language for every figure: white rounded card, zinc greys,
one or two soft accents, 1.5px strokes, system CJK sans + mono.
"""
import math
import re
from xml.sax.saxutils import escape

FONT = "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC','Source Han Sans SC',system-ui,sans-serif"
MONO = "'JetBrains Mono','SF Mono',Menlo,Consolas,'Noto Sans Mono CJK SC',monospace"

INK, INK2, MUTED, LINE, FAINT, FILL, PAPER = (
    '#18181b', '#3f3f46', '#71717a', '#a1a1aa', '#e4e4e7', '#f4f4f5', '#ffffff')

# tone -> (fill, stroke, text)
TONES = {
    'white': ('#ffffff', '#52525b', INK),
    'gray': ('#f4f4f5', '#52525b', INK),
    'light': ('#fafafa', '#a1a1aa', INK2),
    'dark': ('#27272a', '#27272a', '#fafafa'),
    'none': ('none', 'none', INK),
    'blue': ('#e8effc', '#3b6fd4', '#1e3a8a'),
    'green': ('#e3f4e8', '#2f8f57', '#14532d'),
    'amber': ('#fdf1d8', '#c98a12', '#78350f'),
    'red': ('#fde7e4', '#d1493a', '#7f1d1d'),
    'violet': ('#efe9fb', '#7856c9', '#3b0764'),
    'teal': ('#e0f3f1', '#23877c', '#134e4a'),
    'rbred': ('#d1493a', '#b83b2e', '#ffffff'),
    'rbblack': ('#27272a', '#18181b', '#ffffff'),
}
ACCENT = {k: v[1] for k, v in TONES.items()}
ACCENT.update(ink=INK, ink2=INK2, muted=MUTED, line=LINE)


def _w(s, size, mono=False):
    """Approximate rendered width of a string."""
    w = 0.0
    for ch in s:
        if ord(ch) > 0x2E80:
            w += 1.0
        elif mono:
            w += 0.6
        elif ch in 'il.,:;|!\'`':
            w += 0.3
        elif ch in 'mwMW':
            w += 0.85
        elif ch.isupper() or ch.isdigit():
            w += 0.62
        else:
            w += 0.53
    return w * size


def text_width(s, size=15, mono=False):
    plain = re.sub(r'[_^]\{([^}]*)\}', lambda m: m.group(1), s).replace('**', '')
    return max((_w(line, size, mono) for line in plain.split('\n')), default=0)


def _nb(s):
    # keep indentation and runs of spaces (renderers collapse plain spaces)
    s = re.sub(r'^ +', lambda m: '\u00a0' * len(m.group(0)), s)
    return re.sub(r'  +', lambda m: '\u00a0' * len(m.group(0)), s)


def _rich(s):
    s = _nb(s)
    """Inline markup -> tspans: _{sub} ^{sup} **bold** ~~strike~~ [[color:text]]."""
    out = []
    pos = 0
    pat = re.compile(r'_\{([^}]*)\}|\^\{([^}]*)\}|\*\*([^*]+)\*\*|\[\[(\w+):([^\]]*)\]\]|~~([^~]+)~~')
    for m in pat.finditer(s):
        out.append(escape(s[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f'<tspan baseline-shift="-22%" font-size="72%">{escape(m.group(1))}</tspan>')
        elif m.group(2) is not None:
            out.append(f'<tspan baseline-shift="38%" font-size="72%">{escape(m.group(2))}</tspan>')
        elif m.group(3) is not None:
            out.append(f'<tspan font-weight="700">{escape(m.group(3))}</tspan>')
        elif m.group(4) is not None:
            out.append(f'<tspan fill="{ACCENT.get(m.group(4), m.group(4))}" font-weight="600">{escape(m.group(5))}</tspan>')
        else:
            out.append(f'<tspan text-decoration="line-through">{escape(m.group(6))}</tspan>')
        pos = m.end()
    out.append(escape(s[pos:]))
    return ''.join(out)


def f(n):
    return ('%.1f' % n).rstrip('0').rstrip('.')


class Fig:
    def __init__(self, w, h, title=None, caption=None, bg=True):
        self.w, self.h = w, h
        self.items = []
        self.markers = set()
        if bg:
            self.items.append(
                f'<rect x="0.75" y="0.75" width="{f(w - 1.5)}" height="{f(h - 1.5)}" rx="14" fill="{PAPER}" stroke="{FAINT}" stroke-width="1.5"/>')
        if title:
            self.text(24, 34, title, size=17, anchor='start', weight=700, color=INK)
            self.items.append(f'<rect x="24" y="44" width="28" height="3" rx="1.5" fill="{INK}"/>')
        if caption:
            self.text(w / 2, h - 18, caption, size=13, color=MUTED)

    # ---- primitives -------------------------------------------------
    def raw(self, s):
        self.items.append(s)

    def text(self, x, y, s, size=15, anchor='middle', color=INK, weight=400, mono=False,
             italic=False, lh=1.35, valign='baseline', rotate=None, opacity=None, halo=False):
        s = str(s)
        lines = s.split('\n')
        n = len(lines)
        if valign == 'middle':
            y0 = y - (n - 1) * size * lh / 2 + size * 0.35
        elif valign == 'top':
            y0 = y + size * 0.8
        else:
            y0 = y
        color = ACCENT.get(color, color)
        attrs = [f'x="{f(x)}"', f'y="{f(y0)}"', f'font-size="{f(size)}"', f'fill="{color}"']
        if anchor != 'start':
            attrs.append(f'text-anchor="{anchor}"')
        if weight != 400:
            attrs.append(f'font-weight="{weight}"')
        if mono:
            attrs.append('font-family="' + MONO.replace('"', "'") + '"')
        if italic:
            attrs.append('font-style="italic"')
        if opacity:
            attrs.append(f'opacity="{opacity}"')
        if halo:
            attrs.append('stroke="#fff" stroke-width="4" stroke-linejoin="round" paint-order="stroke"')
        if rotate is not None:
            attrs.append(f'transform="rotate({f(rotate)} {f(x)} {f(y)})"')
        if n == 1:
            body = _rich(lines[0])
        else:
            body = ''.join(
                f'<tspan x="{f(x)}" dy="{0 if i == 0 else f(size * lh)}">{_rich(l) or " "}</tspan>'
                for i, l in enumerate(lines))
        self.items.append(f'<text {" ".join(attrs)}>{body}</text>')

    def rect(self, x, y, w, h, fill=FILL, stroke=INK2, sw=1.5, rx=6, dash=None, opacity=None):
        fill = TONES[fill][0] if fill in TONES else fill
        stroke = ACCENT.get(stroke, stroke)
        d = f' stroke-dasharray="{dash}"' if dash else ''
        o = f' opacity="{opacity}"' if opacity else ''
        self.items.append(
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" fill="{fill}" stroke="{stroke}" stroke-width="{f(sw)}"{d}{o}/>')

    def box(self, x, y, w, h, label='', tone='white', size=15, rx=8, mono=False, weight=None,
            dash=None, sw=1.5, color=None, align='middle'):
        fill, stroke, tc = TONES[tone]
        self.rect(x, y, w, h, fill, stroke, sw, rx, dash)
        if label != '' and label is not None:
            if align == 'start':
                self.text(x + 12, y + h / 2, label, size, 'start', color or tc, weight or 400, mono, valign='middle')
            else:
                self.text(x + w / 2, y + h / 2, label, size, 'middle', color or tc,
                          weight or (600 if tone == 'dark' else 400), mono, valign='middle')
        return (x, y, w, h)

    def pill(self, x, y, label, tone='gray', size=13, pad=10, h=None, anchor='start', weight=500):
        w = text_width(label, size) + pad * 2
        h = h or size + 12
        if anchor == 'middle':
            x -= w / 2
        fill, stroke, tc = TONES[tone]
        self.rect(x, y, w, h, fill, stroke, 1.2, h / 2)
        self.text(x + w / 2, y + h / 2, label, size, 'middle', tc, weight, valign='middle')
        return w

    def circle(self, cx, cy, r, label='', tone='white', size=15, sw=1.5, dash=None, weight=500, mono=False):
        fill, stroke, tc = TONES[tone]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{f(sw)}"{d}/>')
        if label != '':
            self.text(cx, cy, label, size, 'middle', tc, weight, mono, valign='middle')

    def ellipse(self, cx, cy, rx, ry, label='', tone='white', size=15, sw=1.5, dash=None):
        fill, stroke, tc = TONES[tone]
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.items.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{f(sw)}"{d}/>')
        if label:
            self.text(cx, cy, label, size, 'middle', tc, 500, valign='middle')

    def _marker(self, color):
        mid = 'a' + color.strip('#')
        if mid not in self.markers:
            self.markers.add(mid)
        return mid

    def path(self, d, color=INK2, sw=1.5, dash=None, arrow=None, fill='none', opacity=None):
        color = ACCENT.get(color, color)
        a = ''
        if arrow in ('end', 'both'):
            a += f' marker-end="url(#{self._marker(color)})"'
        if arrow in ('start', 'both'):
            a += f' marker-start="url(#{self._marker(color)}s)"'
            self.markers.add(self._marker(color) + 's')
        dd = f' stroke-dasharray="{dash}"' if dash else ''
        o = f' opacity="{opacity}"' if opacity else ''
        self.items.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{f(sw)}" stroke-linecap="round" stroke-linejoin="round"{dd}{a}{o}/>')

    def line(self, x1, y1, x2, y2, color=INK2, sw=1.5, dash=None, arrow=None, gap=0, gap2=None):
        if gap or gap2:
            g1, g2 = gap, gap if gap2 is None else gap2
            L = math.hypot(x2 - x1, y2 - y1) or 1
            ux, uy = (x2 - x1) / L, (y2 - y1) / L
            x1, y1, x2, y2 = x1 + ux * g1, y1 + uy * g1, x2 - ux * g2, y2 - uy * g2
        self.path(f'M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}', color, sw, dash, arrow)

    def poly(self, pts, color=INK2, sw=1.5, dash=None, arrow='end', r=6):
        """Polyline with softly rounded corners."""
        d = f'M{f(pts[0][0])} {f(pts[0][1])}'
        for i in range(1, len(pts) - 1):
            (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
            l1 = math.hypot(x1 - x0, y1 - y0) or 1
            l2 = math.hypot(x2 - x1, y2 - y1) or 1
            rr = min(r, l1 / 2, l2 / 2)
            ax, ay = x1 - (x1 - x0) / l1 * rr, y1 - (y1 - y0) / l1 * rr
            bx, by = x1 + (x2 - x1) / l2 * rr, y1 + (y2 - y1) / l2 * rr
            d += f'L{f(ax)} {f(ay)}Q{f(x1)} {f(y1)} {f(bx)} {f(by)}'
        d += f'L{f(pts[-1][0])} {f(pts[-1][1])}'
        self.path(d, color, sw, dash, arrow)

    def curve(self, x1, y1, x2, y2, bend=0.25, color=INK2, sw=1.5, dash=None, arrow='end'):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        cx, cy = mx - dy * bend, my + dx * bend
        self.path(f'M{f(x1)} {f(y1)}Q{f(cx)} {f(cy)} {f(x2)} {f(y2)}', color, sw, dash, arrow)

    def brace(self, x1, x2, y, label='', down=True, color=MUTED, size=13, depth=8):
        s = 1 if down else -1
        m = (x1 + x2) / 2
        self.path(f'M{f(x1)} {f(y)}q0 {f(s*depth)} {f(depth)} {f(s*depth)}H{f(m-depth)}q{f(depth)} 0 {f(depth)} {f(s*depth)}'
                  f'q0 {f(-s*depth)} {f(depth)} {f(-s*depth)}H{f(x2-depth)}q{f(depth)} 0 {f(depth)} {f(-s*depth)}', color, 1.3)
        if label:
            self.text(m, y + s * (2 * depth + size + 2) - (0 if down else -size * 0.2), label, size, color=color)

    def vbrace(self, x, y1, y2, label='', right=True, color=MUTED, size=13, depth=8):
        s = 1 if right else -1
        m = (y1 + y2) / 2
        self.path(f'M{f(x)} {f(y1)}q{f(s*depth)} 0 {f(s*depth)} {f(depth)}V{f(m-depth)}q0 {f(depth)} {f(s*depth)} {f(depth)}'
                  f'q{f(-s*depth)} 0 {f(-s*depth)} {f(depth)}V{f(y2-depth)}q0 {f(depth)} {f(-s*depth)} {f(depth)}', color, 1.3)
        if label:
            self.text(x + s * (2 * depth + 6), m, label, size, 'start' if right else 'end', color, valign='middle')

    # ---- composites --------------------------------------------------
    def cells(self, x, y, vals, cw=40, ch=36, tones=None, index=None, size=15, mono=True,
              index_color=MUTED, gap=0, tone='white', rx=0, label=None, sw=1.5):
        """A row of array cells. Returns list of cell centres."""
        tones = tones or {}
        cs = []
        if gap == 0:
            # draw as one outlined strip with dividers for a crisp look
            for i, v in enumerate(vals):
                t = tones.get(i, tone)
                fill = TONES[t][0]
                self.rect(x + i * cw, y, cw, ch, fill, 'none', 0, 0)
            self.rect(x, y, cw * len(vals), ch, 'none', INK2, sw, rx)
            for i in range(1, len(vals)):
                self.line(x + i * cw, y, x + i * cw, y + ch, INK2, 1)
            for i, v in enumerate(vals):
                t = tones.get(i, tone)
                self.text(x + i * cw + cw / 2, y + ch / 2, v, size, color=TONES[t][2], mono=mono, valign='middle')
                cs.append((x + i * cw + cw / 2, y + ch / 2))
        else:
            for i, v in enumerate(vals):
                cx = x + i * (cw + gap)
                self.box(cx, y, cw, ch, v, tones.get(i, tone), size, rx or 6, mono)
                cs.append((cx + cw / 2, y + ch / 2))
        if index is not None:
            idx = index if isinstance(index, (list, tuple)) else [str(index + i) for i in range(len(vals))]
            for (cx, _), t in zip(cs, idx):
                self.text(cx, y + ch + 17, t, 12, color=index_color, mono=True)
        if label:
            self.text(x - 10, y + ch / 2, label, 14, 'end', INK2, valign='middle')
        return cs

    def table(self, x, y, rows, colw, rowh=32, header=True, size=14, align=None, mono_cols=(),
              head_tone='dark', zebra=True, tones=None, rx=8, line_color=None):
        """rows: list of lists. colw: list of widths. tones: {(r,c): tone}."""
        tones = tones or {}
        W = sum(colw)
        H = rowh * len(rows)
        lc = line_color or '#d4d4d8'
        # body backgrounds
        for r, row in enumerate(rows):
            yy = y + r * rowh
            if r == 0 and header:
                continue
            if zebra and (r % 2 == (0 if header else 1)):
                self.rect(x, yy, W, rowh, '#fafafa', 'none', 0, 0)
            cx = x
            for c, w in enumerate(colw):
                t = tones.get((r, c))
                if t:
                    self.rect(cx, yy, w, rowh, TONES[t][0], 'none', 0, 0)
                cx += w
        if header:
            hf = TONES[head_tone][0]
            self.items.append(
                f'<path d="M{f(x)} {f(y+rowh)}V{f(y+rx)}Q{f(x)} {f(y)} {f(x+rx)} {f(y)}H{f(x+W-rx)}Q{f(x+W)} {f(y)} {f(x+W)} {f(y+rx)}V{f(y+rowh)}Z" fill="{hf}"/>')
        for r in range(1, len(rows)):
            self.line(x, y + r * rowh, x + W, y + r * rowh, lc, 1)
        cx = x
        for c in range(len(colw) - 1):
            cx += colw[c]
            self.line(cx, y + (rowh if header and head_tone == 'dark' else 0), cx, y + H, lc, 1)
        self.rect(x, y, W, H, 'none', '#a1a1aa', 1.2, rx)
        for r, row in enumerate(rows):
            cx = x
            for c, w in enumerate(colw):
                v = row[c] if c < len(row) else ''
                a = (align[c] if align else 'middle')
                hx = cx + w / 2 if a == 'middle' else (cx + 10 if a == 'start' else cx + w - 10)
                is_head = header and r == 0
                t = tones.get((r, c))
                col = TONES[head_tone][2] if is_head else (TONES[t][2] if t else INK)
                self.text(hx, y + r * rowh + rowh / 2, v, size, a, col, 600 if is_head else 400,
                          mono=(c in mono_cols and not is_head), valign='middle')
                cx += w
        return (x, y, W, H)

    def tree(self, x, y, node, unit=48, levelh=70, r=18, tone='white', size=15, tones=None,
             edge_color=INK2, labels=None, shape='circle', bw=None, bh=None, mono=False):
        """Layout a tree. node = 'A' | ('A', [children]) ; None child = empty slot.
        x is left edge, y is root centre. Returns {label: (cx, cy)}."""
        tones = tones or {}
        pos = {}
        counter = [0]

        def lay(n, depth):
            if n is None:
                cx = x + counter[0] * unit + unit / 2
                counter[0] += 1
                return cx
            name, kids = (n, []) if isinstance(n, str) else n
            if not kids:
                cx = x + counter[0] * unit + unit / 2
                counter[0] += 1
            else:
                cxs = [lay(k, depth + 1) for k in kids]
                cx = (cxs[0] + cxs[-1]) / 2
                for k, c in zip(kids, cxs):
                    if k is not None:
                        pos.setdefault('__edges', []).append((name_key(k), (cx, y + depth * levelh), (c, y + (depth + 1) * levelh)))
            pos[name] = (cx, y + depth * levelh)
            return cx

        def name_key(k):
            return k if isinstance(k, str) else k[0]

        lay(node, 0)
        edges = pos.pop('__edges', [])
        hb = (bh or 30) / 2
        for k, (x1, y1), (x2, y2) in edges:
            if shape == 'circle':
                self.line(x1, y1, x2, y2, edge_color, 1.5, gap=r, gap2=((8 if k[1:].split('#')[0].strip() == '' else 13) if k.startswith('□') else r))
            else:
                self.line(x1, y1 + hb, x2, y2 - hb, edge_color, 1.5)
        for k, (cx, cy) in pos.items():
            lab = labels.get(k, k) if labels else k
            lab = re.sub(r'#\d+$', '', lab)
            t = tones.get(k, tone)
            if k.startswith('□'):
                lab = lab[1:]
                w = max(36, text_width(lab, size - 2, mono) + 12)
                if lab.strip() == '':
                    self.rect(cx - 7, cy - 7, 14, 14, '#fafafa', '#71717a', 1.2, 2)
                elif lab == 'NIL':
                    self.box(cx - 13, cy - 9, 26, 18, 'NIL', 'rbblack', 9, 3, True)
                else:
                    self.box(cx - w / 2, cy - 12, w, 24, lab, 'light', size - 2, 4, mono)
            elif shape == 'circle':
                self.circle(cx, cy, r, lab, t, size, mono=mono)
            else:
                w = bw or max(40, text_width(lab, size, mono) + 18)
                self.box(cx - w / 2, cy - hb, w, hb * 2, lab, t, size, 6, mono)
        return pos

    def graph(self, nodes, edges, r=20, directed=True, tones=None, size=15, esize=13, hl=(),
              hl_color='red', node_tone='white', labels=None, mono=False, ecolor=INK2):
        """nodes {name:(x,y)}; edges [(a,b,label?,{bend,side,pos,dash})]. hl: set of (a,b)."""
        tones = tones or {}
        for e in edges:
            a, b = e[0], e[1]
            lab = e[2] if len(e) > 2 else ''
            o = e[3] if len(e) > 3 else {}
            (x1, y1), (x2, y2) = nodes[a], nodes[b]
            L = math.hypot(x2 - x1, y2 - y1) or 1
            ux, uy = (x2 - x1) / L, (y2 - y1) / L
            hot = (a, b) in hl or (not directed and (b, a) in hl)
            col = ACCENT[hl_color] if hot else ACCENT.get(o.get('color', ecolor), o.get('color', ecolor))
            sw = 2.4 if hot else 1.5
            bend = o.get('bend', 0)
            sh = o.get('shift', 0)
            if sh:
                x1, y1, x2, y2 = x1 - uy * sh, y1 + ux * sh, x2 - uy * sh, y2 + ux * sh
            arrow = 'end' if directed else None
            ra, rb = (r if not isinstance(r, dict) else r[a]), (r if not isinstance(r, dict) else r[b])
            if bend:
                ang = math.atan2(uy, ux)
                a1 = ang - bend * 1.2
                a2 = ang + math.pi + bend * 1.2
                sx, sy = x1 + ra * math.cos(a1), y1 + ra * math.sin(a1)
                ex, ey = x2 + (rb + (2 if directed else 0)) * math.cos(a2), y2 + (rb + (2 if directed else 0)) * math.sin(a2)
                self.curve(sx, sy, ex, ey, bend, col, sw, o.get('dash'), arrow)
                mx, my = (sx + ex) / 2 - (ey - sy) * bend / 2, (sy + ey) / 2 + (ex - sx) * bend / 2
            else:
                self.line(x1, y1, x2, y2, col, sw, o.get('dash'), arrow, gap=ra, gap2=rb + (2 if directed else 0))
                t = o.get('pos', 0.5)
                mx, my = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
            if lab != '':
                side = o.get('side', 1)
                off = o.get('off', esize * 0.9)
                lx, ly = mx + uy * off * side, my - ux * off * side
                self.text(lx, ly, lab, esize, 'middle', col if hot else INK2, 600 if hot else 400,
                          mono, valign='middle', halo=True)
        for k, (x, y) in nodes.items():
            lab = labels.get(k, k) if labels else k
            rr = r if not isinstance(r, dict) else r[k]
            self.circle(x, y, rr, lab, tones.get(k, node_tone), size, mono=mono)

    def legend(self, x, y, items, size=13, gap=18):
        """items: [(tone, label)] drawn horizontally."""
        cx = x
        for tone, lab in items:
            fill, stroke, _ = TONES[tone]
            self.rect(cx, y - 10, 14, 14, fill, stroke, 1.3, 3)
            self.text(cx + 20, y + 1, lab, size, 'start', INK2)
            cx += 20 + text_width(lab, size) + gap
        return cx

    def svg(self, label=''):
        defs = []
        for mid in sorted(self.markers):
            start = mid.endswith('s')
            color = '#' + mid[1:].rstrip('s') if start else '#' + mid[1:]
            if start:
                defs.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="1.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M10 0.8L1.5 5 10 9.2z" fill="{color}"/></marker>'.replace('orient="auto-start-reverse"', 'orient="auto"'))
            else:
                defs.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0.8L8.5 5 0 9.2z" fill="{color}"/></marker>')
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(self.w)} {f(self.h)}" width="{f(self.w)}" height="{f(self.h)}"'
                f' font-family="{FONT}" font-size="15" xml:space="preserve" style="white-space:pre" role="img"' + (f' aria-label="{escape(label)}"' if label else '') + '>')
        parts = [head]
        if label:
            parts.append(f'<title>{escape(label)}</title>')
        if defs:
            parts.append('<defs>' + ''.join(defs) + '</defs>')
        parts.extend(self.items)
        parts.append('</svg>')
        return '\n'.join(parts) + '\n'
