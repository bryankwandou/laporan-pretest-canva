# -*- coding: utf-8 -*-
# ============================================================ 03 MATRIKS RESPONS
ws = wb.create_sheet("03 Matriks Respons")
title(ws, "MATRIKS RESPONS 37 SESI × 20 BUTIR",
      "B = benar (hijau) · S = salah (merah) · titik = tidak dijawab / kehabisan waktu (abu-abu). "
      "Baris diurutkan dari skor tertinggi ke terendah, kolom dari butir 1 sampai 20. "
      "Blok abu-abu di sudut kiri atas menunjukkan peserta yang bergabung terlambat; blok abu-abu di sisi kanan bawah menunjukkan peserta yang menyerah di tengah jalan.", 26)
cols = ["#", "Nama"] + ["Q%d" % i for i in range(1, 21)] + ["B", "S", ".", "%"]
head(ws, 4, cols, [5, 24] + [4] * 20 + [6, 6, 6, 8])
ORD = sorted(P, key=lambda n: (-sc[n], -sco[n]))
r = 5
for idx, n in enumerate(ORD, 1):
    ws.cell(r, 1, idx).border = BOX
    c = ws.cell(r, 2, n); c.font = Font(size=10, bold=True); c.border = BOX
    for qi in range(20):
        s_ = CORR[n][qi]
        v = {"C": "B", "X": "S", "-": "·"}[s_]
        cell = ws.cell(r, 3 + qi, v)
        cell.fill = {"C": GRN, "X": RED, "-": F("EDEDED")}[s_]
        cell.font = Font(size=9, bold=True, color={"C": "006100", "X": "9C0006", "-": "AAAAAA"}[s_])
        cell.alignment = Alignment(horizontal="center"); cell.border = BOX
    b = sc[n]; w = CORR[n].count("X"); u = CORR[n].count("-")
    for i, v in zip((23, 24, 25), (b, w, u)):
        cc = ws.cell(r, i, v); cc.alignment = Alignment(horizontal="center"); cc.border = BOX
        cc.font = Font(size=10, bold=True)
    cc = ws.cell(r, 26, b / 20); cc.number_format = "0%"; cc.border = BOX
    cc.alignment = Alignment(horizontal="center"); cc.font = Font(size=10, bold=True)
    r += 1
last = r - 1
# footer per question
ws.cell(r, 2, "Jumlah BENAR per butir").font = Font(bold=True, size=10)
ws.cell(r + 1, 2, "Jumlah SALAH per butir").font = Font(bold=True, size=10)
ws.cell(r + 2, 2, "Jumlah KOSONG per butir").font = Font(bold=True, size=10)
ws.cell(r + 3, 2, "Tingkat kesukaran p").font = Font(bold=True, size=10)
for qi in range(20):
    cB = sum(1 for n in P if CORR[n][qi] == "C")
    cX = sum(1 for n in P if CORR[n][qi] == "X")
    cU = sum(1 for n in P if CORR[n][qi] == "-")
    for off, v, fl in ((0, cB, GRN), (1, cX, RED), (2, cU, F("EDEDED"))):
        c = ws.cell(r + off, 3 + qi, v); c.fill = fl; c.border = BOX
        c.alignment = Alignment(horizontal="center"); c.font = Font(size=9, bold=True)
    c = ws.cell(r + 3, 3 + qi, cB / 37); c.number_format = "0.00"; c.border = BOX
    c.alignment = Alignment(horizontal="center"); c.font = Font(size=8, bold=True)
for off, tot in ((0, 239), (1, 302), (2, 199)):
    c = ws.cell(r + off, 23, tot); c.font = Font(bold=True); c.border = BOX
    c.alignment = Alignment(horizontal="center")
    for i in (1, 2):
        ws.cell(r + off, i).border = BOX
ws.freeze_panes = "C5"

r += 6
secrow(ws, r, "CARA MEMBACA MATRIKS INI", 26); r += 1
for t in [
    "Kolom Q1 hampir seluruhnya abu-abu (23 dari 37 sel). Ini bukan karena butir 1 sulit, melainkan karena butir 1 sudah lewat sebelum sebagian besar peserta berhasil masuk ke sesi live. Hal yang sama berlaku lebih ringan untuk Q2 dan Q3.",
    "Empat baris paling bawah seluruhnya abu-abu penuh: sesi yang tidak pernah benar-benar berjalan. Menyertakan baris ini dalam rata-rata kelas menurunkan akurasi resmi dari 36,2% menjadi 32,3%.",
    "Baris Katrina, Ivonne dan Clementinus Relipurnawan menunjukkan pola abu-abu yang menumpuk di sisi kanan: mereka mulai mengikuti, lalu berhenti sebelum kuis selesai. Pola ini penting untuk desain sesi berikutnya - beri jeda dan pastikan semua peserta sudah masuk sebelum butir pertama ditampilkan.",
    "Kolom Q20 menunjukkan blok hijau paling tebal (22 benar) padahal 13 sel kosong. Artinya di antara mereka yang masih bertahan sampai akhir, hampir semua menjawab benar. Butir terakhir bukan butir tersulit.",
    "Dua peserta terbaik sama-sama salah pada Q10 (asal-usul Canva), Q17 (slogan pelatihan) dan Q19 (nilai Berkarya dengan Hati). Bila peserta paling kuat pun gagal di tiga butir yang sama, itu bukan indikator kemampuan individu melainkan tanda materinya memang belum pernah tersampaikan.",
]:
    note(ws, r, t, 26, 34); r += 1
