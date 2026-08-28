# -*- coding: utf-8 -*-
# ============ 09 METODOLOGI
ws = wb.create_sheet("09 Metodologi")
title(ws, "METODOLOGI, VALIDASI, RUMUS DAN KETERBATASAN",
      "Seluruh angka post-test pada workbook ini dapat direproduksi dari tiga berkas sumber di bawah.", 6)
r = 4
secrow(ws, r, "A. SUMBER DATA", 6); r += 1
head(ws, r, ["Berkas", "Isi", "Peran", "", "", ""], [54, 54, 88])
r += 1
SRC = [
    ("post-testpelatihancanva25agustus2026-...-68e3ea.xlsx",
     "Ekspor resmi Wayground: Overview (naskah, jawaban tiap peserta), Participant Data, Time Data, Quiz Details.",
     "Sumber utama seluruh data respons, waktu, dan metadata sesi."),
    ("Free Printable post-test pelatihan canva 25 agustus 2026.pdf",
     "Naskah cetak resmi 20 butir beserta keempat opsi setiap butir. Dicetak tanpa tanda kunci (graded=false).",
     "Dipakai untuk memverifikasi kunci hasil rekonstruksi dan untuk menemukan opsi yang tidak pernah dipilih siapa pun."),
    ("core.json / stats.json (dari laporan pre-test)",
     "Dataset pre-test terkonsolidasi: 20 butir, 37 peserta, matriks respons dan statistik butir.",
     "Basis pembanding untuk seluruh analisis gain dan pemetaan konstruk."),
]
for a, b, c_ in SRC:
    putrow(ws, r, [a, b, c_], bold=(1,), h=48, fsz=9)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    r += 1
r += 1

secrow(ws, r, "B. VALIDASI YANG DILAKUKAN — TIGA LAPIS", 6); r += 1
for t in [
    "<b>Lapis 1 — jumlah sel kosong.</b> Untuk setiap butir, jumlah sel jawaban yang kosong pada sheet Overview dicocokkan dengan kolom Unattempted. Cocok pada 20 dari 20 butir. Berbeda dengan ekspor pre-test, ekspor post-test TIDAK memuat entri 'hantu', sehingga tidak diperlukan penyaringan.".replace("<b>", "").replace("</b>", ""),
    "Lapis 2 — rekonstruksi kunci. Kunci diambil sebagai opsi yang jumlah pemilihnya sama persis dengan jumlah Correct pada butir tersebut. Cara ini langsung menyelesaikan 18 butir. Dua butir (Q11 dan Q17) menyisakan dua calon karena ada dua opsi dengan jumlah pemilih identik.",
    "Lapis 3 — penyelesaian dua kunci ambigu lewat kendala. Keempat kombinasi calon kunci Q11 x Q17 diuji terhadap syarat: jumlah benar setiap peserta hasil hitungan harus sama persis dengan kolom Correct pada Participant Data untuk seluruh 16 sesi. Hanya SATU kombinasi memenuhi syarat itu, yaitu Q11 = 'Pengaturan resolusi layar monitor' dan Q17 = 'Komentar langsung pada elemen desain di Canva'.",
    "Lapis 4 — verifikasi silang terhadap naskah PDF. Seluruh 20 kunci hasil rekonstruksi dicocokkan ke daftar opsi pada naskah cetak resmi. Kecocokan sempurna (skor kemiripan 1,00) pada 20 dari 20 butir, termasuk kedua kunci yang tadinya ambigu — dan keduanya memang benar secara isi. Kunci pada workbook ini karena itu dapat dianggap pasti, bukan perkiraan.",
    "Lapis 5 — konsistensi setelah Vincent dikeluarkan. Setelah sesi QA dikeluarkan, seluruh statistik butir dihitung ulang dari matriks respons, bukan diambil dari kolom agregat ekspor. Jumlah benar hasil hitung ulang dicocokkan kembali dengan Participant Data untuk 15 sesi tersisa; tidak ada selisih.",
]:
    note(ws, r, t, 6, 52); r += 1
