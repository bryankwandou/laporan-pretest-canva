# -*- coding: utf-8 -*-
# ===== 09 REKOMENDASI
sec("rekomendasi", "09", "Rekomendasi",
    "Dipisahkan menjadi tiga: materi yang masih perlu ditutup, perbaikan instrumen, dan perbaikan rancangan pengukuran berikutnya.")
A("<h3>A. Materi yang masih perlu ditutup</h3>")
PR = [
    ("Cara memberi masukan pada desain rekan (fitur Komentar)",
     "Q17 p=0,13 — hanya 2 dari 15 benar, turun dari 0,43 pada pre-test. Delapan peserta memilih “unduh lalu kirim via email”.",
     "Sesi praktik berpasangan 10 menit: setiap peserta membuka desain rekannya, menambahkan satu komentar pada elemen tertentu, lalu rekannya membalas. Jangan didemonstrasikan di depan — harus dikerjakan sendiri oleh setiap orang."),
    ("Brand Kit — konsistensi warna, font dan logo",
     "Q3 p=0,27, butir tersukar kedua. Tujuh peserta memilih “Warna Elemen Manual”, dua memilih “Gradien Warna”.",
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
     "Bila nilai ini dianggap penting untuk diingat, tampilkan di slide pembuka dan penutup serta cetak pada lembar kerja. Bila tidak, keluarkan dari instrumen agar tidak mengaburkan pengukuran kemampuan teknis."),
]
A('<div class="prios">')
for i, (m, b, t) in enumerate(PR, 1):
    A('<div class="prio"><div class="pn">%d</div><div class="pb"><h4>%s</h4><p class="pev"><span>Bukti</span>%s</p><p class="pme"><span>Tindakan</span>%s</p></div></div>' % (i, m, b, t))
A("</div>")

A("<h3>B. Perbaikan instrumen</h3>")
A('<table><thead><tr><th>Masalah</th><th>Bukti</th><th>Perbaikan</th></tr></thead><tbody>')
for a_, b_, c_ in [
    ("Instrumen post-test berbeda dari pre-test", "Hanya 14 dari 20 konstruk beririsan; hanya dua butir praktis identik.",
     "Gunakan perangkat butir yang identik pada pre dan post. Bila ingin menambah materi baru, tambahkan sebagai butir terpisah di luar 20 butir inti, dan hitung gain hanya dari 20 butir inti."),
    ("42% pengecoh tidak berfungsi", "25 dari 60 opsi salah tidak dipilih siapa pun; tiga butir kehilangan seluruh pengecohnya.",
     "Tulis ulang pengecoh memakai miskonsepsi nyata yang tercatat pada pre-test. Setiap opsi salah harus merupakan kekeliruan yang benar-benar mungkin dipercaya."),
    ("Q8 mengukur pengetahuan di luar materi pelatihan", "Makna teologis warna ungu, p=0,73, tertinggi di seluruh post-test.",
     "Keluarkan dari perhitungan gain kemampuan Canva. Bila dipertahankan, laporkan terpisah sebagai butir konteks, bukan sebagai indikator keberhasilan pelatihan."),
    ("Mode Homework membuka pintu pengerjaan dengan membuka materi", "Rentang tiga hari tanpa pengawasan; rata-rata pengerjaan 10 menit; korelasi waktu dengan skor r=0,12.",
     "Laksanakan post-test langsung di akhir sesi, dalam ruangan yang sama, dengan batas waktu yang sama seperti pre-test. Ini satu perubahan yang paling banyak memulihkan daya tafsir angka gain."),
    ("Kehilangan 60% peserta antara pre dan post", "37 sesi menjadi 15, dan hanya 8 pasangan tuntas.",
     "Jalankan post-test sebelum peserta meninggalkan ruangan. Sediakan perangkat cadangan dan satu panitia khusus penanganan teknis."),
    ("Sesi terputus tercampur dengan hasil ujian", "Lima sesi terputus, empat berhenti di bawah satu menit.",
     "Tandai sesi dengan butir terjawab di bawah 50% sebagai tidak valid sejak awal dan laporkan terpisah. Mencampurnya menurunkan rata-rata gain dari +5,00 menjadi +2,55 dan menghapus signifikansi statistiknya."),
]:
    A('<tr><td class="b">%s</td><td class="s">%s</td><td>%s</td></tr>' % (a_, b_, c_))
A("</tbody></table>")

