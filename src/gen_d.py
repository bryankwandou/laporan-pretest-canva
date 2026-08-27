# -*- coding: utf-8 -*-
# ===== 11 REKOMENDASI
sec("rekomendasi", "11", "Rekomendasi dan Rencana Tindak Lanjut",
    "Urutan prioritas ditentukan oleh data, bukan oleh urutan materi yang lazim. Setiap rekomendasi dikaitkan langsung dengan temuan yang mendasarinya.")
A("<h3>A. Prioritas materi pelatihan</h3>")
PRIOR = [
    ("Daftar akun Canva gratis dan kenali paket harga", "15 menit", "Q1, Q3",
     "Q1 p=0,16 — hanya 6 dari 14 penjawab tahu langkah pertama. Enam orang mengira harus menunggu akun dibagikan panitia.",
     "Praktik langsung di tempat: seluruh peserta membuka www.canva.com dan mendaftar dengan email masing-masing sebelum materi apa pun dimulai. Panitia berkeliling memastikan semua berhasil masuk.",
     "Seluruh peserta berhasil masuk akun sendiri sebelum menit ke-20"),
    ("Ukuran kanvas dan format ekspor", "20 menit", "Q7, Q14",
     "Ranah terlemah, penguasaan 20,3%. Q14 p=0,19 (15 orang memilih 1080×1080 untuk Story), Q7 p=0,22 (19 orang memilih PPTX atau PDF untuk Instagram).",
     "Bagikan satu lembar rujukan berisi tabel ukuran per platform dan tabel kapan memakai PNG, JPG, PDF, MP4. Lalu praktik ekspor satu desain ke dua format berbeda.",
     "Setiap peserta mengekspor satu desain ukuran 1080×1920 dalam format PNG"),
    ("Antarmuka editor: Panel Kiri, Area Desain, Elemen, Template", "25 menit", "Q4, Q5, Q9, Q18",
     "Q5 p=0,22 — 11 orang mengira Panel Kiri dan Area Desain berfungsi sama. Q4 p=0,24 — 9 orang mengira elemen harus diunduh dulu.",
     "Tur layar terpandu sambil peserta mengikuti di perangkat masing-masing. Tunjuk setiap bagian, minta peserta mengklik bersamaan. Jangan pakai slide, pakai layar Canva sungguhan.",
     "Setiap peserta menambahkan satu ikon dari menu Elemen tanpa dibantu"),
    ("Prinsip desain: hierarki visual, ruang kosong, font, warna", "30 menit", "Q6, Q8, Q11, Q15",
     "Penguasaan 35,1%. Q11 — 11 orang mengira ruang kosong adalah pemborosan. Q8 p=0,30 — konsep warna analog belum dikenal.",
     "Tampilkan pasangan contoh buruk versus baik secara berdampingan, minta peserta menebak mana yang lebih baik dan mengapa. Beri nama pada intuisi yang sudah mereka punya.",
     "Peserta dapat menyebutkan alasan mengapa satu desain lebih mudah dibaca"),
    ("Penyimpanan cloud dan kolaborasi tim", "15 menit", "Q12, Q16",
     "Relatif lebih baik (Q12 p=0,41, Q16 p=0,43) tetapi 10 orang masih mengira desain hanya bisa dibuka dari satu perangkat.",
     "Demonstrasi: buka desain yang sama dari laptop dan ponsel secara bersamaan, lalu undang satu peserta ikut mengedit di depan kelas.",
     "Peserta membuka desainnya sendiri dari perangkat kedua"),
    ("Identitas pelatihan: tujuan, slogan, nilai", "5 menit", "Q13, Q17, Q19",
     "Penguasaan 25,2% — wajar karena belum pernah disampaikan. Q17 tidak dijawab benar oleh satu pun peserta.",
     "Sampaikan sekali di pembukaan dan tampilkan di slide penutup. Ulangi butirnya pada post-test untuk mengukur daya ingat isi pelatihan.",
     "Penguasaan ketiga butir naik di atas 70% pada post-test"),
]
A('<div class="prios">')
for i_, (mat, wkt, bt, bukti, met, uk) in enumerate(PRIOR, 1):
    A('<div class="prio"><div class="pn">%d</div><div class="pb"><h4>%s <span class="pill">%s</span> <span class="pill light">%s</span></h4>'
      '<p class="pev"><span>Bukti</span>%s</p><p class="pme"><span>Metode</span>%s</p><p class="puk"><span>Ukuran keberhasilan</span>%s</p></div></div>'
      % (i_, mat, wkt, bt, bukti, met, uk))
A("</div>")

