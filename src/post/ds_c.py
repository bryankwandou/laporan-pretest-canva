# -*- coding: utf-8 -*-
"""Bagian C: 06-07 matriks respons, 08-09 jawaban mentah, 10 berpasangan."""


# ================= 06 / 07 MATRIKS RESPONS
def sheet_respons(nama, judul, sub, ORG, R, CH, meta, prescore=None):
    ws = wb.create_sheet(nama)
    title(ws, judul, sub, 26)
    r = 4
    cols = ["No", "Nama"] + ["Q%d" % i for i in range(1, 21)] + ["Benar", "Salah", "Kosong", "Nilai"]
    r = head(ws, r, cols, [5, 26] + [4.4] * 20 + [8, 8, 8, 8])
    top = r
    for i, o in enumerate(ORG, 1):
        cs = R[o]
        ws.cell(r, 1, i).alignment = CEN
        ws.cell(r, 1).border = BOX
        c = ws.cell(r, 2, o)
        c.border = BOX
        c.font = Font(size=10)
        for qi, s in enumerate(cs):
            cc = ws.cell(r, 3 + qi, {"C": "B", "X": "S", "-": ""}[s])
            cc.border = BOX
            cc.alignment = CEN
            cc.font = Font(size=9, bold=True)
            cc.fill = {"C": GRN, "X": RED, "-": GRY}[s]
        for j, v in enumerate([cs.count("C"), cs.count("X"), cs.count("-"),
                               round(cs.count("C") / 20 * 100)]):
            cc = ws.cell(r, 23 + j, v)
            cc.border = BOX
            cc.alignment = CEN
            cc.font = Font(size=10, bold=(j == 0))
            cc.fill = LG
        r += 1
    bot = r - 1
    c = ws.cell(r, 2, "Benar per butir")
    c.font = Font(bold=True, size=10)
    c.border = BOX
    for qi in range(20):
        cc = ws.cell(r, 3 + qi, sum(1 for o in ORG if R[o][qi] == "C"))
        cc.border = BOX
        cc.alignment = CEN
        cc.font = Font(size=9, bold=True)
        cc.fill = LG
    cc = ws.cell(r, 23, sum(R[o].count("C") for o in ORG))
    cc.border = BOX
    cc.alignment = CEN
    cc.font = Font(bold=True)
    ws.freeze_panes = "C%d" % top
    r += 2
    r = note(ws, r, "B = benar (hijau) · S = salah (merah) · sel kosong abu-abu = butir tidak dijawab. "
                    "Nilai = jumlah benar dikali 5, sehingga 20 butir setara nilai 100. "
                    "Satu baris satu ORANG; bagi yang bersesi ganda, sesi terpilih dicantumkan pada lembar 01 Sensus.", 26, 28)
    return ws, top, bot


sheet_respons("06 Respons Pre-test", "MATRIKS RESPONS PRE-TEST — %d ORANG x 20 BUTIR" % NPRE,
              "Diurutkan dari jumlah jawaban benar terbanyak.", ORANG_PRE, RPRE, CH_PRE, PP)
sheet_respons("07 Respons Post-test", "MATRIKS RESPONS POST-TEST — %d ORANG x 20 BUTIR" % NPOST,
              "Diurutkan dari jumlah jawaban benar terbanyak. Sesi uji perangkat lunak sudah dikeluarkan.",
              ORANG_POST, RPOST, CH_POST, PO)


# ================= 08 / 09 JAWABAN MENTAH
def sheet_jawab(nama, judul, sub, ORG, R, CH, Q, ansget, withtime=False):
    ws = wb.create_sheet(nama)
    title(ws, judul, sub, 22)
    r = 4
    r = head(ws, r, ["No", "Nama"] + ["Q%d" % i for i in range(1, 21)], [5, 24] + [30] * 20)
    for i, o in enumerate(ORG, 1):
        ws.cell(r, 1, i).alignment = CEN
        ws.cell(r, 1).border = BOX
        c = ws.cell(r, 2, o)
        c.border = BOX
        c.font = Font(size=10, bold=True)
        for qi in range(20):
            a = ansget(qi + 1, CH[o])
            cc = ws.cell(r, 3 + qi, a if a else "(tidak dijawab)")
            cc.border = BOX
            cc.font = Font(size=8)
            cc.alignment = WRAP
            cc.fill = {"C": GRN, "X": RED, "-": GRY}[R[o][qi]]
        ws.row_dimensions[r].height = 42
        r += 1
    ws.freeze_panes = "C5"
    r += 1
    r = note(ws, r, "Setiap sel memuat teks opsi yang benar-benar dipilih orang tersebut, disalin apa adanya dari ekspor resmi. "
                    "Hijau benar, merah salah, abu-abu tidak dijawab. Total %d sel jawaban." % (len(ORG) * 20), 22, 24)
    return ws


