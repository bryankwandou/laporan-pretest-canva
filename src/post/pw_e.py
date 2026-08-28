# -*- coding: utf-8 -*-
# ============ 04 KONSTRUK
ws = wb.create_sheet("04 Perbandingan Konstruk")
title(ws, "PERBANDINGAN PER KONSTRUK — MATERI APA YANG BENAR-BENAR BERPINDAH",
      "Karena naskah soal berubah, perbandingan dilakukan pada tingkat konstruk (pokok pengetahuan yang diuji), bukan pada nomor butir. "
      "Pemetaan ditetapkan dengan membaca naskah kedua tes satu per satu; kolom 'jenis' menandai seberapa setara kedua butir.", 9)
r = 4
secrow(ws, r, "A. 14 KONSTRUK YANG DIUJI PADA KEDUA TES", 9); r += 1
head(ws, r, ["Konstruk", "Butir\npre → post", "Jenis", "p pre", "p post", "Δ p",
             "Arah", "Tafsiran", ""], [42, 13, 9, 9, 9, 9, 12, 74])
r += 1
k0 = r
CR = sorted(C1["crows"], key=lambda x: -x[3])
TAFC = {
    "Ukuran kanvas per platform": "Kenaikan terbesar. Materi hafalan murni yang jelas berhasil disampaikan lewat rujukan tabel ukuran.",
    "Tujuan pelatihan": "Wajar naik tajam — pada pre-test materinya memang belum pernah disampaikan.",
    "Asal usul Canva (Fusion Books)": "Butir identik kata per kata pada kedua tes. Kenaikan +0,33 adalah bukti hafalan yang paling bersih pada laporan ini.",
    "Format ekspor PNG untuk gambar": "Ranah terlemah pre-test kini terangkat. Praktik ekspor langsung terbukti bekerja.",
    "Pernyataan benar tentang Canva": "Pemahaman umum tentang sifat platform membaik.",
    "Kolaborasi tim real-time": "Naik sehat, dan konsisten dengan Q1 post-test yang p=0,67.",
    "Hierarki visual — pernyataan yang bertentangan": "Naik, meski kuncinya berubah (pre: ukuran teks seragam; post: terlalu banyak font).",
    "Batas jumlah font dan warna": "Naik, sejalan dengan hierarki visual. Prinsip desain tersampaikan.",
    "Menu panel kiri editor": "Naik tipis dan masih rendah (p=0,33). Pengenalan antarmuka belum tuntas.",
    "Empat nilai berkarya dengan hati": "Naik tipis meski materi disampaikan langsung — daya ingat isi pelatihan lemah.",
    "Teori warna (skema warna)": "Naik tipis. Konstruk berubah dari warna analog menjadi monokromatik, jadi tidak sepenuhnya setara.",
    "Paket harga Canva": "Praktis tidak berubah, tetapi soalnya bergeser dari penalaran memilih paket menjadi hafalan angka harga.",
    "Urutan langkah prosedural di editor": "TURUN. Butir yang menuntut mengingat urutan langkah adalah yang paling cepat luntur.",
    "Komentar pada elemen desain": "TURUN paling tajam. Pada post-test hanya 2 dari 15 peserta menjawab benar.",
}
for lab, a, b, d, jen, bt in CR:
    arah = "Naik" if d > 0.05 else ("Tetap" if d >= -0.05 else "TURUN")
    putrow(ws, r, [lab, bt, jen, round(a, 2), round(b, 2), round(d, 2), arah, TAFC.get(lab, "")],
           ctr=(2, 3, 4, 5, 6, 7), bold=(1, 6), h=30)
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=9)
    ws.cell(r, 6).fill = GRN if d > 0.05 else (RED if d < -0.05 else GRY)
    ws.cell(r, 7).fill = GRN if arah == "Naik" else (RED if arah == "TURUN" else GRY)
    ws.cell(r, 3).fill = BLU if jen == "sama" else YEL
    r += 1
k1 = r - 1
putrow(ws, r, ["RATA-RATA 14 KONSTRUK", "", "", round(st.mean(x[1] for x in CR), 2),
               round(st.mean(x[2] for x in CR), 2), round(st.mean(x[3] for x in CR), 2), "", ""],
       ctr=(4, 5, 6), bold=(1, 4, 5, 6), h=20)
ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=9)
for j in range(1, 10):
    ws.cell(r, j).fill = F(LGREY)
r += 2

ch = BarChart(); ch.type = "bar"; ch.grouping = "clustered"; ch.style = 10
ch.title = "Tingkat kesukaran (p) per konstruk: pre-test versus post-test"
ch.x_axis.title = "Proporsi benar"; ch.height = 14; ch.width = 24
ch.add_data(Reference(ws, min_col=4, max_col=5, min_row=k0 - 1, max_row=k1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=k0, max_row=k1))
ws.add_chart(ch, "A%d" % r)
r += 30

