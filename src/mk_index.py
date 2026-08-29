# -*- coding: utf-8 -*-
import io, os, json, hashlib
from collections import defaultdict

SP = os.path.dirname(os.path.abspath(__file__))
SUB = "E:/Download/SUBMISSION_EVALUASI_PELATIHAN_CANVA"
man = json.load(io.open(os.path.join(SP, "manifest.json"), encoding="utf-8"))
byd = defaultdict(list)
for d, n, s, h in man:
    byd[d].append((n, s, h))

KET = {
    "LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx": "Laporan pre-test — 15 lembar kerja, 16 grafik native",
    "LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx": "Laporan post-test dan perbandingan — 13 lembar kerja, 20 grafik, matriks waktu penuh dan sheet data berpasangan siap olah",
    "index.html": "Halaman web laporan pre-test (13 bagian)",
    "post-test.html": "Halaman web laporan post-test dan perbandingan (11 bagian)",
    "vercel.json": "Konfigurasi deploy statis",
    "Wayground 25 agustus 2026 canva wkri.html": "SUMBER — snapshot HTML laporan admin pre-test, memuat matriks respons berwarna 37x20",
    "pretestpelatihancanva25agustus2026-2026-08-25T09_22_13_634913-c1bee5.xlsx": "SUMBER — ekspor resmi Wayground pre-test",
    "post-testpelatihancanva25agustus2026-2026-08-28T14_07_30_851549-68e3ea.xlsx": "SUMBER — ekspor resmi Wayground post-test",
    "Free Printable post-test pelatihan canva 25 agustus 2026.pdf": "SUMBER — naskah cetak resmi 20 butir post-test beserta keempat opsi",
    "core.json": "Dataset pre-test terkonsolidasi: 20 butir, 37 peserta, matriks waktu dan matriks benar/salah",
    "stats.json": "Statistik butir pre-test: p, D, r-pbis, KR-20, SEM",
    "post_core_raw.json": "Dataset post-test mentah, masih memuat sesi QA tester",
    "post_core.json": "Dataset post-test final setelah sesi QA dikeluarkan, dengan statistik butir dihitung ulang",
    "cmp.json": "Hasil perbandingan: pasangan peserta, pemetaan konstruk, gain",
    "cmp2.json": "Hasil analisis sesi tuntas: uji-t, uji tanda, uji kepekaan, dampak pengeluaran QA",
    "pdf_opts.json": "Opsi lengkap tiap butir dari naskah PDF dan daftar pengecoh mati",
    "cmp_out.txt": "Keluaran perhitungan bagian A-E: gambaran umum, berpasangan, konstruk, butir, peserta",
    "cmp_out2.txt": "Keluaran perhitungan bagian F-I: dampak QA, sesi tuntas, uji statistik, waktu",
    "cmp_out3.txt": "Keluaran verifikasi kunci terhadap PDF dan daftar 25 pengecoh mati",
    "pdf.txt": "Teks hasil ekstraksi naskah PDF",
    "cmp_items.txt": "Naskah 20 butir pre-test dan 20 butir post-test berdampingan, dengan kuncinya",
    "HASIL_VERIFIKASI_PAKET.txt": "Laporan verifikasi keutuhan paket: sidik SHA-256, keterbacaan workbook, konsistensi angka",
    "HASIL_AUDIT_KECUKUPAN_EXCEL.txt": "Laporan audit kecukupan workbook: 60 pemeriksaan isi sel terhadap data sumber",
    "post_time.json": "Matriks waktu post-test per peserta per butir, hasil ekstraksi sheet Time Data",
    "post_time.py": "Ekstraksi matriks waktu post-test",
    "audit_xlsx.py": "Skrip audit kecukupan workbook Excel",
    "verify_sub.py": "Skrip verifikasi keutuhan paket submission",
    "mk_sub.py": "Skrip pembangun paket submission",
    "mk_index.py": "Skrip pembangun indeks paket",
}

L = []
W = L.append
W("=" * 96)
W("PAKET SUBMISSION — EVALUASI PELATIHAN CANVA")
W("Wanita Katolik RI · Pelatihan 25 Agustus 2026 · Post-test ditutup 28 Agustus 2026")
W("Disusun 29 Agustus 2026")
W("=" * 96)
W("")
W("TAUTAN DARING")
W("  Laporan web      https://laporan-pretest-canva.vercel.app")
W("    Pre-test       https://laporan-pretest-canva.vercel.app/")
W("    Post-test      https://laporan-pretest-canva.vercel.app/post-test.html")
W("  Repositori kode  https://github.com/bryankwandou/laporan-pretest-canva")
W("")
W("-" * 96)
W("ANGKA POKOK")
W("-" * 96)
W("%-46s %14s %14s" % ("Ukuran", "PRE-TEST", "POST-TEST"))
for a, b, c in [("Sesi terekam", "37", "15 (QA tester dikeluarkan)"),
                ("Sesi tuntas", "34 aktif", "10 tuntas 20/20"),
                ("Mode pelaksanaan", "Live 14 menit", "Homework 3 hari"),
                ("Akurasi seluruh sesi", "32,3%", "49,7%"),
                ("Rata-rata benar dari 20", "6,46", "9,93"),
                ("Reliabilitas KR-20", "0,751", "0,721 (10 sesi tuntas)"),
                ("Kesalahan baku ukur", "+/-1,87 butir", "+/-1,76 butir")]:
    W("%-46s %14s %14s" % (a, b, c))
