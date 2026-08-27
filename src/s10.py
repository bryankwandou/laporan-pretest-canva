# -*- coding: utf-8 -*-
# ============================================================ 10 DASHBOARD GRAFIK
wsd = wb.create_sheet("10 Data Grafik")
ws = wb.create_sheet("11 Dashboard Grafik")

# ---------- data feed sheet ----------
wsd.sheet_state = "visible"
title(wsd, "DATA PENDUKUNG GRAFIK", "Sheet ini menyimpan angka yang menjadi sumber seluruh grafik pada sheet Dashboard. Boleh diubah; grafik akan mengikuti.", 8)
rr = 4


def block(header, rows, widths):
    global rr
    head(wsd, rr, header, widths)
    rr += 1
    start = rr
    for row in rows:
        for i, v in enumerate(row, 1):
            c = wsd.cell(rr, i, v); c.border = BOX; c.font = Font(size=10)
            if i > 1:
                c.alignment = Alignment(horizontal="center")
        rr += 1
    end = rr - 1
    rr += 2
    return start, end


ORDR = sorted(P, key=lambda n: -sc[n])
UPN, LWN = ORDR[:10], ORDR[-10:]

# 1 akurasi per butir
b1s, b1e = block(["Butir", "Benar", "Salah", "Kosong", "Akurasi (p)"],
                 [["Q%d" % i["no"], i["correct"], i["incorrect"], 37 - i["correct"] - i["incorrect"],
                   round(i["p"], 3)] for i in items], [10, 10, 10, 10, 12])
# 2 daya beda per butir
b2s, b2e = block(["Butir", "Kelompok atas", "Kelompok bawah", "Daya beda D", "r-pbis"],
                 [["Q%d" % i["no"], i["U"], i["L"], round(i["D"], 2), round(i["rpb"], 3)] for i in items],
                 [10, 14, 14, 13, 10])
# 3 distribusi frekuensi
FR = Counter(sc.values())
b3s, b3e = block(["Jumlah benar", "Frekuensi", "Kumulatif %"],
                 [[k, FR.get(k, 0), round(sum(FR.get(j, 0) for j in range(0, k + 1)) / 37, 4)]
                  for k in range(0, 21)], [14, 12, 13])
# 4 ranah
DOMS = defaultdict(list)
for it in items:
    DOMS[DOMAIN[it["no"]]].append(it)
domorder = sorted(DOMS.items(), key=lambda kv: st.mean(i["p"] for i in kv[1]))
b4s, b4e = block(["Ranah materi", "Penguasaan", "Jml butir"],
                 [[d, round(sum(i["correct"] for i in its) / (len(its) * 37), 4), len(its)]
                  for d, its in domorder], [30, 13, 11])
# 5 bloom
BLS = defaultdict(list)
for it in items:
    BLS[BLOOM[it["no"]]].append(it)
b5s, b5e = block(["Level Bloom", "Penguasaan"],
                 [[b, round(sum(i["correct"] for i in BLS[b]) / (len(BLS[b]) * 37), 4)]
                  for b in ["C1 Mengingat", "C2 Memahami", "C3 Menerapkan"]], [20, 13])
# 6 komposisi respons
b6s, b6e = block(["Kategori respons", "Jumlah sel"],
                 [["Benar", 239], ["Salah", 302], ["Kosong / timeout", 199]], [24, 13])
# 7 top 15 peserta
b7s, b7e = block(["Peserta", "Jumlah benar", "Poin Wayground"],
                 [[n, sc[n], sco[n]] for n in ORDR[:15]], [26, 13, 15])
# 8 scatter waktu vs benar
act = [n for n in ORDR if sc[n] > 0]
b8s, b8e = block(["Peserta (aktif)", "Waktu total (detik)", "Jumlah benar"],
                 [[n, tt[n], sc[n]] for n in act], [26, 18, 13])
# 9 waktu per butir vs p
b9s, b9e = block(["Butir", "Waktu rata-rata (detik)", "Akurasi (p)"],
                 [["Q%d" % i["no"], round(st.mean([TIME[n][i["no"]] for n in P if TIME[n].get(i["no"])]), 1),
                   round(i["p"], 3)] for i in items], [10, 20, 12])
