# -*- coding: utf-8 -*-
import json, io, math, statistics as st, html as H
from collections import defaultdict, Counter

D = json.load(io.open("core.json", encoding="utf-8"))
S = json.load(io.open("stats.json", encoding="utf-8"))
Q, P, CORR = D["Q"], D["P"], D["CORR"]
TIME = {n: {int(k): v for k, v in d.items()} for n, d in D["TIME"].items()}
items = S["items"]
N = 37

src = io.open("common.py", encoding="utf-8").read()
g = {}
exec(compile(src[src.index("DOMAIN = {"):], "maps", "exec"), g)
DOMAIN, BLOOM, SHORT = g["DOMAIN"], g["BLOOM"], g["SHORT"]


def fix(t):
    return t.replace("�", "…").strip()


sc = {n: P[n]["correct"] for n in P}
tt = {n: P[n]["time_s"] for n in P}
att = {n: 20 - CORR[n].count("-") for n in P}
ORDR = sorted(P, key=lambda n: (-sc[n], tt[n]))
UPN, LWN, MID = ORDR[:10], ORDR[-10:], ORDR[10:-10]

tot_c = sum(sc.values())
tot_cells = N * 20
tot_x = sum(CORR[n].count("X") for n in P)
tot_b = sum(CORR[n].count("-") for n in P)
acc_all = tot_c / tot_cells
acc_act = tot_c / (tot_c + tot_x)
mean, sd, kr20, sem = S["mean"], S["sd"], S["kr20"], S["sem"]
vals = sorted(sc.values())
med = st.median(vals)
q1 = vals[len(vals) // 4]
q3 = vals[3 * len(vals) // 4]

E = H.escape

NAVY = "#12284b"; ACC = "#2f6fb5"; MUT = "#8a94a6"
GOOD = "#2e7d5b"; WARN = "#c58a1a"; BAD = "#c0473f"


def hbar(rows, maxv=None, w=640, rowh=26, labw=210, colorfn=None):
    maxv = maxv or max(r[1] for r in rows) or 1
    h = rowh * len(rows) + 8
    bw = w - labw - 76
    out = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    for i, (lab, v, note_) in enumerate(rows):
        y = i * rowh + 4
        c = colorfn(v) if colorfn else ACC
        L = max(2, bw * (v / maxv))
        out.append('<text x="%d" y="%d" class="cl" text-anchor="end">%s</text>' % (labw - 10, y + 14, E(str(lab))))
        out.append('<rect x="%d" y="%d" width="%.1f" height="14" rx="2" fill="%s"/>' % (labw, y + 4, L, c))
        out.append('<text x="%.1f" y="%d" class="cv">%s</text>' % (labw + L + 7, y + 15, E(note_)))
    out.append("</svg>")
    return "".join(out)


def vbars(rows, w=680, h=210, pad=34):
    maxv = max(r[1] for r in rows) or 1
    bw = (w - pad * 2) / len(rows)
    out = ['<svg class="chart" viewBox="0 0 %d %d" role="img">' % (w, h)]
    out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#dfe4ec"/>' % (pad, h - 26, w - pad, h - 26))
    for i, (lab, v, col) in enumerate(rows):
        bh = (h - 60) * (v / maxv)
        x = pad + i * bw + bw * .18
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="%s"/>' % (x, h - 26 - bh, bw * .64, bh, col))
        out.append('<text x="%.1f" y="%.1f" class="cv" text-anchor="middle">%s</text>' % (x + bw * .32, h - 30 - bh, v))
        out.append('<text x="%.1f" y="%d" class="cl" text-anchor="middle">%s</text>' % (x + bw * .32, h - 10, E(str(lab))))
    out.append("</svg>")
    return "".join(out)


def pcol(p):
    return BAD if p < .30 else (WARN if p < .70 else GOOD)


def dcol(d):
    return GOOD if d >= .40 else (ACC if d >= .30 else (WARN if d >= .20 else BAD))


def grade(v):
    n_ = v / 20 * 100
    if n_ >= 85: return "A — Sangat Baik"
    if n_ >= 70: return "B — Baik"
    if n_ >= 55: return "C — Cukup"
    if n_ >= 40: return "D — Kurang"
    return "E — Sangat Kurang"


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