r += 1

secrow(ws, r, "C. PERLAKUAN TERHADAP SESI VINCENT (QA TESTER)", 6); r += 1
head(ws, r, ["Ukuran", "Termasuk Vincent", "Dikeluarkan", "Selisih", "", ""], [34, 18, 18, 14])
r += 1
V = C2["vincent"]
vc = V["correct"]
n_in = 16; c_in = sum(sc_post.values()) + vc
VR = [("Jumlah sesi", 16, 15, "−1"),
      ("Total jawaban benar", c_in, sum(sc_post.values()), "−%d" % vc),
      ("Rata-rata benar", round(c_in / n_in, 2), round(st.mean(sc_post.values()), 2),
       "%+.2f" % (st.mean(sc_post.values()) - c_in / n_in)),
      ("Akurasi seluruh sesi (%)", round(c_in / (n_in * 20) * 100, 2),
       round(sum(sc_post.values()) / (15 * 20) * 100, 2),
       "%+.2f" % (sum(sc_post.values()) / (15 * 20) * 100 - c_in / (n_in * 20) * 100))]
for a, b, c_, d in VR:
    putrow(ws, r, [a, b, c_, d], ctr=(2, 3, 4), bold=(1, 4), h=18)
    ws.cell(r, 3).fill = BLU
    r += 1
