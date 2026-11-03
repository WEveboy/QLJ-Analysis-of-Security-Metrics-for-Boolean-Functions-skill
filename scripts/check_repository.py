"""Check compiled hashes and local Markdown destinations using only stdlib."""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
skill=ROOT/'skills/qlj-security-metrics'
manifest=json.loads((skill/'BUILD_MANIFEST.json').read_text(encoding='utf-8'))
count=0
for name,expected in manifest['published_hashes'].items():
    p=skill/Path(name.replace('\\','/'))
    if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
        raise SystemExit('hash mismatch: '+name)
    count+=1
for folder in (ROOT/'skills',ROOT/'research/qlj-security-metrics',ROOT/'docs'):
    for p in folder.rglob('*.md'):
        if '__pycache__' in p.parts:continue
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8-sig')):
            if '://' in target or target.startswith('#'):continue
            target=target.split('#')[0]
            if not (p.parent/target).exists():raise SystemExit(f'broken link: {p}: {target}')
print('PASS compiled hashes:',count,'and local Markdown links')
