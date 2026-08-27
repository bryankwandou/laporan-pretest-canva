# Laporan Evaluasi Pre-test Pelatihan Canva — 25 Agustus 2026

Analisis statistik hasil pre-test pelatihan Canva (Wanita Katolik RI) yang diselenggarakan melalui **Wayground / Quizizz**. Berisi analisis butir, reliabilitas instrumen, segmentasi peserta, pemetaan miskonsepsi, analisis waktu dan rekomendasi rancangan pelatihan.

**Laporan web:** https://laporan-pretest-canva.vercel.app

## Angka pokok

| Ukuran | Nilai |
|---|---|
| Sesi terekam | 37 (33 aktif, 4 sesi nol jawaban) |
| Butir | 20 pilihan ganda |
| Akurasi kelas | 32,3% (36,2% atas sesi aktif) |
| Rata-rata benar | 6,46 dari 20 · simpangan baku 3,75 |
| Reliabilitas KR-20 | 0,751 |
| Kesalahan baku ukur | ±1,87 butir |
| Rata-rata daya beda | 0,470 |

## Isi repositori

| Berkas | Keterangan |
|---|---|
| `index.html` | Laporan web, satu halaman, mandiri (grafik SVG inline) |
| `LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx` | Workbook 15 lembar kerja, 16 grafik native Excel |
| `vercel.json` | Konfigurasi deploy statis |
| `src/core.json` | Dataset terkonsolidasi: 20 butir, 37 peserta, matriks waktu dan matriks benar/salah |
| `src/stats.json` | Statistik butir terhitung (p, D, r-pbis, KR-20, SEM) |
| `src/extract.py`, `src/build_core.py`, `src/remask.py` | Pipeline ekstraksi dan pembersihan data |
| `src/stats_calc.py` | Perhitungan statistik butir dan reliabilitas |
| `src/gen_a.py` … `src/gen_e.py`, `src/run_site.py` | Pembangkit laporan web |
| `src/common.py`, `src/s01.py` … `src/s12.py`, `src/runner.py` | Pembangkit workbook Excel |

## Reproduksi

```bash
cd src
python run_site.py                       # menghasilkan site/index.html
python runner.py s01.py s02.py ... s12.py   # menghasilkan workbook XLSX
```

Membutuhkan Python 3 dan `openpyxl` (hanya untuk workbook Excel).

## Sumber data dan validasi

Dua sumber dipakai bersamaan:

1. **Ekspor resmi Wayground (XLSX)** — naskah soal, jawaban tiap peserta, waktu per butir, metadata sesi.
2. **Snapshot HTML laporan admin** — matriks respons berwarna 37×20, dipakai sebagai penentu status benar / salah / tidak dijawab karena memisahkan “salah” dari “kosong”, sedangkan ekspor XLSX menggabungkan keduanya.

Jumlah benar dan salah per butir dari kedua sumber dicocokkan satu per satu: **identik pada 20 dari 20 butir** (239 benar, 302 salah). Kolom jawaban pada ekspor XLSX memuat entri “hantu” — teks jawaban tetap tercantum untuk sel yang sebenarnya tidak dijawab — dan seluruhnya disaring memakai matriks respons.

Kunci jawaban tidak tersedia dalam kedua berkas; kunci direkonstruksi dari opsi yang dipilih peserta yang ditandai benar oleh sistem. Pada 20 dari 20 butir seluruh peserta yang benar memilih opsi yang sama persis, sehingga kunci tidak ambigu.

## Keterbatasan

- n = 37 tergolong kecil untuk analisis butir; kelompok atas dan bawah masing-masing 10 orang, sehingga satu jawaban berbeda menggeser daya beda sebesar 0,10.
- Q1 hanya dijawab 14 peserta dan Q3 oleh 20 peserta — basis statistik kedua butir ini tipis.
- Kunci jawaban direkonstruksi, bukan diambil dari dokumen resmi.
- Skor Wayground memuat bonus kecepatan; seluruh analisis di sini memakai jumlah jawaban benar, bukan poin.
- Peringkat individu tidak layak dipakai untuk keputusan perorangan mengingat kesalahan baku ukur ±1,87 butir.
