# -*- coding: utf-8 -*-
# ============ 02 PERBANDINGAN UMUM
ws = wb.create_sheet("02 Perbandingan Umum")
title(ws, "PERBANDINGAN PRE-TEST VERSUS POST-TEST — GAMBARAN UMUM",
      "Tiga basis pembanding disajikan berdampingan karena masing-masing menjawab pertanyaan berbeda. "
      "Basis yang paling sah untuk menilai dampak pelatihan adalah kolom paling kanan (peserta berpasangan yang tuntas).", 7)
r = 4
head(ws, r, ["Ukuran", "Pre-test\n(37 sesi)", "Post-test\n(15 sesi)", "Post-test\nsesi tuntas (10)",
             "Berpasangan\npre (8)", "Berpasangan\npost (8)", "Tafsiran"], [34, 13, 13, 14, 13, 13, 72])
r += 1
gaC = [a for _, _, a, _ in PAIRC]; gbC = [b for _, _, _, b in PAIRC]
compv = [sc_post[n] for n in COMP]
allpre = list(sc_pre.values()); allpost = list(sc_post.values())
ROWS = [
    ("Jumlah sesi", 37, 15, 10, 8, 8, "Penyusutan peserta 60% adalah keterbatasan terbesar kedua setelah perubahan instrumen."),
    ("Rata-rata jawaban benar", round(st.mean(allpre), 2), round(st.mean(allpost), 2),
     round(st.mean(compv), 2), round(st.mean(gaC), 2), round(st.mean(gbC), 2),
     "Kolom berpasangan membandingkan orang yang sama, sehingga bebas dari efek perbedaan komposisi peserta."),
    ("Median", st.median(allpre), st.median(allpost), st.median(compv), st.median(gaC), st.median(gbC),
     "Median post-test sesi tuntas (14) tepat berada di ambang KKM."),
    ("Simpangan baku", round(st.pstdev(allpre), 2), round(st.pstdev(allpost), 2),
     round(st.pstdev(compv), 2), round(st.pstdev(gaC), 2), round(st.pstdev(gbC), 2),
     "SD post-test 15 sesi (6,41) menggelembung karena sesi nol; atas sesi tuntas turun ke 3,33."),
    ("Skor tertinggi", max(allpre), max(allpost), max(compv), max(gaC), max(gbC),
     "Satu peserta mencapai 20 dari 20 pada post-test; tertinggi pre-test hanya 14."),
    ("Skor terendah", min(allpre), min(allpost), min(compv), min(gaC), min(gbC),
     "Terendah sesi tuntas post-test (8) setara rata-rata kelompok atas pre-test."),
    ("Akurasi (%)", round(sum(allpre) / (37 * 20) * 100, 1), round(sum(allpost) / (15 * 20) * 100, 1),
     round(sum(compv) / (10 * 20) * 100, 1), round(sum(gaC) / (8 * 20) * 100, 1),
     round(sum(gbC) / (8 * 20) * 100, 1), "Selisih berpasangan +25,0 poin persen adalah angka yang paling layak dikutip."),
    ("Mencapai KKM 14/20", sum(1 for v in allpre if v >= 14), sum(1 for v in allpost if v >= 14),
     sum(1 for v in compv if v >= 14), sum(1 for v in gaC if v >= 14), sum(1 for v in gbC if v >= 14),
     "Dari 8 peserta berpasangan, yang tuntas KKM naik dari 0 menjadi 5 orang."),
]
d0 = r
for a, b, c_, d, e, f_, g in ROWS:
    putrow(ws, r, [a, b, c_, d, e, f_, g], ctr=(2, 3, 4, 5, 6), bold=(1,), h=30)
    for j in (2, 3, 4):
        ws.cell(r, j).fill = BLU
    for j in (5, 6):
        ws.cell(r, j).fill = GRN
    r += 1
d1 = r - 1
r += 1

secrow(ws, r, "DATA GRAFIK — RATA-RATA JAWABAN BENAR MENURUT BASIS PEMBANDING", 7); r += 1
g0 = r
ws.cell(r, 1, "Basis"); ws.cell(r, 2, "Rata-rata benar")
for j in (1, 2):
    ws.cell(r, j).fill = HDR; ws.cell(r, j).font = WF; ws.cell(r, j).border = BOX
r += 1
GB = [("Pre-test, 37 sesi", st.mean(allpre)), ("Post-test, 15 sesi", st.mean(allpost)),
      ("Post-test, 10 sesi tuntas", st.mean(compv)),
      ("Berpasangan — pre", st.mean(gaC)), ("Berpasangan — post", st.mean(gbC))]
for a, b in GB:
    ws.cell(r, 1, a).border = BOX; ws.cell(r, 1).font = Font(size=10)
    ws.cell(r, 2, round(b, 2)).border = BOX
    ws.cell(r, 2).alignment = Alignment(horizontal="center")
    r += 1
g1 = r - 1

ch = BarChart(); ch.type = "col"; ch.style = 10
ch.title = "Rata-rata jawaban benar menurut basis pembanding (dari 20 butir)"
ch.y_axis.title = "Jawaban benar"; ch.height = 9; ch.width = 20
ch.add_data(Reference(ws, min_col=2, min_row=g0, max_row=g1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=g0 + 1, max_row=g1))
ch.dLbls = DataLabelList(); ch.dLbls.showVal = True
ch.legend = None
ws.add_chart(ch, "A%d" % (r + 2))
r += 22

for t in [
    "Ketiga basis memberi angka berbeda karena menjawab pertanyaan berbeda. Basis 37 versus 15 sesi menjawab 'berapa akurasi yang tercatat', bukan 'berapa yang dipelajari'. Basis berpasangan menjawab pertanyaan kedua, dan hanya basis itu yang mengendalikan perbedaan siapa yang ikut.",
    "Perhatikan bahwa rata-rata pre-test kelompok berpasangan (8,62) jauh di atas rata-rata pre-test seluruh kelas (6,46). Artinya yang bertahan mengikuti post-test cenderung peserta yang sejak awal lebih menguasai materi. Ini bias seleksi yang bekerja ke arah melebih-lebihkan keberhasilan bila memakai basis seluruh kelas.",
]:
    note(ws, r, t, 7, 44); r += 1
