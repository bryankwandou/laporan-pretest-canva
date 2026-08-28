# -*- coding: utf-8 -*-
"""Analisis lanjutan: sesi tuntas saja, dampak pengeluaran Vincent, reliabilitas terkoreksi."""
import json, io, math, statistics as st
from collections import Counter

pre = json.load(io.open("core.json", encoding="utf-8"))
S = json.load(io.open("stats.json", encoding="utf-8"))
post = json.load(io.open("post_core.json", encoding="utf-8"))
raw = json.load(io.open("post_core_raw.json", encoding="utf-8"))
cmp_ = json.load(io.open("cmp.json", encoding="utf-8"))

PP, PC = pre["P"], pre["CORR"]
QO, PO, CO = {q["no"]: q for q in post["Q"]}, post["P"], post["CORR"]
onames, pmap = post["names"], post["pmap"]
sc_post = {n: CO[n].count("C") for n in onames}
sc_pre = {n: PP[n]["correct"] for n in PP}
att_post = {n: 20 - CO[n].count("-") for n in onames}

out = []
W = out.append

# ---------- F. dampak pengeluaran Vincent ----------
W("=" * 78)
W("F. DAMPAK PENGELUARAN VINCENT (QA TESTER) DARI ANALISIS")
W("=" * 78)
vq = [q for q in raw["Q"]]
vc = 0
RES = {11: "Pengaturan resolusi layar monitor", 17: "Komentar langsung pada elemen desain di Canva"}
vrow = []
for q in sorted(vq, key=lambda x: x["no"]):
    key = q["key"] or RES[q["no"]]
    a = q["answers"].get("Vincent")
    s = "-" if a is None else ("C" if a == key else "X")
    vrow.append(s)
    if s == "C":
        vc += 1
