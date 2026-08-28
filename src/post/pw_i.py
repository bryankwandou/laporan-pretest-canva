# -*- coding: utf-8 -*-
# ============ 08 REKOMENDASI
ws = wb.create_sheet("08 Rekomendasi")
title(ws, "REKOMENDASI BERDASARKAN HASIL POST-TEST",
      "Dipisahkan menjadi tiga: materi yang masih perlu ditutup, perbaikan instrumen, dan perbaikan rancangan pengukuran.", 8)
r = 4
secrow(ws, r, "A. MATERI YANG MASIH PERLU DITUTUP — URUTAN BERDASARKAN DATA POST-TEST", 8); r += 1
head(ws, r, ["Urutan", "Materi", "Bukti dari post-test", "Tindakan", "", "", "", ""], [8, 34, 52, 84])
r += 1
PR = [
    ("Cara memberi masukan pada desain rekan (fitur Komentar)",
     "Q17 p=0,13 — hanya 2 dari 15 benar, turun dari 0,43 pada pre-test. Delapan peserta memilih 'unduh lalu kirim via email'.",
     "Sesi praktik berpasangan 10 menit: setiap peserta membuka desain rekannya, menambahkan satu komentar pada elemen tertentu, lalu rekannya membalas. Jangan didemonstrasikan di depan — harus dikerjakan sendiri oleh setiap orang."),
    ("Brand Kit — konsistensi warna, font dan logo",
     "Q3 p=0,27, butir tersukar kedua. Tujuh peserta memilih 'Warna Elemen Manual', dua memilih 'Gradien Warna'.",
     "Tunjukkan satu kasus nyata: buat Brand Kit berisi warna dan logo komunitas, lalu terapkan ke dua desain berbeda dalam satu klik. Nilai jualnya adalah hemat waktu, dan itu yang harus terlihat."),
    ("Menu panel kiri editor",
     "Q11 p=0,33, hanya naik 0,12 dari pre-test. Enam peserta masih salah mengenali isi panel kiri.",
     "Tur layar terpandu sambil peserta mengikuti di perangkat masing-masing, bukan slide. Minta peserta menyebutkan nama menu sambil mengkliknya."),
    ("Urutan langkah menggunakan template",
     "Q16 p=0,33, turun dari 0,46 pada pre-test. Lima peserta salah urutan.",
     "Berikan kartu langkah satu halaman yang dapat dibawa pulang. Pengetahuan urutan langkah luntur cepat bila hanya didengar sekali."),
    ("Teori warna",
     "Q19 p=0,40. Konsep monokromatik dikenali kurang dari separuh peserta.",
     "Cukup satu slide roda warna dengan tiga contoh skema (monokromatik, analog, komplementer) dan satu contoh desain untuk masing-masing."),
    ("Empat nilai berkarya dengan hati",
     "Q15 p=0,47 — hanya naik 0,12 meski materi disampaikan langsung dalam pelatihan.",
     "Bila nilai-nilai ini dianggap penting untuk diingat, tampilkan di slide pembuka dan penutup serta cetak pada lembar kerja peserta. Bila tidak, keluarkan dari instrumen agar tidak mengaburkan pengukuran kemampuan teknis."),
]
for i, (m, b, t) in enumerate(PR, 1):
    putrow(ws, r, [i, m, b, t], ctr=(1,), bold=(2,), h=64)
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
    ws.cell(r, 1).fill = HDR; ws.cell(r, 1).font = Font(size=13, bold=True, color="FFFFFF")
    r += 1
r += 1

secrow(ws, r, "B. PERBAIKAN INSTRUMEN POST-TEST", 8); r += 1
head(ws, r, ["Masalah", "Bukti", "Perbaikan", "", "", "", "", ""], [34, 46, 90])
r += 1
INS = [
    ("Instrumen post-test berbeda dari pre-test",
     "Hanya 14 dari 20 konstruk beririsan; tidak satu butir pun identik kata per kata kecuali Q2 dan Q15.",
     "Gunakan perangkat butir yang IDENTIK pada pre dan post. Bila ingin menambah materi baru, tambahkan sebagai butir terpisah di luar 20 butir inti, dan hitung gain hanya dari 20 butir inti."),
    ("42% pengecoh tidak berfungsi",
     "25 dari 60 opsi salah tidak dipilih siapa pun. Tiga butir kehilangan seluruh pengecohnya.",
     "Tulis ulang pengecoh memakai miskonsepsi nyata yang tercatat pada pre-test. Setiap opsi salah harus merupakan kekeliruan yang benar-benar mungkin dipercaya."),
    ("Butir Q8 mengukur pengetahuan di luar materi pelatihan",
     "Makna teologis warna ungu, p=0,73, tertinggi di seluruh post-test.",
     "Keluarkan dari perhitungan gain kemampuan Canva. Bila ingin dipertahankan, laporkan terpisah sebagai butir konteks, bukan sebagai indikator keberhasilan pelatihan."),
    ("Mode Homework membuka pintu pengerjaan dengan membuka materi",
     "Rentang tiga hari, tanpa pengawasan, rata-rata pengerjaan hanya 10 menit dan korelasi waktu dengan skor r=0,12.",
     "Laksanakan post-test langsung di akhir sesi, dalam ruangan yang sama, dengan batas waktu yang sama seperti pre-test. Ini satu perubahan yang paling banyak memulihkan daya tafsir angka gain."),
    ("Kehilangan 60% peserta antara pre dan post",
     "37 sesi pre-test menjadi 15 sesi post-test, dan hanya 8 pasangan yang tuntas.",
     "Jalankan post-test sebelum peserta meninggalkan ruangan. Sediakan perangkat cadangan dan satu panitia khusus penanganan teknis, sebagaimana sudah direkomendasikan pada laporan pre-test."),
    ("Sesi terputus tercampur dengan hasil ujian sesungguhnya",
     "Lima sesi terputus, empat di antaranya berhenti di bawah satu menit.",
     "Tandai sesi dengan jumlah butir terjawab di bawah 50% sebagai tidak valid sejak awal, dan laporkan terpisah. Mencampurnya menurunkan rata-rata gain dari +5,00 menjadi +2,55 dan menghapus signifikansi statistiknya."),
]
for a, b, c_ in INS:
    putrow(ws, r, [a, b, c_], bold=(1,), h=52)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
    r += 1
