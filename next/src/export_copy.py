# -*- coding: utf-8 -*-
"""Export all website copy (German | English) from content.py to an editable Word document.
Each row carries the content key so edits can be imported back.  Usage: python3 next/src/export_copy.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import DE, EN, FACTS, LEGAL_DE, LEGAL_EN
from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'copy', 'BetterHealth-Website-Copy.docx')

def get(L, path):
    cur = L
    for tok in [t for t in re.split(r"[.\[\]]", path) if t]:
        cur = cur[int(tok)] if tok.isdigit() else cur[tok]
    return cur

def clean(s):
    """HTML (placeholders) -> list of (text, is_placeholder)."""
    parts = re.split(r'(<mark class="ph">.*?</mark>)', s)
    out = []
    for p in parts:
        if p.startswith('<mark'):
            out.append((re.sub(r'<[^>]+>', '', p), True))
        elif p:
            out.append((re.sub(r'<[^>]+>', '', p).replace('&amp;', '&'), False))
    return out

SECTIONS = []
def section(title, appears, rows, note=None):
    SECTIONS.append((title, appears, rows, note))

def r(label, path):          # row from a top-level path present in both languages
    return (label, path, get(DE, path), get(EN, path))

def lst(label, path, n):     # numbered rows for list items
    return [(f'{label} {i + 1}', f'{path}[{i}]', get(DE, f'{path}[{i}]'), get(EN, f'{path}[{i}]')) for i in range(n)]

def pairs(label_a, label_b, path, n, extra=None):
    rows = []
    for i in range(n):
        rows.append((f'{label_a} {i + 1}', f'{path}[{i}][0]', get(DE, f'{path}[{i}][0]'), get(EN, f'{path}[{i}][0]')))
        rows.append((f'{label_b} {i + 1}', f'{path}[{i}][1]', get(DE, f'{path}[{i}][1]'), get(EN, f'{path}[{i}][1]')))
        if extra:
            rows.append((f'{extra} {i + 1}', f'{path}[{i}][2]', get(DE, f'{path}[{i}][2]'), get(EN, f'{path}[{i}][2]')))
    return rows

section('Site-wide: header, buttons and footer', 'Every page', [
    r('Preview banner (remove before launch)', 'preview_banner'), r('Skip link (accessibility)', 'skip'),
    *[(f'Navigation link {i + 1}', f'nav[{i}][1]', DE['nav'][i][1], EN['nav'][i][1]) for i in range(5)],
    r('Language switch label (shows the other language)', 'other_label'),
    r('Main button (long)', 'cta'), r('Main button in header (medium screens)', 'cta_short'), r('Main button in header (phones)', 'cta_mini'),
    r('Menu button (phones)', 'menu'), r('Menu close button', 'menu_close'),
    r('Footer heading: pages', 'foot_pages'), r('Footer heading: legal', 'foot_legal'), r('Footer link: privacy', 'foot_privacy'), r('Footer link: imprint', 'foot_imprint'),
    r('Footer emergency note', 'foot_note'), r('Footer copyright', 'foot_copy'),
], 'Phone number, address and the clinician name are facts set in the source (see the last section).')

section('Page titles and introductions', 'Top of every page except Home', [
    r('Browser title: Home', 'title'), r('Search-engine description (all pages)', 'desc'),
    *[(f'{nm}: label', f'pages[{k}][0]', DE['pages'][k][0], EN['pages'][k][0]) if False else None for nm, k in []],
] + [x for k, nm in (('approach', 'Approach page'), ('support', 'Support page'), ('visit', 'First-visit page'), ('about', 'About page'), ('faq', 'Questions page'), ('contact', 'Contact page'))
     for x in ((f'{nm}: small label', f'pages.{k}.0', DE['pages'][k][0], EN['pages'][k][0]), (f'{nm}: main headline', f'pages.{k}.1', DE['pages'][k][1], EN['pages'][k][1]), (f'{nm}: intro text', f'pages.{k}.2', DE['pages'][k][2], EN['pages'][k][2]))])

section('Home: opening screen', 'Home', [
    r('Small label above headline', 'hero_label'), r('Main headline', 'h1'), r('Intro text', 'lead'), r('Link under the main button', 'hero_link'),
    *[(f'Fact tile {i + 1}: big text', f'facts[{i}][0]', DE['facts'][i][0], EN['facts'][i][0]) for i in range(4)],
] + [x for i in range(4) for x in ((f'Fact tile {i + 1}: small text', f'facts[{i}][1]', DE['facts'][i][1], EN['facts'][i][1]),)] + [
    r('Map: accessible description', 'map_label'), r('Map: centre, line 1', 'map_center[0]'), r('Map: centre, line 2', 'map_center[1]'), r('Map: hint under the map', 'map_hint'),
])

section('Four layers', 'Home and Approach page', [
    r('Small label', 'layers_label'), r('Headline', 'layers_h2'), r('Intro text', 'layers_lead'),
] + [x for i in range(4) for x in ((f'Layer {i + 1}: name (also shown in the map)', f'layers[{i}][0]', DE['layers'][i][0], EN['layers'][i][0]), (f'Layer {i + 1}: explanation', f'layers[{i}][1]', DE['layers'][i][1], EN['layers'][i][1]), (f'Layer {i + 1}: what we look at', f'layers[{i}][2]', DE['layers'][i][2], EN['layers'][i][2]))] + [
    r('Label "what we look at"', 'layers_look'), r('Note under the layers', 'layers_note'), r('Link to Approach page (Home)', 'more_approach'),
])

section('Recognition', 'Home and Approach page', [
    r('Small label', 'rec_label'), r('Headline', 'rec_h2'), r('Margin note title', 'rec_rail_title'), r('Margin note text', 'rec_rail'),
] + [x for i in range(4) for x in ((f'Experience {i + 1}', f'rec[{i}][0]', DE['rec'][i][0], EN['rec'][i][0]), (f'Question behind it {i + 1}', f'rec[{i}][1]', DE['rec'][i][1], EN['rec'][i][1]))] + [
    r('Label "the question behind it"', 'rec_q'), r('Note under the list', 'rec_note'),
])

section('Process and the example hypothesis', 'Home (steps only) and First-visit page', [
    r('Small label', 'method_label'), r('Headline', 'method_h2'), r('Short promise under the headline', 'method_lead'),
] + [x for i in range(5) for x in ((f'Step {i + 1}: title', f'steps[{i}][0]', DE['steps'][i][0], EN['steps'][i][0]), (f'Step {i + 1}: text', f'steps[{i}][1]', DE['steps'][i][1], EN['steps'][i][1]))] + [
    r('Link to First-visit page (Home)', 'more_visit'),
    r('Example sheet: small label', 'sheet_kicker'), r('Example sheet: title', 'sheet_title'), r('Example sheet: disclaimer', 'sheet_note'), r('Example sheet: observations heading', 'sheet_obs_title'),
] + [x for i in range(4) for x in ((f'Example observation {i + 1}', f'sheet_obs[{i}][0]', DE['sheet_obs'][i][0], EN['sheet_obs'][i][0]), (f'Example observation {i + 1}: confidence tag', f'sheet_obs[{i}][1]', DE['sheet_obs'][i][1], EN['sheet_obs'][i][1]))] + [
    r('Example sheet: plan heading', 'sheet_plan_title'), r('Example sheet: plan', 'sheet_plan'), r('Example sheet: legend', 'sheet_legend'),
])

section('What we support', 'Home (titles and questions) and Support page', [
    r('Small label', 'conc_label'), r('Headline', 'conc_h2'), r('Intro text', 'conc_lead'),
] + [x for i in range(7) for x in ((f'Area {i + 1}: title', f'conc[{i}][0]', DE['conc'][i][0], EN['conc'][i][0]), (f'Area {i + 1}: question', f'conc[{i}][1]', DE['conc'][i][1], EN['conc'][i][1]), (f'Area {i + 1}: what the assessment covers', f'conc[{i}][2]', DE['conc'][i][2], EN['conc'][i][2]))] + [
    r('Label "the question"', 'conc_q'), r('Label "what the assessment covers"', 'conc_inc'), r('Note under the list', 'conc_note'), r('Link to Support page (Home)', 'more_support'),
])

section('Who we suit, limits, emergencies', 'Support page', [
    r('Small label', 'lim_label'), r('Headline', 'lim_h2'), r('Heading: a good fit if', 'lim_yes_k'),
    *lst('Good fit', 'lim_yes', 3), r('Heading: not a fit if', 'lim_no_k'), *lst('Not a fit', 'lim_no', 3),
    r('Orientation sentence', 'lim_orient'), r('Honesty sentence about extra investigations', 'lim_extra'), r('Emergency box: heading', 'emer_k'), r('Emergency box: text', 'emer'),
])

section('The physician', 'Home (short) and About page', [
    r('Small label', 'team_label'), r('Headline', 'team_h2'), r('Professional title (under the name)', 'team_role'), r('Text about her role', 'team_text'),
    r('Heading: training', 'team_cred_title'), r('Training line', 'team_cred'), r('Influences sentence', 'team_infl'), r('Photo placeholder text', 'portrait'), r('Link to About page (Home)', 'more_about'),
], 'The name "' + FACTS['clinician'] + '" is a fact set in the source.')

section('Fee and first assessment', 'Home (short) and First-visit page', [
    r('Small label', 'fee_label'), r('Headline', 'fee_h2'), r('Draft flag (remove when confirmed)', 'fee_draft'), r('Offer name', 'fee_name'), r('Fee', 'fee_amount'),
    r('Heading: scope', 'fee_dur_k'), r('Scope', 'fee_dur'), r('Heading: included', 'fee_inc_k'), *lst('Included', 'fee_inc', 4),
    r('Heading: not included', 'fee_exc_k'), *lst('Not included', 'fee_exc', 2), r('Heading: after that', 'fee_next_k'), r('After the first assessment', 'fee_next'),
    r('Heading: payment and cancellation', 'fee_terms_k'), r('Payment and cancellation terms', 'fee_terms'), r('Note on self-pay', 'fee_note'), r('Button', 'fee_cta'),
    r('Home teaser sentence', 'teaser_fee_line'),
])

section('Questions and answers', 'Questions page', [
    r('Small label', 'faq_label'), r('Headline (not shown as text on the page; see page introduction)', 'faq_h2'),
] + [x for g in range(3) for x in ((f'Group {g + 1}: title', f'faq_groups[{g}][0]', DE['faq_groups'][g][0], EN['faq_groups'][g][0]),) + tuple(y for q in range(len(DE['faq_groups'][g][1])) for y in ((f'Group {g + 1}, question {q + 1}', f'faq_groups[{g}][1][{q}][0]', DE['faq_groups'][g][1][q][0], EN['faq_groups'][g][1][q][0]), (f'Group {g + 1}, answer {q + 1}', f'faq_groups[{g}][1][{q}][1]', DE['faq_groups'][g][1][q][1], EN['faq_groups'][g][1][q][1])))])

section('Contact page and form', 'Contact page', [
    r('Heading: telephone', 'con_phone_k'), r('Heading: availability', 'con_hours_k'), r('Opening hours', 'con_hours'), r('Heading: practice address', 'con_addr_k'), r('Address line', 'con_addr'), r('Postcode', 'con_zip'),
    r('Field label: first name', 'form_name'), r('Field label: telephone or email', 'form_contact'), r('Marker: required', 'form_required'), r('Field label: preferred time', 'form_time'),
    *lst('Preferred time option', 'form_time_opts', 4), r('Field label: message', 'form_msg'), r('Help text under message', 'form_msg_help'),
    r('Heading: what happens next', 'form_next_k'), r('What happens next', 'form_next'), r('Send button', 'form_send'), r('Consent sentence', 'form_consent'),
    r('Error: first name missing', 'form_error_name'), r('Error: contact missing', 'form_error_contact'),
    r('Message after sending', 'form_sent'), r('Message if sending fails', 'form_failed'), r('Message while the form is not connected (remove at launch)', 'form_preview'),
])

section('Closing call to action', 'Home, Approach, Support, First visit, About, Questions', [r('Headline', 'cta_strip_h2'), r('Text', 'cta_strip_lead')])

def legal_rows(kind):
    rows = [('Page title', f'legal.{kind}.title', LEGAL_DE[kind]['title'], LEGAL_EN[kind]['title']), ('Draft flag (remove when reviewed)', 'legal.draft', LEGAL_DE['draft'], LEGAL_EN['draft'])]
    for i in range(len(LEGAL_DE[kind]['blocks'])):
        rows.append((f'Section {i + 1}: heading', f'legal.{kind}.blocks[{i}][0]', LEGAL_DE[kind]['blocks'][i][0], LEGAL_EN[kind]['blocks'][i][0]))
        rows.append((f'Section {i + 1}: text', f'legal.{kind}.blocks[{i}][1]', LEGAL_DE[kind]['blocks'][i][1], LEGAL_EN[kind]['blocks'][i][1]))
    return rows
section('Privacy page (draft, needs legal review)', 'Privacy page', legal_rows('privacy') + [('Link back to home', 'legal.back', LEGAL_DE['back'], LEGAL_EN['back'])])
section('Imprint page (draft, needs legal review)', 'Imprint page', legal_rows('imprint'))

# ------------------------------------------------------------------ build the document
def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcolor); tcPr.append(shd)

def write(cell, text, size=9.5):
    p = cell.paragraphs[0]
    for t, ph in clean(text):
        run = p.add_run(t); run.font.size = Pt(size)
        if ph: run.font.highlight_color = WD_COLOR_INDEX.YELLOW

def build():
    doc = Document()
    sec = doc.sections[0]; sec.left_margin = sec.right_margin = Cm(1.8); sec.top_margin = sec.bottom_margin = Cm(1.8)
    st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10)
    doc.add_heading('BetterHealth: website copy, German and English', 0)
    p = doc.add_paragraph('Status: 31 October 2026. Draft for editing. The text is grouped by topic, not by page; each block says where it appears, so you edit it once.')
    doc.add_heading('How to use this document', 1)
    for line in [
        'Edit the German and English columns. Leave the grey key under each label unchanged: it is how your edits are put back into the site.',
        'Yellow text in [square brackets] is a placeholder or something not yet confirmed (for example opening hours). Replace it, or leave it and it stays visible on the site.',
        'Some texts are legal wording (privacy, imprint) and must be reviewed by a lawyer before launch.',
        'The fee, the clinician name, the phone number and the address are facts in the source: CHF 500, ' + FACTS['clinician'] + ', ' + FACTS['phone_display'] + ', ' + FACTS['street'] + ', ' + FACTS['city'] + '. Tell me if any of them changes.',
        'When you are done, send the document back to me and I will update the website.']:
        doc.add_paragraph(line, style='List Bullet')
    for title, appears, rows, note in SECTIONS:
        rows = [x for x in rows if x]
        doc.add_heading(title, 1)
        a = doc.add_paragraph(); run = a.add_run('Appears on: ' + appears); run.italic = True; run.font.size = Pt(9); run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        if note:
            n = doc.add_paragraph(); rn = n.add_run(note); rn.font.size = Pt(9)
        t = doc.add_table(rows=1, cols=3); t.style = 'Table Grid'
        widths = [Cm(3.6), Cm(6.9), Cm(6.9)]
        for i, h in enumerate(['Where', 'Deutsch', 'English']):
            c = t.rows[0].cells[i]; c.width = widths[i]; c.paragraphs[0].add_run(h).bold = True; shade(c, 'D9E2E8')
        for label, key, de, en in rows:
            cells = t.add_row().cells
            for i, c in enumerate(cells): c.width = widths[i]
            cp = cells[0].paragraphs[0]; r1 = cp.add_run(label); r1.font.size = Pt(9); r1.bold = True
            kp = cells[0].add_paragraph(); r2 = kp.add_run(key); r2.font.size = Pt(7.5); r2.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
            write(cells[1], de); write(cells[2], en)
        doc.add_paragraph()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    n = sum(len([x for x in s[2] if x]) for s in SECTIONS)
    print('wrote', os.path.abspath(OUT), '| sections:', len(SECTIONS), '| text rows:', n)

if __name__ == '__main__':
    build()
