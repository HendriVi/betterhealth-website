"""Shrink a full-page screenshot into chunks for review: preview.py <site> <slug> <viewport> [width] [chunk_h]
Writes to the session scratchpad, never into evidence/."""
import sys, os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
site, slug, vp = sys.argv[1:4]; w = int(sys.argv[4]) if len(sys.argv) > 4 else 800; ch = int(sys.argv[5]) if len(sys.argv) > 5 else 1800
src = os.path.join(os.path.dirname(__file__), '..', 'evidence', site, 'screens', f'{slug}_{vp}_full.jpg')
out = os.environ.get('PREVIEW_DIR', '/tmp/claude-0/-home-user-betterhealth-website/db52c01a-2e28-5822-a0ca-de470b954790/scratchpad/prev')
os.makedirs(out, exist_ok=True)
im = Image.open(src).convert('RGB'); im = im.resize((w, int(im.height * w / im.width)))
n = 0
for y in range(0, im.height, ch):
    p = os.path.join(out, f'{site}_{slug}_{vp}_{n}.jpg'); im.crop((0, y, w, min(y + ch, im.height))).save(p, quality=80); print(p); n += 1
