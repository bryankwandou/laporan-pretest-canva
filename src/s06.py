# -*- coding: utf-8 -*-
# ============================================================ 06 DISTRIBUSI
ws = wb.create_sheet("06 Distribusi Skor")
title(ws, "DISTRIBUSI SKOR, FREKUENSI DAN NORMA KELAS",
      "Tabel frekuensi tunggal, tabel kelompok, ogive kumulatif, tabel norma nilai huruf, dan uji kenormalan sederhana. "
      "Semua dihitung atas 37 sesi kecuali disebut lain.", 8)

# --- frekuensi tunggal
r = 4
secrow(ws, r, "A. TABEL FREKUENSI TUNGGAL (jumlah benar 0–20)", 8); r += 1
head(ws, r, ["Jumlah\nbenar", "Nilai\n(0–100)", "Frekuensi", "Frekuensi\nrelatif",
             "Frek. kumulatif\nkurang dari", "Frek. kumulatif\nlebih dari",
             "Persentase\nkumulatif", "Nama peserta"], [9, 9, 10, 11, 15, 15, 12, 82])
r += 1
FR = Counter(sc.values())
cum = 0
frow0 = r
for k in range(0, 21):
    f = FR.get(k, 0)
    cum += f
    nm = ", ".join(sorted([n for n in P if sc[n] == k], key=lambda n: -sco[n]))
    row = [k, k * 5, f, f / 37 if f else 0, cum, 37 - cum + f, cum / 37, nm]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i != 8:
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 4).number_format = "0.0%"
    ws.cell(r, 7).number_format = "0.0%"
    if f:
        ws.cell(r, 3).fill = F("BDD7EE"); ws.cell(r, 3).font = Font(bold=True, size=10)
    ws.row_dimensions[r].height = 20
    r += 1
frow1 = r - 1
ws.cell(r, 1, "Σ").font = Font(bold=True)
ws.cell(r, 3, 37).font = Font(bold=True)
ws.cell(r, 4, 1.0).number_format = "0%"
for i in range(1, 9):
    ws.cell(r, i).border = BOX; ws.cell(r, i).fill = F("DCE6F1")
r += 2

# --- kelompok
secrow(ws, r, "B. TABEL DISTRIBUSI BERKELOMPOK (interval 4 butir)", 8); r += 1
head(ws, r, ["Interval\n(benar)", "Interval\nnilai", "Titik\ntengah", "Frekuensi",
             "Frek.\nrelatif", "Frek.\nkumulatif", "Kategori", "Tafsiran"],
     [12, 12, 9, 10, 10, 11, 16, 82])
r += 1
grow0 = r
BINS = [(0, 3, "Sangat Kurang", "Praktis tidak memiliki pengetahuan awal; setara atau di bawah tebakan acak"),
        (4, 7, "Kurang", "Mengenal istilah tetapi belum memahami fungsi; kelompok terbesar"),
        (8, 11, "Cukup", "Sudah memiliki dasar; siap menerima materi lanjutan lebih cepat"),
        (12, 15, "Baik", "Kemungkinan pernah memakai Canva sebelumnya; calon asisten sebaya"),
        (16, 20, "Sangat Baik", "Tidak ada peserta pada kelompok ini")]
cum = 0
for lo, hi, cat, taf in BINS:
    f = sum(1 for x in sc.values() if lo <= x <= hi)
    cum += f
    row = ["%d–%d" % (lo, hi), "%d–%d" % (lo * 5, hi * 5), (lo + hi) / 2, f, f / 37, cum, cat, taf]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i != 8:
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 5).number_format = "0.0%"
    ws.cell(r, 7).fill = {"Sangat Kurang": RED, "Kurang": F("FCE4D6"), "Cukup": YEL,
                          "Baik": F("D9EAD3"), "Sangat Baik": GRN}[cat]
    ws.row_dimensions[r].height = 22
    r += 1
grow1 = r - 1
r += 1

# --- norma
secrow(ws, r, "C. NORMA NILAI HURUF DAN KETUNTASAN", 8); r += 1
head(ws, r, ["Nilai\nhuruf", "Rentang nilai", "Rentang\nbenar", "Frekuensi", "Persentase",
             "Kumulatif", "Predikat", "Nama peserta"], [8, 14, 12, 10, 11, 11, 16, 82])
r += 1
nrow0 = r
cum = 0
for g, lo, hi, lab in [("A", 85, 100, "Sangat Baik"), ("B", 70, 84, "Baik"), ("C", 55, 69, "Cukup"),
                       ("D", 40, 54, "Kurang"), ("E", 0, 39, "Sangat Kurang")]:
    who = [n for n in P if lo <= sc[n] * 5 <= hi]
    f = len(who); cum += f
    row = [g, "%d–%d" % (lo, hi), "%d–%d" % (math.ceil(lo / 5), hi // 5), f, f / 37, cum, lab,
           ", ".join(sorted(who, key=lambda n: -sc[n]))]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i != 8:
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 5).number_format = "0.0%"
    ws.cell(r, 1).fill = {"A": GRN, "B": F("D9EAD3"), "C": YEL, "D": F("FCE4D6"), "E": RED}[g]
    ws.cell(r, 1).font = Font(bold=True, size=12)
    ws.row_dimensions[r].height = 30
    r += 1
nrow1 = r - 1
r += 1

