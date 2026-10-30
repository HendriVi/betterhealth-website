# -*- coding: utf-8 -*-
"""Build the German (next/index.html) and English (next/en/index.html) preview pages from content.py.
Usage: python3 next/src/build.py"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import DE, EN, FACTS

ROOT = os.path.join(os.path.dirname(__file__), '..')

def esc(s):
    return s if '<mark' in s else html.escape(s, quote=False)

def attr(s):
    return html.escape(s, quote=True)

def map_svg(L, kind):
    """kind = 'wide' (desktop ring layout) or 'tall' (mobile 2x2 layout). Text is HTML-escaped via esc()."""
    names = [l[0] for l in L['layers']]
    def split(n):
        if ' & ' in n:
            a, b = n.split(' & ', 1); return [a, '& ' + b]
        return [n]
    if kind == 'wide':
        vb = '0 0 640 560'; c = (320, 280); r = 58
        boxes = [(200, 16, 240, 76), (442, 242, 190, 76), (200, 468, 240, 76), (8, 242, 190, 76)]  # top, right, bottom, left
        spokes = [('M320 222 L320 92'), ('M378 280 L442 280'), ('M320 338 L320 468'), ('M262 280 L198 280')]
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

def render(L, base):
    n = L['nav']
    other_href = ('en/' if L['lang'] == 'de' else '../')
    tel = FACTS['phone_tel']; phone = FACTS['phone_display']
    h = []
    A = h.append
    A(f'<!doctype html><html lang="{L["html_lang"]}" class="no-js"><head><meta charset="utf-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1">')
    A('<meta name="robots" content="noindex, nofollow">')
    A(f'<title>{esc(L["title"])}</title><meta name="description" content="{attr(L["desc"])}">')
    de_href = '' if L['lang'] == 'de' else '../'
    A(f'<link rel="alternate" hreflang="de" href="{de_href}"><link rel="alternate" hreflang="en" href="{"en/" if L["lang"] == "de" else ""}">')
    A(f'<link rel="preload" href="{base}assets/fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>')
    A(f'<link rel="stylesheet" href="{base}assets/css/main.css">')
    A('<script>document.documentElement.classList.remove("no-js");document.documentElement.classList.add("js")</script>')
    A('</head><body>')
    A(f'<a class="skip" href="#main">{esc(L["skip"])}</a>')
    A(f'<div class="preview-banner" role="note">{esc(L["preview_banner"])}</div>')
    # header
    A('<header class="site-header" id="top"><div class="container bar">')
    A(f'<a class="brand" href="#top" aria-label="BetterHealth">BetterHealth</a>')
    A('<nav class="nav" id="nav" aria-label="Main">')
    for k, t in n: A(f'<a href="#{k}">{esc(t)}</a>')
    A(f'<a class="nav-lang" href="{other_href}" hreflang="{L["other_lang"]}" lang="{L["other_lang"]}">{esc(L["other_label"])}</a>')
    A('</nav><div class="bar-actions">')
    A(f'<a class="tel" href="tel:{tel}">{phone}</a>')
    A(f'<a class="btn btn-ice" href="#kontakt"><span class="long">{esc(L["cta"])}</span><span class="short">{esc(L["cta_short"])}</span><span class="mini">{esc(L["cta_mini"])}</span></a>')
    A(f'<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" data-open="{attr(L["menu"])}" data-close="{attr(L["menu_close"])}">{esc(L["menu"])}</button>')
    A('</div></div></header><main id="main">')
    # hero
    A('<section class="hero theme-dark"><div class="container hero-grid"><div class="hero-text">')
    A(f'<p class="kicker">{esc(L["hero_label"])}</p>' if False else f'<div class="kicker">{esc(L["hero_label"])}</div>')
    A(f'<h1>{esc(L["h1"])}</h1><p class="lead">{esc(L["lead"])}</p>')
    A(f'<div class="hero-actions"><a class="btn btn-ice" href="#kontakt">{esc(L["cta"])}</a><a class="textlink" href="#ablauf">{esc(L["hero_link"])}</a></div></div>')
    A('<div class="hero-map">' + map_svg(L, 'wide') + map_svg(L, 'tall') + f'<p class="map-caption" id="map-caption" aria-live="polite" data-default="{attr(L["map_hint"])}">{esc(L["map_hint"])}</p></div></div>')
    A('<div class="container"><ul class="facts">')
    for v, lab in L['facts']: A(f'<li><span class="fv">{esc(v)}</span><span class="fl">{esc(lab)}</span></li>')
    A('</ul></div></section>')
    # layers
    A(f'<section class="theme-dark" id="ansatz"><div class="container"><div class="sec-head"><div class="label">{esc(L["layers_label"])}</div><h2>{esc(L["layers_h2"])}</h2><p class="sec-lead">{esc(L["layers_lead"])}</p></div><ol class="layers">')
    for i, (t, d, lk) in enumerate(L['layers']):
        A(f'<li class="layer" data-layer="{i}"><span class="idx">0{i+1}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><p class="look"><span class="label">{esc(L["layers_look"])}</span> {esc(lk)}</p></li>')
    A(f'</ol><p class="note">{esc(L["layers_note"])}</p></div></section>')
    # recognition
    A(f'<section class="theme-light" id="erkennen"><div class="container rail-grid"><aside class="rail"><div class="label">{esc(L["rec_label"])}</div><p class="rail-title">{esc(L["rec_rail_title"])}</p><p class="rail-text">{esc(L["rec_rail"])}</p></aside><div class="rail-main"><h2>{esc(L["rec_h2"])}</h2><ol class="rec">')
    for i, (a, q) in enumerate(L['rec']):
        A(f'<li><span class="idx">0{i+1}</span><p class="exp">{esc(a)}</p><p class="q"><span class="label">{esc(L["rec_q"])}</span> {esc(q)}</p></li>')
    A(f'</ol><p class="note">{esc(L["rec_note"])}</p></div></div></section>')
    # method + sheet
    A(f'<section class="theme-light" id="ablauf"><div class="container"><div class="sec-head"><div class="label">{esc(L["method_label"])}</div><h2>{esc(L["method_h2"])}</h2></div><div class="method-grid"><ol class="steps">')
    for i, (t, d) in enumerate(L['steps']):
        A(f'<li><span class="idx">0{i+1}</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>')
    A('</ol>')
    A(f'<figure class="sheet" aria-label="{attr(L["sheet_title"])} – {attr(L["sheet_kicker"])}"><div class="sheet-head"><span class="label">{esc(L["sheet_kicker"])}</span><span class="sheet-title">{esc(L["sheet_title"])}</span></div><p class="sheet-note">{esc(L["sheet_note"])}</p>')
    A(f'<div class="label sheet-sub">{esc(L["sheet_obs_title"])}</div><ol class="obs">')
    for i, (t, tag) in enumerate(L['sheet_obs']): A(f'<li><span class="idx">0{i+1}</span><span class="otxt">{esc(t)}</span><span class="tag">{esc(tag)}</span></li>')
    A(f'</ol><div class="label sheet-sub">{esc(L["sheet_plan_title"])}</div><p class="plan">{esc(L["sheet_plan"])}</p><p class="legend">{esc(L["sheet_legend"])}</p></figure></div></div></section>')
    # concerns
    A(f'<section class="theme-dark" id="begleitung"><div class="container"><div class="sec-head"><div class="label">{esc(L["conc_label"])}</div><h2>{esc(L["conc_h2"])}</h2><p class="sec-lead">{esc(L["conc_lead"])}</p></div><div class="selector">')
    A('<div class="sel-list" role="tablist" aria-orientation="vertical">')
    for i, (t, q, inc) in enumerate(L['conc']):
        A(f'<button class="sel-btn" role="tab" type="button" id="tab{i}" aria-controls="panel{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{esc(t)}</button>')
    A('</div><div class="sel-panels">')
    for i, (t, q, inc) in enumerate(L['conc']):
        A(f'<div class="sel-panel" role="tabpanel" id="panel{i}" aria-labelledby="tab{i}"{"" if i == 0 else ""}><h3 class="sel-title">{esc(t)}</h3><p class="label">{esc(L["conc_q"])}</p><p class="sel-q">{esc(q)}</p><p class="label">{esc(L["conc_inc"])}</p><p>{esc(inc)}</p></div>')
    A(f'</div></div><p class="note">{esc(L["conc_note"])}</p></div></section>')
    # team
    A(f'<section class="theme-light" id="team"><div class="container"><div class="sec-head"><div class="label">{esc(L["team_label"])}</div><h2>{esc(L["team_h2"])}</h2></div><div class="team-grid"><div class="portrait" role="img" aria-label="{attr(L["portrait"])}"><span>{esc(L["portrait"])}</span></div><div class="team-text"><h3 class="name">{FACTS["clinician"]}</h3><p class="role">{L["team_role"]}</p><p>{esc(L["team_text"])}</p><div class="label">{esc(L["team_cred_title"])}</div><p>{L["team_cred"]}</p><p class="infl">{esc(L["team_infl"])}</p></div></div></div></section>')
    # fees
    A(f'<section class="theme-dark" id="honorar"><div class="container"><div class="sec-head"><div class="label">{esc(L["fee_label"])}</div><h2>{esc(L["fee_h2"])}</h2></div><div class="schedule"><div class="sched-head"><span class="sched-name">{esc(L["fee_name"])}</span><span class="sched-fee">{esc(L["fee_amount"])}</span></div><dl>')
    A(f'<dt>{esc(L["fee_dur_k"])}</dt><dd>{esc(L["fee_dur"])}</dd>')
    A(f'<dt>{esc(L["fee_inc_k"])}</dt><dd><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in L['fee_inc']) + '</ul></dd>')
    A(f'<dt>{esc(L["fee_exc_k"])}</dt><dd><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in L['fee_exc']) + '</ul></dd>')
    A(f'<dt>{esc(L["fee_next_k"])}</dt><dd>{esc(L["fee_next"])}</dd><dt>{esc(L["fee_terms_k"])}</dt><dd>{L["fee_terms"]}</dd></dl>')
    A(f'<p class="sched-note">{esc(L["fee_note"])}</p><a class="btn btn-graphite" href="#kontakt">{esc(L["fee_cta"])}</a></div></div></section>')
    # limits
    A(f'<section class="theme-light" id="grenzen"><div class="container"><div class="sec-head"><div class="label">{esc(L["lim_label"])}</div><h2>{esc(L["lim_h2"])}</h2></div><div class="lim-grid"><div><div class="label">{esc(L["lim_yes_k"])}</div><ul class="lim">' + ''.join(f'<li>{esc(x)}</li>' for x in L['lim_yes']) + f'</ul></div><div><div class="label">{esc(L["lim_no_k"])}</div><ul class="lim">' + ''.join(f'<li>{esc(x)}</li>' for x in L['lim_no']) + f'</ul></div></div><p class="orient">{esc(L["lim_orient"])}</p><div class="emergency" role="note"><span class="label">{esc(L["emer_k"])}</span><p>{esc(L["emer"])}</p></div></div></section>')
    # faq
    A(f'<section class="theme-light alt" id="fragen"><div class="container"><div class="sec-head"><div class="label">{esc(L["faq_label"])}</div><h2>{esc(L["faq_h2"])}</h2></div><div class="faq">')
    first = True
    for g, qs in L['faq_groups']:
        A(f'<div class="faq-group"><div class="label">{esc(g)}</div>')
        for q, a in qs:
            A(f'<details{" open" if first else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'); first = False
        A('</div>')
    A('</div></div></section>')
    # contact
    A(f'<section class="theme-dark" id="kontakt"><div class="container"><div class="sec-head"><div class="label">{esc(L["con_label"])}</div><h2>{esc(L["con_h2"])}</h2><p class="sec-lead">{esc(L["con_lead"])}</p></div><div class="contact-grid"><div class="contact-info">')
    A(f'<div class="label">{esc(L["con_phone_k"])}</div><p><a class="bigtel" href="tel:{tel}">{phone}</a></p>')
    A(f'<div class="label">{esc(L["con_hours_k"])}</div><p>{L["con_hours"]}</p>')
    A(f'<div class="label">{esc(L["con_addr_k"])}</div><p>{esc(L["con_addr"])} {L["con_zip"]}</p></div>')
    A(f'<form class="form" id="contact-form" novalidate data-preview="{attr(L["form_preview"])}" data-err-name="{attr(L["form_error_name"])}" data-err-contact="{attr(L["form_error_contact"])}">')
    A(f'<div class="field"><label for="f-name">{esc(L["form_name"])} <span class="req">({esc(L["form_required"])})</span></label><input id="f-name" name="name" type="text" autocomplete="given-name" required aria-describedby="e-name"><p class="err" id="e-name" hidden></p></div>')
    A(f'<div class="field"><label for="f-contact">{esc(L["form_contact"])} <span class="req">({esc(L["form_required"])})</span></label><input id="f-contact" name="contact" type="text" autocomplete="email" required aria-describedby="e-contact"><p class="err" id="e-contact" hidden></p></div>')
    A(f'<div class="field"><label for="f-time">{esc(L["form_time"])}</label><select id="f-time" name="time">' + ''.join(f'<option>{esc(o)}</option>' for o in L['form_time_opts']) + '</select></div>')
    A(f'<div class="field"><label for="f-msg">{esc(L["form_msg"])}</label><textarea id="f-msg" name="message" rows="4" aria-describedby="h-msg"></textarea><p class="help" id="h-msg">{esc(L["form_msg_help"])}</p></div>')
    A(f'<div class="next"><span class="label">{esc(L["form_next_k"])}</span><p>{esc(L["form_next"])}</p></div>')
    A(f'<button class="btn btn-ice" type="submit">{esc(L["form_send"])}</button><p class="consent">{L["form_consent"]}</p><p class="form-status" id="form-status" role="status" hidden></p></form></div></div></section>')
    A('</main>')
    # footer
    A(f'<footer class="site-footer theme-dark"><div class="container foot-grid"><div><div class="brand">BetterHealth</div><p>{esc(FACTS["street"])}, {esc(FACTS["city"])}</p><p><a href="tel:{tel}">{phone}</a></p></div>')
    A(f'<div><p>{esc(L["foot_note"])}</p></div><div class="foot-links"><span>{esc(L["foot_privacy"])} <em>({esc(L["foot_soon"])})</em></span><span>{esc(L["foot_imprint"])} <em>({esc(L["foot_soon"])})</em></span><a href="{other_href}" hreflang="{L["other_lang"]}" lang="{L["other_lang"]}">{esc(L["other_label"])}</a></div></div>')
    A(f'<div class="container"><p class="copy">{esc(L["foot_copy"])}</p></div></footer>')
    A(f'<script src="{base}assets/js/main.js" defer></script></body></html>')
    return ''.join(h)

if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'en'), exist_ok=True)
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf8').write(render(DE, ''))
    open(os.path.join(ROOT, 'en', 'index.html'), 'w', encoding='utf8').write(render(EN, '../'))
    print('built next/index.html and next/en/index.html')
