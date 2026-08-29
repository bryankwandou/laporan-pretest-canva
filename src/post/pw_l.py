# -*- coding: utf-8 -*-
# ============ 13 ANALISIS WAKTU
TJ = json.load(io.open("post_time.json", encoding="utf-8"))
raw = json.load(io.open("post_core_raw.json", encoding="utf-8"))
TIME = {n: {int(k): v for k, v in d.items()} for n, d in TJ["TIME"].items()}
AVG = {int(k): v for k, v in TJ["AVG"].items()}

ws = wb.create_sheet("13 Analisis Waktu")
title(ws, "ANALISIS WAKTU POST-TEST — PER BUTIR DAN PER PESERTA",
      "Diambil utuh dari sheet Time Data ekspor resmi Wayground. Kolom Vincent ditampilkan terpisah pada bagian C sebagai bukti "
      "dasar pengeluaran sesi QA, tetapi tidak ikut dalam perhitungan rata-rata mana pun.", 12)
r = 4

secrow(ws, r, "A. WAKTU RATA-RATA PER BUTIR (15 sesi, Vincent dikeluarkan)", 12); r += 1
head(ws, r, ["Butir", "Pokok yang diuji", "Rata-rata\nWayground", "Rata-rata\nhitung ulang", "Tercepat",
             "Terlama", "Penjawab", "p", "Waktu\njawaban benar", "Waktu\njawaban salah", "Selisih", "Catatan"],
     [7, 40, 12, 12, 10, 10, 10, 8, 13, 13, 10, 46])
r += 1
t0 = r
NM = [n for n in post["names"]]
for q in sorted(post["Q"], key=lambda x: x["no"]):
    n_ = q["no"]
    vs = [TIME[p][n_] for p in NM if TIME[p].get(n_) is not None]
    tb = [TIME[p][n_] for p in NM if TIME[p].get(n_) is not None and CO[p][n_ - 1] == "C"]
    tsx = [TIME[p][n_] for p in NM if TIME[p].get(n_) is not None and CO[p][n_ - 1] == "X"]
    mb = st.mean(tb) if tb else 0
    ms = st.mean(tsx) if tsx else 0
    cat = ""
    if vs and st.mean(vs) >= 40:
        cat = "Butir paling lama dibaca — redaksi opsinya panjang."
    elif vs and st.mean(vs) <= 15:
        cat = "Dijawab cepat; hafalan langsung, bukan penalaran."
    if tb and tsx and ms - mb >= 8:
        cat = (cat + " ").strip() + " Yang salah berpikir jauh lebih lama — butir membingungkan."
    putrow(ws, r, [n_, SHORTP[n_], AVG.get(n_, 0), round(st.mean(vs), 1) if vs else 0,
                   min(vs) if vs else 0, max(vs) if vs else 0, len(vs), round(q["p"], 2),
                   round(mb, 1) if tb else "—", round(ms, 1) if tsx else "—",
                   round(ms - mb, 1) if (tb and tsx) else "—", cat],
           ctr=(1, 3, 4, 5, 6, 7, 8, 9, 10, 11), bold=(1,), h=22)
    ws.cell(r, 1).fill = HDR; ws.cell(r, 1).font = Font(size=11, bold=True, color="FFFFFF")
    if vs:
        m_ = st.mean(vs)
        ws.cell(r, 4).fill = RED if m_ >= 40 else (GRN if m_ <= 15 else YEL)
    r += 1
t1 = r - 1
r += 1

ch = BarChart(); ch.type = "col"; ch.style = 10
ch.title = "Waktu rata-rata per butir post-test (detik)"
ch.y_axis.title = "Detik"; ch.height = 9; ch.width = 26
ch.add_data(Reference(ws, min_col=4, min_row=t0 - 1, max_row=t1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=t0, max_row=t1))
ch.dLbls = DataLabelList(); ch.dLbls.showVal = True
ch.legend = None
ws.add_chart(ch, "A%d" % r)

ch2 = BarChart(); ch2.type = "col"; ch2.grouping = "clustered"; ch2.style = 12
ch2.title = "Waktu jawaban benar versus jawaban salah, per butir"
ch2.y_axis.title = "Detik"; ch2.height = 9; ch2.width = 26
ch2.add_data(Reference(ws, min_col=9, max_col=10, min_row=t0 - 1, max_row=t1), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=1, min_row=t0, max_row=t1))
ws.add_chart(ch2, "A%d" % (r + 19))
r += 39

secrow(ws, r, "B. MATRIKS WAKTU PENUH — 15 SESI x 20 BUTIR (detik)", 12); r += 1
head(ws, r, ["Nama"] + ["Q%d" % i for i in range(1, 21)] + ["Total"], [26] + [6] * 20 + [9])
r += 1
m0 = r
for n in ORDP:
    c = ws.cell(r, 1, n); c.font = Font(size=10, bold=True); c.border = BOX
    for qi in range(1, 21):
        v = TIME[n].get(qi)
        cell = ws.cell(r, qi + 1, v if v is not None else "—")
        cell.border = BOX; cell.font = Font(size=9)
        cell.alignment = Alignment(horizontal="center")
        if v is None:
            cell.fill = GRY
        elif v <= 5:
            cell.fill = RED
        elif v >= 45:
            cell.fill = YEL
        else:
            cell.fill = GRN
    c = ws.cell(r, 22, PO[n]["time_s"]); c.font = Font(bold=True, size=10); c.border = BOX
    c.alignment = Alignment(horizontal="center")
    r += 1