# 10 sel kosong per butir
b10s, b10e = block(["Butir", "Sel kosong"],
                   [["Q%d" % i["no"], 37 - i["correct"] - i["incorrect"]] for i in items], [10, 13])
# 11 nilai huruf
b11s, b11e = block(["Nilai huruf", "Jumlah peserta"],
                   [[g, sum(1 for n in P if grade(sc[n] * 5 if True else 0)[0] == g)]
                    for g in ["A", "B", "C", "D", "E"]], [16, 15])
# 12 atas vs bawah per ranah
b12s, b12e = block(["Ranah materi", "Kelompok atas", "Kelompok bawah"],
                   [[d, round(sum(1 for n in UPN for i in its if CORR[n][i["no"] - 1] == "C") / (len(its) * 10), 4),
                     round(sum(1 for n in LWN for i in its if CORR[n][i["no"] - 1] == "C") / (len(its) * 10), 4)]
                    for d, its in domorder], [30, 15, 15])

# ---------- dashboard ----------
title(ws, "DASBOR GRAFIK — DUA BELAS TAMPILAN VISUAL",
      "Seluruh grafik terhubung langsung ke sheet '10 Data Grafik'. Klik grafik untuk mengubah jenis, warna atau label.", 12)
for i in range(1, 13):
    ws.column_dimensions[gcl(i)].width = 13

DN = "'10 Data Grafik'"


def cap(anchor_row, text):
    ws.merge_cells(start_row=anchor_row, start_column=1, end_row=anchor_row, end_column=12)
    c = ws.cell(anchor_row, 1, text)
    c.fill = SUBF; c.font = Font(color="FFFFFF", bold=True, size=10)
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[anchor_row].height = 18


R = 4
# G1 stacked bar composition per question
cap(R, "GRAFIK 1 — Komposisi respons setiap butir: benar, salah, dan tidak dijawab"); R += 1
ch = BarChart(); ch.type = "col"; ch.grouping = "stacked"; ch.overlap = 100
ch.title = "Komposisi Respons per Butir (37 sesi)"
ch.y_axis.title = "Jumlah sesi"; ch.x_axis.title = "Butir soal"
data = Reference(wsd, min_col=2, max_col=4, min_row=b1s - 1, max_row=b1e)
cats = Reference(wsd, min_col=1, min_row=b1s, max_row=b1e)
ch.add_data(data, titles_from_data=True); ch.set_categories(cats)
ch.height = 9; ch.width = 30
ch.series[0].graphicalProperties.solidFill = "63BE7B"
ch.series[1].graphicalProperties.solidFill = "F8696B"
ch.series[2].graphicalProperties.solidFill = "D9D9D9"
ws.add_chart(ch, "A%d" % R); R += 19

# G2 accuracy line
cap(R, "GRAFIK 2 — Tingkat kesukaran (p) setiap butir, diurutkan menurut nomor butir"); R += 1
ch = BarChart(); ch.type = "col"
ch.title = "Tingkat Kesukaran p per Butir"
ch.y_axis.title = "p (proporsi benar)"; ch.x_axis.title = "Butir soal"
data = Reference(wsd, min_col=5, min_row=b1s - 1, max_row=b1e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b1s, max_row=b1e))
ch.series[0].graphicalProperties.solidFill = "2E5C9A"
ch.height = 9; ch.width = 30
ws.add_chart(ch, "A%d" % R); R += 19

# G3 upper vs lower per item
cap(R, "GRAFIK 3 — Kelompok atas versus kelompok bawah pada setiap butir (dasar perhitungan daya beda)"); R += 1
ch = BarChart(); ch.type = "col"; ch.grouping = "clustered"
ch.title = "Jawaban Benar: Kelompok Atas (10) vs Kelompok Bawah (10)"
ch.y_axis.title = "Jumlah benar"; ch.x_axis.title = "Butir soal"
data = Reference(wsd, min_col=2, max_col=3, min_row=b2s - 1, max_row=b2e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b2s, max_row=b2e))
ch.series[0].graphicalProperties.solidFill = "2E5C9A"
ch.series[1].graphicalProperties.solidFill = "F8B4B4"
ch.height = 9; ch.width = 30
ws.add_chart(ch, "A%d" % R); R += 19

