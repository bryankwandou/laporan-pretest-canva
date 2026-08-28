# -*- coding: utf-8 -*-
# ============ 01 RINGKASAN
ws = wb.create_sheet("01 Ringkasan Eksekutif")
title(ws, "POST-TEST PELATIHAN CANVA — RINGKASAN EKSEKUTIF DAN PERBANDINGAN TERHADAP PRE-TEST",
      "Post-test dibuka 25 Agustus 2026 pukul 22:51 dan ditutup 28 Agustus 2026 pukul 22:07 dalam mode Homework. "
      "Sesi atas nama Vincent (QA tester) dikeluarkan dari seluruh perhitungan pada workbook ini.", 8)

r = 4
secrow(ws, r, "A. ANGKA POKOK", 8); r += 1
head(ws, r, ["Ukuran", "Pre-test", "Post-test", "Selisih", "Catatan", "", "", ""], [40, 16, 16, 14, 78])
r += 1
mg = C2["mean_gain_c"]
KP = [
    ("Sesi terekam", "37", "15", "−22", "Post-test diikuti kurang dari separuh peserta pre-test."),
    ("Sesi tuntas (20/20 butir)", "—", "10", "—", "Lima sesi post-test tidak diselesaikan; dua di antaranya nol jawaban."),
    ("Mode pelaksanaan", "Live, 14 menit", "Homework, 3 hari", "berubah", "Perubahan mode adalah pembatas tafsir terbesar pada laporan ini."),
    ("Akurasi seluruh sesi", "32,3%", "49,7%", "+17,4 pp", "Angka kotor; belum dikoreksi terhadap perbedaan komposisi peserta."),
    ("Akurasi sesi tuntas", "—", "69,5%", "—", "Rata-rata 13,90 dari 20 butir atas 10 sesi tuntas."),
    ("Rata-rata benar (semua sesi)", "6,46", "9,93", "+3,47", "Terseret ke bawah oleh sesi yang tidak diselesaikan."),
    ("Mencapai KKM 14/20", "1 dari 37 (2,7%)", "6 dari 15 (40%)", "+37 pp", "Atas sesi tuntas saja: 6 dari 10 (60%)."),
    ("Reliabilitas KR-20", "0,751", "0,721", "−0,030", "Angka post-test dihitung atas 10 sesi tuntas; lihat sheet 09."),
    ("Kesalahan baku ukur", "±1,87 butir", "±1,76 butir", "−0,11", "Selisih skor di bawah angka ini tidak bermakna secara statistik."),
    ("Gain berpasangan (sesi tuntas)", "8,62", "13,62", "+5,00", "8 peserta, seluruhnya naik. t(7)=3,67, signifikan pada α=0,05."),
]
for a, b, c_, d, e in KP:
    putrow(ws, r, [a, b, c_, d, e], ctr=(2, 3, 4), bold=(1, 4), h=26)
    ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=8)
    ws.cell(r, 4).fill = GRN if str(d).startswith("+") else (RED if str(d).startswith("−") else GRY)
    r += 1
r += 1

