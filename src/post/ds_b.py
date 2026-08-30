# -*- coding: utf-8 -*-
"""Bagian B: 01 Sensus, 02-03 Soal lengkap, 04-05 Statistik butir."""

# ================= 01 SENSUS
ws = wb.create_sheet("01 Sensus")
title(ws, "SENSUS PESERTA — DARI SESI MENJADI ORANG",
      "Ekspor Wayground mencatat sesi. Lembar ini menunjukkan bagaimana 37 sesi pre-test menjadi 33 orang "
      "dan 16 sesi post-test menjadi 14 orang, beserta bukti rinci setiap sesi ganda.", 8)
r = 4
r = sec(ws, r, "A. REKONSILIASI", 8)
r = head(ws, r, ["Tahap", "Pre-test", "Post-test", "Keterangan"], [40, 12, 12, 86])
nmul_pre = sum(len(v) - 1 for v in D["MULTI_PRE"].values())
nmul_post = sum(len(v) - 1 for v in D["MULTI_POST"].values())
for a, b, c, k in [
    ("Sesi terekam pada ekspor", 37, 16, "Baris apa adanya pada sheet Participant Data."),
    ("dikurangi sesi uji perangkat lunak", 0, -1, "Sesi Vincent: 15 dari 20 butir dijawab dalam 1 detik."),
    ("Sesi peserta", 37, 15, "Angka inilah yang dipakai pada laporan versi sebelumnya."),
    ("dikurangi sesi ulangan orang yang sama", -nmul_pre, -nmul_post,
     "Pre-test: Sri Suyani 3 sesi, Aqifah 2, farida johannes 2. Post-test: Yovita 2."),
    ("JUMLAH ORANG", NPRE, NPOST, "Satuan analisis pada berkas ini."),
    ("Orang menjawab sedikitnya satu butir", sum(1 for o in ORANG_PRE if RPRE[o].count("-") < 20),
     sum(1 for o in ORANG_POST if RPOST[o].count("-") < 20), "Sisanya membuka tes tanpa menjawab."),
    ("Orang menyelesaikan seluruh 20 butir", sum(1 for o in ORANG_PRE if RPRE[o].count("-") == 0),
     sum(1 for o in ORANG_POST if RPOST[o].count("-") == 0),
     "Pre-test dibatasi 14 menit sehingga sedikit yang tuntas."),
    ("Orang mengikuti KEDUA tes", len(PAIR), len(PAIR), "Hasil pencocokan nama antar kedua daftar."),
    ("Orang mengikuti kedua tes sampai tuntas", len(PAIRT), len(PAIRT), "Dasar seluruh uji statistik."),
]:
    r = row(ws, r, [a, b, c, k], ctr=(2, 3), bold=(1,), h=24, fs=9)
    if a == "JUMLAH ORANG":
        for col in (1, 2, 3):
            ws.cell(r - 1, col).fill = GRN
            ws.cell(r - 1, col).font = Font(bold=True, size=10)
    elif a.startswith("dikurangi"):
        for col in (2, 3):
            ws.cell(r - 1, col).fill = YEL
r += 1

r = sec(ws, r, "B. BUKTI RINCI SETIAP SESI GANDA", 8)
r = head(ws, r, ["Orang", "Nama sesi pada ekspor", "Tes", "Benar", "Salah", "Kosong", "Waktu (dtk)", "Dipakai"],
         [22, 24, 12, 9, 9, 9, 12, 11])
for orang, sesi in sorted(D["MULTI_PRE"].items()):
    for n in sorted(sesi, key=lambda x: -(20 - PC_len(x) if False else 0)) if False else sesi:
        cs = pre["CORR"][n]
        pakai = (n == CH_PRE[orang])
        r = row(ws, r, [orang, n, "Pre-test", cs.count("C"), cs.count("X"), cs.count("-"),
                        PP[n].get("time_s", 0), "YA" if pakai else "tidak"],
                ctr=(3, 4, 5, 6, 7, 8), bold=(1,), h=18, fs=9)
        ws.cell(r - 1, 8).fill = GRN if pakai else RED
for orang, sesi in sorted(D["MULTI_POST"].items()):
    for n in sesi:
        cs = post["CORR"][n]
        pakai = (n == CH_POST[orang])
        r = row(ws, r, [orang, n, "Post-test", cs.count("C"), cs.count("X"), cs.count("-"),
                        PO[n].get("time_s", 0), "YA" if pakai else "tidak"],
                ctr=(3, 4, 5, 6, 7, 8), bold=(1,), h=18, fs=9)
        ws.cell(r - 1, 8).fill = GRN if pakai else RED
r = note(ws, r, "Enam dari tujuh sesi ulangan praktis kosong: peserta masuk lalu keluar tanpa menjawab, atau berhenti "
                "setelah beberapa butir. Pola ini menunjuk ke kendala teknis, bukan ke pengerjaan ulang untuk memperbaiki nilai. "
                "Pada keempat orang, sesi dengan butir terjawab terbanyak juga merupakan sesi dengan jawaban benar terbanyak, "
                "sehingga aturan pemilihan tidak menentukan hasil.", 8, 32)
