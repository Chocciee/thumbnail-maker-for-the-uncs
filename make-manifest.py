"""Run after adding or removing files in bank/ :  python3 make-manifest.py
Works from any folder and creates the bank folders if they are missing."""
import os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
EXT = ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg')
os.makedirs('bank/backgrounds', exist_ok=True)
os.makedirs('bank/images', exist_ok=True)
def files(d):
    return sorted(f'{d}/{f}' for f in os.listdir(d) if f.lower().endswith(EXT))
m = {'backgrounds': files('bank/backgrounds'), 'images': {}}
for c in sorted(os.listdir('bank/images')):
    if os.path.isdir(f'bank/images/{c}'):
        m['images'][c] = files(f'bank/images/{c}')
json.dump(m, open('bank/manifest.json', 'w'), indent=2)
os.makedirs('templates', exist_ok=True)
tpl = sorted(f for f in os.listdir('templates') if f.lower().endswith('.json') and f != 'index.json')
json.dump(tpl, open('templates/index.json', 'w'), indent=2)
print(len(tpl), 'templates')
print(len(m['backgrounds']), 'backgrounds,', sum(map(len, m['images'].values())), 'images in', len(m['images']), 'categories')
print('Wrote', os.path.abspath('bank/manifest.json'))