A("<h3>B. Perbaikan pelaksanaan kuis</h3>")
TEK = [("Peserta bergabung setelah kuis dimulai",
        "Q1 kehilangan 23 dari 37 sel (62%), Q2 12 sel, Q3 17 sel.",
        "Buka ruang kuis 10 menit lebih awal. Tampilkan daftar peserta yang sudah masuk di layar dan baru mulai butir pertama setelah jumlahnya stabil. Untuk post-test, gunakan mode mandiri agar tidak ada yang tertinggal."),
       ("Empat sesi tidak menghasilkan satu jawaban pun",
        "Waktu total di bawah 30 detik pada keempatnya.",
        "Sediakan satu panitia khusus penanganan perangkat dan 2–3 perangkat cadangan. Kirim tautan kuis lewat grup pesan 15 menit sebelum mulai, bukan hanya kode PIN di layar."),
       ("Nama peserta terduplikasi dan sulit dicocokkan",
        "Sri Suyani muncul 3 kali, Aqifah 2 kali, farida johannes 2 kali. Ada pula “Yofita” dan “Yovita” yang mungkin orang yang sama.",
        "Wajibkan format nama baku sesuai daftar hadir. Sebarkan tautan personal per peserta bila memungkinkan, sehingga satu orang menghasilkan tepat satu sesi."),
       ("Butir Q17 tidak mengukur apa pun",
        "Daya beda 0,00 dan r-pbis −0,01.",
        "Keluarkan Q17 dari perhitungan skor pre-test. Pertahankan butirnya hanya untuk post-test sebagai pengukur daya ingat materi."),
       ("Q20 punya pengecoh yang tidak berfungsi",
        "Tiga opsi salah hanya dipilih 4 kali dari 26 penjawab.",
        "Tulis ulang ketiga opsi salah agar sama-sama masuk akal secara akademis, misalnya dengan menyebut jabatan akademik lain yang serupa."),
       ("Durasi terlalu sempit untuk butir bacaan panjang",
        "Rata-rata 17–18 detik per butir, sementara beberapa butir memuat empat pernyataan yang harus dibandingkan.",
        "Perpanjang batas waktu menjadi 45–60 detik untuk butir bertipe pernyataan majemuk, atau perpendek redaksi opsinya.")]
A('<table><thead><tr><th>Masalah yang terbukti</th><th>Bukti angka</th><th>Tindakan perbaikan</th></tr></thead><tbody>')
for m_, b_, t_ in TEK:
    A('<tr><td class="b">%s</td><td class="s">%s</td><td>%s</td></tr>' % (m_, b_, t_))
A("</tbody></table>")

A("<h3>C. Rancangan pengukuran dampak pelatihan</h3>")
DES = [("Instrumen post-test", "Gunakan 19 butir yang sama (Q17 dikeluarkan) tanpa mengubah redaksi.",
        "Perbandingan pre dan post hanya sah bila instrumennya identik. Q17 dikeluarkan karena terbukti tidak mengukur apa pun."),
       ("Garis dasar pembanding", "36,2% (33 sesi aktif), bukan 32,3% (37 sesi).",
        "Empat sesi nol adalah kegagalan teknis, bukan hasil ujian. Memakainya sebagai pembanding akan melebih-lebihkan keberhasilan pelatihan."),
       ("Target kenaikan minimum", "Akurasi kelas 70% pada post-test, naik sekitar 34 poin persen.",
        "Materi yang diuji seluruhnya dasar dan langsung dipraktikkan. Kenaikan di bawah 25 poin persen menandakan penyampaian materi perlu dievaluasi."),
       ("Target per ranah", "Teknis Output &amp; Ukuran minimal 75%; Akses &amp; Model Bisnis minimal 90%.",
        "Kedua ranah ini murni prosedural dan dipraktikkan langsung, sehingga wajar menuntut penguasaan hampir penuh."),
       ("Uji statistik", "Uji-t berpasangan atau uji McNemar per butir, dengan peserta yang sama pada kedua tes.",
        "Hanya peserta yang mengikuti kedua tes yang boleh dibandingkan. Dengan n sekitar 33, uji berpasangan memberi daya uji yang memadai."),
       ("Ambang keberhasilan individu", "Minimal 14 dari 19 butir benar (74%).",
        "Setara ketuntasan 70%. Pada pre-test hanya 1 dari 37 sesi mencapainya; angka ini menjadi pembanding yang jelas."),
       ("Waktu pelaksanaan", "Segera setelah sesi praktik terakhir, di ruangan yang sama.",
        "Menunda post-test memasukkan variabel lupa dan belajar mandiri, sehingga yang terukur bukan lagi dampak pelatihan.")]
A('<table><thead><tr><th>Aspek</th><th>Ketentuan</th><th>Alasan</th></tr></thead><tbody>')
for a_, k_, al in DES:
    A('<tr><td class="b">%s</td><td>%s</td><td class="s">%s</td></tr>' % (a_, k_, al))
A("</tbody></table>")

