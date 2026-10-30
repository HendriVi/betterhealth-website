"""Convert full-page PNG captures to JPEG (q82) to keep the repo small.
Viewport PNGs are kept lossless. Pages taller than the JPEG limit are cropped
at 65000 px and the manifest records that."""
import json, os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
root = os.path.join(os.path.dirname(__file__), '..', 'evidence')
for site in sorted(os.listdir(root)):
    mpath = os.path.join(root, site, 'manifest.json')
    if not os.path.exists(mpath): continue
    m = json.load(open(mpath)); sdir = os.path.join(root, site, 'screens')
    for c in m['captures']:
        new = []
        for f in c['screens']:
            if f.endswith('_full.png') and os.path.exists(os.path.join(sdir, f)):
                im = Image.open(os.path.join(sdir, f)).convert('RGB')
                if im.height > 65000:
                    c['fullPageCroppedAt'] = 65000; im = im.crop((0, 0, im.width, 65000))
                out = f[:-4] + '.jpg'
                im.save(os.path.join(sdir, out), 'JPEG', quality=82, optimize=True)
                os.remove(os.path.join(sdir, f)); new.append(out)
            else: new.append(f)
        c['screens'] = new
    json.dump(m, open(mpath, 'w'), indent=2)