secrow(ws, r, "B. SEMBILAN TEMUAN UTAMA", 8); r += 1
FIND = [
    ("Post-test BUKAN instrumen yang sama dengan pre-test",
     "Hanya 14 dari 20 butir memiliki padanan konstruk di pre-test, dan tidak satu pun identik kata per kata. Enam butir post-test menguji materi yang sama sekali tidak ada di pre-test (Brand Kit, warna liturgi, MP4, tiga pendiri, Eyedropper, etika AI), sementara enam butir pre-test tidak diulang. Akibatnya selisih skor mentah tidak dapat dibaca sebagai murni hasil belajar."),
    ("Mode pelaksanaan berubah dari live menjadi take-home",
     "Pre-test dikerjakan langsung dengan batas waktu per butir. Post-test dibuka tiga hari penuh sebagai Homework, tanpa pengawasan, dengan materi pelatihan tersedia. Sebagian kenaikan skor mencerminkan kesempatan membuka materi, bukan hanya daya ingat."),
    ("Pada peserta yang menyelesaikan kedua tes, kenaikan nyata dan konsisten",
     "Delapan peserta mengikuti kedua tes sampai tuntas. Kedelapannya naik, tanpa kecuali. Rata-rata naik 5,00 butir (dari 8,62 menjadi 13,62). Uji-t berpasangan t(7)=3,67 melampaui nilai kritis 2,365; uji tanda memberi p=0,0039."),
    ("Ukuran efeknya besar, tetapi gain ternormalisasinya hanya sedang",
     "Cohen dz = 1,30 (besar). Namun gain ternormalisasi Hake <g> = 0,44 — artinya hanya 44% dari jarak menuju skor sempurna yang berhasil ditutup. Masih ada 6,4 butir rata-rata yang belum dikuasai."),
    ("Tiga peserta yang tampak turun sebenarnya tidak menyelesaikan post-test",
     "Tintin tityn (0 dari 20 butir dijawab), Maria (3 dari 20) dan Ivonne runturambi (2 dari 20). Ketiganya berhenti dalam waktu di bawah 45 detik. Penurunannya adalah artefak sesi terputus, bukan kemunduran pengetahuan."),
    ("Angka reliabilitas 0,935 atas 15 sesi adalah angka semu",
     "Dua sesi nol jawaban dan dua sesi hampir kosong menciptakan varians buatan yang menggelembungkan KR-20. Dihitung atas 10 sesi tuntas, reliabilitasnya 0,721 — setara pre-test, dan itulah angka yang layak dilaporkan."),
    ("Materi yang paling berhasil ditanamkan: ukuran kanvas, ekspor, dan tujuan pelatihan",
     "Ukuran kanvas per platform naik dari p=0,19 menjadi 0,53. Tujuan pelatihan naik 0,32→0,67. Format ekspor PNG naik 0,22→0,53. Asal usul Canva naik 0,14→0,47. Keempatnya adalah materi yang disampaikan berulang dan dipraktikkan."),
    ("Dua konstruk justru menurun",
     "Komentar pada elemen desain turun dari p=0,43 menjadi 0,13 dan urutan langkah prosedural turun 0,46→0,33. Keduanya butir prosedural yang menuntut mengingat urutan langkah — bagian yang paling cepat luntur bila tidak dipraktikkan berulang."),
    ("42% pengecoh pada post-test tidak berfungsi",
     "Dari 60 opsi salah, 25 tidak dipilih oleh satu pun peserta. Pada Q8, Q19 dan Q20 ketiga pengecohnya mati sekaligus, sehingga butirnya efektif hanya berisi satu opsi masuk akal. Peluang tebakan benar naik dari 25% menjadi 33–50%."),
]
for i, (t, b) in enumerate(FIND, 1):
    ws.cell(r, 1, i).font = Font(size=12, bold=True, color="FFFFFF")
    ws.cell(r, 1).fill = HDR
    ws.cell(r, 1).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(r, 2, t).font = Font(size=10, bold=True)
    ws.cell(r, 2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
    ws.cell(r, 3, b).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 3).font = Font(size=10)
    for j in range(1, 9):
        ws.cell(r, j).border = BOX
    ws.row_dimensions[r].height = 62
    r += 1
ws.column_dimensions["B"].width = 44
r += 1

secrow(ws, r, "C. KESIMPULAN YANG DAPAT DIPERTANGGUNGJAWABKAN", 8); r += 1
for t in [
    "Pernyataan yang didukung data: pada delapan peserta yang menyelesaikan pre-test maupun post-test, penguasaan materi Canva naik rata-rata 5,00 butir dari 20, dan kenaikan itu terjadi pada seluruh delapan orang tanpa kecuali. Secara statistik kenaikan ini signifikan (t(7)=3,67; p<0,05) dengan ukuran efek besar (dz=1,30).",
    "Pernyataan yang TIDAK didukung data: bahwa akurasi kelas naik dari 32,3% menjadi 49,7% sebagai akibat pelatihan. Angka itu membandingkan dua kelompok peserta berbeda (37 versus 15 orang), dua perangkat soal berbeda, dan dua mode pelaksanaan berbeda. Ketiganya berubah bersamaan, sehingga sebabnya tidak dapat dipisahkan.",
    "Batas tafsir: karena post-test dikerjakan tiga hari tanpa pengawasan dengan materi tersedia, angka +5,00 butir sebaiknya dibaca sebagai batas ATAS dampak pelatihan, bukan sebagai perkiraan tak bias. Dampak sesungguhnya berada di antara nol dan angka tersebut.",
    "Rekomendasi paling penting untuk pengukuran berikutnya: gunakan perangkat soal yang identik pada pre dan post, dan laksanakan keduanya dalam mode yang sama. Dengan dua perubahan itu saja, angka gain akan langsung dapat ditafsirkan tanpa catatan kaki.",
]:
    note(ws, r, t, 8, 46); r += 1
