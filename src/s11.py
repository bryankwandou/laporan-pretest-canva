# -*- coding: utf-8 -*-
# ============================================================ 12 REKOMENDASI
ws = wb.create_sheet("12 Rekomendasi")
title(ws, "REKOMENDASI DAN RENCANA TINDAK LANJUT",
      "Setiap rekomendasi dikaitkan langsung dengan temuan data yang mendasarinya. Kolom bukti berisi angka yang dapat ditelusuri kembali ke sheet analisis terkait.", 7)

r = 4
secrow(ws, r, "A. PRIORITAS MATERI PELATIHAN — URUTAN BERDASARKAN DATA", 7); r += 1
head(ws, r, ["Urutan", "Materi", "Bukti dari data", "Alokasi\nwaktu", "Metode yang disarankan",
             "Butir terkait", "Ukuran keberhasilan"],
     [8, 34, 54, 11, 54, 16, 44])
r += 1
PRIOR = [
    (1, "Daftar akun Canva gratis dan kenali paket harga",
     "Q1 p=0,16 — hanya 6 dari 14 penjawab tahu langkah pertama. Enam orang mengira harus menunggu akun dibagikan panitia.",
     "15 menit",
     "Praktik langsung di tempat: seluruh peserta membuka www.canva.com dan mendaftar dengan email masing-masing sebelum materi apa pun dimulai. Panitia berkeliling memastikan semua berhasil masuk.",
     "Q1, Q3",
     "100% peserta berhasil masuk akun sendiri sebelum menit ke-20"),
    (2, "Ukuran kanvas dan format ekspor",
     "Ranah terlemah, penguasaan 20,3%. Q14 p=0,19 (15 orang memilih 1080x1080 untuk Story), Q7 p=0,22 (19 orang memilih PPTX atau PDF untuk Instagram).",
     "20 menit",
     "Bagikan satu lembar rujukan berisi tabel ukuran per platform dan tabel kapan memakai PNG, JPG, PDF, MP4. Lalu praktik ekspor satu desain ke dua format berbeda.",
     "Q7, Q14",
     "Setiap peserta mengekspor satu desain ukuran 1080x1920 dalam format PNG"),
    (3, "Antarmuka editor: Panel Kiri, Area Desain, Elemen, Template",
     "Q5 p=0,22 — 11 orang mengira Panel Kiri dan Area Desain berfungsi sama. Q4 p=0,24 — 9 orang mengira elemen harus diunduh dulu.",
     "25 menit",
     "Tur layar terpandu sambil peserta mengikuti di perangkat masing-masing. Tunjuk setiap bagian, minta peserta mengklik bersamaan. Jangan pakai slide, pakai layar Canva sungguhan.",
     "Q4, Q5, Q9, Q18",
     "Setiap peserta menambahkan satu ikon dari menu Elemen tanpa dibantu"),
    (4, "Prinsip desain: hierarki visual, white space, font, warna",
     "Penguasaan 35,1%. Q11 — 11 orang mengira ruang kosong adalah pemborosan. Q8 p=0,30 — konsep warna analog belum dikenal.",
     "30 menit",
     "Tampilkan pasangan contoh buruk versus baik secara berdampingan, minta peserta menebak mana yang lebih baik dan mengapa. Beri nama pada intuisi yang sudah mereka punya.",
     "Q6, Q8, Q11, Q15",
     "Peserta dapat menyebutkan alasan mengapa satu desain lebih mudah dibaca"),
    (5, "Penyimpanan cloud dan kolaborasi tim",
     "Penguasaan relatif lebih baik (Q12 p=0,41, Q16 p=0,43) tetapi 10 orang masih mengira desain hanya bisa dibuka dari satu perangkat.",
     "15 menit",
     "Demonstrasi: buka desain yang sama dari laptop dan ponsel secara bersamaan, lalu undang satu peserta ikut mengedit di depan kelas.",
     "Q12, Q16",
     "Peserta membuka desainnya sendiri dari perangkat kedua"),
    (6, "Identitas pelatihan: tujuan, slogan, nilai",
     "Penguasaan 25,2% — wajar karena belum pernah disampaikan. Q17 tidak dijawab benar oleh satu pun peserta kelompok atas maupun bawah.",
     "5 menit",
     "Sampaikan sekali di pembukaan dan tampilkan di slide penutup. Ulangi butir Q13, Q17, Q19 pada post-test untuk mengukur daya ingat isi pelatihan.",
     "Q13, Q17, Q19",
     "Penguasaan ketiga butir naik di atas 70% pada post-test"),
]
for no, mat, bukti, wkt, met, bt, uk in PRIOR:
    row = [no, mat, bukti, wkt, met, bt, uk]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i in (1, 4, 6):
            c.alignment = Alignment(horizontal="center", vertical="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 1).font = Font(size=14, bold=True, color="FFFFFF")
    ws.cell(r, 1).fill = HDR
    ws.cell(r, 2).font = Font(size=10, bold=True)
    ws.row_dimensions[r].height = 78
    r += 1
r += 2

secrow(ws, r, "B. PERBAIKAN PELAKSANAAN KUIS (TEKNIS)", 7); r += 1
head(ws, r, ["No", "Masalah yang terbukti", "Bukti angka", "Tindakan perbaikan", "", "", ""],
     [6, 40, 44, 110])
r += 1
TEK = [
    ("Peserta bergabung setelah kuis dimulai",
     "Q1 kehilangan 23 dari 37 sel (62%), Q2 12 sel, Q3 17 sel. Pola menurun tajam khas keterlambatan masuk.",
     "Buka ruang kuis 10 menit lebih awal. Tampilkan daftar peserta yang sudah masuk di layar. Baru mulai butir pertama setelah jumlah yang masuk stabil. Untuk post-test, gunakan mode mandiri (assign) agar tidak ada yang tertinggal."),
    ("Empat sesi tidak menghasilkan satu jawaban pun",
     "Aqifah, Yofita, Sri Suyani dan Sri Suyani* mencatat 0 jawaban dan waktu total 0-30 detik.",
     "Sediakan satu panitia khusus penanganan perangkat. Siapkan 2-3 perangkat cadangan. Kirim tautan kuis lewat grup pesan 15 menit sebelum mulai, bukan hanya kode PIN di layar."),
    ("Nama peserta terduplikasi dan sulit dicocokkan",
     "Sri Suyani muncul 3 kali, Aqifah 2 kali, farida johannes 2 kali. Ada pula 'Yofita' dan 'Yovita' yang mungkin orang yang sama.",
     "Wajibkan format nama baku (nama lengkap sesuai daftar hadir). Sebarkan tautan personal per peserta bila memungkinkan, sehingga satu orang menghasilkan tepat satu sesi."),
    ("Butir Q17 tidak mengukur apa pun",
     "D = 0,00 dan r-pbis = -0,01. Nol benar di kelompok atas maupun bawah.",
     "Keluarkan Q17 dari perhitungan skor pre-test. Pertahankan butirnya hanya untuk post-test sebagai pengukur daya ingat materi. Bila dipakai lagi sebagai pre-test, ganti dengan butir yang bisa dinalar tanpa hafalan."),
    ("Q20 punya pengecoh yang tidak berfungsi",
     "Tiga opsi salah hanya dipilih 4 kali dari 26 penjawab; kunci dipilih 22 kali.",
     "Tulis ulang ketiga opsi salah agar sama-sama masuk akal secara akademis, misalnya dengan menyebut jabatan akademik lain yang serupa."),
    ("Durasi 14 menit terlalu sempit untuk 20 butir bacaan panjang",
     "Rata-rata 17-18 detik per butir, sementara beberapa butir memuat empat pernyataan yang harus dibandingkan.",
     "Perpanjang batas waktu per butir menjadi 45-60 detik untuk butir bertipe pernyataan majemuk (Q2, Q5, Q9, Q11), atau perpendek redaksi opsinya."),
]
for i, (m, b, t) in enumerate(TEK, 1):
    ws.cell(r, 1, i).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(r, 1).font = Font(bold=True)
    ws.cell(r, 2, m).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 2).font = Font(size=10, bold=True)
    ws.cell(r, 3, b).alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=7)
    ws.cell(r, 4, t).alignment = Alignment(wrap_text=True, vertical="top")
    for j in range(1, 8):
        ws.cell(r, j).border = BOX
    ws.row_dimensions[r].height = 62
    r += 1