A("<h3>D. Kesimpulan</h3><ul class=\"ul\">")
for t in ["Pre-test ini berhasil menjalankan fungsinya. Reliabilitas %.3f dan rata-rata daya beda %.3f memenuhi standar untuk tes 20 butir; sembilan belas dari dua puluh butir bekerja sebagaimana mestinya." % (kr20, st.mean(i["D"] for i in items)),
          "Kemampuan awal peserta berada pada tingkat sangat rendah dan merata. Akurasi %.1f%% berbanding 25%% peluang tebakan acak menunjukkan pengetahuan yang dimiliki bersifat sepotong-sepotong dan belum terstruktur." % (acc_all * 100),
          "Kelemahan terbesar bersifat prosedural, bukan konseptual. Peserta mampu menalar tentang prinsip desain tetapi tidak tahu langkah konkret yang harus diambil. Implikasinya tegas: porsi praktik harus melebihi porsi ceramah.",
          "Sebagian besar kesenjangan skor antarpeserta berasal dari jumlah butir yang sempat dijawab, bukan dari ketepatan menjawab. Memperbaiki pelaksanaan teknis kuis akan memperbaiki kualitas data lebih besar daripada memperbaiki soalnya.",
          "<strong>Rekomendasi utama:</strong> alokasikan 15 menit pertama untuk memastikan setiap peserta berhasil mendaftar dan masuk akun Canva gratis miliknya sendiri, lalu 20 menit berikutnya untuk ukuran kanvas dan format ekspor. Dua hal ini adalah penghalang terbesar sekaligus paling cepat dirobohkan, dan keduanya prasyarat bagi seluruh materi berikutnya."]:
    A("<li>%s</li>" % t)
A("</ul>")
endsec()

# ===== 12 METODOLOGI
sec("metode", "12", "Metodologi, Rumus dan Keterbatasan",
    "Seluruh perhitungan pada laporan ini dapat direproduksi dari dua berkas sumber yang disebut di bawah.")
A("<h3>Sumber data dan validasi silang</h3><ul class=\"ul\">")
for t in ["<strong>Ekspor resmi Wayground (XLSX)</strong> — sheet Overview (naskah soal, jawaban tiap peserta), Participant Data, Time Data, Quiz Details. Sumber naskah soal, teks jawaban, waktu per butir dan metadata sesi.",
          "<strong>Snapshot HTML laporan admin</strong> — memuat matriks respons berwarna 37 baris × 20 kolom. Dipakai sebagai penentu status benar/salah/kosong karena memisahkan “salah” dari “tidak dijawab”, sedangkan ekspor XLSX menggabungkan keduanya di tingkat peserta.",
          "Jumlah benar dan salah per butir dari kedua sumber dicocokkan satu per satu. Hasilnya identik pada seluruh 20 butir (%d benar, %d salah)." % (tot_c, tot_x),
          "Kolom jawaban pada sheet Overview memuat entri “hantu”: teks jawaban tetap tercantum untuk sel yang sebenarnya tidak dijawab. Seluruh entri semacam ini disaring memakai matriks respons sebagai penyaring, lalu jumlah pemilih tiap opsi dicocokkan kembali — kecocokan tercapai pada 20 dari 20 butir tanpa selisih.",
          "Kunci jawaban tidak tersedia dalam kedua berkas. Kunci direkonstruksi dari opsi yang dipilih peserta yang ditandai benar. Pada 20 dari 20 butir, semua peserta yang benar memilih opsi yang sama persis — kunci tidak ambigu.",
          "Catatan bawaan Wayground: pada sheet Participant Data, butir yang kehabisan waktu dihitung sebagai “Incorrect”, sedangkan pada sheet Overview tidak. Laporan ini konsisten memakai tiga kategori terpisah."]:
    A("<li>%s</li>" % t)
A("</ul>")
A("<h3>Rumus yang dipakai</h3><table><thead><tr><th>Ukuran</th><th>Rumus</th><th>Penerapan pada data ini</th></tr></thead><tbody>")
for a_, f_, c_ in [("Tingkat kesukaran (p)", "p = B / N", "B = jumlah benar; N = 37 seluruh sesi. Sel kosong dihitung tidak benar, sesuai cara Wayground menghitung akurasi."),
                   ("Daya beda (D)", "D = (BA / nA) − (BB / nB)", "Kelompok atas dan bawah masing-masing 27% dari 37, dibulatkan menjadi 10 sesi."),
                   ("Korelasi point-biserial", "r = ((M₁ − M₀) / SDt) × √(p × q)", "M₁ rata-rata skor total peserta yang benar pada butir; M₀ yang salah; q = 1 − p."),
                   ("Reliabilitas KR-20", "KR20 = (k / (k−1)) × (1 − Σpq / σ²)", "k = 20 butir; σ² = %.2f. Hasil %.3f." % (S["var"], kr20)),
                   ("Kesalahan baku ukur", "SEM = SD × √(1 − r)", "SD = %.2f; r = %.3f. Hasil ±%.2f butir." % (sd, kr20, sem)),
                   ("z-skor dan T-skor", "z = (X − μ) / σ  ·  T = 50 + 10z", "μ = %.2f dan σ = %.2f dihitung atas 37 sesi sebagai populasi, bukan sampel." % (mean, sd)),
                   ("Peringkat persentil", "PR = ((cf + 0,5f) / N) × 100", "cf = jumlah peserta berskor lebih rendah; f = jumlah peserta berskor sama."),
                   ("Pengecoh efektif", "Opsi salah dipilih ≥ 5% penjawab butir", "Penjawab butir = benar + salah, tidak termasuk sel kosong.")]:
    A('<tr><td class="b">%s</td><td class="mono">%s</td><td class="s">%s</td></tr>' % (a_, f_, c_))
