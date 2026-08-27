# -*- coding: utf-8 -*-
# ============================================================ 13 KUNCI JAWABAN
ws = wb.create_sheet("13 Soal dan Kunci")
title(ws, "NASKAH SOAL LENGKAP, KUNCI JAWABAN DAN SEBARAN PILIHAN",
      "Kunci jawaban direkonstruksi dari data: opsi yang dipilih oleh seluruh peserta yang ditandai benar oleh sistem. "
      "Rekonstruksi ini konsisten 100% pada seluruh 20 butir - tidak ada satu pun butir dengan kunci yang ambigu.", 8)
head(ws, 4, ["Butir", "Naskah soal", "Kunci jawaban", "Seluruh opsi yang dipilih peserta (jumlah pemilih)",
             "p", "D", "r-pbis", "Ranah / Bloom"],
     [7, 74, 62, 74, 8, 8, 9, 26])
r = 5
for it in items:
    no = it["no"]
    q = [x for x in Q if x["no"] == no][0]
    opts = "\n".join("%s%s  (%d)" % ("[KUNCI] " if a == it["key"] else "", a, c) for a, c in it["distr"])
    row = [no, q["text"], it["key"], opts, round(it["p"], 3), round(it["D"], 2),
           round(it["rpb"], 3), DOMAIN[no] + "\n" + BLOOM[no]]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i in (1, 5, 6, 7):
            c.alignment = Alignment(horizontal="center", vertical="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 1).font = Font(size=12, bold=True, color="FFFFFF")
    ws.cell(r, 1).fill = HDR
    ws.cell(r, 3).fill = GRN
    ws.cell(r, 3).font = Font(size=10, bold=True)
    ws.row_dimensions[r].height = 96
    r += 1
ws.freeze_panes = "B5"

# ============================================================ 14 DATA MENTAH
ws = wb.create_sheet("14 Data Mentah Jawaban")
title(ws, "DATA MENTAH — JAWABAN YANG DIPILIH SETIAP PESERTA PADA SETIAP BUTIR",
      "Sel hijau berarti benar, merah berarti salah, abu-abu berarti tidak dijawab. Teks yang ditampilkan adalah opsi persis yang dipilih peserta. "
      "Ini adalah sumber tunggal seluruh analisis pada workbook ini.", 22)
head(ws, 4, ["#", "Nama"] + ["Q%d" % i for i in range(1, 21)], [5, 24] + [34] * 20)
r = 5
for idx, n in enumerate(sorted(P, key=lambda n: -sc[n]), 1):
    ws.cell(r, 1, idx).border = BOX
    c = ws.cell(r, 2, n); c.font = Font(size=10, bold=True); c.border = BOX
    c.alignment = Alignment(vertical="center")
    for qi, q in enumerate(Q, 3):
        a = q["answers_real"].get(n)
        cell = ws.cell(r, qi, a if a else "—")
        cell.border = BOX; cell.font = Font(size=9)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        s_ = CORR[n][qi - 3]
        cell.fill = {"C": GRN, "X": RED, "-": F("EDEDED")}[s_]
    ws.row_dimensions[r].height = 40
    r += 1
ws.freeze_panes = "C5"

# ============================================================ 15 METODOLOGI
ws = wb.create_sheet("15 Metodologi")
title(ws, "METODOLOGI, RUMUS DAN CATATAN KETERBATASAN",
      "Seluruh perhitungan pada workbook ini dapat direproduksi dari dua berkas sumber yang disebut di bawah.", 6)

r = 4
secrow(ws, r, "A. SUMBER DATA", 6); r += 1
head(ws, r, ["Berkas", "Isi", "Peran dalam analisis", "", "", ""], [56, 60, 90])
r += 1
SRC = [
    ("pretestpelatihancanva25agustus2026-2026-08-25T09_22_13_634913-c1bee5.xlsx",
     "Export resmi Wayground: sheet Overview (naskah soal, jawaban tiap peserta), Participant Data, Time Data, Quiz Details.",
     "Sumber naskah soal, teks jawaban yang dipilih, waktu per butir, poin, dan metadata sesi."),
    ("Wayground 25 agustus 2026 canva wkri.html",
     "Snapshot HTML halaman laporan admin, memuat matriks respons berwarna 37 baris x 20 kolom.",
     "Sumber status benar/salah/kosong per sel. Dipakai sebagai penentu karena memisahkan 'salah' dari 'tidak dijawab', sedangkan export XLSX menggabungkan keduanya di tingkat peserta."),
]
for a, b, c_ in SRC:
    ws.cell(r, 1, a).font = Font(size=9, bold=True)
    ws.cell(r, 1).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 2, b).alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    ws.cell(r, 3, c_).alignment = Alignment(wrap_text=True, vertical="top")
    for j in range(1, 7):
        ws.cell(r, j).border = BOX
        if j > 1:
            ws.cell(r, j).font = Font(size=10)
    ws.row_dimensions[r].height = 60
    r += 1
