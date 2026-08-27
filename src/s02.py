# -*- coding: utf-8 -*-
# ============================================================ 02 DATA PESERTA
ws = wb.create_sheet("02 Data Peserta")
title(ws, "DATA PESERTA LENGKAP — 37 SESI",
      "Diurutkan menurut poin Wayground. Poin Wayground memperhitungkan kecepatan menjawab, sehingga urutannya dapat sedikit berbeda dari urutan jumlah benar. "
      "Kolom Salah dan Kosong dihitung dari matriks respons asli (hijau/merah/abu-abu pada laporan admin). Perlu dicatat: lembar peserta bawaan Wayground menggabungkan butir yang kehabisan waktu ke dalam kolom Salah, sehingga angkanya berbeda dari tabel ini. Tabel ini memisahkan keduanya. Kolom z-skor, T-skor dan peringkat persentil dihitung terhadap 37 sesi. Sesi bertanda * adalah percobaan ulang dengan nama yang sama.", 18)
cols = ["Peringkat\npoin", "Nama Peserta", "Poin\nWayground", "Benar", "Salah", "Kosong /\ntimeout",
        "Dijawab", "Akurasi\n(dari 20)", "Akurasi atas\nyang dijawab", "z-skor", "T-skor",
        "Peringkat\npersentil", "Kelompok\nkuartil", "Nilai\nhuruf", "Predikat", "Waktu total\n(mm:ss)",
        "Waktu total\n(detik)", "Detik per butir\nyang dijawab", "Status sesi"]
head(ws, 4, cols, [8, 26, 12, 8, 8, 10, 9, 11, 13, 9, 9, 11, 11, 8, 15, 12, 11, 15, 30])
r = 5
seen = Counter()
for rank, n in enumerate(RANK, 1):
    b = sc[n]; wrong = CORR[n].count("X"); blank = CORR[n].count("-"); ans = b + wrong
    z = zof(n); T = 50 + 10 * z; pr = prank(n)
    g, lab = grade(b / 20 * 100)
    kq = "Q4 (atas)" if b >= Q3v else ("Q1 (bawah)" if b <= Q1v else ("Q3" if b >= Q2v else "Q2"))
    seen[base(n)] += 1
    stat = []
    if b == 0 and ans == 0:
        stat.append("SESI NOL — tidak ada jawaban terkirim")
    if seen[base(n)] > 1 or sum(1 for m in P if base(m) == base(n)) > 1:
        stat.append("duplikat nama (%dx)" % sum(1 for m in P if base(m) == base(n)))
    if blank >= 10 and ans > 0:
        stat.append("banyak butir tidak terjawab")
    row = [rank, n, sco[n], b, wrong, blank, ans, b / 20, (b / ans if ans else 0), round(z, 2),
           round(T, 1), round(pr, 1), kq, g, lab, "%d:%02d" % (tt[n] // 60, tt[n] % 60), tt[n],
           (round(tt[n] / ans, 1) if ans else ""), "; ".join(stat) or "normal"]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i in (1, 3, 4, 5, 6, 7, 10, 11, 12, 14, 17, 18):
            c.alignment = Alignment(horizontal="center")
    ws.cell(r, 2).font = Font(size=10, bold=True)
    ws.cell(r, 8).number_format = "0.0%"
    ws.cell(r, 9).number_format = "0.0%"
    gc = ws.cell(r, 14)
    gc.fill = {"A": GRN, "B": F("D9EAD3"), "C": YEL, "D": F("FCE4D6"), "E": RED}[g]
    gc.font = Font(size=10, bold=True)
    if b == 0:
        for i in range(1, 20):
            ws.cell(r, i).font = Font(size=10, color="999999", italic=True)
    r += 1
last = r - 1
# summary row
ws.cell(r, 2, "RATA-RATA (37 sesi)").font = Font(bold=True, size=10)
for col, val in [(3, st.mean(sco.values())), (4, mean_s), (5, 302 / 37),
                 (6, 199 / 37), (7, 541 / 37), (8, mean_s / 20), (17, st.mean(tt.values()))]:
    c = ws.cell(r, col, round(val, 2)); c.font = Font(bold=True, size=10); c.fill = F("DCE6F1")
    c.border = BOX; c.alignment = Alignment(horizontal="center")
ws.cell(r, 8).number_format = "0.0%"
for i in range(1, 20):
    ws.cell(r, i).border = BOX
    if not ws.cell(r, i).fill.fgColor.rgb.endswith("DCE6F1"):
        ws.cell(r, i).fill = F("DCE6F1")
ws.conditional_formatting.add("D5:D%d" % last,
                              ColorScaleRule(start_type="num", start_value=0, start_color="F8696B",
                                             mid_type="num", mid_value=7, mid_color="FFEB84",
                                             end_type="num", end_value=14, end_color="63BE7B"))
ws.conditional_formatting.add("C5:C%d" % last,
                              ColorScaleRule(start_type="min", start_color="FFFFFF",
                                             end_type="max", end_color="8EA9DB"))
ws.freeze_panes = "C5"
ws.auto_filter.ref = "A4:S%d" % last

r += 2
secrow(ws, r, "CATATAN INTEGRITAS DATA", 19); r += 1
for t in [
    "Empat sesi (Aqifah, Yofita, Sri Suyani, Sri Suyani*) mencatat 0 poin, 0 benar dan 0 jawaban terkirim. Ketiganya juga mencatat waktu total 0-30 detik. Ini bukan hasil ujian, melainkan sesi yang gagal masuk atau ditinggalkan seketika. Sesi-sesi ini menekan rata-rata kelas sekitar 0,78 butir.",
    "Tiga nama muncul lebih dari sekali: Sri Suyani (3 sesi: 9, 0 dan 0 benar), Aqifah (2 sesi: 7 dan 0 benar), farida johannes (2 sesi: 5 dan 4 benar). Untuk analisis tingkat individu, gunakan hanya sesi terbaik tiap nama; untuk analisis butir, seluruh 37 sesi tetap dipakai karena setiap respons adalah data valid tentang butir tersebut.",
    "Katrina mengirim 14 jawaban lalu berhenti; farida johannes* hanya bertahan 40 detik. Pola berhenti di tengah ini menjelaskan sebagian besar dari 199 sel kosong.",
    "Peringkat pada kolom pertama mengikuti poin Wayground yang memberi bonus kecepatan. Contoh: Yovita berada di peringkat 5 dengan 10 benar, sedangkan Gerarda Ina di peringkat 6 dengan 12 benar. Untuk penilaian akademik gunakan kolom Benar, bukan kolom Poin.",
]:
    note(ws, r, t, 19, 40); r += 1
