"""Print a compact digest of one site's captured data for dossier writing.
Usage: python3 digest.py <site-id> [page-slug] [--text N]"""
import json, sys, os, glob, collections
site = sys.argv[1]; root = os.path.join(os.path.dirname(__file__), '..', 'evidence', site)
m = json.load(open(os.path.join(root, 'manifest.json')))
print('PAGES:'); [print(' ', c['status'], c['url'], c['viewport'], c['data']) for c in m['captures'] if c['viewport'].startswith('1440')]
slug = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else m['captures'][0]['data'].replace('_desktop.json', '')
tn = int(sys.argv[sys.argv.index('--text') + 1]) if '--text' in sys.argv else 1500
def load(vp): return json.load(open(os.path.join(root, 'data', f'{slug}_{vp}.json')))
d = load('desktop'); mo = load('mobile')
print('\n== ', slug, '|', d['title'], '| generator:', d['generator'], '| docHeight d/m:', d['docHeight'], mo['docHeight'])
print('meta:', d['metaDescription'])
print('FONTS loaded:', d['fontsLoaded'])
b = d['body']; print('BODY:', b['fontFamily'][:60], b['fontSize'], b['fontWeight'], b['lineHeight'], b['color'], b['backgroundColor'])
print('COLORS:', d['colors'][:10]); print('MAXWIDTHS:', d['maxWidths'][:6])
print('\nHEADINGS desktop (level font size/weight/lh/ls/transform color | text):')
for h in d['headings'][:22]:
    print(' ', h['level'], h['fontFamily'].split(',')[0][:22], h['fontSize'], h['fontWeight'], h['lineHeight'], h['letterSpacing'], h['textTransform'], h['color'], '|', h['text'][:80])
print('HEADINGS mobile sizes:', [(h['level'], h['fontSize']) for h in mo['headings'][:8]])
print('\nPARAGRAPH styles:', collections.Counter((p['fontFamily'].split(',')[0][:20], p['fontSize'], p['lineHeight'], p['color']) for p in d['paragraphs']).most_common(4))
print('\nSECTIONS (top,height,bg,img,padTop/Bot | heading):')
for s in d['sections'][:25]:
    print(' ', s['top'], s['height'], s['background'], 'IMG' if s['backgroundImage'] else '', s['paddingTop'], s['paddingBottom'], '|', (s['heading'] or '')[:60])
print('\nCTAs (text | href | radius | padding | bg | color | font):')
seen = set()
for c in d['ctas']:
    k = c['text']
    if k in seen: continue
    seen.add(k)
    if len(seen) > 18: break
    print(' ', c['text'][:34], '|', (c['href'] or '').replace(m['site']['url'], '')[:50], '|', c['borderRadius'], '|', c['padding'], '|', c['backgroundColor'], '|', c['color'], '|', c['fontSize'], c['fontWeight'], c['textTransform'], c['letterSpacing'])
print('\nNAV:', [(n['text'], n['href'].replace(m['site']['url'], '')[:30]) for n in d['nav'][:14]])
print('FORMS:', json.dumps(d['forms'])[:600])
imgs = d['images']; print('IMAGES:', len(imgs), [(i['w'], i['h'], i['natural'], i['objectFit']) for i in imgs[:8]])
print('\nTEXT:\n', d['fullText'][:tn])
