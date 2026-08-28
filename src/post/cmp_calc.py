# -*- coding: utf-8 -*-
"""Perbandingan pre-test vs post-test. Vincent (QA tester) dikeluarkan."""
import json, io, math, statistics as st
from collections import Counter, defaultdict

pre = json.load(io.open("core.json", encoding="utf-8"))
S = json.load(io.open("stats.json", encoding="utf-8"))
post = json.load(io.open("post_core.json", encoding="utf-8"))

PQ, PP, PC = pre["Q"], pre["P"], pre["CORR"]
preit = {i["no"]: i for i in S["items"]}
QO, PO, CO = {q["no"]: q for q in post["Q"]}, post["P"], post["CORR"]
pnames = list(PP.keys())
onames = post["names"]

# ---------- peta konstruk (post -> pre), ditetapkan manual dari naskah soal ----------
# (post_no, pre_no, label konstruk, jenis: "sama" / "mirip")
MAP = [
    (1, 16, "Kolaborasi tim real-time", "sama"),
    (2, 10, "Asal usul Canva (Fusion Books)", "sama"),
    (4, 6, "Hierarki visual — pernyataan yang bertentangan", "sama"),
    (5, 3, "Paket harga Canva", "mirip"),
    (6, 7, "Format ekspor PNG untuk gambar", "sama"),
    (7, 2, "Pernyataan benar tentang Canva", "sama"),
    (10, 15, "Batas jumlah font dan warna", "sama"),
    (11, 5, "Menu panel kiri editor", "sama"),
    (14, 14, "Ukuran kanvas per platform", "mirip"),
    (15, 19, "Empat nilai berkarya dengan hati", "sama"),
    (16, 18, "Urutan langkah prosedural di editor", "mirip"),
    (17, 16, "Komentar pada elemen desain", "mirip"),
    (19, 8, "Teori warna (skema warna)", "mirip"),
    (20, 13, "Tujuan pelatihan", "mirip"),
]
NEW_POST = {3: "Brand Kit", 8: "Warna liturgi ungu", 9: "Format ekspor MP4",
            12: "Tiga pendiri Canva", 13: "Eyedropper", 18: "Etika AI (Ensiklik Paus Leo XIV)"}
DROP_PRE = {1: "Daftar akun gratis", 4: "Cara kerja drag-and-drop", 11: "Ruang kosong (white space)",
            12: "Manfaat penyimpanan cloud", 17: "Slogan pelatihan", 20: "Profil pemateri"}

out = []
W = out.append

# ---------- A. gambaran umum ----------
Npre, Npost = len(pnames), len(onames)
sc_pre = {n: PP[n]["correct"] for n in pnames}
sc_post = {n: CO[n].count("C") for n in onames}
act_pre = [n for n in pnames if 20 - PC[n].count("-") > 0]
act_post = [n for n in onames if 20 - CO[n].count("-") > 0]

cor_pre = sum(sc_pre.values()); wr_pre = sum(PC[n].count("X") for n in pnames)
cor_po = sum(sc_post.values()); wr_po = sum(CO[n].count("X") for n in onames)

W("=" * 78)
W("A. GAMBARAN UMUM  (Vincent dikeluarkan dari post-test)")
W("=" * 78)
W("%-34s %14s %14s %10s" % ("Ukuran", "PRE-TEST", "POST-TEST", "Selisih"))


def row(lab, a, b, fmt="%.2f", d=True):
    try:
        dd = (fmt % (b - a)) if d else ""
        if d and (b - a) > 0: dd = "+" + dd
    except Exception:
        dd = ""
    W("%-34s %14s %14s %10s" % (lab, fmt % a if isinstance(a, float) else a,
                                fmt % b if isinstance(b, float) else b, dd))