A("</tbody></table>")
A("<h3>Ambang tafsir</h3><table><thead><tr><th>Ukuran</th><th>Ambang</th><th>Kategori</th></tr></thead><tbody>")
for a_, b_, c_ in [("Tingkat kesukaran p", "&lt;0,30 / 0,30–0,70 / &gt;0,70", "Sukar / Sedang / Mudah (Arikunto)"),
                   ("Daya beda D", "≥0,40 / 0,30–0,39 / 0,20–0,29 / &lt;0,20", "Sangat baik / Baik / Cukup, perlu revisi / Buruk, ditolak (Ebel &amp; Frisbie)"),
                   ("Korelasi butir-total", "r ≥ 0,30 memadai; r &lt; 0,20 bermasalah", "Nilai r negatif menandakan kunci keliru atau redaksi menyesatkan"),
                   ("Reliabilitas KR-20", "≥0,90 / 0,80–0,89 / 0,70–0,79 / &lt;0,70", "Sangat tinggi / Tinggi / Cukup / Rendah"),
                   ("Nilai huruf", "85–100 / 70–84 / 55–69 / 40–54 / 0–39", "A / B / C / D / E"),
                   ("Ketuntasan", "70% atau 14 dari 20 butir", "Ambang yang lazim dipakai pada pelatihan sejenis")]:
    A('<tr><td class="b">%s</td><td class="mono">%s</td><td class="s">%s</td></tr>' % (a_, b_, c_))
A("</tbody></table>")
A("<h3>Keterbatasan yang harus disadari pembaca</h3><ul class=\"ul warnul\">")
for t in ["Jumlah 37 sesi tergolong kecil untuk analisis butir. Kelompok atas dan bawah masing-masing hanya 10 orang, sehingga satu jawaban berbeda menggeser daya beda sebesar 0,10. Perlakukan nilai D sebagai indikasi arah, bukan angka pasti.",
          "Q1 hanya dijawab 14 peserta dan Q3 oleh 20 peserta. Statistik pada kedua butir ini berdiri di atas basis yang tipis dan paling rapuh di antara seluruh butir.",
          "Kunci jawaban direkonstruksi, bukan diambil dari dokumen resmi. Rekonstruksinya konsisten sempurna, namun bila panitia memiliki dokumen kunci asli sebaiknya dicocokkan sekali lagi — terutama Q6 yang menanyakan penerapan yang BERTENTANGAN dengan prinsip hierarki visual, sehingga kuncinya justru berupa pernyataan yang keliru secara desain.",
          "Laporan ini tidak memuat pemeriksaan kecurangan; sheet Anti-cheating tidak tersedia dalam berkas yang diberikan.",
          "Skor Wayground memberi bonus kecepatan, sehingga peringkat poin tidak sama dengan peringkat kemampuan. Seluruh analisis di sini memakai jumlah jawaban benar, bukan poin.",
          "Hasil pre-test hanya menggambarkan pengetahuan deklaratif tentang Canva. Kemampuan praktik sesungguhnya — apakah peserta bisa membuat desain yang layak — tidak terukur oleh tes pilihan ganda dan memerlukan penilaian karya."]:
    A("<li>%s</li>" % t)
A("</ul>")
endsec()

# ===== 13 UNDUH
sec("unduh", "13", "Unduh Berkas",
    "Workbook Excel memuat 15 lembar kerja dan 16 grafik native, termasuk naskah soal lengkap, kunci jawaban hasil rekonstruksi, distribusi pilihan per opsi dan data mentah jawaban setiap peserta pada setiap butir.")
A('<a class="dl" href="LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx" download>'
  '<span class="dlx">XLSX</span><span class="dlt"><strong>Laporan Evaluasi Pre-test Canva — 25 Agustus 2026</strong>'
  '<em>15 lembar kerja · 16 grafik · data mentah lengkap</em></span></a>')
endsec()
