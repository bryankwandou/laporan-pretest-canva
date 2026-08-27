# -*- coding: utf-8 -*-
# ============================================================ 04 ANALISIS BUTIR
ws = wb.create_sheet("04 Analisis Butir")
title(ws, "ANALISIS BUTIR SOAL (ITEM ANALYSIS) — 20 BUTIR",
      "Tingkat kesukaran p = jumlah benar / 37. Daya beda D = (benar kelompok atas − benar kelompok bawah) / 10, memakai batas 27% atas dan 27% bawah (10 sesi tiap kelompok). "
      "r-pbis adalah korelasi point-biserial antara butir dan skor total, ukuran seberapa selaras butir dengan tes secara keseluruhan. "
      "Pengecoh efektif dihitung dari opsi salah yang dipilih minimal 5% penjawab.", 16)
cols = ["Butir", "Pokok yang diuji", "Ranah materi", "Level\nBloom", "Benar", "Salah", "Kosong",
        "Penjawab", "p\n(kesukaran)", "Kategori\nkesukaran", "Atas\n(n=10)", "Bawah\n(n=10)",
        "D\n(daya beda)", "Kategori\ndaya beda", "r-pbis", "Pengecoh\nefektif",
        "Waktu rata-rata\n(detik)", "Keputusan"]
head(ws, 4, cols, [7, 34, 24, 13, 7, 7, 8, 10, 11, 12, 8, 8, 11, 15, 9, 10, 13, 40])
r = 5
for it in items:
    no = it["no"]
    resp = it["correct"] + it["incorrect"]
    pc, pcol = pcat(it["p"])
    dc, dcol = dcat(it["D"])
    if it["D"] < .20 or it["rpb"] < .20:
        dec = "BUANG atau tulis ulang total"
    elif it["p"] < .20:
        dec = "Pertahankan; materi prioritas pelatihan"
    elif it["D"] >= .40 and .30 <= it["p"] <= .70:
        dec = "Butir unggulan — pakai lagi apa adanya"
    else:
        dec = "Layak pakai; perbaiki redaksi pengecoh"
    avgt = st.mean([TIME[n][no] for n in P if TIME[n].get(no)])
    row = [no, SHORT[no], DOMAIN[no], BLOOM[no], it["correct"], it["incorrect"], 37 - resp, resp,
           round(it["p"], 3), pc, it["U"], it["L"], round(it["D"], 2), dc, round(it["rpb"], 3),
           it["eff_distr"], round(avgt, 1), dec]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i not in (2, 3, 18):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 1).font = Font(size=10, bold=True)
    ws.cell(r, 10).fill = F(pcol)
    ws.cell(r, 14).fill = F(dcol)
    if it["rpb"] < .20:
        ws.cell(r, 15).fill = RED; ws.cell(r, 15).font = Font(size=10, bold=True, color="9C0006")
    if dec.startswith("BUANG"):
        ws.cell(r, 18).fill = RED; ws.cell(r, 18).font = Font(size=10, bold=True, color="9C0006")
    elif dec.startswith("Butir unggulan"):
        ws.cell(r, 18).fill = GRN
    ws.row_dimensions[r].height = 26
    r += 1
last = r - 1
ws.cell(r, 2, "RATA-RATA / TOTAL").font = Font(bold=True)
for col, v in [(5, 239), (6, 302), (7, 199), (8, 541 / 20), (9, st.mean(i["p"] for i in items)),
               (11, st.mean(i["U"] for i in items)), (12, st.mean(i["L"] for i in items)),
               (13, st.mean(i["D"] for i in items)), (15, st.mean(i["rpb"] for i in items)),
               (17, st.mean([v for n in TIME for v in TIME[n].values() if v]))]:
    c = ws.cell(r, col, round(v, 3)); c.font = Font(bold=True); c.alignment = Alignment(horizontal="center")
for i in range(1, 19):
    ws.cell(r, i).border = BOX; ws.cell(r, i).fill = F("DCE6F1")
ws.freeze_panes = "C5"
ws.auto_filter.ref = "A4:R%d" % last