# --- ukuran posisi
secrow(ws, r, "D. UKURAN POSISI DAN PENYEBARAN", 8); r += 1
head(ws, r, ["Ukuran", "Nilai (benar)", "Nilai (0–100)", "Keterangan", "", "", "", ""], [26, 14, 14, 90])
r += 1
srtv = sorted(sc.values())


def perc(p):
    i = (len(srtv) - 1) * p
    lo = int(i); hi = min(lo + 1, len(srtv) - 1)
    return srtv[lo] + (srtv[hi] - srtv[lo]) * (i - lo)


POS = [("Minimum", srtv[0], "sesi yang tidak menjawab sama sekali"),
       ("Desil 1 (P10)", perc(.10), "10% peserta berada di bawah nilai ini"),
       ("Kuartil 1 (P25)", perc(.25), "batas kelompok bawah"),
       ("Desil 3 (P30)", perc(.30), ""),
       ("Median (P50)", perc(.50), "separuh peserta memperoleh 6 jawaban benar atau kurang"),
       ("Desil 7 (P70)", perc(.70), ""),
       ("Kuartil 3 (P75)", perc(.75), "batas kelompok atas"),
       ("Desil 9 (P90)", perc(.90), "hanya 10% peserta mencapai lebih dari ini"),
       ("Maksimum", srtv[-1], "vivi"),
       ("Rentang", srtv[-1] - srtv[0], ""),
       ("IQR", perc(.75) - perc(.25), "sebaran 50% peserta tengah"),
       ("Simpangan baku", sd_s, "populasi"),
       ("Simpangan rata-rata", st.mean(abs(x - mean_s) for x in sc.values()), ""),
       ("Koefisien variasi", sd_s / mean_s, "dalam proporsi; setara %.1f%%" % (sd_s / mean_s * 100)),
       ("Batas pencilan bawah", perc(.25) - 1.5 * (perc(.75) - perc(.25)), "tidak ada pencilan bawah"),
       ("Batas pencilan atas", perc(.75) + 1.5 * (perc(.75) - perc(.25)), "batas 15; skor tertinggi 14 masih di dalam rentang wajar - tidak ada pencilan atas")]
for k, v, ket in POS:
    ws.cell(r, 1, k).font = Font(size=10, bold=True)
    c = ws.cell(r, 2, round(v, 2)); c.alignment = Alignment(horizontal="center")
    c = ws.cell(r, 3, round(v * 5, 1)); c.alignment = Alignment(horizontal="center")
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=8)
    ws.cell(r, 4, ket).font = Font(size=10, italic=True, color="555555")
    for i in range(1, 9):
        ws.cell(r, i).border = BOX
    r += 1
r += 1

# --- perbandingan populasi
secrow(ws, r, "E. PERBANDINGAN TIGA DEFINISI POPULASI", 8); r += 1
head(ws, r, ["Definisi populasi", "n", "Rata-rata\nbenar", "Akurasi", "SD", "Median",
             "Maks", "Kapan dipakai"], [34, 6, 12, 11, 9, 10, 8, 76])
r += 1
act = [n for n in P if sc[n] > 0]
uniqbest = {}
for n in P:
    b = base(n)
    if b not in uniqbest or sc[n] > sc[uniqbest[b]]:
        uniqbest[b] = n
UB = list(uniqbest.values())
for lab, lst, use in [
    ("Seluruh 37 sesi (metrik resmi)", list(P), "Angka yang ditampilkan Wayground dan dipakai untuk pelaporan formal"),
    ("33 sesi aktif (skor > 0)", act, "Cerminan paling jujur atas kemampuan awal peserta yang benar-benar ikut"),
    ("33 peserta unik, sesi terbaik", UB, "Dipakai bila hasil dilaporkan per orang, bukan per sesi"),
]:
    v = [sc[n] for n in lst]
    row = [lab, len(lst), round(st.mean(v), 2), sum(v) / (len(v) * 20), round(st.pstdev(v), 2),
           st.median(v), max(v), use]
    for i, x in enumerate(row, 1):
        c = ws.cell(r, i, x); c.border = BOX; c.font = Font(size=10)
        if i not in (1, 8):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 4).number_format = "0.0%"
    ws.row_dimensions[r].height = 26
    r += 1
r += 1

for t in [
    "Distribusi tidak berbentuk lonceng. Terdapat dua puncak: satu di 6–7 jawaban benar (12 sesi) dan satu tumpukan di 0 (4 sesi). Puncak kedua adalah artefak teknis, bukan kelompok kemampuan.",
    "Tidak ada satu pun peserta yang mencapai kategori Sangat Baik (16 butir ke atas). Nilai tertinggi 14 benar setara 70 - tepat di ambang KKM. Ini menegaskan bahwa pelatihan memang dibutuhkan seluruh peserta, bukan hanya sebagian.",
    "Sebaran 50% peserta tengah hanya selebar 4 butir (IQR = 4, dari 5 sampai 9). Mayoritas peserta berada pada tingkat pengetahuan yang mirip - materi pelatihan dapat disampaikan seragam tanpa perlu pengelompokan tingkat.",
    "Bila keempat sesi nol dikeluarkan, rata-rata naik dari 6,46 menjadi 7,24 dan akurasi dari 32,3% menjadi 36,2%. Gunakan 36,2% sebagai garis dasar pembanding untuk post-test agar perbandingannya adil.",
]:
    note(ws, r, t, 8, 34); r += 1
