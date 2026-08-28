# -*- coding: utf-8 -*-
# ============ 03 BERPASANGAN
ws = wb.create_sheet("03 Analisis Berpasangan")
title(ws, "ANALISIS BERPASANGAN — PESERTA YANG MENGIKUTI PRE-TEST DAN POST-TEST",
      "Ini adalah bukti terkuat pada seluruh laporan: membandingkan orang yang sama dengan dirinya sendiri, "
      "sehingga perbedaan komposisi peserta tidak lagi menjadi penjelasan tandingan.", 9)
r = 4
secrow(ws, r, "A. SELURUH 11 PESERTA BERPASANGAN", 9); r += 1
head(ws, r, ["#", "Nama pada post-test", "Nama pada pre-test", "Pre", "Post", "Gain",
             "Gain ternormalisasi", "Butir dijawab\npost-test", "Status"], [5, 26, 24, 8, 8, 9, 15, 14, 30])
r += 1
p0 = r
for i, (o, p, a, b) in enumerate(sorted(PAIR, key=lambda x: -(x[3] - x[2])), 1):
    g = b - a
    gn = g / (20 - a) if a < 20 else 0
    tuntas = att[o] == 20
    stt = "Tuntas" if tuntas else "TIDAK tuntas — dikeluarkan"
    putrow(ws, r, [i, o, p, a, b, g, round(gn, 3), att[o], stt], ctr=(1, 4, 5, 6, 7, 8), bold=(2, 6), h=20)
    ws.cell(r, 6).fill = GRN if g > 0 else (RED if g < 0 else GRY)
    ws.cell(r, 9).fill = GRN if tuntas else RED
    ws.cell(r, 7).number_format = "0.0%"
    r += 1
p1 = r - 1
r += 1

secrow(ws, r, "B. UJI STATISTIK ATAS 8 PESERTA BERPASANGAN YANG TUNTAS", 9); r += 1
head(ws, r, ["Ukuran", "Nilai", "Ambang / pembanding", "Kesimpulan", "", "", "", "", ""], [34, 16, 26, 76])
r += 1
gg = [b - a for _, _, a, b in PAIRC]
ST = [
    ("Jumlah pasangan (n)", "8", "—", "Kecil, tetapi memadai untuk uji berpasangan karena tiap orang menjadi pembanding dirinya sendiri."),
    ("Rata-rata pre-test", "%.2f butir" % st.mean(gaC), "Kelas pre-test 6,46", "Kelompok ini sejak awal di atas rata-rata kelas — ada bias seleksi."),
    ("Rata-rata post-test", "%.2f butir" % st.mean(gbC), "KKM 14 butir", "Rata-rata berada tepat di bawah ambang ketuntasan."),
    ("Rata-rata gain", "+%.2f butir" % st.mean(gg), "SEM ±1,76 butir", "Gain hampir tiga kali kesalahan baku ukur, sehingga bukan sekadar derau pengukuran."),
    ("Simpangan baku gain", "%.2f" % C2["sd_gain_c"], "—", "Sebaran gain lebar: dari +2 sampai +14 butir."),
    ("Uji-t berpasangan", "t(7) = %.2f" % C2["t_c"], "kritis 2,365 (α=0,05 dua sisi)", "SIGNIFIKAN — kenaikan tidak dapat dijelaskan oleh kebetulan semata."),
    ("Uji tanda (binomial)", "8 dari 8 naik", "p = %.4f satu sisi" % C2["pbin"], "Konsisten pada tiap individu, bukan hanya pada rata-rata. Ini bukti yang lebih kuat daripada rata-rata."),
    ("Ukuran efek Cohen dz", "%.2f" % C2["dz_c"], "0,20 kecil / 0,50 sedang / 0,80 besar", "BESAR."),
    ("Gain ternormalisasi <g>", "%.3f" % C2["g_c"], "<0,30 rendah / 0,30–0,70 sedang", "SEDANG — 44% dari jarak menuju skor sempurna berhasil ditutup."),
    ("Naik / tetap / turun", "8 / 0 / 0", "—", "Tidak ada satu pun peserta tuntas yang skornya tetap atau turun."),
]
for a, b, c_, d in ST:
    putrow(ws, r, [a, b, c_, d], ctr=(2,), bold=(1, 2), h=24)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=9)
    r += 1