r += 2

secrow(ws, r, "C. RANCANGAN PENGUKURAN DAMPAK PELATIHAN", 7); r += 1
head(ws, r, ["Aspek", "Ketentuan", "Alasan", "", "", "", ""], [26, 60, 110])
r += 1
DES = [
    ("Instrumen post-test", "Gunakan 19 butir yang sama (Q17 dikeluarkan) tanpa mengubah redaksi.",
     "Perbandingan pre dan post hanya sah bila instrumennya identik. Q17 dikeluarkan karena terbukti tidak mengukur apa pun."),
    ("Garis dasar pembanding", "36,2% (33 sesi aktif), bukan 32,3% (37 sesi).",
     "Empat sesi nol adalah kegagalan teknis, bukan hasil ujian. Memakainya sebagai pembanding akan melebih-lebihkan keberhasilan pelatihan."),
    ("Target kenaikan minimum", "Akurasi kelas mencapai 70% pada post-test, naik sekitar 34 poin persen.",
     "Materi yang diuji seluruhnya bersifat dasar dan langsung dipraktikkan. Kenaikan di bawah 25 poin persen menandakan penyampaian materi perlu dievaluasi."),
    ("Target per ranah", "Teknis Output & Ukuran minimal 75%; Akses & Model Bisnis minimal 90%.",
     "Kedua ranah ini murni prosedural dan dipraktikkan langsung, sehingga wajar menuntut penguasaan hampir penuh."),
    ("Uji statistik", "Uji-t berpasangan atau uji McNemar per butir, dengan peserta yang sama pada kedua tes.",
     "Hanya peserta yang mengikuti pre-test dan post-test yang boleh dibandingkan. Dengan n sekitar 33, uji berpasangan memberi daya uji yang memadai."),
    ("Ambang keberhasilan individu", "Minimal 14 dari 19 butir benar (74%).",
     "Setara KKM 70%. Pada pre-test hanya 1 dari 37 sesi mencapainya; angka ini menjadi pembanding yang jelas."),
    ("Waktu pelaksanaan", "Segera setelah sesi praktik terakhir, dalam ruangan yang sama.",
     "Menunda post-test memasukkan variabel lupa dan belajar mandiri, sehingga yang terukur bukan lagi dampak pelatihan."),
]
for a, k, al in DES:
    ws.cell(r, 1, a).font = Font(size=10, bold=True)
    ws.cell(r, 1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 2, k).alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
    ws.cell(r, 3, al).alignment = Alignment(wrap_text=True, vertical="top")
    for j in range(1, 8):
        ws.cell(r, j).border = BOX
        if j > 1:
            ws.cell(r, j).font = Font(size=10)
    ws.row_dimensions[r].height = 48
    r += 1
