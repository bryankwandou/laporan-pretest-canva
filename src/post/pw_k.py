# -*- coding: utf-8 -*-
# ============ 10 DASHBOARD
ws = wb.create_sheet("10 Dashboard Grafik")
title(ws, "DASHBOARD GRAFIK — SELURUH VISUAL DALAM SATU HALAMAN",
      "Setiap grafik tertaut ke tabel datanya di kolom A–F pada sheet ini, sehingga angka dapat ditelusuri dan grafik ikut berubah bila data disunting.", 6)

r = 4
blocks = []


def dtab(r, judul, cols, rows, w=None):
    secrow(ws, r, judul, 6); r += 1
    h0 = r
    for j, c in enumerate(cols, 1):
        cell = ws.cell(r, j, c); cell.fill = HDR; cell.font = WF; cell.border = BOX
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
    if w:
        for j, x in enumerate(w, 1):
            ws.column_dimensions[gcl(j)].width = x
    r += 1
    for row in rows:
        for j, v in enumerate(row, 1):
            cell = ws.cell(r, j, v); cell.border = BOX; cell.font = Font(size=10)
            if j > 1:
                cell.alignment = Alignment(horizontal="center")
        r += 1
    return h0, r - 1, r + 1


# 1 gain berpasangan
rows = [(o, a, b) for o, p, a, b in sorted(PAIRC, key=lambda x: -(x[3] - x[2]))]
h0, h1, r = dtab(r, "G1. PRE VERSUS POST PER PESERTA (8 PESERTA BERPASANGAN TUNTAS)",
                 ["Peserta", "Pre-test", "Post-test"], rows, [30, 14, 14, 14, 14, 14])
c = BarChart(); c.type = "col"; c.grouping = "clustered"; c.style = 10
c.title = "G1  Jawaban benar sebelum dan sesudah pelatihan"
c.y_axis.title = "Benar (dari 20)"; c.height = 10; c.width = 26
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 21)

# 2 konstruk
rows = [(lab[:40], round(a, 2), round(b, 2)) for lab, a, b, d, jen, bt in sorted(C1["crows"], key=lambda x: -x[3])]
h0, h1, r = dtab(r, "G2. TINGKAT KESUKARAN PER KONSTRUK, PRE VERSUS POST",
                 ["Konstruk", "p pre", "p post"], rows)
c = BarChart(); c.type = "bar"; c.grouping = "clustered"; c.style = 10
c.title = "G2  Penguasaan per konstruk (proporsi benar)"
c.x_axis.title = "Proporsi benar"; c.height = 14; c.width = 26
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 29)

# 3 selisih konstruk
rows = [(lab[:40], round(d, 2)) for lab, a, b, d, jen, bt in sorted(C1["crows"], key=lambda x: x[3])]
h0, h1, r = dtab(r, "G3. PERUBAHAN PENGUASAAN PER KONSTRUK (DELTA p)",
                 ["Konstruk", "Perubahan p"], rows)
c = BarChart(); c.type = "bar"; c.style = 11
c.title = "G3  Perubahan penguasaan: dua konstruk menurun"
c.x_axis.title = "Perubahan proporsi benar"; c.height = 12; c.width = 24
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
c.legend = None
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 25)

# 4 butir post p
rows = [("Q%d" % q["no"], round(q["p"], 2), round(q["D"], 2), round(q["rpb"], 2))
        for q in sorted(post["Q"], key=lambda x: -x["p"])]
h0, h1, r = dtab(r, "G4. STATISTIK BUTIR POST-TEST", ["Butir", "p", "D", "r-pbis"], rows)
c = BarChart(); c.type = "col"; c.style = 10
c.title = "G4  Tingkat kesukaran per butir post-test"
c.y_axis.title = "p"; c.height = 9; c.width = 26
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
c.legend = None
ws.add_chart(c, "H%d" % h0)
c2 = LineChart(); c2.style = 12
c2.title = "G5  Daya beda dan korelasi butir-total"
c2.height = 9; c2.width = 26
c2.add_data(Reference(ws, min_col=3, max_col=4, min_row=h0, max_row=h1), titles_from_data=True)
c2.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ws.add_chart(c2, "H%d" % (h0 + 19))
r = max(r, h1 + 40)

# 6 komposisi sesi
rows = [("Tuntas 20/20", len(COMP)), ("Terputus sebagian", len([n for n in INC if att[n] > 0])),
        ("Nol jawaban", len([n for n in INC if att[n] == 0]))]
h0, h1, r = dtab(r, "G6. KOMPOSISI SESI POST-TEST", ["Status sesi", "Jumlah"], rows)
c = PieChart(); c.style = 10
c.title = "G6  Komposisi 15 sesi post-test"
c.height = 9; c.width = 13
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dataLabels = DataLabelList(); c.dataLabels.showVal = True; c.dataLabels.showPercent = True
ws.add_chart(c, "H%d" % h0)

# 7 sebaran
cnt = Counter(sc_post.values())
rows = [(k, cnt.get(k, 0)) for k in range(0, 21)]
h0b, h1b, r = dtab(r, "G7. SEBARAN SKOR POST-TEST", ["Jawaban benar", "Jumlah sesi"], rows)
c = BarChart(); c.type = "col"; c.style = 10; c.gapWidth = 20
c.title = "G7  Sebaran jumlah jawaban benar (15 sesi)"
c.y_axis.title = "Jumlah sesi"; c.x_axis.title = "Jawaban benar"
c.height = 9; c.width = 22
c.add_data(Reference(ws, min_col=2, min_row=h0b, max_row=h1b), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0b + 1, max_row=h1b))
c.legend = None
ws.add_chart(c, "H%d" % h0b)
r = max(r, h1b + 20)

