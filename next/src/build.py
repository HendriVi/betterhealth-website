# -*- coding: utf-8 -*-
"""Build the multi-page BetterHealth preview (German in next/, English in next/en/) from content.py.
Pages: home, approach, support, first visit, about, questions, contact, privacy, imprint.
Usage: python3 next/src/build.py"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import DE, EN, FACTS, LEGAL_DE, LEGAL_EN

ROOT = os.path.join(os.path.dirname(__file__), '..')
SL = {
    'de': dict(home='index.html', approach='ansatz.html', support='begleitung.html', visit='erster-termin.html', about='ueber-uns.html', faq='fragen.html', contact='kontakt.html', privacy='datenschutz.html', imprint='impressum.html'),
    'en': dict(home='index.html', approach='approach.html', support='support.html', visit='first-visit.html', about='about.html', faq='questions.html', contact='contact.html', privacy='privacy.html', imprint='imprint.html'),
}

def esc(s):
    return s if '<mark' in s else html.escape(s, quote=False)

def attr(s):
    return html.escape(s, quote=True)

# ------------------------------------------------------------------ the clinical map (home hero)
def map_svg(L, kind):
    names = [l[0] for l in L['layers']]
    def split(n):
        if ' & ' in n:
            a, b = n.split(' & ', 1); return [a, '& ' + b]
        return [n]
    if kind == 'wide':
        vb = '0 0 640 560'; c = (320, 280); r = 58
        boxes = [(200, 16, 240, 76), (442, 242, 190, 76), (200, 468, 240, 76), (8, 242, 190, 76)]
        spokes = ['M320 222 L320 92', 'M378 280 L442 280', 'M320 338 L320 468', 'M262 280 L198 280']
        rings = ['M440 54 Q537 54 537 242', 'M537 318 Q537 506 440 506', 'M200 506 Q103 506 103 318', 'M103 242 Q103 54 200 54']
    else:
        vb = '0 0 360 400'; c = (180, 200); r = 44
        boxes = [(12, 24, 160, 92), (188, 24, 160, 92), (12, 284, 160, 92), (188, 284, 160, 92)]
        spokes = ['M156 168 L112 116', 'M204 168 L248 116', 'M156 232 L112 284', 'M204 232 L248 284']
        rings = ['M172 70 L188 70', 'M172 330 L188 330']
    out = [f'<svg class="map map-{kind}" viewBox="{vb}" role="group" aria-label="{attr(L["map_label"])}" focusable="false">']
    for d in rings: out.append(f'<path class="ring" d="{d}"/>')
    for d in spokes: out.append(f'<path class="link" pathLength="1" d="{d}"/>')
    cx, cy = c
    out.append(f'<circle class="core" cx="{cx}" cy="{cy}" r="{r}"/>')
    for i, t in enumerate(L['map_center']):
        out.append(f'<text class="core-t" x="{cx}" y="{cy + (-4 if i == 0 else 16)}" text-anchor="middle">{esc(t)}</text>')
    for i, (x, y, w, h) in enumerate(boxes):
        lines = split(names[i])
        out.append(f'<g class="map-node" role="button" tabindex="0" data-layer="{i}" aria-label="{attr(names[i])}">')
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>')
        out.append(f'<text class="idx" x="{x + 16}" y="{y + 24}">0{i + 1}</text>')
        for j, ln in enumerate(lines):
            out.append(f'<text class="nt" x="{x + 16}" y="{y + 48 + j * 20}">{esc(ln)}</text>')
        out.append('</g>')
    out.append('</svg>')
    return ''.join(out)

# ------------------------------------------------------------------ sections (each returns an HTML string)
def sec_head(label, h2, lead=None, tag='h2'):
    return f'<div class="sec-head"><div class="label">{esc(label)}</div><{tag}>{esc(h2)}</{tag}>' + (f'<p class="sec-lead">{esc(lead)}</p>' if lead else '') + '</div>'

def link(href, text, cls='textlink'):
    return f'<a class="{cls}" href="{href}">{esc(text)} →</a>'

def seg_hero(L, S):
    h = [f'<section class="hero theme-dark"><div class="container hero-grid"><div class="hero-text"><div class="kicker">{esc(L["hero_label"])}</div><h1>{esc(L["h1"])}</h1><p class="lead">{esc(L["lead"])}</p>',
         f'<div class="hero-actions"><a class="btn btn-ice" href="{S["contact"]}">{esc(L["cta"])}</a><a class="textlink" href="{S["visit"]}">{esc(L["hero_link"])}</a></div></div>',
         '<div class="hero-map">' + map_svg(L, 'wide') + map_svg(L, 'tall') + f'<p class="map-caption" id="map-caption" aria-live="polite" data-default="{attr(L["map_hint"])}">{esc(L["map_hint"])}</p></div></div>',
         '<div class="container"><ul class="facts">']
    for v, lab in L['facts']: h.append(f'<li><span class="fv">{esc(v)}</span><span class="fl">{esc(lab)}</span></li>')
    h.append('</ul></div></section>')
    return ''.join(h)

def page_hero(L, key):
    label, h1, lead = L['pages'][key]
    return f'<section class="page-hero theme-dark"><div class="container"><div class="label">{esc(label)}</div><h1>{esc(h1)}</h1><p class="lead">{esc(lead)}</p></div></section>'

def seg_layers(L, S, more=False):
    h = [f'<section class="theme-dark" id="ansatz"><div class="container">{sec_head(L["layers_label"], L["layers_h2"], L["layers_lead"])}<ol class="layers">']
    for i, (t, d, lk) in enumerate(L['layers']):
        h.append(f'<li class="layer" data-layer="{i}"><span class="idx">0{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><p class="look"><span class="label">{esc(L["layers_look"])}</span> {esc(lk)}</p></li>')
    h.append(f'</ol><p class="note">{esc(L["layers_note"])}</p>' + (f'<p class="more">{link(S["approach"], L["more_approach"])}</p>' if more else '') + '</div></section>')
    return ''.join(h)

def seg_recognition(L):
    h = [f'<section class="theme-light" id="erkennen"><div class="container rail-grid"><aside class="rail"><div class="label">{esc(L["rec_label"])}</div><p class="rail-title">{esc(L["rec_rail_title"])}</p><p class="rail-text">{esc(L["rec_rail"])}</p></aside><div class="rail-main"><h2>{esc(L["rec_h2"])}</h2><ol class="rec">']
    for i, (a, q) in enumerate(L['rec']):
        h.append(f'<li><span class="idx">0{i+1}</span><p class="exp">{esc(a)}</p><p class="q"><span class="label">{esc(L["rec_q"])}</span> {esc(q)}</p></li>')
    h.append(f'</ol><p class="note">{esc(L["rec_note"])}</p></div></div></section>')
    return ''.join(h)

def seg_method(L):
    h = [f'<section class="theme-light" id="ablauf"><div class="container">{sec_head(L["method_label"], L["method_h2"], L["method_lead"])}<div class="method-grid"><ol class="steps">']
    for i, (t, d) in enumerate(L['steps']):
        h.append(f'<li><span class="idx">0{i+1}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>')
    h.append('</ol>')
    h.append(f'<figure class="sheet" aria-label="{attr(L["sheet_title"])} – {attr(L["sheet_kicker"])}"><div class="sheet-head"><span class="label">{esc(L["sheet_kicker"])}</span><span class="sheet-title">{esc(L["sheet_title"])}</span></div><p class="sheet-note">{esc(L["sheet_note"])}</p><div class="label sheet-sub">{esc(L["sheet_obs_title"])}</div><ol class="obs">')
    for i, (t, tag) in enumerate(L['sheet_obs']): h.append(f'<li><span class="idx">0{i+1}</span><span class="otxt">{esc(t)}</span><span class="tag">{esc(tag)}</span></li>')
    h.append(f'</ol><div class="label sheet-sub">{esc(L["sheet_plan_title"])}</div><p class="plan">{esc(L["sheet_plan"])}</p><p class="legend">{esc(L["sheet_legend"])}</p></figure></div></div></section>')
    return ''.join(h)

def seg_steps_teaser(L, S):
    h = [f'<section class="theme-light tight-top"><div class="container">{sec_head(L["method_label"], L["method_h2"], L["method_lead"])}<ol class="steps-row">']
    for i, (t, d) in enumerate(L['steps']):
        h.append(f'<li><span class="idx">0{i+1}</span><h3>{esc(t)}</h3></li>')
    h.append(f'</ol><p class="more">{link(S["visit"], L["more_visit"], "textlink-dark")}</p></div></section>')
    return ''.join(h)

def seg_concerns(L):
    h = [f'<section class="theme-dark" id="begleitung"><div class="container">{sec_head(L["conc_label"], L["conc_h2"], L["conc_lead"])}<div class="selector"><div class="sel-list" role="tablist" aria-orientation="vertical">']
    for i, (t, q, inc) in enumerate(L['conc']):
        h.append(f'<button class="sel-btn" role="tab" type="button" id="tab{i}" aria-controls="panel{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{esc(t)}</button>')
    h.append('</div><div class="sel-panels">')
    for i, (t, q, inc) in enumerate(L['conc']):
        h.append(f'<div class="sel-panel" role="tabpanel" id="panel{i}" aria-labelledby="tab{i}"><h3 class="sel-title">{esc(t)}</h3><p class="label">{esc(L["conc_q"])}</p><p class="sel-q">{esc(q)}</p><p class="label">{esc(L["conc_inc"])}</p><p>{esc(inc)}</p></div>')
    h.append(f'</div></div><p class="note">{esc(L["conc_note"])}</p></div></section>')
    return ''.join(h)

def seg_concerns_teaser(L, S):
    h = [f'<section class="theme-dark"><div class="container">{sec_head(L["conc_label"], L["conc_h2"], L["conc_lead"])}<ul class="teaser-list">']
    for t, q, inc in L['conc']:
        h.append(f'<li><h3>{esc(t)}</h3><p>{esc(q)}</p></li>')
    h.append(f'</ul><p class="more">{link(S["support"], L["more_support"])}</p></div></section>')
    return ''.join(h)

def seg_team(L):
    return (f'<section class="theme-light" id="team"><div class="container">{sec_head(L["team_label"], L["team_h2"])}<div class="team-grid"><div class="portrait" role="img" aria-label="{attr(L["portrait"])}"><span>{esc(L["portrait"])}</span></div>'
            f'<div class="team-text"><h3 class="name">{FACTS["clinician"]}</h3><p class="role">{L["team_role"]}</p><p>{esc(L["team_text"])}</p><div class="label">{esc(L["team_cred_title"])}</div><p>{L["team_cred"]}</p><p class="infl">{esc(L["team_infl"])}</p></div></div></div></section>')

def seg_team_teaser(L, S):
    return (f'<section class="theme-light"><div class="container">{sec_head(L["team_label"], L["team_h2"])}<div class="team-teaser"><div class="portrait small" role="img" aria-label="{attr(L["portrait"])}"><span>{esc(L["portrait"])}</span></div>'
            f'<div><h3 class="name">{FACTS["clinician"]}</h3><p class="role">{L["team_role"]}</p><p>{esc(L["team_text"])}</p><p class="more">{link(S["about"], L["more_about"], "textlink-dark")}</p></div></div></div></section>')

def seg_fees(L):
    h = [f'<section class="theme-dark" id="honorar"><div class="container">{sec_head(L["fee_label"], L["fee_h2"])}<div class="schedule"><p class="sched-draft">{L["fee_draft"]}</p><div class="sched-head"><span class="sched-name">{esc(L["fee_name"])}</span><span class="sched-fee">{esc(L["fee_amount"])}</span></div><dl>']
    h.append(f'<dt>{esc(L["fee_dur_k"])}</dt><dd>{esc(L["fee_dur"])}</dd><dt>{esc(L["fee_inc_k"])}</dt><dd><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in L['fee_inc']) + '</ul></dd>')
    h.append(f'<dt>{esc(L["fee_exc_k"])}</dt><dd><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in L['fee_exc']) + f'</ul></dd><dt>{esc(L["fee_next_k"])}</dt><dd>{esc(L["fee_next"])}</dd><dt>{esc(L["fee_terms_k"])}</dt><dd>{L["fee_terms"]}</dd></dl>')
    h.append(f'<p class="sched-note">{esc(L["fee_note"])}</p><a class="btn btn-graphite" href="{S_CONTACT[0]}">{esc(L["fee_cta"])}</a></div></div></section>')
    return ''.join(h)

def seg_fee_teaser(L, S):
    return (f'<section class="theme-dark"><div class="container">{sec_head(L["fee_label"], L["fee_h2"])}<div class="schedule teaser"><div class="sched-head"><span class="sched-name">{esc(L["fee_name"])}</span><span class="sched-fee">{esc(L["fee_amount"])}</span></div>'
            f'<p class="sched-line">{esc(L["teaser_fee_line"])}</p><p class="sched-draft">{L["fee_draft"]}</p><p class="more">{link(S["visit"], L["more_visit"], "textlink-dark")}</p></div></div></section>')

def seg_limits(L):
    return (f'<section class="theme-light" id="grenzen"><div class="container">{sec_head(L["lim_label"], L["lim_h2"])}<div class="lim-grid"><div><div class="label">{esc(L["lim_yes_k"])}</div><ul class="lim">' + ''.join(f'<li>{esc(x)}</li>' for x in L['lim_yes'])
            + f'</ul></div><div><div class="label">{esc(L["lim_no_k"])}</div><ul class="lim">' + ''.join(f'<li>{esc(x)}</li>' for x in L['lim_no'])
            + f'</ul></div></div><p class="orient">{esc(L["lim_orient"])}</p><p class="orient">{esc(L["lim_extra"])}</p><div class="emergency" role="note"><span class="label">{esc(L["emer_k"])}</span><p>{esc(L["emer"])}</p></div></div></section>')

def seg_faq(L):
    h = [f'<section class="theme-light alt" id="fragen"><div class="container"><div class="faq">']
    first = True
    for g, qs in L['faq_groups']:
        h.append(f'<div class="faq-group"><div class="label">{esc(g)}</div>')
        for q, a in qs:
            h.append(f'<details{" open" if first else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'); first = False
        h.append('</div>')
    h.append('</div></div></section>')
    return ''.join(h)

def seg_contact(L):
    tel = FACTS['phone_tel']; phone = FACTS['phone_display']
    h = ['<section class="theme-dark" id="kontakt"><div class="container"><div class="contact-grid"><div class="contact-info">']
    h.append(f'<div class="label">{esc(L["con_phone_k"])}</div><p><a class="bigtel" href="tel:{tel}">{phone}</a></p><div class="label">{esc(L["con_hours_k"])}</div><p>{L["con_hours"]}</p><div class="label">{esc(L["con_addr_k"])}</div><p>{esc(L["con_addr"])} {L["con_zip"]}</p></div>')
    h.append(f'<form class="form" id="contact-form" novalidate data-preview="{attr(L["form_preview"])}" data-err-name="{attr(L["form_error_name"])}" data-err-contact="{attr(L["form_error_contact"])}" data-endpoint="{attr(FACTS["form_endpoint"])}" data-sent="{attr(L["form_sent"])}" data-failed="{attr(L["form_failed"])}">')
    h.append(f'<div class="field"><label for="f-name">{esc(L["form_name"])} <span class="req">({esc(L["form_required"])})</span></label><input id="f-name" name="name" type="text" autocomplete="given-name" required aria-describedby="e-name"><p class="err" id="e-name" hidden></p></div>')
    h.append(f'<div class="field"><label for="f-contact">{esc(L["form_contact"])} <span class="req">({esc(L["form_required"])})</span></label><input id="f-contact" name="contact" type="text" autocomplete="email" required aria-describedby="e-contact"><p class="err" id="e-contact" hidden></p></div>')
    h.append(f'<div class="field"><label for="f-time">{esc(L["form_time"])}</label><select id="f-time" name="time">' + ''.join(f'<option>{esc(o)}</option>' for o in L['form_time_opts']) + '</select></div>')
    h.append(f'<div class="field"><label for="f-msg">{esc(L["form_msg"])}</label><textarea id="f-msg" name="message" rows="4" aria-describedby="h-msg"></textarea><p class="help" id="h-msg">{esc(L["form_msg_help"])}</p></div>')
    h.append(f'<div class="next"><span class="label">{esc(L["form_next_k"])}</span><p>{esc(L["form_next"])}</p></div><button class="btn btn-ice" type="submit">{esc(L["form_send"])}</button><p class="consent">{L["form_consent"]}</p><p class="form-status" id="form-status" role="status" hidden></p></form></div></div></section>')
    return ''.join(h)

def seg_cta_strip(L, S):
    tel = FACTS['phone_tel']; phone = FACTS['phone_display']
    return (f'<section class="theme-dark cta-strip"><div class="container"><h2>{esc(L["cta_strip_h2"])}</h2><p class="sec-lead">{esc(L["cta_strip_lead"])}</p>'
            f'<div class="hero-actions"><a class="btn btn-ice" href="{S["contact"]}">{esc(L["cta"])}</a><a class="bigtel small" href="tel:{tel}">{phone}</a></div></div></section>')

S_CONTACT = ['kontakt.html']  # set per language in build_pages

# ------------------------------------------------------------------ chrome
def header(L, S, current, lang_href, base):
    tel = FACTS['phone_tel']; phone = FACTS['phone_display']
    h = [f'<header class="site-header" id="top"><div class="container bar"><a class="brand" href="{S["home"]}" aria-label="BetterHealth">BetterHealth</a><nav class="nav" id="nav" aria-label="Main">']
    for k, t in L['nav']:
        h.append(f'<a href="{S[k]}"' + (' aria-current="page"' if k == current else '') + f'>{esc(t)}</a>')
    h.append(f'<a class="nav-lang" href="{lang_href}" hreflang="{L["other_lang"]}" lang="{L["other_lang"]}">{esc(L["other_label"])}</a></nav><div class="bar-actions"><a class="tel" href="tel:{tel}">{phone}</a>')
    h.append(f'<a class="btn btn-ice" href="{S["contact"]}"><span class="long">{esc(L["cta"])}</span><span class="short">{esc(L["cta_short"])}</span><span class="mini">{esc(L["cta_mini"])}</span></a>')
    h.append(f'<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" data-open="{attr(L["menu"])}" data-close="{attr(L["menu_close"])}">{esc(L["menu"])}</button></div></div></header>')
    return ''.join(h)

def footer(L, S, lang_href):
    tel = FACTS['phone_tel']; phone = FACTS['phone_display']
    pages = [k for k, _ in L['nav']] + ['faq']
    names = dict(L['nav']); names['faq'] = L['pages']['faq'][0]
    h = [f'<footer class="site-footer theme-dark"><div class="container foot-grid"><div><div class="brand">BetterHealth</div><p>{esc(FACTS["street"])}, {esc(FACTS["city"])}</p><p><a href="tel:{tel}">{phone}</a></p><p>{esc(L["foot_note"])}</p></div>']
    h.append(f'<div><div class="label">{esc(L["foot_pages"])}</div><ul class="foot-links">' + ''.join(f'<li><a href="{S[k]}">{esc(names[k])}</a></li>' for k in pages) + '</ul></div>')
    h.append(f'<div><div class="label">{esc(L["foot_legal"])}</div><ul class="foot-links"><li><a href="{S["privacy"]}">{esc(L["foot_privacy"])}</a></li><li><a href="{S["imprint"]}">{esc(L["foot_imprint"])}</a></li><li><a href="{lang_href}" hreflang="{L["other_lang"]}" lang="{L["other_lang"]}">{esc(L["other_label"])}</a></li></ul></div></div>')
    h.append(f'<div class="container"><p class="copy">{esc(L["foot_copy"])}</p></div></footer>')
    return ''.join(h)

def document(L, S, base, current, title, body, lang_href):
    return ('<!doctype html><html lang="%s" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">' % L['html_lang']
            + f'<title>{esc(title)}</title><meta name="description" content="{attr(L["desc"])}">'
            + f'<link rel="preload" href="{base}assets/fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{base}assets/css/main.css">'
            + '<script>document.documentElement.classList.remove("no-js");document.documentElement.classList.add("js")</script></head><body>'
            + f'<a class="skip" href="#main">{esc(L["skip"])}</a><div class="preview-banner" role="note">{esc(L["preview_banner"])}</div>'
            + header(L, S, current, lang_href, base) + '<main id="main">' + body + '</main>' + footer(L, S, lang_href)
            + f'<script src="{base}assets/js/main.js" defer></script></body></html>')

# ------------------------------------------------------------------ pages
def pages_for(L, S):
    return {
        'home': seg_hero(L, S) + seg_layers(L, S, more=True) + seg_recognition(L) + seg_steps_teaser(L, S) + seg_concerns_teaser(L, S) + seg_team_teaser(L, S) + seg_fee_teaser(L, S) + seg_cta_strip(L, S).replace('theme-dark cta-strip', 'theme-dark cta-strip tight-top'),
        'approach': page_hero(L, 'approach') + seg_layers(L, S) + seg_recognition(L) + seg_cta_strip(L, S),
        'support': page_hero(L, 'support') + seg_concerns(L) + seg_limits(L) + seg_cta_strip(L, S),
        'visit': page_hero(L, 'visit') + seg_method(L) + seg_fees(L) + seg_cta_strip(L, S).replace('theme-dark cta-strip', 'theme-dark cta-strip tight-top'),
        'about': page_hero(L, 'about') + seg_team(L) + seg_cta_strip(L, S),
        'faq': page_hero(L, 'faq') + seg_faq(L) + seg_cta_strip(L, S),
        'contact': page_hero(L, 'contact') + seg_contact(L),
    }

def render_legal(L, LG, kind, S, base, lang_href):
    d = LG[kind]
    body = (f'<section class="theme-light legal"><div class="container"><div class="legal-body"><h1>{esc(d["title"])}</h1><p>{LG["draft"]}</p>'
            + ''.join(f'<h2>{esc(t)}</h2><p>{txt}</p>' for t, txt in d['blocks'])
            + f'<p><a class="textlink-dark" href="{S["home"]}">{esc(LG["back"])}</a></p></div></div></section>')
    return document(L, S, base, None, f'{d["title"]} · BetterHealth', body, lang_href)

def build():
    os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
    written = []
    for L, LG, lang, base, outdir in ((DE, LEGAL_DE, 'de', '', ROOT), (EN, LEGAL_EN, 'en', '../', os.path.join(ROOT, 'en'))):
        S = SL[lang]; O = SL['en' if lang == 'de' else 'de']; S_CONTACT[0] = S['contact']
        other_prefix = 'en/' if lang == 'de' else '../'
        for key, body in pages_for(L, S).items():
            title = 'BetterHealth · ' + L['pages'][key][0] if key != 'home' else L['title']
            lang_href = other_prefix + O[key]
            open(os.path.join(outdir, S[key]), 'w', encoding='utf8').write(document(L, S, base, key if key != 'home' else None, title, body, lang_href)); written.append(S[key])
        for kind in ('privacy', 'imprint'):
            open(os.path.join(outdir, S[kind]), 'w', encoding='utf8').write(render_legal(L, LG, kind, S, base, other_prefix + O[kind])); written.append(S[kind])
    print('built', len(written), 'pages')

if __name__ == '__main__':
    build()
