# -*- coding: utf-8 -*-
# ============================================================ 09 SEGMENTASI
ws = wb.create_sheet("09 Segmentasi Peserta")
title(ws, "SEGMENTASI PESERTA DAN ANALISIS KESENJANGAN KELOMPOK ATAS VERSUS BAWAH",
      "Kelompok atas = 10 sesi dengan jawaban benar terbanyak. Kelompok bawah = 10 sesi terendah. "
      "Kolom selisih menunjukkan butir mana yang paling memisahkan keduanya - itulah materi yang membedakan orang yang sudah tahu dari yang belum.", 12)

ORDR = sorted(P, key=lambda n: -sc[n])
UPN, LWN = ORDR[:10], ORDR[-10:]
MID = ORDR[10:-10]

r = 4
secrow(ws, r, "A. EMPAT SEGMEN PESERTA DAN PERLAKUAN YANG DISARANKAN", 12); r += 1
head(ws, r, ["Segmen", "Kriteria", "Jml", "%", "Rata-rata\nbenar", "Rentang", "Anggota",
             "Perlakuan yang disarankan", "", "", "", ""],
     [22, 20, 6, 8, 11, 10, 56, 74])
r += 1
SEG = [
    ("SIAP JADI ASISTEN", "12 benar ke atas", lambda n: sc[n] >= 12,
     "Sudah mengenal Canva. Jadikan pendamping meja saat sesi praktik; beri tugas tambahan membuat template komunitas."),
    ("SIAP IKUT PENUH", "8–11 benar", lambda n: 8 <= sc[n] <= 11,
     "Fondasi cukup. Bisa mengikuti kecepatan normal. Fokuskan pada praktik ekspor dan ukuran kanvas."),
    ("PERLU PENDAMPINGAN", "1–7 benar", lambda n: 1 <= sc[n] <= 7,
     "Kelompok terbesar. Butuh langkah demi langkah di layar besar, jangan hanya instruksi lisan. Pastikan setiap orang berhasil membuat satu desain utuh sebelum lanjut."),
    ("SESI TIDAK VALID", "0 benar, 0 jawaban terkirim", lambda n: sc[n] == 0,
     "Bukan indikator kemampuan. Hubungi kembali, pastikan perangkat dan koneksi siap sebelum hari pelatihan."),
]
for name, krit, fn, act in SEG:
    who = [n for n in ORDR if fn(n)]
    v = [sc[n] for n in who]
    row = [name, krit, len(who), len(who) / 37, round(st.mean(v), 2) if v else 0,
           "%d–%d" % (min(v), max(v)) if v else "-", ", ".join(who), act]
    for i, x in enumerate(row, 1):
        c = ws.cell(r, i, x); c.border = BOX; c.font = Font(size=10)
        if i in (3, 4, 5, 6):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=12)
    ws.cell(r, 4).number_format = "0.0%"
    ws.cell(r, 1).font = Font(size=10, bold=True)
    ws.cell(r, 1).fill = {"SIAP JADI ASISTEN": GRN, "SIAP IKUT PENUH": F("D9EAD3"),
                          "PERLU PENDAMPINGAN": YEL, "SESI TIDAK VALID": F("EDEDED")}[name]
    ws.row_dimensions[r].height = 56
    r += 1
r += 2

secrow(ws, r, "B. KESENJANGAN PER BUTIR: KELOMPOK ATAS (10) VERSUS KELOMPOK BAWAH (10)", 12); r += 1
head(ws, r, ["Butir", "Pokok yang diuji", "Ranah", "Atas\nbenar", "Atas %", "Bawah\nbenar",
             "Bawah %", "Selisih\n(D)", "Kelompok\ntengah (17)", "Tengah %", "Tafsiran", ""],
     [7, 34, 24, 8, 9, 9, 9, 9, 12, 10, 66])
