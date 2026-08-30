# -*- coding: utf-8 -*-
"""Bagian D: 11 Grafik, 12 Data Olah, simpan."""

# ================= 11 GRAFIK
ws = wb.create_sheet("11 Grafik")
title(ws, "GRAFIK — SETIAP GRAFIK TERTAUT KE TABEL DATANYA DI KOLOM A-D",
      "Menyunting angka pada tabel akan mengubah grafiknya. Tidak ada gambar tempel pada berkas ini.", 6)
r = 4


def dtab(r, judul, cols, rows, widths=None):
    r = sec(ws, r, judul, 6)
    h0 = r
    for i, t in enumerate(cols):
        c = ws.cell(r, 1 + i, t)
        c.fill = HDR; c.font = WF; c.border = BOX; c.alignment = CEN
    if widths:
        for i, w in enumerate(widths):
            ws.column_dimensions[gcl(1 + i)].width = w
    r += 1
    for rw in rows:
        for i, v in enumerate(rw):
            c = ws.cell(r, 1 + i, v)
            c.border = BOX; c.font = Font(size=10)
            if i:
                c.alignment = CEN
        r += 1
    return h0, r - 1, r + 1


# G1 pre vs post per orang
rows = [(o, a, b) for o, p, a, b, ta, tb in sorted(PAIRT, key=lambda x: -x[3])]
h0, h1, r = dtab(r, "G1. JAWABAN BENAR SEBELUM DAN SESUDAH — %d ORANG BERPASANGAN" % STAT["n"],
                 ["Nama", "Pre-test", "Post-test"], rows, [30, 12, 12, 12, 12, 12])
c = BarChart(); c.type = "col"; c.grouping = "clustered"; c.style = 10
c.title = "G1  Jawaban benar sebelum dan sesudah pelatihan"
c.y_axis.title = "Benar dari 20"; c.height, c.width = 10, 24
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 22)

# G2 gain
rows = [(o, b - a) for o, p, a, b, ta, tb in sorted(PAIRT, key=lambda x: -(x[3] - x[2]))]
h0, h1, r = dtab(r, "G2. BESAR KENAIKAN PER ORANG", ["Nama", "Gain (butir)"], rows)
c = BarChart(); c.type = "bar"; c.style = 11
c.title = "G2  Kenaikan per orang — seluruhnya positif"
c.x_axis.title = "Butir"; c.height, c.width = 10, 22
c.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
c.legend = None
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 22)

# G3 sebaran skor
cp = Counter([RPRE[o].count("C") for o in ORANG_PRE])
cq = Counter([RPOST[o].count("C") for o in ORANG_POST])
rows = [(k, cp.get(k, 0), cq.get(k, 0)) for k in range(0, 21)]
h0, h1, r = dtab(r, "G3. SEBARAN SKOR — PRE-TEST (%d ORANG) DAN POST-TEST (%d ORANG)" % (NPRE, NPOST),
                 ["Jawaban benar", "Pre-test", "Post-test"], rows)
c = BarChart(); c.type = "col"; c.grouping = "clustered"; c.style = 12; c.gapWidth = 30
c.title = "G3  Sebaran jumlah jawaban benar"
c.y_axis.title = "Jumlah orang"; c.x_axis.title = "Jawaban benar"
c.height, c.width = 10, 24
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 22)

# G4 tingkat kesukaran butir
rows = [("Q%d" % n, round(SPRE_I[n]["p"], 3), round(SPOST_I[n]["p"], 3)) for n in range(1, 21)]
h0, h1, r = dtab(r, "G4. TINGKAT KESUKARAN TIAP BUTIR", ["Butir", "p pre-test", "p post-test"], rows)
c = BarChart(); c.type = "col"; c.grouping = "clustered"; c.style = 10
c.title = "G4  Tingkat kesukaran per butir (nomor butir kedua tes TIDAK sepadan)"
c.y_axis.title = "Proporsi benar"; c.height, c.width = 10, 26
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 22)

# G5 daya beda
rows = [("Q%d" % n, round(SPOST_I[n]["D"], 3), round(SPOST_I[n]["rpb"], 3)) for n in range(1, 21)]
h0, h1, r = dtab(r, "G5. DAYA BEDA DAN KORELASI BUTIR-TOTAL POST-TEST", ["Butir", "D", "r-pbis"], rows)
c = LineChart(); c.style = 12
c.title = "G5  Daya beda dan korelasi butir-total"
c.height, c.width = 9, 26
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 20)

# G6 pengecoh
nd_pre = sum(len(v) for v in DEAD_PRE.values())
nd_post = sum(len(v) for v in DEAD_POST.values())
rows = [("Pre-test", 60 - nd_pre, nd_pre), ("Post-test", 60 - nd_post, nd_post)]
h0, h1, r = dtab(r, "G6. KEBERFUNGSIAN PENGECOH — DARI 60 OPSI SALAH TIAP TES",
                 ["Tes", "Pengecoh berfungsi", "Pengecoh mati"], rows)
c = BarChart(); c.type = "col"; c.grouping = "stacked"; c.overlap = 100; c.style = 12
c.title = "G6  Pengecoh yang tidak pernah dipilih siapa pun"
c.y_axis.title = "Jumlah opsi"; c.height, c.width = 9, 16
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 20)