# G4 D and rpb line
cap(R, "GRAFIK 4 — Daya beda (D) dan korelasi butir-total (r-pbis). Butir di bawah garis 0,30 perlu ditinjau"); R += 1
ch = LineChart()
ch.title = "Daya Beda dan Korelasi Butir-Total"
ch.y_axis.title = "Nilai koefisien"; ch.x_axis.title = "Butir soal"
data = Reference(wsd, min_col=4, max_col=5, min_row=b2s - 1, max_row=b2e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b2s, max_row=b2e))
for sname in ch.series:
    sname.smooth = False
    sname.marker = Marker(symbol="circle", size=6)
ch.height = 9; ch.width = 30
ws.add_chart(ch, "A%d" % R); R += 19

# G5 histogram
cap(R, "GRAFIK 5 — Histogram distribusi jumlah jawaban benar (37 sesi)"); R += 1
ch = BarChart(); ch.type = "col"; ch.gapWidth = 15
ch.title = "Distribusi Jumlah Jawaban Benar"
ch.y_axis.title = "Jumlah sesi"; ch.x_axis.title = "Jumlah jawaban benar (0-20)"
data = Reference(wsd, min_col=2, min_row=b3s - 1, max_row=b3e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b3s, max_row=b3e))
ch.series[0].graphicalProperties.solidFill = "2E5C9A"
ch.height = 9; ch.width = 22
ws.add_chart(ch, "A%d" % R)

# G6 ogive
ch = LineChart()
ch.title = "Ogive: Persentase Kumulatif"
ch.y_axis.title = "% kumulatif"; ch.x_axis.title = "Jumlah jawaban benar"
data = Reference(wsd, min_col=3, min_row=b3s - 1, max_row=b3e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b3s, max_row=b3e))
ch.series[0].marker = Marker(symbol="circle", size=5)
ch.series[0].smooth = False
ch.height = 9; ch.width = 16
ws.add_chart(ch, "M%d" % R); R += 19

# G7 domain bar
cap(R, "GRAFIK 6 — Penguasaan per ranah materi, diurutkan dari yang terlemah"); R += 1
ch = BarChart(); ch.type = "bar"
ch.title = "Penguasaan per Ranah Materi"
ch.x_axis.title = "Ranah"; ch.y_axis.title = "Proporsi benar"
data = Reference(wsd, min_col=2, min_row=b4s - 1, max_row=b4e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b4s, max_row=b4e))
ch.series[0].graphicalProperties.solidFill = "C55A11"
ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True
ch.height = 9; ch.width = 22
ws.add_chart(ch, "A%d" % R)

# G8 bloom pie
ch = BarChart(); ch.type = "col"
ch.title = "Penguasaan per Level Bloom"
ch.y_axis.title = "Proporsi benar"
data = Reference(wsd, min_col=2, min_row=b5s - 1, max_row=b5e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b5s, max_row=b5e))
ch.series[0].graphicalProperties.solidFill = "548235"
ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True
ch.height = 9; ch.width = 16
ws.add_chart(ch, "M%d" % R); R += 19

# G9 pie composition
cap(R, "GRAFIK 7 — Komposisi seluruh 740 sel data dan sebaran nilai huruf"); R += 1
ch = PieChart()
ch.title = "Komposisi 740 Sel Respons"
data = Reference(wsd, min_col=2, min_row=b6s - 1, max_row=b6e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b6s, max_row=b6e))
ch.dataLabels = DataLabelList(); ch.dataLabels.showPercent = True
ch.height = 9; ch.width = 16
ws.add_chart(ch, "A%d" % R)

ch = PieChart()
ch.title = "Sebaran Nilai Huruf (37 sesi)"
data = Reference(wsd, min_col=2, min_row=b11s - 1, max_row=b11e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b11s, max_row=b11e))
ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True; ch.dataLabels.showPercent = True
ch.height = 9; ch.width = 16
ws.add_chart(ch, "L%d" % R); R += 19