r += 1
grow0 = r
for it in sorted(items, key=lambda i: -i["D"]):
    no = it["no"]
    u = it["U"]; l = it["L"]
    m = sum(1 for n in MID if CORR[n][no - 1] == "C")
    if it["D"] >= .60:
        taf = "Pembeda paling tajam. Materi ini yang benar-benar memisahkan yang tahu dari yang tidak."
    elif it["D"] >= .40:
        taf = "Pembeda kuat dan sehat."
    elif it["D"] >= .30:
        taf = "Pembeda memadai."
    elif it["D"] > 0:
        taf = "Pembeda lemah - redaksi opsi perlu dipertajam."
    else:
        taf = "Tidak membedakan sama sekali. Butir gagal."
    row = [no, SHORT[no], DOMAIN[no], u, u / 10, l, l / 10, round(it["D"], 2), m,
           m / len(MID), taf]
    for i, x in enumerate(row, 1):
        c = ws.cell(r, i, x); c.border = BOX; c.font = Font(size=10)
        if i not in (2, 3, 11):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=11, end_row=r, end_column=12)
    for cc in (5, 7, 10):
        ws.cell(r, cc).number_format = "0%"
    ws.cell(r, 8).fill = F(dcat(it["D"])[1])
    ws.cell(r, 8).font = Font(size=10, bold=True)
    ws.row_dimensions[r].height = 24
    r += 1
grow1 = r - 1
r += 2

secrow(ws, r, "C. PROFIL DUA KELOMPOK", 12); r += 1
head(ws, r, ["Indikator", "Kelompok atas (10)", "Kelompok tengah (17)", "Kelompok bawah (10)",
             "Selisih atas−bawah", "", "", "", "", "", "", ""], [34, 22, 22, 22, 20])
r += 1


def prof(lst, f):
    return f([x for x in lst])


ROWS = [
    ("Rata-rata jawaban benar", lambda L: round(st.mean(sc[n] for n in L), 2)),
    ("Rata-rata poin Wayground", lambda L: round(st.mean(sco[n] for n in L))),
    ("Rata-rata jawaban terkirim", lambda L: round(st.mean(20 - CORR[n].count("-") for n in L), 1)),
    ("Rata-rata sel kosong", lambda L: round(st.mean(CORR[n].count("-") for n in L), 1)),
    ("Akurasi atas yang dijawab", lambda L: "%.1f%%" % (sum(sc[n] for n in L) / max(1, sum(20 - CORR[n].count("-") for n in L)) * 100)),
    ("Rata-rata waktu total (detik)", lambda L: round(st.mean(tt[n] for n in L))),
    ("Rata-rata detik per butir dijawab", lambda L: round(st.mean([tt[n] / max(1, 20 - CORR[n].count("-")) for n in L]), 1)),
]
for lab, fn in ROWS:
    a, m, b = fn(UPN), fn(MID), fn(LWN)
    ws.cell(r, 1, lab).font = Font(size=10, bold=True)
    for i, v in zip((2, 3, 4), (a, m, b)):
        c = ws.cell(r, i, v); c.alignment = Alignment(horizontal="center"); c.font = Font(size=10)
    try:
        d = round(float(str(a).rstrip("%")) - float(str(b).rstrip("%")), 2)
    except Exception:
        d = ""
    c = ws.cell(r, 5, d); c.alignment = Alignment(horizontal="center")
    c.font = Font(size=10, bold=True, color=NAVY)
    for i in range(1, 6):
        ws.cell(r, i).border = BOX
    r += 1
r += 2

for t in [
    "Kesenjangan terbesar ada pada Q20 (selisih 0,90), Q2 (0,70) dan Q5 (0,70). Ketiganya menuntut membaca teliti dan membandingkan pernyataan, bukan menghafal. Peserta kelompok atas unggul karena terbiasa membaca cermat, bukan karena lebih banyak tahu tentang Canva.",
    "Kelompok atas mengirim rata-rata 18,6 jawaban, kelompok bawah hanya 6,6 - selisih 12 butir. Sementara selisih jawaban benar hanya 9,4 butir. Artinya seluruh kesenjangan skor dapat dijelaskan oleh perbedaan jumlah butir yang sempat dijawab, bukan oleh perbedaan ketepatan. Hambatan utamanya teknis, bukan kognitif.",
    "Kelompok tengah (17 sesi) sangat rapat: sebagian besar berada di 5 sampai 8 jawaban benar. Untuk pelatihan, ketiga segmen ini praktis dapat diperlakukan sebagai satu kelas homogen, dengan tiga orang teratas dijadikan pendamping meja.",
    "Q17 adalah satu-satunya butir dengan selisih nol: kelompok atas maupun bawah sama-sama tidak ada yang benar. Butir seperti ini tidak boleh masuk dalam penilaian karena tidak menyumbang informasi apa pun.",
]:
    note(ws, r, t, 12, 40); r += 1