W("")
W("HASIL UTAMA — ANALISIS BERPASANGAN (8 peserta menyelesaikan kedua tes)")
W("  Rata-rata pre -> post        8,62 -> 13,62 butir")
W("  Rata-rata gain              +5,00 butir")
W("  Naik / tetap / turun        8 / 0 / 0  (seluruhnya naik)")
W("  Uji-t berpasangan           t(7) = 3,67  vs kritis 2,365 pada alfa 0,05  -> SIGNIFIKAN")
W("  Uji tanda binomial          8 dari 8 naik, p = 0,0039")
W("  Ukuran efek Cohen dz        1,30 (besar)")
W("  Gain ternormalisasi Hake    0,440 (sedang)")
W("  Uji kepekaan tanpa outlier  t(6) = 7,12; dz = 2,69  -> kesimpulan bertahan")
W("")
W("BATAS TAFSIR — WAJIB DIBACA SEBELUM MENGUTIP ANGKA MANA PUN")
W("  Tiga hal berubah bersamaan antara kedua pengukuran, seluruhnya ke arah membuat")
W("  kenaikan terlihat lebih besar daripada sebenarnya:")
W("    1. Instrumen berubah. Hanya 14 dari 20 konstruk beririsan; hanya 2 butir praktis")
W("       identik kata per kata. Enam butir post-test menguji materi yang tidak ada di")
W("       pre-test, dan enam butir pre-test tidak diulang.")
W("    2. Mode berubah. Pre-test live berbatas waktu; post-test take-home tiga hari tanpa")
W("       pengawasan dengan materi pelatihan tersedia.")
W("    3. Peserta menyusut 60%. Yang bertahan rata-rata pre-test-nya 8,62 berbanding 6,46")
W("       untuk seluruh kelas — bias seleksi.")
W("")
W("  Karena itu +5,00 butir diperlakukan sebagai BATAS ATAS dampak pelatihan, bukan")
W("  perkiraan tak bias. Selisih akurasi kelas 32,3% -> 49,7% TIDAK boleh dikutip sebagai")
W("  hasil belajar, karena membandingkan dua kelompok peserta, dua perangkat soal, dan dua")
W("  mode pelaksanaan yang berbeda sekaligus.")
W("")
W("VALIDASI KUNCI JAWABAN")
W("  Pre-test  : kunci direkonstruksi dari pola respons; konsisten pada 20 dari 20 butir,")
W("              tanpa pembanding naskah resmi.")
W("  Post-test : kunci direkonstruksi lalu diverifikasi terhadap naskah cetak resmi PDF —")
W("              kecocokan sempurna pada 20 dari 20 butir, termasuk dua kunci yang tadinya")
W("              ambigu dan diselesaikan lewat kendala jumlah benar tiap peserta.")
W("  Pengecoh  : 25 dari 60 opsi salah post-test (42%) tidak dipilih satu pun peserta.")
W("              Q8, Q19 dan Q20 kehilangan seluruh pengecohnya.")
W("")
W("PERLAKUAN SESI QA TESTER")
W("  Sesi atas nama Vincent dikeluarkan dari SELURUH perhitungan post-test: 13 benar dalam")
W("  waktu total 1 menit 28 detik untuk 20 butir, dengan sejumlah entri waktu 00:00:01.")
W("  Ia juga tidak muncul pada daftar peserta pre-test. Dampak pengeluarannya kecil")
W("  (rata-rata turun 0,19 butir; akurasi turun 0,96 poin persen) dan didokumentasikan")
W("  penuh pada sheet 09 Metodologi bagian C.")
W("")