r += 1

r = sec(ws, r, "C. AKIBAT TERHADAP ANGKA DESKRIPTIF", 8)
r = head(ws, r, ["Ukuran", "Basis sesi", "Basis orang", "Selisih", "Catatan"], [34, 14, 14, 12, 78])
m_ses = st.mean([pre["CORR"][n].count("C") for n in PP])
m_org = st.mean([RPRE[o].count("C") for o in ORANG_PRE])
for a, b, c, k in [
    ("Pre-test: rata-rata benar", round(m_ses, 2), round(m_org, 2),
     "Sesi kosong tidak lagi menekan rata-rata ke bawah."),
    ("Pre-test: akurasi kelas (%)", round(m_ses / 20 * 100, 1), round(m_org / 20 * 100, 1),
     "Naik sekitar tiga poin persen."),
    ("Post-test: rata-rata benar", round(st.mean([post["CORR"][n].count("C") for n in post["names"]]), 2),
     round(st.mean([RPOST[o].count("C") for o in ORANG_POST]), 2),
     "Satu sesi kosong milik Yovita tidak lagi dihitung sebagai orang kedua."),
    ("Gain berpasangan (butir)", 5.00, round(STAT["mean_gain"], 2),
     "TIDAK BERUBAH — tidak satu pun orang bersesi ganda masuk ke kelompok berpasangan."),
    ("Uji-t berpasangan", 3.669, round(STAT["t"], 3), "TIDAK BERUBAH."),
    ("Ukuran efek Cohen dz", 1.297, round(STAT["dz"], 3), "TIDAK BERUBAH."),
]:
    d = round(c - b, 3)
    r = row(ws, r, [a, b, c, d, k], ctr=(2, 3, 4), bold=(1,), h=20, fs=9)
    ws.cell(r - 1, 4).fill = GRY if abs(d) < 1e-9 else YEL


# ================= 02 / 03 SOAL LENGKAP
def sheet_soal(nama, judul, sub, Q, OPTM, IT, RES, ORG, CH, KEYOF, DEAD, ansof):
    ws = wb.create_sheet(nama)
    title(ws, judul, sub, 7)
    r = 4
    r = head(ws, r, ["Butir", "Naskah soal (apa adanya dari naskah cetak resmi)", "Opsi",
                     "Teks opsi (apa adanya)", "Kunci", "Pemilih", "Status opsi"],
             [7, 62, 7, 62, 8, 9, 20])
    for n in range(1, 21):
        opts = OPTM[n]["opts"]
        key = KEYOF(n)
        cnt = ansof(n)
        first = r
        for li, (let, txt) in enumerate(opts):
            iskey = (norm_(txt) == norm_(key))
            nc = cnt.get(norm_(txt), 0)
            mati = (not iskey) and nc == 0
            r = row(ws, r, ["" if li else n, "" if li else Q[n]["text"], let + ")", txt,
                            "KUNCI" if iskey else "", nc,
                            "kunci" if iskey else ("pengecoh mati" if mati else "pengecoh berfungsi")],
                    ctr=(1, 3, 5, 6, 7), bold=(1, 5), h=30, fs=9)
            cc = ws.cell(r - 1, 4)
            cc.fill = GRN if iskey else (GRY if mati else BLU)
            ws.cell(r - 1, 6).fill = GRN if iskey else (RED if mati else LG)
        ws.merge_cells(start_row=first, start_column=1, end_row=r - 1, end_column=1)
        ws.merge_cells(start_row=first, start_column=2, end_row=r - 1, end_column=2)
        ws.cell(first, 1).alignment = CEN
        ws.cell(first, 2).alignment = WRAP
        ws.cell(first, 1).fill = HDR
        ws.cell(first, 1).font = Font(bold=True, size=11, color="FFFFFF")
    nd = sum(len(v) for v in DEAD.values())
    r += 1
    r = note(ws, r, "Seluruh %d opsi (20 butir x 4) disalin apa adanya dari naskah cetak resmi. Kolom Pemilih dihitung dari "
                    "jawaban %d orang. Opsi salah dengan nol pemilih ditandai pengecoh mati: %d dari 60 (%.0f%%)."
             % (sum(len(OPTM[n]["opts"]) for n in range(1, 21)), len(ORG), nd, nd / 60 * 100), 7, 26)
    return ws