r += 1
for t in [
    "Vincent tercatat %d benar, %d salah, 0 kosong, dengan waktu total hanya %d menit %d detik untuk 20 butir. Sheet Time Data memuat sejumlah entri 00:00:01 pada sesinya — pola khas penelusuran perangkat lunak, bukan orang yang membaca soal." % (vc, 20 - vc, V["time_s"] // 60, V["time_s"] % 60),
    "Vincent juga tidak muncul pada daftar peserta pre-test, sehingga tidak dapat masuk analisis berpasangan dalam keadaan apa pun.",
    "Dampak pengeluarannya kecil terhadap angka agregat (rata-rata turun 0,19 butir, akurasi turun 0,96 poin persen) tetapi pengeluaran tetap dilakukan karena sesi uji perangkat lunak bukan hasil ujian peserta dan tidak boleh ikut membentuk statistik butir maupun penetapan kelompok atas dan bawah.",
]:
    note(ws, r, t, 6, 40); r += 1
r += 1

secrow(ws, r, "D. RUMUS", 6); r += 1
head(ws, r, ["Ukuran", "Rumus", "Penerapan", "", "", ""], [30, 50, 92])
r += 1
FRM = [
    ("Tingkat kesukaran (p)", "p = B / N", "B = jumlah benar; N = 15 sesi post-test setelah Vincent dikeluarkan. Sel kosong dihitung tidak benar."),
    ("Daya beda (D)", "D = (BA / nA) − (BB / nB)", "Kelompok atas dan bawah masing-masing 27% dari 15, dibulatkan menjadi 4 sesi."),
    ("Point-biserial", "r = ((M1 − M0) / SDt) × akar(p × q)", "M1 rata-rata skor total peserta yang benar; M0 yang salah; q = 1 − p."),
    ("Reliabilitas KR-20", "KR20 = (k/(k−1)) × (1 − jumlah pq / varians)", "k = 20. Dihitung dua kali: atas 15 sesi (0,935) dan atas 10 sesi tuntas (0,721). Yang dilaporkan adalah angka kedua."),
    ("Kesalahan baku ukur", "SEM = SD × akar(1 − r)", "SD sesi tuntas 3,33; r = 0,721. Hasil ±1,76 butir."),
    ("Gain mentah", "gain = post − pre", "Dihitung per individu, hanya untuk peserta yang mengikuti kedua tes sampai tuntas."),
    ("Gain ternormalisasi (Hake)", "g = (post − pre) / (maks − pre)", "Mengukur berapa persen dari jarak menuju skor sempurna yang berhasil ditutup. Hasil 0,440."),
    ("Uji-t berpasangan", "t = rata gain / (SD gain / akar n)", "n = 8, derajat bebas 7. Hasil t = 3,67 melawan nilai kritis 2,365 pada alfa 0,05 dua sisi."),
    ("Ukuran efek Cohen dz", "dz = rata gain / SD gain", "Hasil 1,30, tergolong besar (ambang: 0,20 kecil, 0,50 sedang, 0,80 besar)."),
    ("Uji tanda", "peluang binomial k naik dari n, p = 0,5", "8 dari 8 naik memberi p = 0,0039 satu sisi. Tidak bergantung pada asumsi sebaran normal."),
]
for a, b, c_ in FRM:
    putrow(ws, r, [a, b, c_], bold=(1,), h=32)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    ws.cell(r, 2).font = Font(size=10, name="Consolas")
    r += 1
r += 1

secrow(ws, r, "E. KETERBATASAN — HARUS DIBACA SEBELUM MENGUTIP ANGKA MANA PUN", 6); r += 1
for t in [
    "1. Instrumen berubah. Post-test bukan pengulangan pre-test. Hanya 14 dari 20 konstruk beririsan dan hanya dua butir yang praktis identik kata per kata. Selisih skor mentah karena itu memuat campuran antara hasil belajar dan perbedaan tingkat kesukaran perangkat soal, dan keduanya tidak dapat dipisahkan dari data yang tersedia.",
    "2. Mode berubah. Pre-test live berbatas waktu, post-test Homework selama tiga hari tanpa pengawasan dengan materi pelatihan tersedia. Ini penjelasan tandingan yang paling kuat terhadap kenaikan skor dan tidak dapat dikesampingkan.",
    "3. Penyusutan peserta 60%. Dari 37 sesi pre-test hanya 15 yang muncul di post-test, dan hanya 8 pasangan tuntas. Peserta yang bertahan rata-rata pre-testnya 8,62 berbanding 6,46 untuk seluruh kelas — yang bertahan adalah yang sejak awal lebih menguasai. Bias seleksi ini bekerja ke arah melebih-lebihkan keberhasilan.",
    "4. n = 8 pada uji berpasangan. Delapan orang adalah jumlah yang kecil, dan satu peserta dengan gain +14 (Agnes Nurak) menyumbang besar terhadap rata-rata. Uji kepekaan dilakukan dengan mengeluarkan pengamatan tersebut: rata-rata gain turun dari 5,00 menjadi 3,71 butir, tetapi simpangan bakunya menyusut tajam dari 3,85 menjadi 1,38 sehingga t(6) justru naik menjadi 7,12 dan dz menjadi 2,69. Kesimpulan bahwa terjadi kenaikan karena itu TIDAK bergantung pada satu pengamatan ekstrem; yang bergantung padanya hanyalah besaran rata-ratanya.",
    "5. Daya beda post-test menggelembung. Sepuluh butir mencapai D = 1,00 karena kelompok bawah sebagian besar terdiri atas sesi terputus yang tidak menjawab apa pun. Nilai D pada post-test tidak sebanding dengan nilai D pada pre-test dan sebaiknya tidak diperbandingkan langsung.",
    "6. Tidak ada kelompok pembanding. Tanpa kelompok yang tidak mengikuti pelatihan, sebagian kenaikan yang teramati dapat berasal dari efek mengerjakan tes serupa untuk kedua kalinya, bukan dari pelatihan itu sendiri.",
    "7. Laporan ini tidak memuat pemeriksaan kecurangan. Dalam mode take-home tanpa pengawasan, pemeriksaan semacam itu justru paling dibutuhkan, tetapi datanya tidak tersedia dalam berkas yang diberikan.",
    "8. Yang diukur tetap pengetahuan deklaratif. Apakah peserta benar-benar mampu membuat desain yang layak tidak terukur oleh tes pilihan ganda dan memerlukan penilaian karya.",
]:
    note(ws, r, t, 6, 50); r += 1

wb.save("LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx")
print("saved; sheets=%d" % len(wb.sheetnames), wb.sheetnames)