r += 2
secrow(ws, r, "RINGKASAN MUTU INSTRUMEN", 18); r += 1
head(ws, r, ["Kriteria", "Jumlah butir", "Persentase", "Daftar butir", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
r += 1
CRIT = [
    ("Sukar (p < 0,30)", [i["no"] for i in items if i["p"] < .30]),
    ("Sedang (0,30 ≤ p ≤ 0,70)", [i["no"] for i in items if .30 <= i["p"] <= .70]),
    ("Mudah (p > 0,70)", [i["no"] for i in items if i["p"] > .70]),
    ("Daya beda sangat baik (D ≥ 0,40)", [i["no"] for i in items if i["D"] >= .40]),
    ("Daya beda baik (0,30 ≤ D < 0,40)", [i["no"] for i in items if .30 <= i["D"] < .40]),
    ("Daya beda lemah / ditolak (D < 0,30)", [i["no"] for i in items if i["D"] < .30]),
    ("Korelasi butir-total memadai (r ≥ 0,30)", [i["no"] for i in items if i["rpb"] >= .30]),
    ("Korelasi butir-total bermasalah (r < 0,30)", [i["no"] for i in items if i["rpb"] < .30]),
    ("Seluruh pengecoh berfungsi (3 pengecoh efektif)", [i["no"] for i in items if i["eff_distr"] == 3]),
    ("Ada pengecoh mati (kurang dari 3 efektif)", [i["no"] for i in items if i["eff_distr"] < 3]),
]
for k, lst in CRIT:
    ws.cell(r, 1, k).font = Font(size=10, bold=True)
    c = ws.cell(r, 2, len(lst)); c.alignment = Alignment(horizontal="center"); c.font = Font(bold=True)
    c = ws.cell(r, 3, len(lst) / 20); c.number_format = "0%"; c.alignment = Alignment(horizontal="center")
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=10)
    c = ws.cell(r, 4, ", ".join("Q%d" % x for x in lst) or "tidak ada")
    c.font = Font(size=10); c.alignment = Alignment(vertical="center")
    for i in range(1, 11):
        ws.cell(r, i).border = BOX
    r += 1

r += 1
secrow(ws, r, "BACAAN ATAS ANALISIS BUTIR", 18); r += 1
for t in [
    "Tidak ada satu pun butir yang tergolong mudah. Sembilan butir tergolong sukar dan sebelas butir sedang. Untuk sebuah pre-test, komposisi ini justru ideal: tes berhasil memotret ketidaktahuan tanpa membuat peserta menyerah seluruhnya.",
    "Rata-rata daya beda 0,470 tergolong sangat baik. Artinya butir-butir ini konsisten memisahkan peserta yang tahu dari yang tidak tahu. Kombinasi kesukaran tinggi dengan daya beda tinggi adalah tanda instrumen yang sehat, bukan instrumen yang terlalu sulit.",
    "Hanya satu butir yang gagal: Q17 dengan D = 0,00 dan r-pbis = -0,01. Nol dari sepuluh peserta kelompok atas DAN nol dari sepuluh kelompok bawah menjawabnya benar. Butir ini menguji hafalan slogan yang belum pernah disampaikan kepada siapa pun, sehingga tidak mengukur apa-apa.",
    "Q11 (r-pbis 0,28) dan Q19 (r-pbis 0,29) berada tepat di bawah ambang 0,30 dan perlu diperbaiki redaksinya. Pada Q11 sebelas peserta memilih 'ruang kosong sebaiknya diisi agar terlihat penuh' - miskonsepsi yang sangat umum dan justru layak dijadikan bahan diskusi di kelas.",
    "Q20 memiliki pengecoh mati: tiga opsi salah hanya dipilih total 4 kali dari 26 penjawab, sedangkan kunci dipilih 22 kali. Butir ini terlalu mudah ditebak karena hanya satu opsi yang terdengar akademis. Bila dipakai lagi, buat keempat opsi sama-sama masuk akal.",
    "Q1 dan Q3 punya penjawab paling sedikit (14 dan 20 dari 37) sehingga statistik keduanya paling rapuh. Perlakukan angka p pada dua butir ini sebagai perkiraan kasar, bukan sebagai ukuran pasti.",
]:
    note(ws, r, t, 18, 34); r += 1