r += 1

secrow(ws, r, "C. RANCANGAN PENGUKURAN BERIKUTNYA", 8); r += 1
head(ws, r, ["Aspek", "Ketentuan", "Alasan", "", "", "", "", ""], [26, 52, 92])
r += 1
DS = [
    ("Instrumen", "20 butir identik pada pre dan post, tanpa perubahan redaksi sedikit pun.",
     "Ini syarat mutlak agar selisih skor dapat dibaca sebagai hasil belajar. Tanpa ini, seluruh angka gain memerlukan catatan kaki seperti pada laporan ini."),
    ("Mode", "Keduanya live, batas waktu sama, di ruangan yang sama.",
     "Menyamakan mode menghilangkan penjelasan tandingan terbesar terhadap kenaikan skor."),
    ("Waktu post-test", "Segera setelah sesi praktik terakhir, sebelum peserta pulang.",
     "Mencegah penyusutan peserta 60% seperti yang terjadi kali ini, sekaligus menutup peluang membuka materi."),
    ("Garis dasar", "Rata-rata pre-test peserta yang sama, bukan rata-rata seluruh kelas.",
     "Kelompok berpasangan kali ini rata-rata pre-testnya 8,62 sementara kelas 6,46 — memakai angka kelas akan melebih-lebihkan gain sebesar 2,2 butir."),
    ("Ambang keberhasilan kelompok", "Rata-rata gain berpasangan minimal +5 butir dengan seluruh peserta naik.",
     "Angka ini persis yang tercapai kali ini, sehingga menjadi tolok ukur yang realistis sekaligus sudah terbukti dapat dicapai."),
    ("Ambang keberhasilan individu", "14 dari 20 butir (KKM 70%).",
     "Pada post-test kali ini dicapai 6 dari 10 sesi tuntas. Sasaran berikutnya: 8 dari 10."),
    ("Uji statistik", "Uji-t berpasangan ditambah uji tanda, hanya atas sesi tuntas.",
     "Uji tanda tidak bergantung pada asumsi sebaran normal dan lebih meyakinkan pada n kecil. Keduanya dilaporkan berdampingan."),
    ("Pelaporan", "Sertakan jumlah sesi tuntas, sesi terputus, dan peserta yang hilang antara pre dan post.",
     "Tanpa ketiga angka itu, pembaca tidak dapat menilai seberapa jauh hasil dapat dipercaya."),
]
for a, b, c_ in DS:
    putrow(ws, r, [a, b, c_], bold=(1,), h=44)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
    r += 1
r += 1

secrow(ws, r, "D. KESIMPULAN", 8); r += 1
for t in [
    "Pelatihan berdampak. Pada delapan peserta yang menyelesaikan kedua tes, penguasaan naik rata-rata 5,00 dari 20 butir, dan kenaikan terjadi pada seluruh delapan orang tanpa kecuali (t(7)=3,67; p<0,05; dz=1,30). Konsistensi inilah bukti terkuatnya, bukan besarnya rata-rata.",
    "Besaran dampaknya tidak dapat dipastikan. Instrumen berubah, mode berubah dari live menjadi take-home tiga hari, dan 60% peserta hilang. Ketiganya bekerja ke arah yang sama, yaitu membuat angka gain terlihat lebih besar daripada sebenarnya. Angka +5,00 butir sebaiknya diperlakukan sebagai batas atas.",
    "Materi teknis berhasil, materi prosedural belum. Ukuran kanvas, format ekspor, dan tujuan pelatihan naik tajam. Sebaliknya urutan langkah dan penggunaan fitur komentar justru turun. Pola ini menegaskan kembali kesimpulan laporan pre-test: yang dipraktikkan sendiri akan menempel, yang hanya didemonstrasikan akan luntur.",
    "Satu perbaikan yang paling menentukan untuk pengukuran berikutnya: pakai perangkat soal yang sama persis dan laksanakan post-test di ruangan yang sama sebelum peserta pulang. Dua langkah itu tidak menambah biaya sama sekali, tetapi mengubah angka gain dari perkiraan bersyarat menjadi bukti yang berdiri sendiri.",
]:
    note(ws, r, t, 8, 48); r += 1
