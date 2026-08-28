# -*- coding: utf-8 -*-
# ============ 06 PESERTA + MATRIKS
ws = wb.create_sheet("06 Peserta dan Matriks")
title(ws, "PESERTA POST-TEST DAN MATRIKS RESPONS",
      "Sesi atas nama Vincent (QA tester) tidak ditampilkan. Peringkat memakai jumlah jawaban benar, bukan poin Wayground.", 14)
r = 4
secrow(ws, r, "A. DAFTAR PESERTA POST-TEST", 14); r += 1
head(ws, r, ["#", "Nama", "Benar", "Salah", "Kosong", "Dijawab", "Nilai", "Akurasi atas\nyang dijawab",
             "Waktu", "Detik/butir", "Skor pre-test", "Gain", "Status sesi", "Kategori"],
     [5, 26, 8, 8, 8, 9, 8, 13, 10, 11, 12, 8, 15, 16])
r += 1
a0 = r
mean_c = st.mean([sc_post[n] for n in COMP]); sd_c = st.pstdev([sc_post[n] for n in COMP])
for i, n in enumerate(ORDP, 1):
    p = pmap.get(n)
    v = sc_post[n]; a_ = att[n]
    nil = v / 20 * 100
    gr = "A Sangat Baik" if nil >= 85 else ("B Baik" if nil >= 70 else ("C Cukup" if nil >= 55 else ("D Kurang" if nil >= 40 else "E Sangat Kurang")))
    tuntas = a_ == 20
    putrow(ws, r, [i, n, v, CO[n].count("X"), CO[n].count("-"), a_, round(nil),
                   round(v / a_ * 100) if a_ else 0,
                   "%d:%02d" % (PO[n]["time_s"] // 60, PO[n]["time_s"] % 60),
                   round(PO[n]["time_s"] / a_, 1) if a_ else 0,
                   ("%d/20" % sc_pre[p]) if p else "tidak ikut",
                   (v - sc_pre[p]) if p else "—",
                   "Tuntas" if tuntas else "Terputus (%d/20)" % a_, gr],
           ctr=tuple(range(1, 14)), bold=(2, 3), h=20)
    ws.cell(r, 13).fill = GRN if tuntas else RED
    ws.cell(r, 14).fill = GRN if nil >= 70 else (YEL if nil >= 40 else RED)
    if p:
        ws.cell(r, 12).fill = GRN if v > sc_pre[p] else (RED if v < sc_pre[p] else GRY)
    r += 1
a1 = r - 1
r += 1

secrow(ws, r, "B. MATRIKS RESPONS — 15 SESI x 20 BUTIR  (hijau benar, merah salah, abu-abu tidak dijawab)", 14); r += 1
head(ws, r, ["Nama"] + ["Q%d" % i for i in range(1, 21)] + ["Benar"], [26] + [5] * 20 + [8])
r += 1
m0 = r
for n in ORDP:
    c = ws.cell(r, 1, n); c.font = Font(size=10, bold=True); c.border = BOX
    for qi in range(20):
        s_ = CO[n][qi]
        cell = ws.cell(r, qi + 2, {"C": "B", "X": "S", "-": ""}[s_])
        cell.border = BOX; cell.font = Font(size=9, bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.fill = {"C": GRN, "X": RED, "-": GRY}[s_]
    c = ws.cell(r, 22, sc_post[n]); c.font = Font(bold=True); c.border = BOX
    c.alignment = Alignment(horizontal="center")
    r += 1
c = ws.cell(r, 1, "Benar per butir"); c.font = Font(size=10, bold=True); c.border = BOX
for qi in range(20):
    cell = ws.cell(r, qi + 2, QO[qi + 1]["correct_excl"])
    cell.border = BOX; cell.font = Font(size=9, bold=True)
    cell.alignment = Alignment(horizontal="center")
    cell.fill = F(LGREY)
ws.cell(r, 22, sum(sc_post.values())).font = Font(bold=True)
ws.cell(r, 22).border = BOX
ws.cell(r, 22).alignment = Alignment(horizontal="center")
ws.freeze_panes = "B%d" % m0
r += 2

secrow(ws, r, "DATA GRAFIK — SEBARAN SKOR POST-TEST", 14); r += 1
h0 = r
ws.cell(r, 1, "Jawaban benar").fill = HDR; ws.cell(r, 1).font = WF; ws.cell(r, 1).border = BOX
ws.cell(r, 2, "Jumlah sesi").fill = HDR; ws.cell(r, 2).font = WF; ws.cell(r, 2).border = BOX
r += 1
cnt = Counter(sc_post.values())
for k in range(0, 21):
    ws.cell(r, 1, k).border = BOX; ws.cell(r, 1).alignment = Alignment(horizontal="center")
    ws.cell(r, 2, cnt.get(k, 0)).border = BOX; ws.cell(r, 2).alignment = Alignment(horizontal="center")
    r += 1
h1 = r - 1
ch = BarChart(); ch.type = "col"; ch.style = 10; ch.gapWidth = 20
ch.title = "Sebaran jumlah jawaban benar — post-test (15 sesi)"
ch.y_axis.title = "Jumlah sesi"; ch.x_axis.title = "Jawaban benar"
ch.height = 9; ch.width = 22
ch.add_data(Reference(ws, min_col=2, min_row=h0, max_row=h1), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=h0 + 1, max_row=h1))
ch.legend = None
ws.add_chart(ch, "D%d" % h0)

ch2 = ScatterChart(); ch2.style = 13
ch2.title = "Waktu pengerjaan versus jawaban benar (sesi tuntas)"
ch2.x_axis.title = "Menit"; ch2.y_axis.title = "Jawaban benar"
ch2.height = 9; ch2.width = 16
s0 = r + 2
ws.cell(s0, 1, "Menit").fill = HDR; ws.cell(s0, 1).font = WF
ws.cell(s0, 2, "Benar").fill = HDR; ws.cell(s0, 2).font = WF
rr = s0 + 1
for n in COMP:
    ws.cell(rr, 1, round(PO[n]["time_s"] / 60, 1))
    ws.cell(rr, 2, sc_post[n]); rr += 1
xs = Reference(ws, min_col=1, min_row=s0 + 1, max_row=rr - 1)
ys = Reference(ws, min_col=2, min_row=s0, max_row=rr - 1)
se = Series(ys, xs, title_from_data=True)
se.marker.symbol = "circle"; se.graphicalProperties.line.noFill = True
ch2.series.append(se)
ws.add_chart(ch2, "N%d" % h0)
r = rr + 2

for t in [
    "Sepuluh dari 15 sesi diselesaikan penuh. Lima sesi terputus, dan empat di antaranya berhenti dalam waktu kurang dari satu menit — pola yang menunjuk ke kendala perangkat atau tautan, bukan ke peserta yang menyerah setelah membaca soal.",
    "Yovita tercatat dua kali: satu sesi tuntas dengan 13 benar dan satu sesi nol jawaban. Sesi nol diabaikan dalam analisis berpasangan dan sesi terbaik yang dipakai, sesuai perlakuan yang sama pada laporan pre-test.",
    "Korelasi waktu pengerjaan dengan jumlah benar pada sesi tuntas hanya r = 0,115 — praktis nol. Mengerjakan lebih lama tidak menghasilkan skor lebih tinggi. Dalam mode take-home tiga hari, waktu tercatat tidak lagi menjadi ukuran usaha yang bermakna.",
    "Empat peserta post-test tidak mengikuti pre-test: Mien (18 benar), Netty Nusaly (12), Silvya Runturambi (7, sesi terputus). Nilai mereka tidak dapat dipakai untuk mengukur dampak pelatihan karena tidak ada titik awal pembanding.",
]:
    note(ws, r, t, 14, 44); r += 1
