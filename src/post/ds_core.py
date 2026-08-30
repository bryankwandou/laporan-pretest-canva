# -*- coding: utf-8 -*-
"""Bangun dataset penelitian berbasis ORANG (bukan sesi) dari sumber terverifikasi.
Aturan pemilihan sesi bagi orang bersesi ganda: ambil sesi dengan butir terjawab
TERBANYAK; bila seri, ambil yang jawaban benarnya terbanyak.
"""
import json, io, math, re, statistics as st
from collections import Counter

pre = json.load(io.open("core.json", encoding="utf-8"))
post = json.load(io.open("post_core.json", encoding="utf-8"))
Spre = json.load(io.open("stats.json", encoding="utf-8"))
C1 = json.load(io.open("cmp.json", encoding="utf-8"))
C2 = json.load(io.open("cmp2.json", encoding="utf-8"))
OPRE = json.load(io.open("pdf_opts_pre.json", encoding="utf-8"))
OPOST = json.load(io.open("pdf_opts.json", encoding="utf-8"))
TJ = json.load(io.open("post_time.json", encoding="utf-8"))

PC, CO, P, PO = pre["CORR"], post["CORR"], pre["P"], post["P"]
QPRE = {q["no"]: q for q in pre["Q"]}
QPOST = {q["no"]: q for q in post["Q"]}
IPRE = {i["no"]: i for i in Spre["items"]}


def canon(s):
    s = str(s).strip().rstrip("*")
    return re.sub(r"\s+", " ", s).strip()


def collapse(names, corr):
    """Kelompokkan sesi menjadi orang; pilih sesi paling lengkap."""
    grp = {}
    for n in names:
        grp.setdefault(canon(n), []).append(n)
    chosen, multi = {}, {}
    for orang, sesi in grp.items():
        pick = max(sesi, key=lambda x: (20 - corr[x].count("-"), corr[x].count("C")))
        chosen[orang] = pick
        if len(sesi) > 1:
            multi[orang] = sesi
    return chosen, multi


CH_PRE, MULTI_PRE = collapse(list(P.keys()), PC)
CH_POST, MULTI_POST = collapse(post["names"], CO)

ORANG_PRE = sorted(CH_PRE, key=lambda o: -PC[CH_PRE[o]].count("C"))
ORANG_POST = sorted(CH_POST, key=lambda o: -CO[CH_POST[o]].count("C"))
RPRE = {o: PC[CH_PRE[o]] for o in CH_PRE}
RPOST = {o: CO[CH_POST[o]] for o in CH_POST}
NPRE, NPOST = len(ORANG_PRE), len(ORANG_POST)


def itemstats(orang, R, n):
    """p, D, r-pbis per butir atas basis orang."""
    tot = {o: R[o].count("C") for o in orang}
    order = sorted(orang, key=lambda o: -tot[o])
    k = max(1, round(n * 0.27))
    up, lo = order[:k], order[-k:]
    sd = st.pstdev([tot[o] for o in orang]) or 1e-9
    out = {}
    for q in range(20):
        c = sum(1 for o in orang if R[o][q] == "C")
        p = c / n
        D = (sum(1 for o in up if R[o][q] == "C") / k
             - sum(1 for o in lo if R[o][q] == "C") / k)
        g1 = [tot[o] for o in orang if R[o][q] == "C"]
        g0 = [tot[o] for o in orang if R[o][q] != "C"]
        rpb = 0.0
        if g1 and g0:
            rpb = (st.mean(g1) - st.mean(g0)) / sd * math.sqrt(p * (1 - p))
        out[q + 1] = {"benar": c, "salah": sum(1 for o in orang if R[o][q] == "X"),
                      "kosong": sum(1 for o in orang if R[o][q] == "-"),
                      "p": round(p, 4), "D": round(D, 4), "rpb": round(rpb, 4)}
    return out, k


