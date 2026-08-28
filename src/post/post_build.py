# -*- coding: utf-8 -*-
"""Bangun dataset post-test lengkap + pemetaan silang ke pre-test.
Vincent (QA tester) dikeluarkan dari seluruh analisis."""
import json, io, re, math, statistics as st
from collections import Counter, defaultdict
from difflib import SequenceMatcher

EXCLUDE = {"Vincent"}

raw = json.load(io.open("post_core_raw.json", encoding="utf-8"))
Q, P = raw["Q"], raw["P"]

RESOLVED = {11: "Pengaturan resolusi layar monitor",
            17: "Komentar langsung pada elemen desain di Canva"}
for q in Q:
    if q["key"] is None:
        q["key"] = RESOLVED[q["no"]]
        q["key_solved"] = True

# --- buang Vincent
names = [n for n in raw["names"] if n not in EXCLUDE]
P = {n: v for n, v in P.items() if n not in EXCLUDE}
for q in Q:
    q["answers"] = {n: a for n, a in q["answers"].items() if n not in EXCLUDE}

# --- matriks respons
CORR = {}
for n in names:
    row = []
    for q in sorted(Q, key=lambda x: x["no"]):
        a = q["answers"][n]
        row.append("-" if a is None else ("C" if a == q["key"] else "X"))
    CORR[n] = row

# --- verifikasi terhadap Participant Data
mis = [(n, CORR[n].count("C"), P[n]["correct"]) for n in names if CORR[n].count("C") != P[n]["correct"]]
print("verif peserta (harus kosong):", mis)

# --- hitung ulang statistik butir TANPA Vincent
N = len(names)
for q in Q:
    qi = q["no"] - 1
    c = sum(1 for n in names if CORR[n][qi] == "C")
    x = sum(1 for n in names if CORR[n][qi] == "X")
    u = sum(1 for n in names if CORR[n][qi] == "-")
    q["correct_excl"], q["incorrect_excl"], q["unatt_excl"] = c, x, u
    q["p"] = c / N
    cnt = Counter(a for n, a in q["answers"].items() if a is not None)
    q["distr"] = sorted(cnt.items(), key=lambda kv: -kv[1])

sc = {n: CORR[n].count("C") for n in names}
ORD = sorted(names, key=lambda n: (-sc[n], P[n]["time_s"]))
k = max(1, round(N * 0.27))
UP, LW = ORD[:k], ORD[-k:]
vals = [sc[n] for n in names]
mean = st.mean(vals); sd = st.pstdev(vals); var = st.pvariance(vals)
for q in Q:
    qi = q["no"] - 1
    U = sum(1 for n in UP if CORR[n][qi] == "C")
    L = sum(1 for n in LW if CORR[n][qi] == "C")
    q["U"], q["L"], q["k"] = U, L, k
    q["D"] = (U - L) / k
    g1 = [sc[n] for n in names if CORR[n][qi] == "C"]
    g0 = [sc[n] for n in names if CORR[n][qi] != "C"]
    if g1 and g0 and sd > 0:
        p = q["p"]
        q["rpb"] = (st.mean(g1) - st.mean(g0)) / sd * math.sqrt(p * (1 - p))
    else:
        q["rpb"] = 0.0

spq = sum(q["p"] * (1 - q["p"]) for q in Q)
kn = len(Q)
kr20 = (kn / (kn - 1)) * (1 - spq / var) if var else 0
sem = sd * math.sqrt(max(0, 1 - kr20))
print("N=%d mean=%.3f sd=%.3f var=%.3f KR20=%.4f SEM=%.3f k_group=%d" % (N, mean, sd, var, kr20, sem, k))

# ================= pemetaan silang ke pre-test =================
pre = json.load(io.open("core.json", encoding="utf-8"))
PQ, PPre, PCORR = pre["Q"], pre["P"], pre["CORR"]


def norm(t):
    t = re.sub(r"[^a-z0-9 ]", " ", str(t).lower())
    return re.sub(r"\s+", " ", t).strip()


# --- cocokkan butir
pairs = []
used = set()
for q in sorted(Q, key=lambda x: x["no"]):
    best, bs = None, 0
    for pq in PQ:
        if pq["no"] in used:
            continue
        s = SequenceMatcher(None, norm(q["text"]), norm(pq["text"])).ratio()
        ks = SequenceMatcher(None, norm(q["key"]), norm(pq.get("key") or "")).ratio()
        s = max(s, (s + ks) / 2)
        if s > bs:
            best, bs = pq, s
    pairs.append((q, best, bs))
    if bs >= .60:
        used.add(best["no"])

print("\n--- PEMETAAN BUTIR post -> pre ---")
for q, pq, s in pairs:
    tag = "MATCH" if s >= .60 else "baru "
    print("post Q%-2d -> pre Q%-2s  sim=%.2f  %s | %s" % (q["no"], pq["no"] if s >= .60 else "-", s, tag, q["text"][:70]))

# --- cocokkan nama peserta
def nkey(n):
    n = norm(n).replace("*", "")
    return n


prenames = list(PPre.keys())
pmap = {}
for n in names:
    best, bs = None, 0
    a = nkey(n)
    for pn in prenames:
        b = nkey(pn)
        s = SequenceMatcher(None, a, b).ratio()
        if a.split()[0] == b.split()[0]:
            s = max(s, .85)
        if b in a or a in b:
            s = max(s, .9)
        if s > bs:
            best, bs = pn, s
    pmap[n] = (best, bs)

print("\n--- PEMETAAN PESERTA post -> pre ---")
for n in ORD:
    b, s = pmap[n]
    print("%-24s -> %-24s sim=%.2f %s" % (n, b, s, "OK" if s >= .8 else "TIDAK ADA"))

json.dump({"Q": Q, "P": P, "CORR": CORR, "names": names,
           "stats": {"N": N, "mean": mean, "sd": sd, "var": var, "kr20": kr20, "sem": sem, "k": k},
           "pairs": [(q["no"], (pq["no"] if s >= .60 else None), round(s, 3)) for q, pq, s in pairs],
           "pmap": {n: (b if s >= .8 else None) for n, (b, s) in pmap.items()}},
          io.open("post_core.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nsaved post_core.json")
