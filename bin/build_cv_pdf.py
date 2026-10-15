#!/usr/bin/env python3
"""Build assets/pdf/cv.pdf from _data/cv.yml, _data/socials.yml and _bibliography/papers.bib.

The deploy workflow runs this only when assets/pdf/cv.pdf is NOT in the repository, so uploading
your own CV (dashboard → Bio & files → Upload CV) replaces the generated one automatically.

Usage: python3 bin/build_cv_pdf.py [output.pdf]
"""
import re, sys, os, datetime
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "assets", "pdf", "cv.pdf")

cv = yaml.safe_load(open(os.path.join(ROOT, "_data", "cv.yml")))["cv"]
socials = yaml.safe_load(open(os.path.join(ROOT, "_data", "socials.yml"))) or {}
config = yaml.safe_load(open(os.path.join(ROOT, "_config.yml")))
sections = cv.get("sections", {})


def esc(s):
    return (str(s) if s is not None else "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def year(d):
    d = str(d or "").strip()
    if not d:
        return ""
    if d.lower() == "present":
        return "Present"
    return d.split("-")[0]


def span(e):
    s, t = year(e.get("start_date") or e.get("startDate")), year(e.get("end_date") or e.get("endDate")) or "Present"
    return s if s == t else f"{s} – {t}"


# ---------- BibTeX (minimal parser: @type{key, field = {value} or "value", ...}) ----------
def parse_bib(path):
    if not os.path.exists(path):
        return []
    text = open(path, encoding="utf-8").read()
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        etype, key = m.group(1).lower(), m.group(2)
        if etype in ("comment", "string", "preamble"):
            continue
        i, depth, fields = m.end(), 1, {}
        start = i
        while i < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        body = text[start:i - 1]
        for fm in re.finditer(r"(\w+)\s*=\s*(\{((?:[^{}]|\{[^{}]*\})*)\}|\"([^\"]*)\"|(\d+))", body):
            fields[fm.group(1).lower()] = (fm.group(3) if fm.group(3) is not None else fm.group(4) or fm.group(5) or "").strip()
        fields["_type"], fields["_key"] = etype, key
        entries.append(fields)
    entries.sort(key=lambda f: f.get("year", ""), reverse=True)
    return entries


def fmt_authors(a):
    out = []
    for name in re.split(r"\s+and\s+", a):
        name = name.strip().replace("{", "").replace("}", "")
        if "," in name:
            last, first = [x.strip() for x in name.split(",", 1)]
            name = f"{first} {last}".strip()
        out.append(name)
    return ", ".join(out)


# ---------- styles ----------
base = "Helvetica"
st = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20, leading=24, spaceAfter=2),
    "sub": ParagraphStyle("sub", fontName=base, fontSize=10.5, leading=14, textColor=colors.HexColor("#444444")),
    "links": ParagraphStyle("links", fontName=base, fontSize=9, leading=12, textColor=colors.HexColor("#555555")),
    "h": ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=11.5, leading=14, spaceBefore=10, spaceAfter=3, textColor=colors.HexColor("#0f7b6c")),
    "body": ParagraphStyle("body", fontName=base, fontSize=9.8, leading=13),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=10.2, leading=13),
    "meta": ParagraphStyle("meta", fontName=base, fontSize=9.3, leading=12, textColor=colors.HexColor("#555555")),
    "date": ParagraphStyle("date", fontName=base, fontSize=9.3, leading=12, textColor=colors.HexColor("#555555")),
    "bullet": ParagraphStyle("bullet", fontName=base, fontSize=9.4, leading=12.2, leftIndent=10, bulletIndent=0),
}

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.8 * inch, rightMargin=0.8 * inch, topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                        title=f"{cv.get('name', '')} — CV", author=cv.get("name", ""))
W = letter[0] - 1.6 * inch
flow = []

# ---------- header ----------
flow.append(Paragraph(esc(cv.get("name", "")), st["name"]))
flow.append(Paragraph(esc(cv.get("label", "")), st["sub"]))
links = []
if cv.get("email"):
    links.append(esc(cv["email"]))