r += 1

secrow(ws, r, "B. VALIDASI SILANG YANG DILAKUKAN", 6); r += 1
for t in [
    "Jumlah jawaban benar dan salah per butir dari kedua sumber dicocokkan satu per satu. Hasilnya identik pada seluruh 20 butir (239 benar, 302 salah). Ini memastikan pembacaan matriks warna dari HTML sudah tepat.",
    "Kolom jawaban pada sheet Overview ternyata memuat entri 'hantu': teks jawaban tetap tercantum untuk sel yang sebenarnya tidak dijawab. Contohnya vivi tercatat memilih opsi pada Q1 padahal matriks menunjukkan butir itu tidak pernah dijawabnya. Seluruh entri semacam ini disaring memakai matriks respons sebagai penyaring.",
    "Setelah penyaringan, jumlah pemilih setiap opsi dicocokkan kembali dengan jumlah benar dan salah resmi per butir. Kecocokan tercapai pada 20 dari 20 butir tanpa selisih.",
    "Kunci jawaban tidak tersedia dalam kedua berkas. Kunci direkonstruksi dengan mengambil opsi yang dipilih oleh peserta yang ditandai benar. Pada seluruh 20 butir, semua peserta yang benar memilih opsi yang sama persis, sehingga kunci tidak ambigu.",
    "Perlu dicatat satu ketidakkonsistenan bawaan Wayground: pada sheet Participant Data, butir yang kehabisan waktu dihitung sebagai 'Incorrect', sedangkan pada sheet Overview tidak. Workbook ini konsisten memakai tiga kategori terpisah (benar, salah, kosong) sesuai matriks respons.",
]:
    note(ws, r, t, 6, 40); r += 1
r += 1

secrow(ws, r, "C. RUMUS YANG DIPAKAI", 6); r += 1
head(ws, r, ["Ukuran", "Rumus", "Penerapan pada data ini", "", "", ""], [30, 56, 100])
r += 1
FORM = [
    ("Tingkat kesukaran (p)", "p = B / N", "B = jumlah peserta yang menjawab benar; N = 37 (seluruh sesi). Sel kosong dihitung sebagai tidak benar, sesuai cara Wayground menghitung akurasi."),
    ("Daya beda (D)", "D = (BA / nA) − (BB / nB)", "Kelompok atas dan bawah masing-masing 27% dari 37, dibulatkan menjadi 10 sesi. BA dan BB adalah jumlah benar pada masing-masing kelompok."),
    ("Korelasi point-biserial", "r-pbis = ((M1 − M0) / SDt) × √(p × q)", "M1 = rata-rata skor total peserta yang benar pada butir; M0 = rata-rata skor peserta yang salah; SDt = simpangan baku skor total; q = 1 − p."),
    ("Reliabilitas KR-20", "KR20 = (k / (k−1)) × (1 − Σpq / σ²)", "k = 20 butir; σ² = varians skor total (14,04). Hasil 0,751."),
    ("Standard Error of Measurement", "SEM = SD × √(1 − r)", "SD = 3,75; r = KR-20 = 0,751. Hasil ±1,87 butir."),
    ("z-skor", "z = (X − μ) / σ", "μ = 6,46 dan σ = 3,75 dihitung atas 37 sesi sebagai populasi, bukan sampel."),
    ("T-skor", "T = 50 + 10z", "Skala turunan agar tidak ada nilai negatif; rata-rata kelas selalu 50."),
    ("Peringkat persentil", "PR = ((cf_bawah + 0,5 × f) / N) × 100", "cf_bawah = jumlah peserta dengan skor lebih rendah; f = jumlah peserta dengan skor sama."),
    ("Pengecoh efektif", "Opsi salah dipilih ≥ 5% penjawab butir", "Penjawab butir = benar + salah, tidak termasuk sel kosong."),
    ("Koefisien variasi", "CV = σ / μ", "Dipakai membandingkan penyebaran relatif; nilai di atas 50% menandakan kelompok tidak homogen."),
]
for a, b, c_ in FORM:
    ws.cell(r, 1, a).font = Font(size=10, bold=True)
    ws.cell(r, 1).alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 2, b).font = Font(size=10, name="Consolas")
    ws.cell(r, 2).alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    ws.cell(r, 3, c_).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(r, 3).font = Font(size=10)
    for j in range(1, 7):
        ws.cell(r, j).border = BOX
    ws.row_dimensions[r].height = 42
    r += 1