r += 1

secrow(ws, r, "DATA GRAFIK — PRE VERSUS POST PER PESERTA (8 PESERTA TUNTAS)", 9); r += 1
c0 = r
for j, v in enumerate(["Nama", "Pre-test", "Post-test"], 1):
    ws.cell(r, j, v).fill = HDR; ws.cell(r, j).font = WF; ws.cell(r, j).border = BOX
r += 1
for o, p, a, b in sorted(PAIRC, key=lambda x: -(x[3] - x[2])):
    ws.cell(r, 1, o).border = BOX; ws.cell(r, 1).font = Font(size=10)
    ws.cell(r, 2, a).border = BOX; ws.cell(r, 3, b).border = BOX
    for j in (2, 3):
        ws.cell(r, j).alignment = Alignment(horizontal="center")
    r += 1
c1 = r - 1

ch = BarChart(); ch.type = "col"; ch.grouping = "clustered"; ch.style = 10
ch.title = "Jawaban benar sebelum dan sesudah pelatihan, per peserta"
ch.y_axis.title = "Jawaban benar (dari 20)"; ch.height = 10; ch.width = 24
ch.add_data(Reference(ws, min_col=2, max_col=3, min_row=c0, max_row=c1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=c0 + 1, max_row=c1))
ch.dLbls = DataLabelList(); ch.dLbls.showVal = True
ws.add_chart(ch, "A%d" % (r + 2))

ch2 = BarChart(); ch2.type = "bar"; ch2.style = 11
ch2.title = "Besar kenaikan (gain) per peserta"
ch2.x_axis.title = "Butir"; ch2.height = 9; ch2.width = 14
gcol = c1 + 40
ws.cell(gcol, 5, "Gain").fill = HDR; ws.cell(gcol, 5).font = WF
rr = gcol + 1
for o, p, a, b in sorted(PAIRC, key=lambda x: (x[3] - x[2])):
    ws.cell(rr, 4, o); ws.cell(rr, 5, b - a); rr += 1
ch2.add_data(Reference(ws, min_col=5, min_row=gcol, max_row=rr - 1), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=4, min_row=gcol + 1, max_row=rr - 1))
ch2.dLbls = DataLabelList(); ch2.dLbls.showVal = True
ch2.legend = None
ws.add_chart(ch2, "N%d" % (r + 2))
r += 24

for t in [
    "Kedelapan peserta naik. Pola ini penting karena uji tanda tidak bergantung pada asumsi sebaran normal — dengan 8 dari 8 naik, peluang munculnya pola ini bila pelatihan tidak berpengaruh sama sekali hanya 0,39%.",
    "Kenaikan terbesar dialami Agnes Nurak (+14 butir, dari 6 menjadi 20 sempurna). Kenaikan sebesar ini pada mode take-home tiga hari perlu dicatat apa adanya: ia bisa berarti penguasaan penuh, bisa juga berarti pengerjaan dengan membuka materi. Data yang tersedia tidak dapat memisahkan keduanya.",
    "Kenaikan terkecil dialami Marsia Sairina (+2 butir, dari 6 menjadi 8). Ia dan Ivo Emelia (10) adalah dua peserta yang setelah pelatihan masih di bawah KKM, dan keduanya berangkat dari skor pre-test 6. Keduanya kandidat utama untuk pendampingan lanjutan.",
    "Tiga peserta berpasangan lain (Tintin tityn, Maria, Ivonne runturambi) dikeluarkan dari uji statistik karena tidak menyelesaikan post-test — masing-masing hanya menjawab 0, 3 dan 2 butir dalam waktu di bawah 45 detik. Memasukkan mereka akan menurunkan rata-rata gain dari +5,00 menjadi +2,55 dan membuat hasil uji-t menjadi tidak signifikan, padahal yang diukur di situ adalah kegagalan teknis, bukan pengetahuan.",
]:
    note(ws, r, t, 9, 46); r += 1