elif socials.get("email"):
    links.append(esc(socials["email"]))
if socials.get("github_username"):
    links.append(f"github.com/{esc(socials['github_username'])}")
if socials.get("linkedin_username"):
    links.append(f"linkedin.com/in/{esc(socials['linkedin_username'])}")
if socials.get("scholar_userid"):
    links.append("Google Scholar")
site_url = (config.get("url") or "").replace("https://", "")
if site_url:
    links.append(esc(site_url))
if cv.get("location"):
    links.append(esc(cv["location"]))
flow.append(Paragraph("  ·  ".join(links), st["links"]))
flow.append(Spacer(1, 4))
flow.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#cccccc")))

if cv.get("summary"):
    flow.append(Paragraph(esc(" ".join(str(cv["summary"]).split())), st["body"]))


def heading(t):
    flow.append(Paragraph(t.upper(), st["h"]))


def entry(title, org, where, when, summary=None, bullets=None, highlights_limit=None):
    left = [Paragraph(esc(title), st["title"]), Paragraph(esc(" · ".join([x for x in [org, where] if x])), st["meta"])]
    if summary:
        left.append(Paragraph(esc(summary), st["meta"]))
    for b in (bullets or [])[:highlights_limit]:
        left.append(Paragraph(esc(b), st["bullet"], bulletText="•"))
    t = Table([[left, Paragraph(esc(when), st["date"])]], colWidths=[W - 1.15 * inch, 1.15 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    flow.append(KeepTogether(t))


# ---------- education ----------
edu = [e for e in sections.get("Education", []) if not e.get("placeholder")]
if edu:
    heading("Education")
    for e in edu:
        deg = e.get("studyType") or e.get("degree") or ""
        if e.get("area"):
            deg = f"{deg} in {e['area']}" if deg else e["area"]
        entry(deg, e.get("institution", ""), e.get("location", ""), span(e), None, e.get("highlights"))

# ---------- experience ----------
exp = [e for e in sections.get("Experience", []) if not e.get("placeholder")]
if exp:
    heading("Experience")
    for e in exp:
        entry(e.get("position", ""), e.get("company") or e.get("name", ""), e.get("location", ""), span(e), None, e.get("highlights"))

# ---------- publications ----------
pubs = parse_bib(os.path.join(ROOT, "_bibliography", "papers.bib"))
if pubs:
    heading("Publications")
    for p in pubs:
        venue = p.get("booktitle") or p.get("journal") or p.get("publisher") or ""
        line = f"<b>{esc(p.get('title', ''))}</b>. {esc(fmt_authors(p.get('author', '')))}. <i>{esc(venue)}</i>, {esc(p.get('year', ''))}."
        extras = []
        if p.get("doi"):
            extras.append(f"doi:{esc(p['doi'])}")
        if p.get("arxiv"):
            extras.append(f"arXiv:{esc(p['arxiv'])}")
        if extras:
            line += " " + " · ".join(extras)
        flow.append(Paragraph(line, st["bullet"], bulletText="•"))

# ---------- awards / skills / interests ----------
aw = sections.get("Awards", [])
if aw:
    heading("Awards")
    for a in aw:
        entry(a.get("title", ""), a.get("awarder", ""), "", year(a.get("date")), a.get("summary"))

sk = sections.get("Skills", [])
if sk:
    heading("Skills")
    rows = [[Paragraph(f"<b>{esc(s.get('name', ''))}</b>", st["body"]), Paragraph(esc(s.get("keywords", "")), st["body"])] for s in sk]
    t = Table(rows, colWidths=[1.6 * inch, W - 1.6 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    flow.append(t)

it = sections.get("Interests", [])
if it:
    heading("Research interests")
    flow.append(Paragraph(esc(" · ".join(i.get("name", "") for i in it)), st["body"]))

flow.append(Spacer(1, 10))
flow.append(Paragraph(f"Generated from {esc(site_url or 'the website')} on {datetime.date.today():%B %d, %Y}.", st["links"]))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.build(flow)
print(f"wrote {OUT}")