ws.freeze_panes = "B%d" % m0
tot_cells = sum(1 for n in ORDP for qi in range(1, 21) if TIME[n].get(qi) is not None)
r += 1
note(ws, r, "Merah = 5 detik atau kurang (terlalu cepat untuk membaca soal) · hijau = wajar · kuning = 45 detik atau lebih · "
            "abu-abu = butir tidak dijawab. Total %d sel waktu terisi dari 300 sel yang mungkin; sisanya adalah butir yang memang "
            "tidak dijawab pada sesi terputus." % tot_cells, 12, 32)
r += 2

secrow(ws, r, "C. DASAR FORENSIK PENGELUARAN SESI QA TESTER (VINCENT)", 12); r += 1
head(ws, r, ["Butir", "Waktu Vincent\n(detik)", "Rata-rata\n15 peserta", "Selisih", "Penilaian", "", "", "", "", "", "", ""],
     [8, 14, 14, 10, 76])
r += 1
v1 = 0
for qi in range(1, 21):
    v = TIME["Vincent"].get(qi)
    vs = [TIME[p][qi] for p in NM if TIME[p].get(qi) is not None]
    m_ = st.mean(vs) if vs else 0
    if v == 1:
        v1 += 1
        pen = "Satu detik — mustahil untuk membaca soal beserta empat opsinya."
    elif v is None:
        pen = "Tidak dijawab."
    elif v < 5:
        pen = "Di bawah 5 detik; masih terlalu cepat untuk dibaca."
    else:
        pen = "Wajar."
    putrow(ws, r, [qi, v if v is not None else "—", round(m_, 1), round(v - m_, 1) if v is not None else "—", pen],
           ctr=(1, 2, 3, 4), bold=(1,), h=18)
    ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=12)
    ws.cell(r, 2).fill = RED if (v is not None and v <= 5) else GRN
    r += 1
r += 1
for t in [
    "Dari 20 butir, %d dijawab Vincent dalam waktu persis 1 detik. Membaca satu butir post-test beserta keempat opsinya membutuhkan "
    "sekurang-kurangnya beberapa detik; rata-rata 15 peserta lain adalah %.1f detik per butir. Pola satu detik berulang adalah tanda "
    "penelusuran otomatis atau klik cepat untuk menguji jalannya kuis, bukan pengerjaan soal."
    % (v1, st.mean([TIME[p][q] for p in NM for q in range(1, 21) if TIME[p].get(q) is not None])),
    "Waktu total sesi Vincent %d menit %d detik untuk 20 butir, sementara rata-rata sesi tuntas peserta lain adalah 10 menit 18 detik."
    % (raw["P"]["Vincent"]["time_s"] // 60, raw["P"]["Vincent"]["time_s"] % 60),
    "Vincent juga tidak muncul pada daftar 37 peserta pre-test, sehingga tidak dapat masuk analisis berpasangan dalam keadaan apa pun.",
    "Atas ketiga dasar itu sesi ini dikeluarkan dari seluruh perhitungan. Dampaknya terhadap angka agregat kecil dan dilaporkan penuh "
    "pada sheet 09 Metodologi bagian C: rata-rata turun 0,19 butir, akurasi turun 0,96 poin persen.",
]:
    note(ws, r, t, 12, 40); r += 1
r += 1

secrow(ws, r, "D. TEMUAN", 12); r += 1
allv = [TIME[p][q] for p in NM for q in range(1, 21) if TIME[p].get(q) is not None]
tb_all = [TIME[p][q] for p in NM for q in range(1, 21) if TIME[p].get(q) is not None and CO[p][q - 1] == "C"]
ts_all = [TIME[p][q] for p in NM for q in range(1, 21) if TIME[p].get(q) is not None and CO[p][q - 1] == "X"]
for t in [
    "Rata-rata waktu per butir %.1f detik, dengan rentang %d sampai %d detik. Sebagai pembanding, pre-test yang dijalankan live "
    "mencatat rata-rata 17-18 detik per butir." % (st.mean(allv), min(allv), max(allv)),
    "Jawaban benar rata-rata memakan %.1f detik, jawaban salah %.1f detik — selisih %.1f detik. Peserta yang menjawab salah justru "
    "berpikir sedikit lebih lama, sehingga tidak ada bukti kesalahan disebabkan oleh terburu-buru."
    % (st.mean(tb_all), st.mean(ts_all), st.mean(ts_all) - st.mean(tb_all)),
    "Meskipun kuis dibuka tiga hari, tidak ada sesi tuntas yang memakai waktu ekstrem: yang tercepat 4 menit 28 detik dan yang terlama "
    "18 menit 41 detik. Artinya peserta mengerjakan dalam satu duduk, bukan mencicil selama tiga hari.",
    "Perlu dicatat bahwa waktu tercatat hanya menghitung durasi butir terbuka di layar. Dalam mode take-home, peserta dapat membuka "
    "materi pada perangkat lain tanpa terekam sebagai waktu pengerjaan. Karena itu waktu yang wajar pada tabel ini bukan bukti bahwa "
    "pengerjaan dilakukan tanpa membuka materi.",
]:
    note(ws, r, t, 12, 40); r += 1

wb.save("LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx")
print("saved sheets=%d charts=%d timecells=%d vincent_1s=%d"
      % (len(wb.sheetnames), sum(len(w._charts) for w in wb), tot_cells, v1))
