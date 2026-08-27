# -*- coding: utf-8 -*-

# ============================================================ 01 RINGKASAN
ws = wb.active
ws.title = "01 Ringkasan Eksekutif"
title(ws, "LAPORAN EVALUASI PRE-TEST PELATIHAN CANVA — 25 AGUSTUS 2026",
      "Wayground/Quizizz Live Quiz · aktivitas 6a8cff9925d33c69acbdef23 · 10:45–10:59 WITA (14 menit) · 20 butir pilihan ganda 4 opsi · "
      "Data diverifikasi silang antara export XLSX resmi dan snapshot HTML laporan admin: kecocokan hitungan benar/salah 20 dari 20 butir (100%).", 4)

skew = sum((x - mean_s) ** 3 for x in sc.values()) / N / sd_s ** 3
kurt = sum((x - mean_s) ** 4 for x in sc.values()) / N / sd_s ** 4 - 3
avg_qt = st.mean([v for n in TIME for v in TIME[n].values() if v])

KPI = [
    ("CAKUPAN & INTEGRITAS DATA", "", "", ""),
    ("Total attempt (sesi) tercatat", 37, "sesi", "37 baris pada leaderboard"),
    ("Peserta unik", 33, "orang", "sesuai metadata resmi Wayground"),
    ("Sesi duplikat", 4, "sesi", "Sri Suyani 3x, Aqifah 2x, farida johannes 2x"),
    ("Sesi berskor nol mutlak", 4, "sesi", "Aqifah, Yofita, Sri Suyani, Sri Suyani* - 0 dari 20"),
    ("Sel data total", 740, "sel", "37 sesi x 20 butir"),
    ("Sel terisi jawaban", 541, "sel", "73,1% - sisanya kosong atau kehabisan waktu"),
    ("HASIL POKOK", "", "", ""),
    ("Respons benar", 239, "jawaban", "32,3% dari 740 sel"),
    ("Respons salah", 302, "jawaban", "40,8% dari 740 sel"),
    ("Kosong / timeout", 199, "sel", "26,9% dari 740 sel"),
    ("Akurasi kelas (metrik resmi Wayground)", "32%", "", "239 dibagi 740"),
    ("Akurasi atas jawaban yang benar-benar dikirim", "44,2%", "", "239 dibagi 541"),
    ("Peluang benar bila menebak acak", "25,0%", "", "4 opsi setiap butir"),
    ("Kelebihan di atas tebakan acak", "+7,3", "poin persen", "sinyal pengetahuan awal sangat tipis"),
    ("STATISTIK SKOR (jumlah benar dari 20)", "", "", ""),
    ("Rata-rata", round(mean_s, 2), "butir", "setara %.1f%%" % (mean_s / 20 * 100)),
    ("Median", Q2v, "butir", ""),
    ("Modus", st.mode(sc.values()), "butir", "muncul %d kali" % Counter(sc.values())[st.mode(sc.values())]),
    ("Simpangan baku (populasi)", round(sd_s, 2), "butir", ""),
    ("Varians", round(st.pvariance(sc.values()), 2), "", ""),
    ("Koefisien variasi", "%.1f%%" % (sd_s / mean_s * 100), "", "di atas 50% berarti kelompok sangat tidak homogen"),
    ("Skewness (kemencengan)", round(skew, 3), "", "menceng kanan tipis - skor rendah menumpuk"),
    ("Kurtosis (excess)", round(kurt, 3), "", "lebih landai dari kurva normal - skor tersebar merata"),
    ("Nilai maksimum", max(sc.values()), "butir", "vivi - 12.310 poin"),
    ("Nilai minimum", min(sc.values()), "butir", "4 sesi"),
    ("Rentang", max(sc.values()) - min(sc.values()), "butir", ""),
    ("Kuartil 1", Q1v, "butir", ""),
    ("Kuartil 3", Q3v, "butir", ""),
    ("Jangkauan antarkuartil (IQR)", Q3v - Q1v, "butir", ""),
    ("MUTU INSTRUMEN", "", "", ""),
    ("Reliabilitas KR-20", round(S["kr20"], 3), "", "kategori cukup baik (0,70-0,80): perbedaan skor antarpeserta nyata, bukan keberuntungan"),
    ("Standard Error of Measurement", "+/- %.2f" % S["sem"], "butir", "skor sejati berada dalam rentang 1,87 butir dari skor tampak"),
    ("Rata-rata tingkat kesukaran (p)", round(st.mean(i["p"] for i in items), 3), "", "instrumen tergolong SUKAR bagi populasi ini"),
    ("Rata-rata daya beda (D)", round(st.mean(i["D"] for i in items), 3), "", "kategori BAIK (di atas 0,40) - tes memilah peserta dengan efektif"),
    ("Butir yang wajib direvisi atau dibuang", 1, "butir", "Q17 - daya beda 0,00 dan korelasi butir-total -0,01"),
    ("WAKTU", "", "", ""),
    ("Rata-rata waktu total pengerjaan", "%d:%02d" % (st.mean(tt.values()) // 60, st.mean(tt.values()) % 60), "menit:detik", ""),
    ("Waktu tercepat dengan skor di atas nol", "3:40", "menit:detik", "Yovita - 10 benar"),
    ("Waktu terlama", "%d:%02d" % (max(tt.values()) // 60, max(tt.values()) % 60), "menit:detik", ""),
    ("Rata-rata waktu per butir yang dijawab", round(avg_qt, 1), "detik", ""),
    ("KETUNTASAN", "", "", ""),
    ("Lulus KKM 70% (minimal 14 benar)", sum(1 for x in sc.values() if x >= 14), "sesi", "2,7% dari 37"),
    ("Mencapai minimal 50% (10 benar)", sum(1 for x in sc.values() if x >= 10), "sesi", "%.1f%%" % (sum(1 for x in sc.values() if x >= 10) / N * 100)),
    ("Di bawah 25% (kurang dari 5 benar)", sum(1 for x in sc.values() if x < 5), "sesi", "%.1f%%" % (sum(1 for x in sc.values() if x < 5) / N * 100)),
]
head(ws, 4, ["INDIKATOR", "NILAI", "SATUAN", "CATATAN / INTERPRETASI"], [46, 16, 22, 92])
r = 5
for k, v, u, nt in KPI:
    if v == "" and u == "" and nt == "":
        secrow(ws, r, k, 4)
    else:
        ws.cell(r, 1, k).font = Font(bold=True, size=10)
        c = ws.cell(r, 2, v); c.font = Font(bold=True, size=11, color=NAVY)
        c.alignment = Alignment(horizontal="center")
        ws.cell(r, 3, u).font = Font(size=9)
        ws.cell(r, 4, nt).font = Font(size=9, italic=True, color="555555")
        for cc in range(1, 5):
            ws.cell(r, cc).border = BOX
    r += 1

r += 1
secrow(ws, r, "SEPULUH TEMUAN YANG MENENTUKAN", 4); r += 1
FIND = [
    ("1. Ini benar-benar pre-test: pengetahuan awal peserta hampir nol.",
     "Akurasi kelas 32% dengan 4 opsi jawaban. Tebakan acak murni menghasilkan 25%. Kelebihan pengetahuan nyata hanya 7,3 poin persen. "
     "Bahkan bila dihitung hanya atas jawaban yang benar-benar dikirim (44,2%), separuh lebih tetap salah. Ini justru kabar baik untuk pelatihan: "
     "ruang perbaikan sangat lebar dan post-test akan mudah menunjukkan kenaikan."),
    ("2. Seperempat data hilang karena masalah teknis, bukan karena peserta tidak tahu.",
     "199 dari 740 sel kosong. Sebarannya tidak merata: Q1 kehilangan 23 sel (62%), Q3 17 sel, Q20 13 sel dan Q2 12 sel. "
     "Pola menurun tajam ini adalah tanda khas peserta bergabung terlambat setelah kuis live dimulai, bukan tanda soal terlalu sulit. "
     "Konsekuensinya akurasi resmi 32% adalah angka yang MERENDAHKAN kemampuan sebenarnya."),
    ("3. Q17 (slogan pelatihan) rusak secara statistik dan harus dibuang.",
     "Tingkat kesukaran 0,08, daya beda 0,00, korelasi butir-total -0,01. Butir ini sama sekali tidak membedakan peserta kuat dan lemah. "
     "15 dari 28 penjawab memilih 'Kreativitas adalah Berkat, Melayani adalah Rasa Syukur' - pengecoh yang lima kali lebih menarik daripada kunci "
     "'Desain Kreatif, Komunikasi Efektif' (3 penjawab). Ini bukan soal pengetahuan, ini soal hafalan materi yang belum pernah disampaikan."),
    ("4. Q20 (profil pemateri) adalah butir dengan mutu terbaik.",
     "p=0,59, daya beda 0,90 (tertinggi), korelasi butir-total 0,57. Sembilan dari sepuluh peserta kelompok atas menjawab benar, "
     "hanya nol dari sepuluh kelompok bawah. Namun perlu dicatat butir ini terakhir dan nama pemateri sudah tampil di layar - "
     "sebagian daya bedanya berasal dari siapa yang masih bertahan sampai butir ke-20, bukan murni dari pengetahuan."),
    ("5. Miskonsepsi terbesar: peserta mengira Canva harus dibayar dulu.",
     "Pada Q1 hanya 6 dari 14 penjawab tahu langkah pertama adalah mendaftar akun gratis. Enam lainnya memilih 'menunggu panitia membagikan akun bersama' "
     "dan dua memilih 'mengunduh aplikasi berbayar'. Sebaliknya pada Q3, 17 dari 20 penjawab (85%) sudah benar memilih Paket Gratis. "
     "Artinya peserta paham paket gratis itu cukup, tetapi tidak tahu cara mengaksesnya sendiri. Hambatannya operasional, bukan konseptual."),
    ("6. Kelemahan terkonsentrasi pada hal teknis-operasional, bukan pada konsep.",
     "Rata-rata p per ranah: Teknis Output & Ukuran 0,20 (terlemah) - Materi Internal Pelatihan 0,25 - Akses & Model Bisnis 0,31 - "
     "Prinsip Desain Grafis 0,35 - Sejarah & Profil 0,36 - Konsep & Fitur Canva 0,36 (terkuat). "
     "Peserta bisa menalar tentang desain, tetapi tidak tahu angka 1080x1920 atau kapan memakai PNG."),
    ("7. Empat sesi nol mutlak dan empat duplikat nama mencemari peringkat.",
     "Aqifah, Yofita, Sri Suyani dan Sri Suyani* mendapat 0 dari 20 tanpa satu pun jawaban terkirim - ini sesi hantu akibat gagal masuk atau salah perangkat. "
     "Bila keempatnya dikeluarkan, rata-rata kelas naik dari 6,46 menjadi 7,24 benar dan akurasi naik dari 32,3% menjadi 36,2%. "
     "Angka 36,2% adalah cerminan yang lebih jujur atas kemampuan awal peserta."),
    ("8. Kecepatan tidak berhubungan dengan ketepatan.",
     "Di antara 33 sesi aktif, korelasi antara waktu total pengerjaan dan jumlah jawaban benar adalah -0,03 alias praktis nol. "
     "Yovita menyelesaikan tercepat (3 menit 40 detik) dengan 10 benar; Elisabet bunga memakai waktu terlama (8 menit 32 detik) dan hanya meraih 6 benar. "
     "Pada tingkat butir polanya sama: jawaban benar rata-rata butuh 17,1 detik, jawaban salah 18,6 detik. Peserta yang lambat bukan sedang berpikir lebih dalam - mereka sedang ragu."),
    ("9. Reliabilitas 0,751 membuat hasil ini layak dipakai untuk keputusan kelompok, tidak untuk menghakimi individu.",
     "KR-20 0,751 pada tes 20 butir tergolong cukup baik. Namun SEM +/- 1,87 butir berarti peserta dengan 9 benar dan peserta dengan 7 benar "
     "secara statistik tidak dapat dibedakan. Gunakan data ini untuk merancang materi, bukan untuk membuat ranking yang dipublikasikan."),
    ("10. Rekomendasi tunggal paling berdampak: alokasikan 15 menit pertama pelatihan untuk praktik pendaftaran akun dan ekspor file.",
     "Dua ranah terlemah (akses akun dan format ekspor) adalah keterampilan prosedural yang bisa dikuasai dalam satu sesi praktik singkat, "
     "dan keduanya adalah prasyarat untuk semua materi berikutnya. Tanpa itu, peserta tidak bisa menyelesaikan latihan apa pun."),
]
for h, b in FIND:
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    c = ws.cell(r, 1, h); c.font = Font(bold=True, size=10, color=NAVY)
    c.alignment = Alignment(wrap_text=True, vertical="center"); c.fill = F("F7F9FC")
    c.border = BOX; ws.row_dimensions[r].height = 18; r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    c = ws.cell(r, 1, b); c.font = Font(size=10)
    c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = BOX
    ws.row_dimensions[r].height = 46; r += 1
ws.freeze_panes = "A5"