secrow(ws, r, "B. BUTIR POST-TEST YANG TIDAK ADA PADANANNYA DI PRE-TEST (6 BUTIR)", 9); r += 1
head(ws, r, ["Butir", "Materi", "p post", "Kategori", "Mengapa penting dicatat", "", "", "", ""],
     [8, 34, 9, 12, 92])
r += 1
WHY = {
    3: "Materi baru yang tidak pernah diuji sebelumnya. p=0,27 menjadikannya butir tersukar kedua — Brand Kit belum tersampaikan.",
    8: "Materi liturgi, bukan materi Canva. p=0,73 tertinggi di seluruh post-test, tetapi mengukur pengetahuan yang sudah dimiliki peserta sebelum pelatihan.",
    9: "Format ekspor video. Melengkapi ranah teknis yang pada pre-test hanya diwakili PNG dan ukuran kanvas.",
    12: "Perluasan dari butir asal usul Canva. p=0,53, wajar untuk hafalan nama yang baru disampaikan.",
    13: "Fitur Eyedropper. p=0,53 — separuh peserta mengenalinya setelah pelatihan.",
    18: "Etika penggunaan AI. Materi paling baru dan paling jauh dari Canva teknis; p=0,47.",
}
for no in sorted(NEWP):
    p = QO[no]["p"]
    kat = "Sukar" if p < .30 else ("Sedang" if p <= .70 else "Mudah")
    putrow(ws, r, ["Q%d" % no, NEWP[no], round(p, 2), kat, WHY[no]], ctr=(1, 3, 4), bold=(1, 2), h=30)
    ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=9)
    ws.cell(r, 4).fill = {"Sukar": RED, "Sedang": YEL, "Mudah": GRN}[kat]
    r += 1
r += 1

secrow(ws, r, "C. BUTIR PRE-TEST YANG TIDAK DIULANG PADA POST-TEST (6 BUTIR)", 9); r += 1
head(ws, r, ["Butir", "Materi", "p pre", "Akibat tidak diulang", "", "", "", "", ""], [8, 34, 9, 104])
r += 1
LOSS = {
    1: "Ini penghalang nomor satu pada pre-test (p=0,16) dan menjadi rekomendasi utama laporan sebelumnya. Karena tidak diulang, keberhasilan menutup penghalang itu TIDAK TERUKUR.",
    4: "Konsep drag-and-drop (p=0,24) tidak diuji ulang, padahal ini fondasi cara kerja Canva.",
    11: "Prinsip ruang kosong (p=0,24) hilang dari pengukuran, padahal termasuk kelemahan prinsip desain yang paling menonjol.",
    12: "Manfaat penyimpanan cloud (p=0,41) tidak diuji ulang; sebagian tercakup tidak langsung oleh Q1 dan Q17 post-test.",
    17: "Slogan pelatihan (p=0,08) adalah butir gagal pada pre-test dan memang sudah direkomendasikan untuk dikeluarkan. Ini satu-satunya penghapusan yang sejalan dengan rekomendasi.",
    20: "Profil pemateri (p=0,59) tidak diulang. Kehilangannya tidak merugikan karena butir ini mengukur hafalan yang tidak berkaitan dengan kemampuan desain.",
}
for no in sorted(DROPP):
    putrow(ws, r, ["Q%d" % no, DROPP[no], round(preit[no]["p"], 2), LOSS[no]], ctr=(1, 3), bold=(1, 2), h=32)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=9)
    r += 1
r += 1
for t in [
    "Rata-rata 14 konstruk naik dari p=0,34 menjadi 0,49 — kenaikan 0,15 atau 15 poin persen. Angka ini lebih rendah daripada selisih akurasi kelas (+17,4 pp) dan jauh lebih rendah daripada gain berpasangan (+25,0 pp), karena membandingkan seluruh peserta kedua tes tanpa mengendalikan siapa yang ikut.",
    "Dua konstruk yang turun keduanya bertipe prosedural: mengingat urutan langkah dan mengetahui fitur mana yang dipakai untuk memberi masukan. Ini pola yang lazim — pengetahuan prosedural luntur paling cepat bila hanya didemonstrasikan sekali dan tidak dipraktikkan berulang oleh peserta sendiri.",
    "Kehilangan butir 'daftar akun gratis' dari post-test adalah kelemahan rancangan yang paling merugikan. Rekomendasi utama laporan pre-test adalah mengalokasikan 15 menit pertama untuk memastikan setiap peserta berhasil mendaftar akun sendiri. Karena butirnya tidak diulang, keberhasilan rekomendasi itu tidak dapat dibuktikan maupun dibantah oleh data post-test.",
]:
    note(ws, r, t, 9, 46); r += 1