r += 2

secrow(ws, r, "D. KESIMPULAN", 7); r += 1
for t in [
    "Pre-test ini berhasil menjalankan fungsinya. Instrumen memiliki reliabilitas 0,751 dan rata-rata daya beda 0,470 - keduanya memenuhi standar untuk tes 20 butir. Sembilan belas dari dua puluh butir bekerja sebagaimana mestinya.",
    "Kemampuan awal peserta terhadap Canva berada pada tingkat sangat rendah dan merata. Akurasi 32,3% atas seluruh sesi atau 36,2% atas sesi aktif, dibandingkan 25% peluang tebakan acak, menunjukkan pengetahuan yang dimiliki peserta bersifat sepotong-sepotong dan belum terstruktur. Tidak ada satu pun peserta yang mencapai kategori Sangat Baik.",
    "Kelemahan terbesar bersifat prosedural, bukan konseptual. Peserta mampu menalar tentang prinsip desain (C2 = 35,9%) tetapi tidak tahu langkah konkret yang harus diambil (C3 = 27,9%). Implikasinya tegas: porsi praktik harus melebihi porsi ceramah.",
    "Sebagian besar kesenjangan skor antarpeserta berasal dari jumlah butir yang sempat dijawab, bukan dari ketepatan menjawab. Kelompok atas mengirim 18,6 jawaban rata-rata, kelompok bawah hanya 6,6. Memperbaiki pelaksanaan teknis kuis akan memperbaiki kualitas data lebih besar daripada memperbaiki soalnya.",
    "Rekomendasi utama: alokasikan 15 menit pertama pelatihan untuk memastikan setiap peserta berhasil mendaftar dan masuk akun Canva gratis miliknya sendiri, lalu 20 menit berikutnya untuk ukuran kanvas dan format ekspor. Dua hal ini adalah penghalang terbesar sekaligus paling cepat dirobohkan, dan keduanya prasyarat bagi seluruh materi berikutnya.",
]:
    note(ws, r, t, 7, 44); r += 1
