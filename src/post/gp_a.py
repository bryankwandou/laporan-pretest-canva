# -*- coding: utf-8 -*-
import json, io, math, statistics as st, html as H
from collections import Counter, defaultdict

pre = json.load(io.open("core.json", encoding="utf-8"))
S = json.load(io.open("stats.json", encoding="utf-8"))
post = json.load(io.open("post_core.json", encoding="utf-8"))
C1 = json.load(io.open("cmp.json", encoding="utf-8"))
C2 = json.load(io.open("cmp2.json", encoding="utf-8"))
PD = json.load(io.open("pdf_opts.json", encoding="utf-8"))

PP, PC = pre["P"], pre["CORR"]
preit = {i["no"]: i for i in S["items"]}
QO = {q["no"]: q for q in post["Q"]}
PO, CO = post["P"], post["CORR"]
onames, pmap = post["names"], post["pmap"]
OPT = {int(k): v for k, v in PD["OPT"].items()}
DEAD = {int(k): v for k, v in PD["DEAD"].items()}

sc_post = {n: CO[n].count("C") for n in onames}
sc_pre = {n: PP[n]["correct"] for n in PP}
att = {n: 20 - CO[n].count("-") for n in onames}
COMP, INC = C2["comp"], C2["inc"]
PAIR, PAIRC = C1["PAIR"], C2["PAIRC"]
NEWP = {int(k): v for k, v in C1["NEW_POST"].items()}
DROPP = {int(k): v for k, v in C1["DROP_PRE"].items()}
ORDP = sorted(onames, key=lambda n: (-sc_post[n], PO[n]["time_s"]))
gaC = [a for _, _, a, _ in PAIRC]
gbC = [b for _, _, _, b in PAIRC]
gg = [b - a for _, _, a, b in PAIRC]
compv = [sc_post[n] for n in COMP]
ndead = sum(len(v) for v in DEAD.values())

E = H.escape
NAVY = "#12284b"; ACC = "#2f6fb5"
GOOD = "#2e7d5b"; WARN = "#c58a1a"; BAD = "#c0473f"

SHORTP = {1: "Kolaborasi real-time", 2: "Asal usul Canva (Fusion Books)", 3: "Brand Kit",
          4: "Hierarki visual — yang bertentangan", 5: "Harga paket Pro", 6: "Format ekspor PNG",
          7: "Pernyataan benar tentang Canva", 8: "Makna warna ungu liturgi", 9: "Format ekspor MP4",
          10: "Batas jumlah warna dan font", 11: "Menu panel kiri", 12: "Tiga pendiri Canva",
          13: "Eyedropper", 14: "Ukuran Instagram Feed", 15: "Empat nilai berkarya",
          16: "Urutan langkah template", 17: "Komentar pada elemen", 18: "Etika AI",
          19: "Skema warna monokromatik", 20: "Esensi tujuan pelatihan"}


def hbar(rows, maxv=None, w=640, rowh=26, labw=210, colorfn=None):
    maxv = maxv or max(r[1] for r in rows) or 1
    h = rowh * len(rows) + 8
    bw = w - labw - 76
    o = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    for i, (lab, v, nt) in enumerate(rows):
        y = i * rowh + 4
        c = colorfn(v) if colorfn else ACC
        L = max(2, bw * (v / maxv))
        o.append('<text x="%d" y="%d" class="cl" text-anchor="end">%s</text>' % (labw - 10, y + 14, E(str(lab))))
        o.append('<rect x="%d" y="%d" width="%.1f" height="14" rx="2" fill="%s"/>' % (labw, y + 4, L, c))
        o.append('<text x="%.1f" y="%d" class="cv">%s</text>' % (labw + L + 7, y + 15, E(nt)))
    o.append("</svg>")
    return "".join(o)