DESC = {
    "01_LAPORAN_EXCEL": "Berkas utama yang diserahkan. Kedua workbook memuat grafik native Excel, bukan gambar.",
    "02_LAPORAN_WEB": "Salinan luring laporan web. Buka index.html langsung di peramban; kedua workbook disertakan agar tombol unduh pada halaman berfungsi tanpa jaringan.",
    "03_DATA_SUMBER": "Berkas mentah apa adanya dari Wayground. Tidak diubah sama sekali.",
    "04_DATA_OLAHAN": "Dataset hasil pengolahan dalam format JSON, dapat dibaca ulang oleh skrip mana pun.",
    "05_SKRIP_REPRODUKSI": "Seluruh kode pengolahan. Menjalankannya kembali menghasilkan workbook dan halaman web yang identik.",
    "06_KELUARAN_PERHITUNGAN": "Keluaran teks mentah seluruh perhitungan, untuk menelusuri angka mana pun sampai ke sumbernya.",
}

W("=" * 96)
W("ISI PAKET")
W("=" * 96)
tot = 0
for d in ["01_LAPORAN_EXCEL", "02_LAPORAN_WEB", "03_DATA_SUMBER", "04_DATA_OLAHAN",
          "05_SKRIP_REPRODUKSI", "05_SKRIP_REPRODUKSI/pre", "05_SKRIP_REPRODUKSI/post", "06_KELUARAN_PERHITUNGAN"]:
    files = byd.get(d, [])
    W("")
    W("%s  (%d berkas)" % (d, len(files)))
    key = d.split("/")[0]
    if not d.endswith("/post"):
        W("  %s" % DESC[key])
    W("  " + "-" * 92)
    for n, s, h in sorted(files):
        k = KET.get(n, "")
        if not k:
            if n.startswith(("s0", "s1")) or n.startswith("pw_"):
                k = "pembangkit lembar kerja Excel"
            elif n.startswith(("gen_", "gp_")):
                k = "pembangkit halaman web"
            elif n.startswith("run_"):
                k = "penjalan pipeline"
            elif n == "style.css":
                k = "gaya bersama halaman web"
            elif n in ("common.py", "runner.py"):
                k = "utilitas bersama pembangkit Excel"
            else:
                k = "skrip pengolahan"
        W("  %-62s %9s  %s" % (n, "{:,}".format(s).replace(",", "."), k))
        tot += s
W("")
W("  " + "=" * 92)
W("  TOTAL %d berkas, %s byte" % (len(man), "{:,}".format(tot).replace(",", ".")))
W("")
W("=" * 96)
W("CARA REPRODUKSI")
W("=" * 96)
W("  Membutuhkan Python 3 dengan paket openpyxl dan pypdf.")
W("  Salin isi 03_DATA_SUMBER dan 04_DATA_OLAHAN ke folder kerja yang sama dengan skrip.")
W("")
W("  Pre-test :  python extract.py && python build_core.py && python remask.py")
W("              python stats_calc.py")
W("              python runner.py s01.py s02.py ... s12.py     -> workbook pre-test")
W("              python run_site.py                            -> index.html")
W("")
W("  Post-test:  python post_extract.py && python post_build.py")
W("              python cmp_calc.py && python cmp_calc2.py && python pdf_opts.py")
W("              python run_pw.py                              -> workbook post-test")
W("              python run_gp.py                              -> post-test.html")
W("")
W("=" * 96)
W("KETERBATASAN")
W("=" * 96)
for t in [
    "n = 8 pada uji berpasangan tergolong kecil. Uji kepekaan sudah dilakukan dan kesimpulan bertahan, tetapi besaran rata-ratanya sensitif terhadap satu pengamatan.",
    "Daya beda post-test menggelembung (sepuluh butir D = 1,00) karena kelompok bawah sebagian besar terdiri atas sesi terputus. Nilai D post-test tidak sebanding dengan nilai D pre-test.",
    "Tidak ada kelompok pembanding, sehingga sebagian kenaikan dapat berasal dari efek mengerjakan tes serupa untuk kedua kalinya.",
    "Tidak ada pemeriksaan kecurangan. Dalam mode take-home tanpa pengawasan justru paling dibutuhkan, tetapi datanya tidak tersedia dalam berkas yang diberikan.",
    "Yang terukur adalah pengetahuan deklaratif. Kemampuan praktik membuat desain memerlukan penilaian karya.",
    "Kunci pre-test direkonstruksi tanpa pembanding naskah resmi, berbeda dengan post-test yang terverifikasi PDF.",
    "Paket ini memuat nama asli peserta. Bila diperlukan persetujuan etik untuk publikasi, nama perlu diganti kode peserta terlebih dahulu.",
]:
    W("  - " + t)
W("")
W("=" * 96)
W("DAFTAR SIDIK BERKAS (SHA-256, 16 karakter pertama)")
W("=" * 96)
for d, n, s, h in man:
    W("  %s  %s/%s" % (h, d, n))
W("")

txt = "\n".join(L)
io.open(os.path.join(SUB, "00_BACA_INI_DULU.txt"), "w", encoding="utf-8").write(txt)
print("index written: %d baris, %d berkas, %s byte" % (len(L), len(man), "{:,}".format(tot)))
