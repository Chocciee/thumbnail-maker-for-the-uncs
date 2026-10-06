"""Run this after adding or removing files in bank/ :  python3 make-manifest.py"""
import os, json
EXT = ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg')
def files(d):
    return sorted(f'{d}/{f}' for f in os.listdir(d) if f.lower().endswith(EXT)) if os.path.isdir(d) else []
m = {'backgrounds': files('bank/backgrounds'), 'images': {}}
root = 'bank/images'
for c in sorted(os.listdir(root)) if os.path.isdir(root) else []:
    if os.path.isdir(f'{root}/{c}'):
        m['images'][c] = files(f'{root}/{c}')
json.dump(m, open('bank/manifest.json', 'w'), indent=2)
print(len(m['backgrounds']), 'backgrounds,', sum(map(len, m['images'].values())), 'images in', len(m['images']), 'categories')
