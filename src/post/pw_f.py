# -*- coding: utf-8 -*-
# ============ 05 BUTIR POST
ws = wb.create_sheet("05 Analisis Butir Post")
title(ws, "ANALISIS BUTIR POST-TEST",
      "n = 15 sesi (Vincent dikeluarkan). Kelompok atas dan bawah masing-masing 4 sesi (27% dari 15). "
      "Kunci jawaban diverifikasi terhadap naskah PDF resmi: cocok pada 20 dari 20 butir.", 11)
r = 4
head(ws, r, ["Butir", "Pokok yang diuji", "Kunci (huruf pada naskah)", "Benar", "Salah", "Kosong",
             "p", "Kategori", "D", "r-pbis", "Keputusan"],
     [7, 46, 46, 8, 8, 8, 8, 11, 8, 9, 30])
r += 1
b0 = r
LET = {}
for n in range(1, 21):
    key = QO[n]["key"]
    from difflib import SequenceMatcher as SM
    import re as _re
    best = max(OPT[n]["opts"], key=lambda o: SM(None, _re.sub(r"[^a-z0-9]", "", o[1].lower()),
                                                _re.sub(r"[^a-z0-9]", "", key.lower())).ratio())
    LET[n] = best[0]
SHORTP = {1: "Kolaborasi real-time", 2: "Asal usul Canva (Fusion Books)", 3: "Brand Kit",
          4: "Hierarki visual — yang bertentangan", 5: "Harga paket Pro", 6: "Format ekspor PNG",
          7: "Pernyataan benar tentang Canva", 8: "Makna warna ungu liturgi", 9: "Format ekspor MP4",
          10: "Batas jumlah warna dan font", 11: "Menu panel kiri", 12: "Tiga pendiri Canva",
          13: "Eyedropper", 14: "Ukuran Instagram Feed", 15: "Empat nilai berkarya",
          16: "Urutan langkah template", 17: "Komentar pada elemen", 18: "Etika AI",
          19: "Skema warna monokromatik", 20: "Esensi tujuan pelatihan"}
for q in sorted(post["Q"], key=lambda x: x["no"]):
    n = q["no"]; p = q["p"]; d = q["D"]; rp = q["rpb"]
    kat = "Sukar" if p < .30 else ("Sedang" if p <= .70 else "Mudah")
    if d < .20 or rp < .20:
        dec = "Buang / tulis ulang"
    elif d >= .40 and .30 <= p <= .70:
        dec = "Unggulan"
    elif d >= .30:
        dec = "Pertahankan"
    else:
        dec = "Revisi opsi"
    putrow(ws, r, [n, SHORTP[n], "%s)  %s" % (LET[n], q["key"]), q["correct_excl"], q["incorrect_excl"],
                   q["unatt_excl"], round(p, 2), kat, round(d, 2), round(rp, 2), dec],
           ctr=(1, 4, 5, 6, 7, 8, 9, 10), bold=(1, 7), h=26)
    ws.cell(r, 1).fill = HDR; ws.cell(r, 1).font = Font(size=11, bold=True, color="FFFFFF")
    ws.cell(r, 8).fill = {"Sukar": RED, "Sedang": YEL, "Mudah": GRN}[kat]
    ws.cell(r, 9).fill = GRN if d >= .40 else (BLU if d >= .30 else (YEL if d >= .20 else RED))
    ws.cell(r, 11).fill = RED if dec.startswith("Buang") else (GRN if dec == "Unggulan" else GRY)
    ws.cell(r, 3).font = Font(size=9)
    r += 1
b1 = r - 1
ws.freeze_panes = "B%d" % b0
r += 1

ch = BarChart(); ch.type = "col"; ch.style = 10
ch.title = "Tingkat kesukaran (p) per butir post-test"
ch.y_axis.title = "Proporsi benar"; ch.height = 9; ch.width = 26
ch.add_data(Reference(ws, min_col=7, min_row=b0 - 1, max_row=b1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=b0, max_row=b1))
ch.dLbls = DataLabelList(); ch.dLbls.showVal = True
ch.legend = None
ws.add_chart(ch, "A%d" % r)

ch2 = LineChart(); ch2.style = 12
ch2.title = "Daya beda (D) dan korelasi butir-total (r-pbis) per butir"
ch2.y_axis.title = "Nilai"; ch2.height = 9; ch2.width = 26
ch2.add_data(Reference(ws, min_col=9, max_col=10, min_row=b0 - 1, max_row=b1), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=1, min_row=b0, max_row=b1))
ws.add_chart(ch2, "A%d" % (r + 19))

ch3 = BarChart(); ch3.type = "col"; ch3.grouping = "stacked"; ch3.overlap = 100; ch3.style = 12
ch3.title = "Komposisi respons per butir: benar, salah, tidak dijawab"
ch3.height = 9; ch3.width = 26
ch3.add_data(Reference(ws, min_col=4, max_col=6, min_row=b0 - 1, max_row=b1), titles_from_data=True)
ch3.set_categories(Reference(ws, min_col=1, min_row=b0, max_row=b1))
ws.add_chart(ch3, "A%d" % (r + 38))
r += 58

for t in [
    "Seluruh 20 butir masuk kategori Sukar atau Sedang; tidak ada butir yang terlalu mudah. Rata-rata p = %.2f." % st.mean(q["p"] for q in post["Q"]),
    "Daya beda post-test sangat tinggi — sepuluh butir mencapai D = 1,00. Angka ini harus dibaca dengan hati-hati: dengan kelompok atas dan bawah masing-masing hanya 4 sesi, dan dengan sebagian sesi bawah tidak menjawab sama sekali, nilai D = 1,00 lebih mencerminkan perbedaan siapa yang menyelesaikan tes daripada perbedaan penguasaan materi.",
    "Q17 (komentar pada elemen desain) adalah butir tersukar dengan p=0,13 — hanya 2 dari 15 peserta benar, dan 8 memilih 'Download desain lalu kirim via email'. Ini miskonsepsi yang bertahan setelah pelatihan dan layak dibahas ulang secara khusus.",
    "Q2 memiliki r-pbis terendah (0,20) dan D terendah (0,25) meski butirnya identik dengan pre-test. Enam peserta salah, tersebar merata di kelompok atas maupun bawah — pola khas butir hafalan murni yang tidak berkaitan dengan penguasaan keseluruhan.",
]:
    note(ws, r, t, 11, 44); r += 1