def kr20(orang, R, n):
    tot = [R[o].count("C") for o in orang]
    var = st.pvariance(tot)
    spq = sum((sum(1 for o in orang if R[o][q] == "C") / n) *
              (1 - sum(1 for o in orang if R[o][q] == "C") / n) for q in range(20))
    if var == 0:
        return 0.0, 0.0
    r = (20 / 19) * (1 - spq / var)
    return round(r, 4), round(st.stdev(tot) * math.sqrt(max(0, 1 - r)), 4)


SPRE_I, KPRE = itemstats(ORANG_PRE, RPRE, NPRE)
SPOST_I, KPOST = itemstats(ORANG_POST, RPOST, NPOST)
KR_PRE, SEM_PRE = kr20(ORANG_PRE, RPRE, NPRE)
KR_POST, SEM_POST = kr20(ORANG_POST, RPOST, NPOST)

# --- pasangan, berbasis orang
pmap = {o: p for o, p, a, b in C1["PAIR"]}
PAIR = []
for o in ORANG_POST:
    src = CH_POST[o]
    p = pmap.get(src)
    if not p:
        continue
    po = canon(p)
    if po not in RPRE:
        continue
    PAIR.append((o, po, RPRE[po].count("C"), RPOST[o].count("C"),
                 20 - RPRE[po].count("-"), 20 - RPOST[o].count("-")))
PAIRT = [x for x in PAIR if x[5] == 20]           # post tuntas
PAIRT.sort(key=lambda x: -(x[3] - x[2]))

g = [b - a for o, p, a, b, ta, tb in PAIRT]
n = len(g)
mg, sg = st.mean(g), st.stdev(g)
tval = mg / (sg / math.sqrt(n))
dz = mg / sg
hake = mg / (20 - st.mean([a for o, p, a, b, ta, tb in PAIRT]))
naik = sum(1 for x in g if x > 0)
pbin = sum(math.comb(n, k) for k in range(naik, n + 1)) / 2 ** n

OUT = {
    "ORANG_PRE": ORANG_PRE, "ORANG_POST": ORANG_POST,
    "RPRE": RPRE, "RPOST": RPOST,
    "CH_PRE": CH_PRE, "CH_POST": CH_POST,
    "MULTI_PRE": MULTI_PRE, "MULTI_POST": MULTI_POST,
    "SPRE_I": SPRE_I, "SPOST_I": SPOST_I,
    "KPRE": KPRE, "KPOST": KPOST,
    "KR_PRE": KR_PRE, "SEM_PRE": SEM_PRE, "KR_POST": KR_POST, "SEM_POST": SEM_POST,
    "PAIR": PAIR, "PAIRT": PAIRT,
    "stat": {"n": n, "mean_gain": round(mg, 4), "sd_gain": round(sg, 4),
             "t": round(tval, 4), "dz": round(dz, 4), "hake": round(hake, 4),
             "naik": naik, "pbin": round(pbin, 6)},
}
json.dump(OUT, io.open("ds_core.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("ORANG  pre=%d  post=%d" % (NPRE, NPOST))
print("Sesi ganda pre :", MULTI_PRE)
print("Sesi ganda post:", MULTI_POST)
print("Sesi dipakai   :", {o: CH_PRE[o] for o in MULTI_PRE}, {o: CH_POST[o] for o in MULTI_POST})
print()
print("PRE  rata-rata benar %.2f  KR-20 %.3f  SEM %.2f  kelompok atas/bawah %d" %
      (st.mean([RPRE[o].count("C") for o in ORANG_PRE]), KR_PRE, SEM_PRE, KPRE))
print("POST rata-rata benar %.2f  KR-20 %.3f  SEM %.2f  kelompok atas/bawah %d" %
      (st.mean([RPOST[o].count("C") for o in ORANG_POST]), KR_POST, SEM_POST, KPOST))
print()
print("Pasangan total %d, tuntas %d" % (len(PAIR), len(PAIRT)))
print("gain %s" % g)
print("mean %.2f sd %.2f t(%d)=%.3f dz=%.3f hake=%.3f naik %d/%d p=%.4f" %
      (mg, sg, n - 1, tval, dz, hake, naik, n, pbin))
