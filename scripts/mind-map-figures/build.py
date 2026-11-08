"""Render figs/<id>.py -> public SVG, apply figs/<id>.md as Markdown, rewrite MDX refs."""
import os, re, sys, json, glob
KIT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, KIT)
import svgkit
REPO = os.path.abspath(os.path.join(KIT, '..', '..'))
PUB = REPO + '/public/images/408-mind-maps'
DOCS = REPO + '/content/docs/408/mind-maps'
only = set(sys.argv[1:])

def render(fid):
    src = open(f'{KIT}/figs/{fid}.py').read()
    ns = {}
    exec('from svgkit import *\n' + src, ns)
    F = ns['F']
    label = ns.get('LABEL', '')
    open(f'{PUB}/{fid}.svg', 'w').write(F.svg(label))
    dw = ns.get('DW', 300 if F.w >= 400 else F.w)
    return dw, round(dw * F.h / F.w), F

IMG = re.compile(r'<img src="/images/408-mind-maps/([a-z0-9-]+)\.(png|svg)" alt="([^"]*)" width="(\d+)" height="(\d+)">')

def apply():
    sizes, mds = {}, {}
    for p in sorted(glob.glob(f'{KIT}/figs/*.py')):
        fid = os.path.basename(p)[:-3]
        if only and fid not in only and os.path.exists(f'{PUB}/{fid}.svg'):
            # keep previous size
            pass
        try:
            dw, dh, F = render(fid)
        except Exception as e:
            print('ERR', fid, e); raise
        sizes[fid] = (dw, dh)
    for p in sorted(glob.glob(f'{KIT}/figs/*.md')):
        fid = os.path.basename(p)[:-3]
        mds[fid] = open(p).read().rstrip('\n')
    changed = 0
    for path in glob.glob(f'{DOCS}/*/*.mdx'):
        lines = open(path).read().split('\n')
        out = []
        for line in lines:
            m = IMG.search(line)
            if not m:
                out.append(line); continue
            fid, ext, alt = m.group(1), m.group(2), m.group(3)
            if fid in mds:
                ind = len(line) - len(line.lstrip(' '))
                label = (line[:m.start()] + line[m.end():]).strip()
                assert label.startswith('-'), line
                label = label[1:].strip()
                md = mds[fid].split('\n')
                if label:
                    out.append(' ' * ind + '- ' + label)
                    pad = ' ' * (ind + 2)
                else:
                    pad = ' ' * ind
                out.extend((pad + l) if l.strip() else '' for l in md)
                changed += 1
            elif fid in sizes:
                w, h = sizes[fid]
                out.append(line[:m.start()] + f'<img src="/images/408-mind-maps/{fid}.svg" alt="{alt}" width="{w}" height="{h}">' + line[m.end():])
                changed += ext == 'png'
            else:
                out.append(line)
        open(path, 'w').write('\n'.join(out))
    for fid in list(sizes) + list(mds):
        p = f'{PUB}/{fid}.png'
        if os.path.exists(p): os.remove(p)
        if fid in mds and os.path.exists(f'{PUB}/{fid}.svg') and fid not in sizes:
            os.remove(f'{PUB}/{fid}.svg')
    left = len(glob.glob(f'{PUB}/*.png'))
    print(f'svg={len(sizes)} md={len(mds)} changed_refs={changed} png_left={left}')

apply()
