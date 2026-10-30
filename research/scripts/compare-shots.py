"""Compare two folders of QC screenshots (same filenames) and report the share of changed pixels.
Usage: compare-shots.py <before-dir> <after-dir> [--threshold=0.02]
Prints one line per image: changed % and a PASS/CHANGED label. Writes <after-dir>/diff-<name>.png highlighting changes in red.
A change is expected after a revision; use this to confirm that a fix touched only what you intended."""
import os, sys
from PIL import Image, ImageChops
Image.MAX_IMAGE_PIXELS = None
a, b = sys.argv[1], sys.argv[2]
th = float(next((x.split('=')[1] for x in sys.argv if x.startswith('--threshold=')), 0.02))
for name in sorted(os.listdir(b)):
    if not name.endswith('.png') or name.startswith('diff-') or not os.path.exists(os.path.join(a, name)): continue
    x, y = Image.open(os.path.join(a, name)).convert('RGB'), Image.open(os.path.join(b, name)).convert('RGB')
    if x.size != y.size:
        print(f'{name}: SIZE {x.size} -> {y.size} (page height changed)'); h = min(x.height, y.height); x, y = x.crop((0, 0, x.width, h)), y.crop((0, 0, y.width, h))
    d = ImageChops.difference(x, y).convert('L').point(lambda v: 255 if v > 24 else 0)
    share = d.histogram()[255] / (d.width * d.height)
    if share:
        red = Image.new('RGB', y.size, (255, 0, 0)); Image.composite(red, y, d).save(os.path.join(b, 'diff-' + name))
    print(f'{name}: {share*100:.2f}% changed {"PASS" if share <= th else "CHANGED"}')