# G7 sensus
rows = [("Sesi terekam", 37, 16), ("Sesi peserta", 37, 15), ("Orang unik", NPRE, NPOST),
        ("Ikut kedua tes", len(PAIR), len(PAIR)), ("Kedua tes tuntas", len(PAIRT), len(PAIRT))]
h0, h1, r = dtab(r, "G7. SESI VERSUS ORANG", ["Basis", "Pre-test", "Post-test"], rows)
c = BarChart(); c.type = "col"; c.grouping = "clustered"; c.style = 10
c.title = "G7  Sesi versus orang pada kedua tes"
c.y_axis.title = "Jumlah"; c.height, c.width = 9, 20
c.add_data(Reference(ws, min_col=2, max_col=3, min_row=h0, max_row=h1), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
c.dLbls = DataLabelList(); c.dLbls.showVal = True
ws.add_chart(c, "H%d" % h0)
r = max(r, h1 + 20)

# G8 waktu vs skor
h0 = r + 1
ws.cell(h0, 1, "Menit").fill = HDR; ws.cell(h0, 1).font = WF
ws.cell(h0, 2, "Benar").fill = HDR; ws.cell(h0, 2).font = WF
rr = h0 + 1
tun = [o for o in ORANG_POST if RPOST[o].count("-") == 0]
for o in tun:
    ws.cell(rr, 1, round(PO[CH_POST[o]].get("time_s", 0) / 60, 1))
    ws.cell(rr, 2, RPOST[o].count("C"))
    rr += 1
c = ScatterChart(); c.style = 13
c.title = "G8  Waktu pengerjaan versus jawaban benar (post-test tuntas)"
c.x_axis.title = "Menit"; c.y_axis.title = "Benar dari 20"
c.height, c.width = 9, 18
se = Series(Reference(ws, min_col=2, min_row=h0, max_row=rr - 1),
            Reference(ws, min_col=1, min_row=h0 + 1, max_row=rr - 1), title_from_data=True)
se.marker.symbol = "circle"
se.graphicalProperties.line.noFill = True
c.series.append(se)
ws.add_chart(c, "H%d" % h0)

# ================= 12 DATA OLAH
ws = wb.create_sheet("12 Data Olah")
title(ws, "DATA SIAP OLAH — FORMAT PANJANG UNTUK SPSS, JAMOVI ATAU R",
      "Satu baris satu orang. Saring pada kolom tuntas = 1 untuk mengulang uji statistik pada lembar 10.", 13)
r = head(ws, 4, ["id", "nama_post", "nama_pre", "pre", "post", "gain", "gain_ternormalisasi",
                 "butir_dijawab_pre", "butir_dijawab_post", "tuntas", "waktu_post_detik",
                 "nilai_pre", "nilai_post"],
         [5, 26, 26, 8, 8, 8, 18, 16, 17, 8, 15, 10, 10])
for i, (o, p, a, b, ta, tb) in enumerate(sorted(PAIR, key=lambda x: -(x[3] - x[2])), 1):
    tuntas = 1 if tb == 20 else 0
    r = row(ws, r, [i, o, p, a, b, b - a,
                    round((b - a) / (20 - a), 4) if a < 20 else 0,
                    ta, tb, tuntas, PO[CH_POST[o]].get("time_s", 0), a * 5, b * 5],
            ctr=(1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), h=18, fs=10)
    ws.cell(r - 1, 10).fill = GRN if tuntas else RED
r += 1
r = sec(ws, r, "SELURUH ORANG PRE-TEST DAN POST-TEST (untuk analisis tingkat kelas)", 13)
r = head(ws, r, ["id", "nama", "tes", "benar", "salah", "kosong", "butir_dijawab", "nilai", "ikut_kedua_tes"],
         [5, 28, 12, 9, 9, 9, 14, 9, 16])
pset = {o for o, p, a, b, ta, tb in PAIR}
preset = {p for o, p, a, b, ta, tb in PAIR}
i = 0
for lab, ORG, R, S in (("pre-test", ORANG_PRE, RPRE, preset), ("post-test", ORANG_POST, RPOST, pset)):
    for o in ORG:
        i += 1
        cs = R[o]
        r = row(ws, r, [i, o, lab, cs.count("C"), cs.count("X"), cs.count("-"),
                        20 - cs.count("-"), cs.count("C") * 5, 1 if o in S else 0],
                ctr=(1, 3, 4, 5, 6, 7, 8, 9), h=16, fs=9)
r += 1
r = note(ws, r, "Untuk mengulang uji-t berpasangan: pakai tabel pertama, saring tuntas = 1, "
                "lalu jalankan Paired-Samples T Test pada pasangan variabel pre dan post. "
                "Untuk uji non-parametrik gunakan Wilcoxon Signed-Rank atau uji tanda pada pasangan yang sama.", 13, 26)

wb.save("DATASET_PENELITIAN_CANVA_2026.xlsx")
print("tersimpan: %d lembar, %d grafik" % (len(wb.sheetnames), sum(len(w._charts) for w in wb)))
for w in wb:
    print("  %-26s baris=%4d grafik=%d" % (w.title, w.max_row, len(w._charts)))