A("<h3>C. Rancangan pengukuran berikutnya</h3>")
A('<table><thead><tr><th>Aspek</th><th>Ketentuan</th><th>Alasan</th></tr></thead><tbody>')
for a_, b_, c_ in [
    ("Instrumen", "20 butir identik pada pre dan post, tanpa perubahan redaksi sedikit pun.",
     "Syarat mutlak agar selisih skor dapat dibaca sebagai hasil belajar. Tanpa ini, seluruh angka gain memerlukan catatan kaki seperti pada laporan ini."),
    ("Mode", "Keduanya live, batas waktu sama, di ruangan yang sama.",
     "Menyamakan mode menghilangkan penjelasan tandingan terbesar terhadap kenaikan skor."),
    ("Waktu post-test", "Segera setelah sesi praktik terakhir, sebelum peserta pulang.",
     "Mencegah penyusutan peserta 60% seperti yang terjadi kali ini, sekaligus menutup peluang membuka materi."),
    ("Garis dasar", "Rata-rata pre-test peserta yang sama, bukan rata-rata seluruh kelas.",
     "Kelompok berpasangan kali ini rata-rata pre-testnya 8,62 sementara kelas 6,46 — memakai angka kelas melebih-lebihkan gain sebesar 2,2 butir."),
    ("Ambang keberhasilan kelompok", "Rata-rata gain berpasangan minimal +5 butir dengan seluruh peserta naik.",
     "Angka ini persis yang tercapai kali ini, sehingga menjadi tolok ukur yang realistis sekaligus sudah terbukti dapat dicapai."),
    ("Ambang keberhasilan individu", "14 dari 20 butir (ketuntasan 70%).",
     "Pada post-test kali ini dicapai 6 dari 10 sesi tuntas. Sasaran berikutnya: 8 dari 10."),
    ("Uji statistik", "Uji-t berpasangan ditambah uji tanda, hanya atas sesi tuntas.",
     "Uji tanda tidak bergantung pada asumsi sebaran normal dan lebih meyakinkan pada n kecil. Keduanya dilaporkan berdampingan."),
    ("Pelaporan", "Sertakan jumlah sesi tuntas, sesi terputus, dan peserta yang hilang antara pre dan post.",
     "Tanpa ketiga angka itu, pembaca tidak dapat menilai seberapa jauh hasil dapat dipercaya."),
]:
    A('<tr><td class="b">%s</td><td>%s</td><td class="s">%s</td></tr>' % (a_, b_, c_))
A("</tbody></table>")

A("<h3>D. Kesimpulan</h3><ul class=\"ul\">")
for t in [
    "<strong>Pelatihan berdampak.</strong> Pada delapan peserta yang menyelesaikan kedua tes, penguasaan naik rata-rata 5,00 dari 20 butir, dan kenaikan terjadi pada seluruh delapan orang tanpa kecuali (t(7)=3,67; p&lt;0,05; dz=1,30). Konsistensi inilah bukti terkuatnya, bukan besarnya rata-rata.",
    "<strong>Besaran dampaknya tidak dapat dipastikan.</strong> Instrumen berubah, mode berubah dari live menjadi take-home tiga hari, dan 60% peserta hilang. Ketiganya bekerja ke arah yang sama, yaitu membuat angka gain terlihat lebih besar daripada sebenarnya. Angka +5,00 butir sebaiknya diperlakukan sebagai batas atas.",
    "<strong>Materi teknis berhasil, materi prosedural belum.</strong> Ukuran kanvas, format ekspor dan tujuan pelatihan naik tajam. Sebaliknya urutan langkah dan penggunaan fitur komentar justru turun. Pola ini menegaskan kembali kesimpulan laporan pre-test: yang dipraktikkan sendiri akan menempel, yang hanya didemonstrasikan akan luntur.",
    "<strong>Satu perbaikan yang paling menentukan:</strong> pakai perangkat soal yang sama persis dan laksanakan post-test di ruangan yang sama sebelum peserta pulang. Dua langkah itu tidak menambah biaya sama sekali, tetapi mengubah angka gain dari perkiraan bersyarat menjadi bukti yang berdiri sendiri.",
]:
    A("<li>%s</li>" % t)
A("</ul>")
endsec()

# ===== 10 METODOLOGI
sec("metode", "10", "Metodologi dan Keterbatasan",
    "Seluruh angka post-test dapat direproduksi dari tiga berkas sumber di bawah. Skrip pengolahannya tersedia di repositori.")
A("<h3>Sumber data</h3><ul class=\"ul\">")
for t in ["<strong>Ekspor resmi Wayground (XLSX)</strong> — Overview (naskah, jawaban tiap peserta), Participant Data, Time Data, Quiz Details. Sumber utama seluruh data respons, waktu dan metadata sesi.",
          "<strong>Naskah cetak resmi (PDF)</strong> — 20 butir beserta keempat opsi setiap butir, dicetak tanpa tanda kunci. Dipakai untuk memverifikasi kunci hasil rekonstruksi dan menemukan opsi yang tidak pernah dipilih.",
          "<strong>Dataset pre-test</strong> — 20 butir, 37 peserta, matriks respons dan statistik butir dari laporan sebelumnya. Basis pembanding seluruh analisis gain."]:
    A("<li>%s</li>" % t)