# 8 basis pembanding
compv = [sc_post[n] for n in COMP]
rows = [("Pre-test 37 sesi", round(st.mean(sc_pre.values()), 2)),
        ("Post-test 15 sesi", round(st.mean(sc_post.values()), 2)),
        ("Post-test 10 tuntas", round(st.mean(compv), 2)),
        ("Berpasangan pre (8)", round(st.mean(gaC), 2)),
        ("Berpasangan post (8)", round(st.mean(gbC), 2))]
h0, h1, r = dtab(r, "G8. RATA-RATA MENURUT BASIS PEMBANDING", ["Basis", "Rata-rata benar"], rows)
c = BarChart(); c.type = "col"; c.style = 12
c.title = "G8  Angka berbeda menurut basis pembanding yang dipakai"
c.y_axis.title = "Rata-rata benar"; c.height = 9; c.width = 22
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
c.legend = None
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 20)

# 9 pengecoh
rows = [("Pengecoh hidup", 60 - sum(len(v) for v in DEAD.values())),
        ("Pengecoh mati", sum(len(v) for v in DEAD.values()))]
h0, h1, r = dtab(r, "G9. KEBERFUNGSIAN PENGECOH POST-TEST", ["Status", "Jumlah opsi"], rows)
c = PieChart(); c.style = 10
c.title = "G9  Dari 60 opsi salah, berapa yang benar-benar dipilih"
c.height = 9; c.width = 13
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dataLabels = DataLabelList(); c.dataLabels.showVal = True; c.dataLabels.showPercent = True
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 20)


# ============ 11 DATA MENTAH
ws = wb.create_sheet("11 Data Mentah")
title(ws, "DATA MENTAH — JAWABAN YANG DIPILIH SETIAP PESERTA PADA SETIAP BUTIR",
      "Hijau benar, merah salah, abu-abu tidak dijawab. Teks yang ditampilkan adalah opsi persis yang dipilih. "
      "Sesi Vincent tidak ditampilkan. Ini sumber tunggal seluruh analisis post-test pada workbook ini.", 22)
head(ws, 4, ["#", "Nama"] + ["Q%d" % i for i in range(1, 21)], [5, 24] + [30] * 20)
r = 5
for i, n in enumerate(ORDP, 1):
    ws.cell(r, 1, i).border = BOX
    ws.cell(r, 1).alignment = Alignment(horizontal="center")
    c = ws.cell(r, 2, n); c.font = Font(size=10, bold=True); c.border = BOX
    for qi in range(20):
        a = QO[qi + 1]["answers"].get(n)
        cell = ws.cell(r, qi + 3, a if a else "—")
        cell.border = BOX; cell.font = Font(size=9)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.fill = {"C": GRN, "X": RED, "-": GRY}[CO[n][qi]]
    ws.row_dimensions[r].height = 40
    r += 1
ws.freeze_panes = "C5"

# ============ 12 DATA BERPASANGAN
ws = wb.create_sheet("12 Data Berpasangan")
title(ws, "DATA BERPASANGAN SIAP OLAH — UNTUK ANALISIS LANJUTAN (SPSS, R, JAMOVI)",
      "Satu baris satu peserta. Format panjang tersedia di kolom sebelah kanan. Kolom 'tuntas' menandai baris yang dipakai pada uji statistik utama.", 12)
head(ws, 4, ["id", "nama_post", "nama_pre", "pre", "post", "gain", "gain_norm",
             "butir_dijawab_post", "tuntas", "waktu_post_detik", "nilai_pre", "nilai_post"],
     [5, 26, 24, 8, 8, 8, 11, 16, 9, 15, 11, 11])
r = 5
for i, (o, p, a, b) in enumerate(sorted(PAIR, key=lambda x: -(x[3] - x[2])), 1):
    tuntas = 1 if att[o] == 20 else 0
    putrow(ws, r, [i, o, p, a, b, b - a, round((b - a) / (20 - a), 4) if a < 20 else 0,
                   att[o], tuntas, PO[o]["time_s"], a * 5, b * 5],
           ctr=(1, 4, 5, 6, 7, 8, 9, 10, 11, 12), h=18)
    ws.cell(r, 9).fill = GRN if tuntas else RED
    r += 1
r += 2
secrow(ws, r, "CATATAN PEMAKAIAN", 12); r += 1
for t in [
    "Uji statistik utama pada laporan ini memakai baris dengan tuntas = 1 (n = 8). Menyertakan baris tuntas = 0 akan mencampurkan kegagalan teknis dengan hasil ujian dan menghapus signifikansi statistik.",
    "Kolom gain_norm adalah gain ternormalisasi Hake, dihitung sebagai (post − pre) / (20 − pre). Nilainya menyatakan berapa bagian dari jarak menuju skor sempurna yang berhasil ditutup.",
    "Skala nilai memakai konversi 5 poin per butir benar, sehingga 20 butir setara nilai 100.",
    "Untuk analisis di SPSS atau jamovi: gunakan Paired-Samples T Test dengan pasangan variabel pre dan post, disaring pada tuntas = 1. Untuk uji non-parametrik gunakan Wilcoxon Signed-Rank atau uji tanda pada pasangan yang sama.",
]:
    note(ws, r, t, 12, 40); r += 1

wb.save("LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx")
print("saved sheets=%d charts=%d" % (len(wb.sheetnames), sum(len(w._charts) for w in wb)))