r += 1

secrow(ws, r, "D. AMBANG TAFSIR YANG DIPAKAI", 6); r += 1
head(ws, r, ["Ukuran", "Ambang", "Kategori", "", "", ""], [30, 30, 120])
r += 1
AMB = [
    ("Tingkat kesukaran p", "p < 0,30 / 0,30–0,70 / p > 0,70", "Sukar / Sedang / Mudah (Arikunto)"),
    ("Daya beda D", "≥0,40 / 0,30–0,39 / 0,20–0,29 / <0,20", "Sangat baik / Baik / Cukup, perlu revisi / Buruk, ditolak (Ebel & Frisbie)"),
    ("Korelasi butir-total", "r ≥ 0,30 memadai; r < 0,20 bermasalah", "Butir dengan r negatif menandakan kunci keliru atau redaksi menyesatkan"),
    ("Reliabilitas KR-20", "≥0,90 / 0,80–0,89 / 0,70–0,79 / <0,70", "Sangat tinggi / Tinggi / Cukup / Rendah"),
    ("Nilai huruf", "85–100 / 70–84 / 55–69 / 40–54 / 0–39", "A Sangat Baik / B Baik / C Cukup / D Kurang / E Sangat Kurang"),
    ("KKM", "70% atau 14 dari 20 butir", "Ambang ketuntasan yang lazim dipakai pada pelatihan sejenis"),
]
for a, b, c_ in AMB:
    ws.cell(r, 1, a).font = Font(size=10, bold=True)
    ws.cell(r, 2, b).font = Font(size=10)
    ws.cell(r, 2).alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=6)
    ws.cell(r, 3, c_).font = Font(size=10)
    ws.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="center")
    for j in range(1, 7):
        ws.cell(r, j).border = BOX
    ws.row_dimensions[r].height = 30
    r += 1
r += 1

secrow(ws, r, "E. KETERBATASAN YANG HARUS DISADARI PEMBACA", 6); r += 1
for t in [
    "Jumlah peserta 37 sesi tergolong kecil untuk analisis butir. Kelompok atas dan bawah masing-masing hanya 10 orang, sehingga satu jawaban berbeda menggeser daya beda sebesar 0,10. Perlakukan nilai D sebagai indikasi arah, bukan angka pasti.",
    "Q1 hanya dijawab 14 peserta dan Q3 oleh 20 peserta. Statistik pada kedua butir ini berdiri di atas basis yang tipis dan paling rapuh di antara seluruh butir.",
    "Kunci jawaban direkonstruksi, bukan diambil dari dokumen resmi. Rekonstruksinya konsisten sempurna, namun bila panitia memiliki dokumen kunci asli, sebaiknya dicocokkan sekali lagi - terutama Q6 yang menanyakan penerapan yang BERTENTANGAN dengan prinsip hierarki visual, sehingga kuncinya justru berupa pernyataan yang keliru secara desain.",
    "Analisis ini tidak memuat pemeriksaan kecurangan. Sheet Anti-cheating pada laporan Wayground tidak tersedia dalam berkas yang diberikan.",
    "Skor Wayground memberi bonus kecepatan, sehingga peringkat poin tidak sama dengan peringkat kemampuan. Seluruh analisis akademik pada workbook ini memakai jumlah jawaban benar, bukan poin.",
    "Hasil pre-test ini hanya menggambarkan pengetahuan deklaratif tentang Canva. Kemampuan praktik sesungguhnya - apakah peserta bisa membuat desain yang layak - tidak terukur oleh tes pilihan ganda dan memerlukan penilaian karya.",
]:
    note(ws, r, t, 6, 40); r += 1