vt = raw["P"]["Vincent"]["time_s"]
W("Vincent tercatat: %d benar, %d salah, %d kosong, waktu total %d:%02d."
  % (vc, vrow.count("X"), vrow.count("-"), vt // 60, vt % 60))
W("Pola waktu per butir dari sheet Time Data memuat sejumlah entri 00:00:01 — khas")
W("penelusuran perangkat lunak, bukan orang yang membaca soal.")
W("")
W("%-30s %10s %10s %8s" % ("Ukuran post-test", "TERMASUK", "DIKELUARKAN", "Selisih"))
n_in = len(onames) + 1
c_in = sum(sc_post.values()) + vc
W("%-30s %10d %10d %8d" % ("Sesi", n_in, len(onames), -1))
W("%-30s %10.2f %10.2f %+8.2f" % ("Rata-rata benar", c_in / n_in, st.mean(sc_post.values()),
                                  st.mean(sc_post.values()) - c_in / n_in))
W("%-30s %10.2f %10.2f %+8.2f" % ("Akurasi seluruh sesi (%)", c_in / (n_in * 20) * 100,
                                  sum(sc_post.values()) / (len(onames) * 20) * 100,
                                  sum(sc_post.values()) / (len(onames) * 20) * 100 - c_in / (n_in * 20) * 100))
W("")
W("Seluruh angka post-test pada laporan ini memakai kolom DIKELUARKAN (n=15).")
W("")

# ---------- G. sesi tuntas ----------
comp = [n for n in onames if att_post[n] == 20]
inc = [n for n in onames if att_post[n] < 20]
W("=" * 78)
W("G. SESI TUNTAS VERSUS SESI TIDAK TUNTAS")
W("=" * 78)
W("Sesi tuntas (menjawab 20/20 butir) : %d dari %d" % (len(comp), len(onames)))
W("Sesi tidak tuntas                  : %d" % len(inc))
for n in sorted(inc, key=lambda n: -att_post[n]):
    W("   %-24s menjawab %2d/20, benar %2d, waktu %d:%02d"
      % (n, att_post[n], sc_post[n], PO[n]["time_s"] // 60, PO[n]["time_s"] % 60))
W("")
cv = [sc_post[n] for n in comp]
W("Sesi tuntas — rata-rata benar %.2f dari 20 (%.1f%%), median %.1f, rentang %d-%d, SD %.2f"
  % (st.mean(cv), st.mean(cv) / 20 * 100, st.median(cv), min(cv), max(cv), st.pstdev(cv)))
W("Sesi tuntas — mencapai KKM 14/20 : %d dari %d (%.0f%%)"
  % (sum(1 for v in cv if v >= 14), len(cv), sum(1 for v in cv if v >= 14) / len(cv) * 100))

# reliabilitas atas sesi tuntas
var_c = st.pvariance(cv)
spq = 0
for q in post["Q"]:
    qi = q["no"] - 1
    p = sum(1 for n in comp if CO[n][qi] == "C") / len(comp)
    spq += p * (1 - p)
kr_c = (20 / 19) * (1 - spq / var_c) if var_c else 0
sem_c = st.pstdev(cv) * math.sqrt(max(0, 1 - kr_c))
W("Sesi tuntas — KR-20 %.3f, SEM +/-%.2f butir  (dibanding KR-20 %.3f atas seluruh 15 sesi)"
  % (kr_c, sem_c, post["stats"]["kr20"]))
W("")
W("Catatan: KR-20 0,935 atas seluruh 15 sesi adalah angka semu. Dua sesi nol jawaban")
W("dan dua sesi hampir kosong menciptakan varians buatan yang menggelembungkan")
W("reliabilitas. Angka yang layak dilaporkan adalah %.3f atas %d sesi tuntas." % (kr_c, len(comp)))
W("")

# ---------- H. berpasangan, sesi tuntas ----------
PAIRC = [(o, p, a, b) for o, p, a, b in cmp_["PAIR"] if att_post[o] == 20]
W("=" * 78)
W("H. ANALISIS BERPASANGAN ATAS SESI TUNTAS SAJA (n=%d)" % len(PAIRC))
W("=" * 78)
W("Tiga peserta yang tampak 'turun' pada tabel B seluruhnya adalah sesi tidak tuntas:")
for o, p, a, b in cmp_["PAIR"]:
    if att_post[o] < 20:
        W("   %-24s pre %2d -> post %2d, tetapi hanya menjawab %d/20 butir"
          % (o, a, b, att_post[o]))
W("Penurunannya adalah artefak sesi yang tidak diselesaikan, bukan kemunduran pengetahuan.")
W("")
W("%-24s %5s %5s %7s %8s" % ("Nama", "PRE", "POST", "Gain", "Gain %"))
for o, p, a, b in sorted(PAIRC, key=lambda r: -(r[3] - r[2])):
    W("%-24s %5d %5d %+7d %7.0f%%" % (o[:24], a, b, b - a, (b - a) / (20 - a) * 100))
ga = [a for _, _, a, _ in PAIRC]; gb = [b for _, _, _, b in PAIRC]
gg = [b - a for _, _, a, b in PAIRC]
n_ = len(gg); sdg = st.stdev(gg); t = st.mean(gg) / (sdg / math.sqrt(n_))
W("-" * 78)
W("%-24s %5.2f %5.2f %+7.2f" % ("RATA-RATA", st.mean(ga), st.mean(gb), st.mean(gg)))
W("")
W("Naik %d, tetap %d, turun %d dari %d peserta." % (sum(1 for g in gg if g > 0), sum(1 for g in gg if g == 0), sum(1 for g in gg if g < 0), n_))
W("Rata-rata gain        : %+.2f butir (SD %.2f)" % (st.mean(gg), sdg))
W("Uji-t berpasangan     : t(%d) = %.2f" % (n_ - 1, t))
CRIT = {5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179}
cv_ = CRIT.get(n_ - 1, 2.2)
W("Nilai kritis t(%d) pada alfa 0,05 dua sisi = %.3f  ->  %s"
  % (n_ - 1, cv_, "SIGNIFIKAN" if abs(t) > cv_ else "TIDAK signifikan"))
W("Cohen dz              : %.2f (%s)" % (st.mean(gg) / sdg,
                                         "besar" if st.mean(gg) / sdg >= .8 else ("sedang" if st.mean(gg) / sdg >= .5 else "kecil")))
W("Gain ternormalisasi <g>: %.3f (%s)" % ((st.mean(gb) - st.mean(ga)) / (20 - st.mean(ga)),
                                          "sedang" if (st.mean(gb) - st.mean(ga)) / (20 - st.mean(ga)) >= .3 else "rendah"))
# uji tanda
k_pos = sum(1 for g in gg if g > 0)
from math import comb
pbin = sum(comb(n_, i) for i in range(k_pos, n_ + 1)) / 2 ** n_
W("Uji tanda (binomial)  : %d dari %d naik, p satu sisi = %.4f" % (k_pos, n_, pbin))
W("")

# ---------- I. waktu ----------
W("=" * 78)
W("I. WAKTU PENGERJAAN")
W("=" * 78)
W("Pre-test  : live, batas waktu per butir, rata-rata total %d detik"
  % st.mean([PP[n]["time_s"] for n in PP if PP[n]["correct"] > 0 or 20 - PC[n].count("-") > 0]))
tc = [PO[n]["time_s"] for n in comp]
W("Post-test : mode Homework, dibuka 25 Agu 22:51 dan ditutup 28 Agu 22:07 (3 hari)")
W("            rata-rata waktu sesi tuntas %d menit %d detik (rentang %d:%02d - %d:%02d)"
  % (st.mean(tc) // 60, st.mean(tc) % 60, min(tc) // 60, min(tc) % 60, max(tc) // 60, max(tc) % 60))
W("")
W("%-24s %6s %6s %8s" % ("Nama (sesi tuntas)", "Benar", "Menit", "Detik/butir"))
for n in sorted(comp, key=lambda n: -sc_post[n]):
    W("%-24s %6d %6.1f %8.1f" % (n[:24], sc_post[n], PO[n]["time_s"] / 60, PO[n]["time_s"] / 20))
r = st.correlation([PO[n]["time_s"] for n in comp], cv) if len(comp) > 2 else 0
W("")
W("Korelasi waktu total dengan jumlah benar (sesi tuntas): r = %.3f" % r)
W("")

txt = "\n".join(out)
io.open("cmp_out2.txt", "w", encoding="utf-8").write(txt)
json.dump({"PAIRC": PAIRC, "comp": comp, "inc": inc, "kr_c": kr_c, "sem_c": sem_c,
           "t_c": t, "dz_c": st.mean(gg) / sdg, "g_c": (st.mean(gb) - st.mean(ga)) / (20 - st.mean(ga)),
           "mean_gain_c": st.mean(gg), "sd_gain_c": sdg, "pbin": pbin, "crit": cv_,
           "vincent": {"correct": vc, "row": vrow, "time_s": vt}},
          io.open("cmp2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written")