row("Sesi terekam", Npre, Npost, "%d")
row("Sesi aktif (>=1 jawaban)", len(act_pre), len(act_post), "%d")
row("Butir", 20, 20, "%d")
row("Mode pelaksanaan", "Live (14 menit)", "Homework (3 hari)", "%s", False)
row("Akurasi seluruh sesi (%)", cor_pre / (Npre * 20) * 100, cor_po / (Npost * 20) * 100)
row("Akurasi sesi aktif (%)", cor_pre / (len(act_pre) * 20) * 100, cor_po / (len(act_post) * 20) * 100)
row("Akurasi atas butir dijawab (%)", cor_pre / (cor_pre + wr_pre) * 100, cor_po / (cor_po + wr_po) * 100)
row("Rata-rata benar (semua sesi)", st.mean(sc_pre.values()), st.mean(sc_post.values()))
row("Rata-rata benar (sesi aktif)", st.mean([sc_pre[n] for n in act_pre]), st.mean([sc_post[n] for n in act_post]))
row("Median benar (sesi aktif)", float(st.median([sc_pre[n] for n in act_pre])), float(st.median([sc_post[n] for n in act_post])))
row("Simpangan baku", st.pstdev(list(sc_pre.values())), st.pstdev(list(sc_post.values())))
row("Skor tertinggi", max(sc_pre.values()), max(sc_post.values()), "%d")
row("Skor terendah (sesi aktif)", min(sc_pre[n] for n in act_pre), min(sc_post[n] for n in act_post), "%d")
row("Reliabilitas KR-20", S["kr20"], post["stats"]["kr20"], "%.3f")
row("Kesalahan baku ukur (butir)", S["sem"], post["stats"]["sem"], "%.2f")
row("Mencapai KKM 14/20", sum(1 for v in sc_pre.values() if v >= 14), sum(1 for v in sc_post.values() if v >= 14), "%d")
row("Sel tidak dijawab (%)", sum(PC[n].count("-") for n in pnames) / (Npre * 20) * 100,
    sum(CO[n].count("-") for n in onames) / (Npost * 20) * 100)
W("")

# ---------- B. peserta berpasangan ----------
pmap = post["pmap"]
paired = [(o, pmap[o]) for o in onames if pmap.get(o)]
# hilangkan duplikat sesi kedua Yovita*: pilih sesi post terbaik per orang pre
bymap = defaultdict(list)
for o, p in paired:
    bymap[p].append(o)
PAIR = []
for p, os in bymap.items():
    o = max(os, key=lambda x: sc_post[x])
    PAIR.append((o, p, sc_pre[p], sc_post[o]))
PAIR.sort(key=lambda r: -(r[3] - r[2]))

W("=" * 78)
W("B. ANALISIS BERPASANGAN — %d PESERTA YANG MENGIKUTI KEDUA TES" % len(PAIR))
W("=" * 78)
W("%-24s %-22s %5s %5s %7s %8s" % ("Nama post-test", "Nama pre-test", "PRE", "POST", "Gain", "Gain %"))
for o, p, a, b in PAIR:
    g = b - a
    gp = (g / (20 - a) * 100) if a < 20 else 0
    W("%-24s %-22s %5d %5d %+7d %7.0f%%" % (o[:24], p[:22], a, b, g, gp))
ga = [a for _, _, a, _ in PAIR]; gb = [b for _, _, _, b in PAIR]
gains = [b - a for _, _, a, b in PAIR]
W("-" * 78)
W("%-47s %5.2f %5.2f %+7.2f" % ("RATA-RATA", st.mean(ga), st.mean(gb), st.mean(gains)))
W("%-47s %5.1f %5.1f" % ("MEDIAN", st.median(ga), st.median(gb)))
n_ = len(PAIR)
sdg = st.stdev(gains) if n_ > 1 else 0
t = st.mean(gains) / (sdg / math.sqrt(n_)) if sdg else float("inf")
dz = st.mean(gains) / sdg if sdg else float("inf")
sdp = st.pstdev(ga + gb)
W("")
W("Naik   : %d peserta" % sum(1 for g in gains if g > 0))
W("Tetap  : %d peserta" % sum(1 for g in gains if g == 0))
W("Turun  : %d peserta" % sum(1 for g in gains if g < 0))
W("Rata-rata gain      : %+.2f butir (SD gain %.2f)" % (st.mean(gains), sdg))
W("Uji-t berpasangan   : t(%d) = %.2f" % (n_ - 1, t))
W("Ukuran efek Cohen dz: %.2f" % dz)
W("Gain ternormalisasi <g> (Hake) : %.3f" % ((st.mean(gb) - st.mean(ga)) / (20 - st.mean(ga))))
W("")