sheet_jawab("08 Jawaban Pre-test", "JAWABAN MENTAH PRE-TEST — TEKS OPSI YANG DIPILIH",
            "Sumber tunggal seluruh statistik pre-test pada berkas ini.",
            ORANG_PRE, RPRE, CH_PRE, QPRE,
            lambda n, s: QPRE[n].get("answers_real", {}).get(s))

sheet_jawab("09 Jawaban Post-test", "JAWABAN MENTAH POST-TEST — TEKS OPSI YANG DIPILIH",
            "Sumber tunggal seluruh statistik post-test pada berkas ini.",
            ORANG_POST, RPOST, CH_POST, QPOST,
            lambda n, s: QPOST[n]["answers"].get(s))

# waktu per butir post-test
ws = wb.create_sheet("09b Waktu Post-test")
title(ws, "WAKTU PENGERJAAN POST-TEST — DETIK PER BUTIR",
      "Diambil utuh dari sheet Time Data ekspor resmi. Sel kosong berarti butir tidak dijawab.", 23)
r = head(ws, 4, ["No", "Nama"] + ["Q%d" % i for i in range(1, 21)] + ["Total"], [5, 24] + [5.5] * 20 + [9])
for i, o in enumerate(ORANG_POST, 1):
    s = CH_POST[o]
    ws.cell(r, 1, i).alignment = CEN
    ws.cell(r, 1).border = BOX
    c = ws.cell(r, 2, o)
    c.border = BOX
    c.font = Font(size=10, bold=True)
    for qi in range(1, 21):
        v = TIME.get(s, {}).get(qi)
        cc = ws.cell(r, 2 + qi, v if v is not None else "")
        cc.border = BOX
        cc.alignment = CEN
        cc.font = Font(size=9)
        cc.fill = GRY if v is None else (RED if v <= 5 else (YEL if v >= 45 else GRN))
    cc = ws.cell(r, 23, PO[s].get("time_s", 0))
    cc.border = BOX
    cc.alignment = CEN
    cc.font = Font(bold=True, size=10)
    r += 1
ws.freeze_panes = "C5"
r += 1
r = note(ws, r, "Merah = 5 detik atau kurang · hijau = wajar · kuning = 45 detik atau lebih · abu-abu = tidak dijawab.", 23, 20)

# ================= 10 BERPASANGAN
ws = wb.create_sheet("10 Berpasangan")
title(ws, "ANALISIS BERPASANGAN — ORANG YANG MENGIKUTI KEDUA TES",
      "Membandingkan orang yang sama dengan dirinya sendiri, sehingga perbedaan komposisi peserta "
      "tidak lagi menjadi penjelasan tandingan. Inilah dasar seluruh kesimpulan pada penelitian ini.", 9)
r = 4
r = sec(ws, r, "A. SELURUH %d ORANG YANG MENGIKUTI KEDUA TES" % len(PAIR), 9)
r = head(ws, r, ["No", "Nama (post-test)", "Nama (pre-test)", "Pre", "Post", "Gain",
                 "Butir dijawab post", "Status", "Dipakai uji statistik"],
         [5, 26, 26, 8, 8, 8, 16, 14, 18])
for i, (o, p, a, b, ta, tb) in enumerate(sorted(PAIR, key=lambda x: -(x[3] - x[2])), 1):
    tuntas = tb == 20
    r = row(ws, r, [i, o, p, a, b, b - a, tb, "Tuntas" if tuntas else "Terputus",
                    "YA" if tuntas else "tidak"],
            ctr=(1, 4, 5, 6, 7, 8, 9), bold=(2, 6), h=18, fs=9)
    ws.cell(r - 1, 6).fill = GRN if b > a else (RED if b < a else GRY)
    ws.cell(r - 1, 8).fill = GRN if tuntas else RED
    ws.cell(r - 1, 9).fill = GRN if tuntas else RED
