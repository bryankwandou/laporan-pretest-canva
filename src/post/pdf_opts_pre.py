# -*- coding: utf-8 -*-
"""Parse naskah cetak resmi PRE-TEST, verifikasi kunci rekonstruksi,
dan temukan pengecoh yang tidak pernah dipilih siapa pun."""
import io, re, json
from difflib import SequenceMatcher

raw = io.open("pdf_pre.txt", encoding="utf-8").read()
raw = re.sub(r"\n?\d+/\d+/\d+,\s*\d+:\d+\s*[AP]M\s*Free Printable.*?\n", "\n", raw)
raw = re.sub(r"https://\S+", " ", raw)
raw = re.sub(r"\b\d+/\d+\b", " ", raw)
flat = re.sub(r"\s+", " ", raw)
i = flat.find("1. Sebelum")
flat = flat[i:] if i > 0 else flat

idx = [(int(m.group(1)), m.start()) for m in re.finditer(r"(?:(?<= )|^)(\d{1,2})\.\s+(?=[A-Z])", flat)]
idx = [(n, s) for n, s in idx if 1 <= n <= 20]
seen, keep = set(), []
for n, s in idx:
    if n not in seen:
        seen.add(n); keep.append((n, s))
keep.sort(key=lambda x: x[1])
blocks = {}
for j, (n, s) in enumerate(keep):
    e = keep[j + 1][1] if j + 1 < len(keep) else len(flat)
    blocks[n] = flat[s:e]

OPT = {}
for n, b in blocks.items():
    parts = re.split(r"\b([a-d])\)\s*", b)
    stem = re.sub(r"^\d+\.\s*", "", parts[0]).strip()
    opts = [(parts[k], re.sub(r"\s+", " ", parts[k + 1]).strip())
            for k in range(1, len(parts) - 1, 2)]
    OPT[n] = {"stem": stem, "opts": opts}

S = json.load(io.open("stats.json", encoding="utf-8"))
IT = {i["no"]: i for i in S["items"]}


def sim(a, b):
    return SequenceMatcher(None, re.sub(r"[^a-z0-9]", "", str(a).lower()),
                           re.sub(r"[^a-z0-9]", "", str(b).lower())).ratio()


L = []
W = L.append
W("=" * 92)
W("VERIFIKASI KUNCI PRE-TEST TERHADAP NASKAH CETAK RESMI, DAN PENGECOH MATI")
W("Naskah PDF dicetak tanpa tanda kunci. Kunci hasil rekonstruksi dicocokkan ke daftar opsi.")
W("=" * 92)
W("")
W("%-5s %-6s %-54s %6s %5s" % ("No", "Huruf", "Kunci rekonstruksi (padanan di naskah)", "sim", "Opsi"))
bad, DEAD, LET = [], {}, {}
nopt_all = 0
for n in range(1, 21):
    if n not in OPT or len(OPT[n]["opts"]) != 4:
        W("Q%-4d  naskah TIDAK terbaca utuh (%d opsi)" % (n, len(OPT.get(n, {}).get("opts", []))))
        bad.append(n); continue
    nopt_all += 4
    key = IT[n]["key"]
    best = max(OPT[n]["opts"], key=lambda o: sim(o[1], key))
    s = sim(best[1], key)
    LET[n] = best[0]
    W("Q%-4d %-6s %-54s %6.2f %5d" % (n, best[0] + ")", best[1][:54], s, 4))
    if s < .85:
        bad.append(n)
    chosen = [o for o, c in IT[n]["distr"]]
    dead = [(l, t) for l, t in OPT[n]["opts"]
            if max([sim(t, c) for c in chosen] or [0]) < .85]
    if dead:
        DEAD[n] = dead
W("")
W("Butir dengan kunci tidak cocok mulus: %s" % (bad if bad else "tidak ada"))
W("Total opsi terbaca dari naskah: %d" % nopt_all)
W("")
nd = sum(len(v) for v in DEAD.values())
W("PENGECOH MATI PRE-TEST — opsi salah yang tidak dipilih satu pun peserta (%d butir, %d opsi):" % (len(DEAD), nd))
for n in sorted(DEAD):
    for l, t in DEAD[n]:
        W("   Q%-3d %s) %s" % (n, l, t[:70]))
W("")
W("Total %d dari 60 pengecoh pre-test (%.0f%%) tidak berfungsi." % (nd, nd / 60 * 100))
W("Sebagai pembanding, pada post-test angkanya 25 dari 60 (42%).")

txt = "\n".join(L)
io.open("cmp_out4.txt", "w", encoding="utf-8").write(txt)
json.dump({"OPT": OPT, "DEAD": DEAD, "bad": bad, "LET": LET},
          io.open("pdf_opts_pre.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(txt[:200])
print("...")
print("bad=%s dead=%d nopt=%d" % (bad, nd, nopt_all))