A("</ul>")
A("<h3>Validasi lima lapis</h3><ol class=\"ol\">")
for t in ["<strong>Jumlah sel kosong.</strong> Untuk setiap butir, jumlah sel jawaban kosong pada sheet Overview dicocokkan dengan kolom Unattempted. Cocok pada 20 dari 20 butir. Berbeda dengan ekspor pre-test, ekspor post-test tidak memuat entri “hantu”, sehingga tidak diperlukan penyaringan.",
          "<strong>Rekonstruksi kunci.</strong> Kunci diambil sebagai opsi yang jumlah pemilihnya sama persis dengan jumlah Correct pada butir tersebut. Cara ini langsung menyelesaikan 18 butir; Q11 dan Q17 menyisakan dua calon masing-masing.",
          "<strong>Penyelesaian lewat kendala.</strong> Keempat kombinasi calon kunci Q11 × Q17 diuji terhadap syarat bahwa jumlah benar setiap peserta hasil hitungan harus sama persis dengan kolom Correct pada Participant Data untuk seluruh 16 sesi. Hanya satu kombinasi memenuhi syarat.",
          "<strong>Verifikasi terhadap naskah PDF.</strong> Seluruh 20 kunci dicocokkan ke daftar opsi pada naskah cetak resmi. Kecocokan sempurna pada 20 dari 20 butir, termasuk kedua kunci yang tadinya ambigu — dan keduanya memang benar secara isi. Kunci pada laporan ini karena itu dapat dianggap pasti, bukan perkiraan.",
          "<strong>Konsistensi setelah Vincent dikeluarkan.</strong> Seluruh statistik butir dihitung ulang dari matriks respons, bukan diambil dari kolom agregat ekspor. Jumlah benar hasil hitung ulang dicocokkan kembali dengan Participant Data untuk 15 sesi tersisa; tidak ada selisih."]:
    A("<li>%s</li>" % t)
A("</ol>")
A("<h3>Perlakuan terhadap sesi QA tester</h3>")
V = C2["vincent"]
A('<table><thead><tr><th>Ukuran post-test</th><th class="n">Termasuk Vincent</th><th class="n">Dikeluarkan</th><th class="n">Selisih</th></tr></thead><tbody>')
n_in = 16; c_in = sum(sc_post.values()) + V["correct"]
for a_, b_, c_, d_ in [("Jumlah sesi", 16, 15, "−1"),
                       ("Total jawaban benar", c_in, sum(sc_post.values()), "−%d" % V["correct"]),
                       ("Rata-rata benar", "%.2f" % (c_in / n_in), "%.2f" % st.mean(sc_post.values()),
                        "%+.2f" % (st.mean(sc_post.values()) - c_in / n_in)),
                       ("Akurasi seluruh sesi", "%.2f%%" % (c_in / (n_in * 20) * 100),
                        "%.2f%%" % (sum(sc_post.values()) / 300 * 100),
                        "%+.2f pp" % (sum(sc_post.values()) / 300 * 100 - c_in / (n_in * 20) * 100))]:
    A('<tr><td class="b">%s</td><td class="n">%s</td><td class="n b">%s</td><td class="n">%s</td></tr>' % (a_, b_, c_, d_))
