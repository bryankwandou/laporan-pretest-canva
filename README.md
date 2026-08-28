# Evaluasi Pelatihan Canva — Pre-test dan Post-test

Analisis statistik pelatihan Canva (Wanita Katolik RI, 25 Agustus 2026) yang diselenggarakan melalui **Wayground / Quizizz**. Mencakup analisis butir kedua instrumen, reliabilitas, segmentasi peserta, pemetaan miskonsepsi, analisis berpasangan pre–post, dan rekomendasi rancangan pengukuran.

**Laporan web:** https://laporan-pretest-canva.vercel.app
· [Pre-test](https://laporan-pretest-canva.vercel.app/) · [Post-test & Perbandingan](https://laporan-pretest-canva.vercel.app/post-test.html)

## Angka pokok

| Ukuran | Pre-test | Post-test |
|---|---|---|
| Sesi terekam | 37 | 15 (Vincent, QA tester, dikeluarkan) |
| Sesi tuntas | 34 aktif | 10 tuntas 20/20 |
| Mode pelaksanaan | Live, 14 menit | Homework, 3 hari |
| Akurasi seluruh sesi | 32,3% | 49,7% |
| Rata-rata benar | 6,46 / 20 | 9,93 / 20 |
| Reliabilitas KR-20 | 0,751 | 0,721 (atas 10 sesi tuntas) |
| Kesalahan baku ukur | ±1,87 butir | ±1,76 butir |

### Hasil utama — analisis berpasangan

Delapan peserta menyelesaikan kedua tes. **Seluruh delapan naik, tanpa kecuali.**

| Ukuran | Nilai |
|---|---|
| Rata-rata pre → post | 8,62 → 13,62 butir |
| Rata-rata gain | **+5,00 butir** |
| Uji-t berpasangan | t(7) = 3,67 (kritis 2,365 pada α=0,05) — **signifikan** |
| Uji tanda | 8 dari 8 naik, p = 0,0039 |
| Ukuran efek Cohen dz | 1,30 — **besar** |
| Gain ternormalisasi ⟨g⟩ (Hake) | 0,440 — sedang |
| Uji kepekaan tanpa nilai ekstrem | t(6) = 7,12; dz = 2,69 — kesimpulan bertahan |

## Batas tafsir — wajib dibaca sebelum mengutip

Tiga hal berubah bersamaan antara kedua pengukuran, dan ketiganya bekerja ke arah membuat kenaikan terlihat lebih besar daripada sebenarnya:

1. **Instrumen berubah.** Hanya 14 dari 20 konstruk beririsan; hanya dua butir praktis identik kata per kata. Enam butir post-test menguji materi yang tidak ada di pre-test, enam butir pre-test tidak diulang.
2. **Mode berubah.** Pre-test live berbatas waktu; post-test Homework tiga hari tanpa pengawasan dengan materi pelatihan tersedia.
3. **Peserta menyusut 60%.** Yang bertahan rata-rata pre-test-nya 8,62 berbanding 6,46 untuk seluruh kelas — bias seleksi.

Karena itu angka **+5,00 butir diperlakukan sebagai batas atas** dampak pelatihan, bukan perkiraan tak bias. Selisih akurasi kelas (32,3% → 49,7%) **tidak** dapat dibaca sebagai hasil belajar.

## Isi repositori

| Berkas | Keterangan |
|---|---|
| `index.html` | Laporan web pre-test, 13 bagian, mandiri |
| `post-test.html` | Laporan web post-test dan perbandingan, 11 bagian |
| `LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx` | 15 lembar kerja, 16 grafik native |
| `LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx` | 12 lembar kerja, 18 grafik native, termasuk sheet data berpasangan siap olah |
| `src/` | Pipeline pre-test: ekstraksi, pembersihan, statistik, pembangkit laporan |
| `src/post/` | Pipeline post-test dan perbandingan |

### Pipeline post-test (`src/post/`)

| Berkas | Fungsi |
|---|---|
| `post_extract.py` | Ekstraksi ekspor XLSX Wayground, rekonstruksi kunci dari pola respons |
| `post_build.py` | Matriks respons, pengeluaran sesi QA, statistik butir, pemetaan silang ke pre-test |
| `cmp_calc.py` | Perbandingan umum, analisis berpasangan, pemetaan konstruk |
| `cmp_calc2.py` | Analisis sesi tuntas, uji-t, uji tanda, uji kepekaan, dampak pengeluaran QA |
| `pdf_opts.py` | Parsing naskah cetak PDF, verifikasi kunci, deteksi pengecoh mati |
| `pw_*.py`, `run_pw.py` | Pembangkit workbook Excel post-test |
| `gp_*.py`, `run_gp.py` | Pembangkit halaman web post-test |
| `post_core.json`, `cmp.json`, `cmp2.json`, `pdf_opts.json` | Dataset dan hasil hitungan |
| `cmp_out*.txt` | Keluaran teks lengkap seluruh perhitungan, untuk penelusuran |

## Reproduksi

```bash
cd src/post && python post_extract.py && python post_build.py && python cmp_calc.py && python cmp_calc2.py && python pdf_opts.py && python run_pw.py && python run_gp.py
```

Membutuhkan Python 3, `openpyxl`, dan `pypdf`.

## Sumber data dan validasi

**Pre-test** memakai dua sumber: ekspor resmi Wayground (XLSX) dan snapshot HTML laporan admin. Jumlah benar dan salah per butir dari kedua sumber dicocokkan satu per satu — identik pada 20 dari 20 butir (239 benar, 302 salah). Kolom jawaban pada ekspor XLSX memuat entri "hantu" (teks jawaban tetap tercantum untuk sel yang sebenarnya tidak dijawab); seluruhnya disaring memakai matriks respons HTML.

**Post-test** memakai ekspor XLSX ditambah naskah cetak resmi (PDF). Validasinya lima lapis:

1. Jumlah sel kosong per butir dicocokkan dengan kolom `Unattempted` — cocok 20/20. Ekspor post-test tidak memuat entri "hantu".
2. Kunci diambil sebagai opsi yang jumlah pemilihnya sama persis dengan jumlah `Correct`. Menyelesaikan 18 butir.
3. Dua butir tersisa (Q11, Q17) diselesaikan lewat kendala: dari empat kombinasi calon, hanya satu yang membuat jumlah benar tiap peserta cocok dengan `Participant Data` pada seluruh 16 sesi.
4. Seluruh 20 kunci diverifikasi terhadap daftar opsi pada naskah cetak resmi — **kecocokan sempurna 20/20**, termasuk kedua kunci yang tadinya ambigu. Kunci karena itu pasti, bukan perkiraan.
5. Setelah sesi QA dikeluarkan, statistik dihitung ulang dari matriks respons dan dicocokkan kembali dengan `Participant Data` — tanpa selisih.

Analisis pengecoh menemukan **25 dari 60 opsi salah (42%) tidak dipilih oleh satu pun peserta**. Pada Q8, Q19 dan Q20 ketiga pengecohnya mati sekaligus, sehingga tingginya angka p pada butir-butir itu tidak boleh dibaca sebagai bukti penguasaan.

## Perlakuan terhadap sesi QA tester

Sesi atas nama **Vincent** dikeluarkan dari seluruh perhitungan post-test: 13 benar dalam waktu total 1 menit 28 detik untuk 20 butir, dengan sejumlah entri waktu 00:00:01 — pola penelusuran perangkat lunak, bukan orang yang membaca soal. Ia juga tidak muncul pada daftar peserta pre-test. Dampak pengeluarannya kecil (rata-rata turun 0,19 butir; akurasi turun 0,96 poin persen) tetapi tetap dilakukan karena sesi uji perangkat lunak tidak boleh ikut membentuk statistik butir maupun penetapan kelompok atas dan bawah.

## Keterbatasan

- n = 8 pada uji berpasangan tergolong kecil. Uji kepekaan sudah dilakukan dan kesimpulan bertahan, tetapi besaran rata-ratanya sensitif terhadap satu pengamatan.
- Daya beda post-test menggelembung (sepuluh butir D = 1,00) karena kelompok bawah sebagian besar terdiri atas sesi terputus. Nilai D post-test tidak sebanding dengan nilai D pre-test.
- Tidak ada kelompok pembanding, sehingga sebagian kenaikan dapat berasal dari efek mengerjakan tes serupa untuk kedua kalinya.
- Tidak ada pemeriksaan kecurangan; dalam mode take-home tanpa pengawasan justru paling dibutuhkan, tetapi datanya tidak tersedia.
- Yang terukur adalah pengetahuan deklaratif. Kemampuan praktik membuat desain memerlukan penilaian karya.
- Kunci pre-test direkonstruksi tanpa pembanding naskah resmi (berbeda dengan post-test yang terverifikasi PDF).
