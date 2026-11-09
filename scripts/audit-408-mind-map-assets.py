"""Validate 408 image references and standalone SVG dependencies without a build."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'content/docs/408/mind-maps'
ASSETS = ROOT / 'public/images/408-mind-maps'


def audit():
    errors = []
    references = Counter()
    documents = sorted(DOCS.rglob('*.mdx'))
    for path in documents:
        for name in re.findall(r'/images/408-mind-maps/([a-z0-9-]+\.svg)', path.read_text()):
            references[name] += 1
            if not (ASSETS / name).is_file():
                errors.append(f'{path.relative_to(ROOT)}: missing {name}')
    for path in sorted(ASSETS.glob('*.svg')):
        try:
            svg = ET.parse(path).getroot()
        except ET.ParseError as error:
            errors.append(f'{path.name}: {error}')
            continue
        ids = [node.attrib['id'] for node in svg.iter() if 'id' in node.attrib]
        if len(set(ids)) != len(ids):
            errors.append(f'{path.name}: duplicate SVG IDs')
        known = set(ids)
        try:
            viewbox = [float(n) for n in svg.attrib['viewBox'].split()]
            assert len(viewbox) == 4 and viewbox[2] > 0 and viewbox[3] > 0
        except (KeyError, ValueError, AssertionError):
            errors.append(f'{path.name}: invalid viewBox')
        for node in svg.iter():
            for key, value in node.attrib.items():
                local = key.rsplit('}', 1)[-1]
                dependencies = ([value] if local == 'href' else [])
                dependencies += re.findall(r'''url\(\s*['"]?([^)'"\s]+)''', value)
                for dependency in dependencies:
                    if not dependency.startswith('#'):
                        errors.append(f'{path.name}: external dependency {dependency}')
                    elif dependency[1:] not in known:
                        errors.append(f'{path.name}: missing SVG definition {dependency}')
            if node.tag.rsplit('}', 1)[-1] == 'style':
                css = ''.join(node.itertext())
                if '@import' in css:
                    errors.append(f'{path.name}: external stylesheet dependency')
                for dependency in re.findall(r'''url\(\s*['"]?([^)'"\s]+)''', css):
                    if not dependency.startswith('#') or dependency[1:] not in known:
                        errors.append(f'{path.name}: invalid CSS dependency {dependency}')
    migration = json.loads((ROOT / 'reports/408-mind-map-image-migration.json').read_text())
    replacements = {entry['asset'] for entry in migration['placements'] if entry['selectedAsset'] != entry['asset']}
    unused = {path.name for path in ASSETS.glob('*.svg')} - references.keys()
    for name in unused - replacements:
        errors.append(f'{name}: no reference or verified replacement')
    return {
        'documents': len(documents),
        'svgFiles': len(list(ASSETS.glob('*.svg'))),
        'referencedSvgFiles': len(references),
        'imageOccurrences': sum(references.values()),
        'intentionallySupersededSvgFiles': len(unused),
        'errors': errors,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = audit()
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.report:
        args.report.write_text(output)
    print(output, end='')
    raise SystemExit(bool(result['errors']))