# ---------- C. konstruk ----------
W("=" * 78)
W("C. PERBANDINGAN PER KONSTRUK — %d konstruk yang diuji pada kedua tes" % len(MAP))
W("=" * 78)
W("%-44s %6s %6s %6s %8s %6s" % ("Konstruk", "pre p", "post p", "Δ p", "Jenis", "Butir"))
crows = []
for po, pr, lab, jen in MAP:
    a = preit[pr]["p"]; b = QO[po]["p"]
    crows.append((lab, a, b, b - a, jen, "Q%d→Q%d" % (pr, po)))
for lab, a, b, d, jen, bt in sorted(crows, key=lambda r: -r[3]):
    W("%-44s %6.2f %6.2f %+6.2f %8s %6s" % (lab[:44], a, b, d, jen, bt))
W("-" * 78)
W("%-44s %6.2f %6.2f %+6.2f" % ("RATA-RATA konstruk",
                                st.mean(r[1] for r in crows), st.mean(r[2] for r in crows),
                                st.mean(r[3] for r in crows)))
W("")
W("Butir post-test yang TIDAK ada padanannya di pre-test (%d):" % len(NEW_POST))
for k, v in sorted(NEW_POST.items()):
    W("   post Q%-2d  p=%.2f  %s" % (k, QO[k]["p"], v))
W("")
W("Butir pre-test yang TIDAK diulang di post-test (%d):" % len(DROP_PRE))
for k, v in sorted(DROP_PRE.items()):
    W("   pre  Q%-2d  p=%.2f  %s" % (k, preit[k]["p"], v))
W("")

# ---------- D. butir post ----------
W("=" * 78)
W("D. ANALISIS BUTIR POST-TEST (n=%d, Vincent dikeluarkan)" % Npost)
W("=" * 78)
W("%-4s %-40s %5s %5s %5s %5s %6s %6s %5s" % ("No", "Pokok", "B", "S", "0", "p", "D", "rpb", "Kat"))
for q in sorted(post["Q"], key=lambda x: -x["p"]):
    kat = "Sukar" if q["p"] < .30 else ("Sedang" if q["p"] <= .70 else "Mudah")
    W("Q%-3d %-40s %5d %5d %5d %5.2f %6.2f %6.2f %5s"
      % (q["no"], q["key"][:40], q["correct_excl"], q["incorrect_excl"], q["unatt_excl"],
         q["p"], q["D"], q["rpb"], kat))
W("")

# ---------- E. peserta post ----------
W("=" * 78)
W("E. PESERTA POST-TEST")
W("=" * 78)
ordp = sorted(onames, key=lambda n: (-sc_post[n], PO[n]["time_s"]))
W("%-4s %-24s %5s %5s %5s %6s %9s %10s" % ("#", "Nama", "B", "S", "0", "Nilai", "Waktu", "Pre-test"))
for i, n in enumerate(ordp, 1):
    p = pmap.get(n)
    W("%-4d %-24s %5d %5d %5d %6.0f %9s %10s"
      % (i, n[:24], sc_post[n], CO[n].count("X"), CO[n].count("-"), sc_post[n] / 20 * 100,
         "%d:%02d" % (PO[n]["time_s"] // 60, PO[n]["time_s"] % 60),
         ("%d/20" % sc_pre[p]) if p else "—"))
W("")

txt = "\n".join(out)
io.open("cmp_out.txt", "w", encoding="utf-8").write(txt)
json.dump({"PAIR": PAIR, "crows": crows, "gains": gains,
           "t": t, "dz": dz, "sdg": sdg,
           "sc_post": sc_post, "sc_pre": sc_pre,
           "NEW_POST": NEW_POST, "DROP_PRE": DROP_PRE, "MAP": MAP},
          io.open("cmp.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written")