pa0 = r - len(PAIR)
r += 1
r = note(ws, r, "Tiga orang tidak dipakai pada uji statistik karena post-test-nya terputus (masing-masing hanya menjawab "
                "0, 2, dan 3 butir, seluruhnya berhenti di bawah 45 detik). Yang terukur pada ketiganya adalah kegagalan "
                "teknis, bukan pengetahuan. Memasukkan mereka menurunkan rata-rata gain menjadi +2,55 butir dan menghapus "
                "signifikansi statistiknya.", 9, 30)
r += 1

r = sec(ws, r, "B. UJI STATISTIK ATAS %d ORANG YANG TUNTAS" % STAT["n"], 9)
r = head(ws, r, ["Ukuran", "Nilai", "Pembanding", "Kesimpulan"], [30, 20, 26, 76])
crit = 2.365
for a, b, c, k in [
    ("Jumlah pasangan (n)", STAT["n"], "—", "Kecil, sehingga uji tanda dilaporkan berdampingan dengan uji-t."),
    ("Rata-rata pre-test", round(st.mean([x[2] for x in PAIRT]), 2), "kelas %.2f" % st.mean([RPRE[o].count("C") for o in ORANG_PRE]),
     "Kelompok berpasangan berangkat dari titik yang lebih tinggi daripada kelas — bias seleksi."),
    ("Rata-rata post-test", round(st.mean([x[3] for x in PAIRT]), 2), "—", ""),
    ("Rata-rata gain", "+%.2f butir" % STAT["mean_gain"], "SEM %.2f butir" % D["SEM_POST"],
     "Gain hampir tiga kali kesalahan baku ukur, sehingga bukan sekadar derau pengukuran."),
    ("Simpangan baku gain", round(STAT["sd_gain"], 2), "—", ""),
    ("Uji-t berpasangan", "t(%d) = %.3f" % (STAT["n"] - 1, STAT["t"]), "kritis %.3f (a=0,05 dua sisi)" % crit,
     "SIGNIFIKAN. Kenaikan tidak dapat dijelaskan oleh kebetulan semata."),
    ("Uji tanda (binomial)", "%d dari %d naik" % (STAT["naik"], STAT["n"]), "p = %.4f satu sisi" % STAT["pbin"],
     "Konsisten pada tiap individu. Tidak bergantung pada asumsi sebaran normal."),
    ("Ukuran efek Cohen dz", round(STAT["dz"], 3), "0,20 kecil · 0,50 sedang · 0,80 besar", "BESAR."),
    ("Gain ternormalisasi Hake", round(STAT["hake"], 3), "<0,30 rendah · 0,30-0,70 sedang",
     "SEDANG. %.0f persen jarak menuju skor sempurna berhasil ditutup." % (STAT["hake"] * 100)),
]:
    r = row(ws, r, [a, b, c, k], ctr=(2, 3), bold=(1, 2), h=22, fs=9)
r += 1

# uji kepekaan
g = sorted([x[3] - x[2] for x in PAIRT])
g2 = g[:-1]
m2, s2 = st.mean(g2), st.stdev(g2)
t2 = m2 / (s2 / math.sqrt(len(g2)))
r = sec(ws, r, "C. UJI KEPEKAAN — MENGELUARKAN PENGAMATAN EKSTREM", 9)
r = head(ws, r, ["Kelompok", "n", "Rata-rata gain", "SD", "t", "dz", "Kesimpulan"],
         [30, 8, 16, 10, 12, 10, 66])
for a, b, c, d_, e, f, k in [
    ("Seluruh pasangan tuntas", STAT["n"], round(STAT["mean_gain"], 2), round(STAT["sd_gain"], 2),
     round(STAT["t"], 3), round(STAT["dz"], 3), "Signifikan terhadap kritis 2,365."),
    ("Tanpa gain tertinggi (+%d)" % g[-1], len(g2), round(m2, 2), round(s2, 2), round(t2, 3),
     round(m2 / s2, 3), "Rata-rata turun tetapi sebarannya menyempit, sehingga t justru NAIK. "
     "Kesimpulan tidak bergantung pada satu pengamatan; yang bergantung padanya hanya besaran rata-ratanya."),
]:
    r = row(ws, r, [a, b, c, d_, e, f, k], ctr=(2, 3, 4, 5, 6), bold=(1,), h=26, fs=9)
