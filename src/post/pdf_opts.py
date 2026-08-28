# -*- coding: utf-8 -*-
"""Ambil seluruh opsi dari naskah PDF, cocokkan dengan kunci rekonstruksi,
dan temukan pengecoh yang tidak pernah dipilih siapa pun."""
import io, re, json
from difflib import SequenceMatcher

raw = io.open("pdf.txt", encoding="utf-8").read()
raw = re.sub(r"\n?\d+/\d+/\d+, \d+:\d+ [AP]M Free Printable.*?\n", "\n", raw)
raw = re.sub(r"https://wayground\.com/\S+", "", raw)
raw = re.sub(r"--- PAGE \d+", "", raw)
flat = re.sub(r"\s+", " ", raw)

# potong per nomor soal
idx = [(int(m.group(1)), m.start()) for m in re.finditer(r"(?:(?<= )|^)(\d{1,2})\.(?=[A-Z])", flat)]
idx = [(n, s) for n, s in idx if 1 <= n <= 20]
seen, keep = set(), []
for n, s in idx:
    if n not in seen:
        seen.add(n); keep.append((n, s))
keep.sort(key=lambda x: x[1])
blocks = {}
for i, (n, s) in enumerate(keep):
    e = keep[i + 1][1] if i + 1 < len(keep) else len(flat)
    blocks[n] = flat[s:e]

OPT = {}
for n, b in blocks.items():
    parts = re.split(r"\b([a-d])\)", b)
    stem = parts[0]
    opts = []
    for j in range(1, len(parts) - 1, 2):
        opts.append((parts[j], re.sub(r"\s+", " ", parts[j + 1]).strip()))
    OPT[n] = {"stem": re.sub(r"^\d+\.", "", stem).strip(), "opts": opts}

post = json.load(io.open("post_core.json", encoding="utf-8"))
Q = {q["no"]: q for q in post["Q"]}


def sim(a, b):
    return SequenceMatcher(None, re.sub(r"[^a-z0-9]", "", a.lower()),
                           re.sub(r"[^a-z0-9]", "", b.lower())).ratio()


out = []
W = out.append
W("=" * 78)
W("J. VERIFIKASI KUNCI TERHADAP NASKAH SOAL (PDF) DAN PENGECOH MATI")
W("=" * 78)
W("Naskah PDF tidak memuat tanda kunci (graded=false), tetapi memuat seluruh 4 opsi")
W("setiap butir. Kunci hasil rekonstruksi dicocokkan ke daftar opsi tersebut.")
W("")
W("%-4s %-6s %-52s %5s %5s" % ("No", "Huruf", "Kunci rekonstruksi (cocok ke opsi PDF)", "sim", "Opsi"))
bad = []
DEAD = {}
for n in range(1, 21):
    if n not in OPT:
        W("Q%-3d  ??? tidak terbaca dari PDF" % n); continue
    key = Q[n]["key"]
    best = max(OPT[n]["opts"], key=lambda o: sim(o[1], key))
    s = sim(best[1], key)
    W("Q%-3d %-6s %-52s %5.2f %5d" % (n, best[0] + ")", best[1][:52], s, len(OPT[n]["opts"])))
    if s < .80:
        bad.append(n)
    chosen = {o for o, _ in Q[n]["distr"]}
    dead = [(o, t) for o, t in OPT[n]["opts"]
            if max([sim(t, c) for c in chosen] or [0]) < .80]
    if dead:
        DEAD[n] = dead
W("")
W("Kunci yang tidak cocok mulus ke opsi PDF: %s" % (bad if bad else "tidak ada"))
W("Jumlah opsi per butir: seluruhnya 4 (%s)" % ("konsisten" if all(len(OPT[n]["opts"]) == 4 for n in OPT) else "TIDAK konsisten"))
W("")
W("PENGECOH MATI — opsi salah yang tidak dipilih oleh satu pun peserta (%d butir):" % len(DEAD))
tot = 0
for n in sorted(DEAD):
    for o, t in DEAD[n]:
        W("   Q%-3d %s) %s" % (n, o, t[:66]))
        tot += 1
W("")
W("Total %d dari 60 pengecoh (%.0f%%) tidak berfungsi sama sekali." % (tot, tot / 60 * 100))
W("Pengecoh yang tidak pernah dipilih tidak menyumbang informasi dan secara efektif")
W("mengubah butir 4 opsi menjadi butir 2-3 opsi, sehingga peluang tebakan benar naik")
W("dari 25%% menjadi 33-50%%.")
W("")

txt = "\n".join(out)
io.open("cmp_out3.txt", "w", encoding="utf-8").write(txt)
json.dump({"OPT": OPT, "DEAD": DEAD, "bad": bad}, io.open("pdf_opts.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("written; dead=%d bad=%s" % (tot, bad))