A("</tbody></table>")
note("Vincent tercatat %d benar, %d salah, 0 kosong, dengan waktu total hanya %d menit %d detik untuk 20 butir; sheet Time Data memuat sejumlah entri 00:00:01 pada sesinya — pola khas penelusuran perangkat lunak, bukan orang yang membaca soal. Ia juga tidak muncul pada daftar peserta pre-test. Dampak pengeluarannya kecil terhadap angka agregat, tetapi pengeluaran tetap dilakukan karena sesi uji perangkat lunak bukan hasil ujian peserta dan tidak boleh ikut membentuk statistik butir maupun penetapan kelompok atas dan bawah." % (V["correct"], 20 - V["correct"], V["time_s"] // 60, V["time_s"] % 60))
A("<h3>Rumus</h3><table><thead><tr><th>Ukuran</th><th>Rumus</th><th>Penerapan</th></tr></thead><tbody>")
for a_, b_, c_ in [("Tingkat kesukaran (p)", "p = B / N", "N = 15 sesi setelah Vincent dikeluarkan. Sel kosong dihitung tidak benar."),
                   ("Daya beda (D)", "D = (BA / nA) − (BB / nB)", "Kelompok atas dan bawah masing-masing 27% dari 15, dibulatkan menjadi 4 sesi."),
                   ("Point-biserial", "r = ((M₁ − M₀) / SDt) × √(p × q)", "M₁ rata-rata skor total peserta yang benar; M₀ yang salah; q = 1 − p."),
                   ("Reliabilitas KR-20", "KR20 = (k/(k−1)) × (1 − Σpq / σ²)", "Dihitung dua kali: atas 15 sesi (0,935) dan atas 10 sesi tuntas (0,721). Yang dilaporkan adalah angka kedua."),
                   ("Kesalahan baku ukur", "SEM = SD × √(1 − r)", "SD sesi tuntas 3,33; r = 0,721. Hasil ±1,76 butir."),
                   ("Gain ternormalisasi (Hake)", "g = (post − pre) / (maks − pre)", "Berapa bagian dari jarak menuju skor sempurna yang tertutup. Hasil 0,440."),
                   ("Uji-t berpasangan", "t = ḡ / (SDg / √n)", "n = 8, derajat bebas 7. t = 3,67 melawan kritis 2,365 pada α=0,05 dua sisi."),
                   ("Ukuran efek Cohen dz", "dz = ḡ / SDg", "Hasil 1,30 (0,20 kecil · 0,50 sedang · 0,80 besar)."),
                   ("Uji tanda", "peluang binomial k naik dari n, p = 0,5", "8 dari 8 naik memberi p = 0,0039 satu sisi.")]:
    A('<tr><td class="b">%s</td><td class="mono">%s</td><td class="s">%s</td></tr>' % (a_, b_, c_))
A("</tbody></table>")
A("<h3>Keterbatasan — baca sebelum mengutip angka mana pun</h3><ol class=\"ol warnul\">")
for t in ["<strong>Instrumen berubah.</strong> Post-test bukan pengulangan pre-test. Selisih skor mentah memuat campuran antara hasil belajar dan perbedaan tingkat kesukaran perangkat soal, dan keduanya tidak dapat dipisahkan dari data yang tersedia.",
          "<strong>Mode berubah.</strong> Pre-test live berbatas waktu, post-test Homework tiga hari tanpa pengawasan dengan materi tersedia. Ini penjelasan tandingan terkuat terhadap kenaikan skor.",
          "<strong>Penyusutan peserta 60%.</strong> Yang bertahan rata-rata pre-testnya 8,62 berbanding 6,46 untuk seluruh kelas. Bias seleksi ini bekerja ke arah melebih-lebihkan keberhasilan.",
          "<strong>n = 8 pada uji berpasangan.</strong> Uji kepekaan dilakukan dengan mengeluarkan gain +14: rata-rata turun menjadi 3,71 butir tetapi simpangan bakunya menyusut dari 3,85 menjadi 1,38, sehingga t(6) justru naik menjadi 7,12. Kesimpulan bahwa terjadi kenaikan tidak bergantung pada satu pengamatan ekstrem; yang bergantung padanya hanyalah besaran rata-ratanya.",
          "<strong>Daya beda post-test menggelembung.</strong> Sepuluh butir mencapai D = 1,00 karena kelompok bawah sebagian besar terdiri atas sesi terputus. Nilai D post-test tidak sebanding dengan nilai D pre-test.",
          "<strong>Tidak ada kelompok pembanding.</strong> Tanpa kelompok yang tidak mengikuti pelatihan, sebagian kenaikan dapat berasal dari efek mengerjakan tes serupa untuk kedua kalinya, bukan dari pelatihan itu sendiri.",
          "<strong>Tidak ada pemeriksaan kecurangan.</strong> Dalam mode take-home tanpa pengawasan pemeriksaan semacam itu justru paling dibutuhkan, tetapi datanya tidak tersedia dalam berkas yang diberikan.",
          "<strong>Yang diukur tetap pengetahuan deklaratif.</strong> Apakah peserta benar-benar mampu membuat desain yang layak tidak terukur oleh tes pilihan ganda dan memerlukan penilaian karya."]:
    A("<li>%s</li>" % t)
A("</ol>")
endsec()

# ===== 11 UNDUH
sec("unduh", "11", "Unduh Berkas",
    "Kedua workbook memuat grafik native Excel, tabel data mentah, dan sheet siap olah untuk analisis lanjutan di SPSS, R atau jamovi.")
A('<a class="dl" href="LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx" download><span class="dlx">XLSX</span><span class="dlt"><strong>Laporan Post-test dan Perbandingan</strong><em>12 lembar kerja · 18 grafik · data berpasangan siap olah</em></span></a>')
A('<a class="dl" href="LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx" download><span class="dlx">XLSX</span><span class="dlt"><strong>Laporan Evaluasi Pre-test</strong><em>15 lembar kerja · 16 grafik · data mentah lengkap</em></span></a>')
endsec()