def norm_(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def counts_pre(n):
    c = {}
    for o in ORANG_PRE:
        a = QPRE[n].get("answers_real", {}).get(CH_PRE[o])
        if a:
            c[norm_(a)] = c.get(norm_(a), 0) + 1
    return c


def counts_post(n):
    c = {}
    for o in ORANG_POST:
        a = QPOST[n]["answers"].get(CH_POST[o])
        if a:
            c[norm_(a)] = c.get(norm_(a), 0) + 1
    return c


sheet_soal("02 Soal Pre-test", "NASKAH LENGKAP PRE-TEST — 20 BUTIR, 80 OPSI",
           "Disalin apa adanya dari naskah cetak resmi. Kunci ditetapkan dari pola respons lalu diverifikasi ke naskah: "
           "cocok pada 20 dari 20 butir dengan skor kemiripan 1,00.",
           QPRE, OPT_PRE, IPRE, RPRE, ORANG_PRE, CH_PRE,
           lambda n: IPRE[n]["key"], DEAD_PRE, counts_pre)

sheet_soal("03 Soal Post-test", "NASKAH LENGKAP POST-TEST — 20 BUTIR, 80 OPSI",
           "Disalin apa adanya dari naskah cetak resmi. Kunci diverifikasi ke naskah: cocok 20 dari 20 butir. "
           "Dua kunci yang semula ambigu diselesaikan lewat kendala jumlah benar tiap peserta.",
           QPOST, OPT_POST, None, RPOST, ORANG_POST, CH_POST,
           lambda n: QPOST[n]["key"], DEAD_POST, counts_post)


# ================= 04 / 05 STATISTIK BUTIR
def sheet_butir(nama, judul, sub, Q, SI, ORG, R, N, K, KR, SEM, KEYOF, avgt):
    ws = wb.create_sheet(nama)
    title(ws, judul, sub, 11)
    r = 4
    r = head(ws, r, ["Butir", "Naskah soal", "Kunci", "Benar", "Salah", "Kosong",
                     "p", "Kategori", "D", "r-pbis", "Waktu rata-rata (dtk)"],
             [7, 58, 46, 9, 9, 9, 9, 12, 9, 10, 14])
    t0 = r
    for n in range(1, 21):
        s = SI[n]
        p = s["p"]
        kat = "Sukar" if p < .30 else ("Sedang" if p <= .70 else "Mudah")
        r = row(ws, r, [n, Q[n]["text"], KEYOF(n), s["benar"], s["salah"], s["kosong"],
                        round(p, 3), kat, round(s["D"], 3), round(s["rpb"], 3),
                        avgt(n) if avgt else "—"],
                ctr=(1, 4, 5, 6, 7, 8, 9, 10, 11), bold=(1,), h=34, fs=9)
        ws.cell(r - 1, 1).fill = HDR
        ws.cell(r - 1, 1).font = Font(bold=True, size=11, color="FFFFFF")
        ws.cell(r - 1, 7).fill = RED if p < .30 else (YEL if p <= .70 else GRN)
        ws.cell(r - 1, 8).fill = RED if kat == "Sukar" else (YEL if kat == "Sedang" else GRN)
    t1 = r - 1
    r += 1
    r = sec(ws, r, "RINGKASAN", 11)
    r = head(ws, r, ["Ukuran", "Nilai", "Tafsiran"], [30, 14, 100])
    tot = [R[o].count("C") for o in ORG]
    for a, b, c in [
        ("Jumlah orang", N, "Satu baris satu orang; sesi ulangan sudah digabungkan."),
        ("Rata-rata benar", round(st.mean(tot), 2), "Dari 20 butir."),
        ("Simpangan baku", round(st.pstdev(tot), 2), "Sebaran skor antar orang."),
        ("Skor tertinggi / terendah", "%d / %d" % (max(tot), min(tot)), ""),
        ("Rata-rata p", round(st.mean([SI[n]["p"] for n in range(1, 21)]), 3),
         "Proporsi jawaban benar rata-rata seluruh butir."),
        ("Reliabilitas KR-20", KR,
         "0,70 lazim dipakai sebagai ambang memadai untuk keputusan kelompok."),
        ("Kesalahan baku ukur (SEM)", SEM, "Dalam satuan butir."),
        ("Kelompok atas / bawah", "%d orang" % K, "27 persen dari jumlah orang, dipakai menghitung daya beda D."),
    ]:
        r = row(ws, r, [a, b, c], ctr=(2,), bold=(1,), h=18, fs=9)
    return ws, t0, t1


def avgt_post(n):
    vs = [TIME[CH_POST[o]][n] for o in ORANG_POST
          if TIME.get(CH_POST[o], {}).get(n) is not None]
    return round(st.mean(vs), 1) if vs else "—"


def avgt_pre(n):
    v = QPRE[n].get("avgt")
    return v if v else "—"


sheet_butir("04 Butir Pre-test", "ANALISIS BUTIR PRE-TEST",
            "Dihitung ulang atas basis %d orang. Butir tidak dijawab dihitung tidak benar." % NPRE,
            QPRE, SPRE_I, ORANG_PRE, RPRE, NPRE, D["KPRE"], D["KR_PRE"], D["SEM_PRE"],
            lambda n: IPRE[n]["key"], avgt_pre)

sheet_butir("05 Butir Post-test", "ANALISIS BUTIR POST-TEST",
            "Dihitung ulang atas basis %d orang, setelah sesi uji perangkat lunak dikeluarkan." % NPOST,
            QPOST, SPOST_I, ORANG_POST, RPOST, NPOST, D["KPOST"], D["KR_POST"], D["SEM_POST"],
            lambda n: QPOST[n]["key"], avgt_post)