def dumbbell(rows, w=700, rowh=28, labw=250, maxv=1.0):
    """rows: (label, a, b, note)"""
    h = rowh * len(rows) + 26
    bw = w - labw - 96
    o = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    for gx in range(0, 6):
        x = labw + bw * gx / 5
        o.append('<line x1="%.1f" y1="16" x2="%.1f" y2="%d" stroke="#eef0f4"/>' % (x, x, h - 10))
        o.append('<text x="%.1f" y="12" class="cl" text-anchor="middle">%d%%</text>' % (x, gx * 20))
    for i, (lab, a, b, nt) in enumerate(rows):
        y = i * rowh + 30
        xa = labw + bw * (a / maxv); xb = labw + bw * (b / maxv)
        col = GOOD if b > a else BAD
        o.append('<text x="%d" y="%d" class="cl" text-anchor="end">%s</text>' % (labw - 10, y + 4, E(str(lab))))
        o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="3"/>' % (xa, y, xb, y, col))
        o.append('<circle cx="%.1f" cy="%d" r="4.5" fill="#fff" stroke="#8a94a6" stroke-width="2"/>' % (xa, y))
        o.append('<circle cx="%.1f" cy="%d" r="4.5" fill="%s"/>' % (xb, y, col))
        o.append('<text x="%.1f" y="%d" class="cv" fill="%s">%s</text>' % (max(xa, xb) + 10, y + 4, col, E(nt)))
    o.append("</svg>")
    return "".join(o)


def vbars(rows, w=680, h=210, pad=34):
    maxv = max(r[1] for r in rows) or 1
    bw = (w - pad * 2) / len(rows)
    o = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#dfe4ec"/>' % (pad, h - 26, w - pad, h - 26))
    for i, (lab, v, col) in enumerate(rows):
        bh = (h - 60) * (v / maxv)
        x = pad + i * bw + bw * .18
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x, h - 26 - bh, bw * .64, bh, col))
        o.append('<text x="%.1f" y="%.1f" class="cv" text-anchor="middle">%s</text>' % (x + bw * .32, h - 30 - bh, v))
        o.append('<text x="%.1f" y="%d" class="cl" text-anchor="middle">%s</text>' % (x + bw * .32, h - 10, E(str(lab))))
    o.append("</svg>")
    return "".join(o)


def slope(rows, w=520, h=300, pad=52):
    """rows: (label, a, b) — grafik kemiringan pre->post"""
    mx = 20
    o = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    x0, x1 = pad + 66, w - pad - 66
    for v in range(0, 21, 5):
        y = h - pad - (h - pad * 2) * (v / mx)
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#f2f4f8"/>' % (x0, y, x1, y))
        o.append('<text x="%d" y="%.1f" class="cl" text-anchor="end">%d</text>' % (x0 - 8, y + 3, v))
    o.append('<text x="%d" y="%d" class="cv" text-anchor="middle">Pre-test</text>' % (x0, h - 16))
    o.append('<text x="%d" y="%d" class="cv" text-anchor="middle">Post-test</text>' % (x1, h - 16))
    for lab, a, b in rows:
        ya = h - pad - (h - pad * 2) * (a / mx)
        yb = h - pad - (h - pad * 2) * (b / mx)
        o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.8" opacity=".8"/>' % (x0, ya, x1, yb, GOOD))
        o.append('<circle cx="%d" cy="%.1f" r="3.5" fill="%s"/>' % (x0, ya, GOOD))
        o.append('<circle cx="%d" cy="%.1f" r="3.5" fill="%s"/>' % (x1, yb, GOOD))
        o.append('<text x="%d" y="%.1f" class="cl" text-anchor="start">%s</text>' % (x1 + 9, yb + 3, E(lab[:16])))
    o.append("</svg>")
    return "".join(o)


def pcol(p):
    return BAD if p < .30 else (WARN if p < .70 else GOOD)


buf = []
A = buf.append


def sec(sid, num, t, lead=""):
    A('<section id="%s"><div class="secno">%s</div><h2>%s</h2>' % (sid, num, t))
    if lead:
        A('<p class="lead">%s</p>' % lead)


def endsec():
    A("</section>")


def note(t):
    A('<p class="note">%s</p>' % t)


def warn(t):
    A('<p class="note warnbox">%s</p>' % t)