# G11 top15
cap(R, "GRAFIK 8 — Lima belas peserta teratas: jumlah benar dan poin Wayground"); R += 1
ch = BarChart(); ch.type = "bar"
ch.title = "Peringkat 15 Besar - Jumlah Jawaban Benar"
data = Reference(wsd, min_col=2, min_row=b7s - 1, max_row=b7e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b7s, max_row=b7e))
ch.series[0].graphicalProperties.solidFill = "1F3864"
ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True
ch.height = 11; ch.width = 20
ws.add_chart(ch, "A%d" % R)

ch = BarChart(); ch.type = "bar"
ch.title = "Peringkat 15 Besar - Poin Wayground"
data = Reference(wsd, min_col=3, min_row=b7s - 1, max_row=b7e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b7s, max_row=b7e))
ch.series[0].graphicalProperties.solidFill = "BF8F00"
ch.height = 11; ch.width = 20
ws.add_chart(ch, "L%d" % R); R += 23

# G13 scatter time vs correct
cap(R, "GRAFIK 9 — Hubungan waktu total pengerjaan dengan jumlah jawaban benar (33 sesi aktif). Titik yang tersebar acak menandakan tidak ada hubungan"); R += 1
ch = ScatterChart(); ch.style = 13
ch.title = "Waktu Total vs Jumlah Benar"
ch.x_axis.title = "Waktu total (detik)"; ch.y_axis.title = "Jumlah jawaban benar"
xref = Reference(wsd, min_col=2, min_row=b8s, max_row=b8e)
yref = Reference(wsd, min_col=3, min_row=b8s - 1, max_row=b8e)
sser = Series(yref, xref, title_from_data=True)
sser.marker = Marker(symbol="circle", size=8)
sser.graphicalProperties.line.noFill = True
ch.series.append(sser)
ch.height = 11; ch.width = 20
ws.add_chart(ch, "A%d" % R)

# G14 scatter avg time vs p
ch = ScatterChart(); ch.style = 13
ch.title = "Waktu Rata-rata per Butir vs Tingkat Kesukaran"
ch.x_axis.title = "Waktu rata-rata (detik)"; ch.y_axis.title = "p (proporsi benar)"
xref = Reference(wsd, min_col=2, min_row=b9s, max_row=b9e)
yref = Reference(wsd, min_col=3, min_row=b9s - 1, max_row=b9e)
sser = Series(yref, xref, title_from_data=True)
sser.marker = Marker(symbol="diamond", size=8)
sser.graphicalProperties.line.noFill = True
ch.series.append(sser)
ch.height = 11; ch.width = 20
ws.add_chart(ch, "L%d" % R); R += 23

# G15 missing per question
cap(R, "GRAFIK 10 — Sel kosong per butir. Lonjakan di Q1-Q3 adalah bukti peserta bergabung terlambat, bukan bukti soal sulit"); R += 1
ch = BarChart(); ch.type = "col"
ch.title = "Jumlah Sel Kosong / Timeout per Butir"
ch.y_axis.title = "Jumlah sesi"; ch.x_axis.title = "Butir soal"
data = Reference(wsd, min_col=2, min_row=b10s - 1, max_row=b10e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b10s, max_row=b10e))
ch.series[0].graphicalProperties.solidFill = "808080"
ch.height = 9; ch.width = 30
ws.add_chart(ch, "A%d" % R); R += 19

# G16 upper vs lower per domain
cap(R, "GRAFIK 11 — Kesenjangan penguasaan antara kelompok atas dan bawah pada setiap ranah materi"); R += 1
ch = BarChart(); ch.type = "col"; ch.grouping = "clustered"
ch.title = "Penguasaan Ranah: Kelompok Atas vs Kelompok Bawah"
ch.y_axis.title = "Proporsi benar"
data = Reference(wsd, min_col=2, max_col=3, min_row=b12s - 1, max_row=b12e)
ch.add_data(data, titles_from_data=True)
ch.set_categories(Reference(wsd, min_col=1, min_row=b12s, max_row=b12e))
ch.series[0].graphicalProperties.solidFill = "2E5C9A"
ch.series[1].graphicalProperties.solidFill = "F8B4B4"
ch.dataLabels = DataLabelList(); ch.dataLabels.showVal = True
ch.height = 10; ch.width = 30
ws.add_chart(ch, "A%d" % R); R += 21
