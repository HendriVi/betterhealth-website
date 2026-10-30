"""Join <page>_desktop_frames/NNN_<scrollY>.jpg into <page>_desktop_stitched.jpg (frames placed at their real scrollY).
Fixed headers repeat in each frame; that is expected. Usage: stitch.py <site-id>"""
import os, sys, glob
from PIL import Image
site = sys.argv[1]; sd = os.path.join(os.path.dirname(__file__), '..', 'evidence', site, 'screens')
for fd in sorted(glob.glob(os.path.join(sd, '*_desktop_frames'))):
    frames = sorted(glob.glob(os.path.join(fd, '*.jpg')))
    if not frames: continue
    items = [(int(os.path.basename(f).split('_')[1].split('.')[0]), f) for f in frames]
    w, h = Image.open(items[0][1]).size
    total = max(y for y, _ in items) + h
    canvas = Image.new('RGB', (w, min(total, 65000)))
    for y, f in items:
        if y < 65000: canvas.paste(Image.open(f), (0, y))
    out = fd.replace('_frames', '_stitched') + '.jpg'; canvas.save(out, quality=80, optimize=True); print(out, canvas.size)
