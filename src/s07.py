# -*- coding: utf-8 -*-
# ============================================================ 07 ANALISIS WAKTU
ws = wb.create_sheet("07 Analisis Waktu")
title(ws, "ANALISIS WAKTU PENGERJAAN — PER BUTIR DAN PER PESERTA",
      "Waktu dalam detik. Sel kosong berarti butir tidak dijawab. Warna semakin merah berarti semakin lama. "
      "Analisis waktu mengungkap butir yang membingungkan (lama tetapi banyak salah) dan butir yang dijawab asal-asalan (cepat tetapi banyak salah).", 24)

# A. per butir
r = 4
secrow(ws, r, "A. STATISTIK WAKTU PER BUTIR", 24); r += 1
head(ws, r, ["Butir", "Pokok yang diuji", "Penjawab", "Rata-rata\n(detik)", "Median",
             "Minimum", "Maksimum", "SD", "Waktu rata-rata\nJAWABAN BENAR",
             "Waktu rata-rata\nJAWABAN SALAH", "Selisih\nsalah−benar", "p", "Diagnosis waktu"],
     [7, 34, 10, 11, 9, 9, 10, 8, 15, 15, 11, 8, 58])
r += 1
trow0 = r
for it in items:
    no = it["no"]
    ts = [TIME[n][no] for n in P if TIME[n].get(no) is not None]
    tc = [TIME[n][no] for n in P if CORR[n][no - 1] == "C" and TIME[n].get(no) is not None]
    tx = [TIME[n][no] for n in P if CORR[n][no - 1] == "X" and TIME[n].get(no) is not None]
    mc = st.mean(tc) if tc else 0
    mx = st.mean(tx) if tx else 0
    diff = mx - mc
    if it["p"] < .30 and st.mean(ts) > 22:
        diag = "LAMA DAN BANYAK SALAH — materi benar-benar tidak dikuasai, bukan sekadar kurang teliti"
    elif it["p"] < .30 and st.mean(ts) <= 16:
        diag = "CEPAT TETAPI BANYAK SALAH — peserta merasa yakin padahal keliru; miskonsepsi kuat"
    elif it["p"] >= .40 and st.mean(ts) <= 18:
        diag = "Cepat dan banyak benar — pengetahuan yang sudah mapan"
    elif diff > 4:
        diag = "Yang salah butuh waktu jauh lebih lama — peserta ragu lalu menebak"
    else:
        diag = "Pola waktu normal"
    row = [no, SHORT[no], len(ts), round(st.mean(ts), 1), st.median(ts), min(ts), max(ts),
           round(st.pstdev(ts), 1), round(mc, 1), round(mx, 1), round(diff, 1),
           round(it["p"], 2), diag]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i not in (2, 13):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 1).font = Font(bold=True, size=10)
    if diag.startswith("LAMA"):
        ws.cell(r, 13).fill = RED
    elif diag.startswith("CEPAT"):
        ws.cell(r, 13).fill = YEL
    elif diag.startswith("Cepat dan"):
        ws.cell(r, 13).fill = GRN
    ws.row_dimensions[r].height = 26
    r += 1
trow1 = r - 1
ws.conditional_formatting.add("D%d:D%d" % (trow0, trow1),
                              ColorScaleRule(start_type="min", start_color="63BE7B",
                                             end_type="max", end_color="F8696B"))
r += 2

# B. matriks waktu
secrow(ws, r, "B. MATRIKS WAKTU 37 SESI × 20 BUTIR (detik)", 24); r += 1
head(ws, r, ["#", "Nama"] + ["Q%d" % i for i in range(1, 21)] + ["Total", "Rata-rata"],
     [5, 24] + [5] * 20 + [8, 10])
r += 1
mrow0 = r
ORD = sorted(P, key=lambda n: (-sc[n], -sco[n]))
for idx, n in enumerate(ORD, 1):
    ws.cell(r, 1, idx).border = BOX
    c = ws.cell(r, 2, n); c.font = Font(size=10, bold=True); c.border = BOX
    got = []
    for qi in range(1, 21):
        v = TIME[n].get(qi)
        cell = ws.cell(r, 2 + qi, v if v is not None else "")
        cell.border = BOX; cell.font = Font(size=9)
        cell.alignment = Alignment(horizontal="center")
        if v is None:
            cell.fill = F("EDEDED")
        elif CORR[n][qi - 1] == "C":
            cell.font = Font(size=9, bold=True, color="006100")
        else:
            cell.font = Font(size=9, color="9C0006")
        if v is not None:
            got.append(v)
    c = ws.cell(r, 23, sum(got)); c.border = BOX; c.font = Font(size=10, bold=True)
    c.alignment = Alignment(horizontal="center")
    c = ws.cell(r, 24, round(st.mean(got), 1) if got else ""); c.border = BOX
    c.alignment = Alignment(horizontal="center"); c.font = Font(size=10)
    r += 1
mrow1 = r - 1
ws.conditional_formatting.add("C%d:V%d" % (mrow0, mrow1),
                              ColorScaleRule(start_type="num", start_value=0, start_color="FFFFFF",
                                             mid_type="num", mid_value=20, mid_color="FFE699",
                                             end_type="num", end_value=45, end_color="F8696B"))
r += 2

secrow(ws, r, "C. APA YANG DIKATAKAN DATA WAKTU", 24); r += 1
slow = sorted(items, key=lambda i: -st.mean([TIME[n][i["no"]] for n in P if TIME[n].get(i["no"])]))[:3]
fast = sorted(items, key=lambda i: st.mean([TIME[n][i["no"]] for n in P if TIME[n].get(i["no"])]))[:3]
for t in [
    "Waktu rata-rata jawaban benar 17,1 detik, jawaban salah 18,6 detik. Selisihnya hanya 1,5 detik. Artinya peserta yang salah bukan sedang berpikir lebih keras - mereka sama-sama menebak, hanya sedikit lebih ragu.",
    "Butir paling lama dikerjakan: Q%d (%s), Q%d (%s), Q%d (%s). Ketiganya menuntut membaca opsi panjang dan membandingkan beberapa pernyataan sekaligus - beban baca, bukan beban berpikir." % (
        slow[0]["no"], SHORT[slow[0]["no"]], slow[1]["no"], SHORT[slow[1]["no"]], slow[2]["no"], SHORT[slow[2]["no"]]),
    "Butir paling cepat dijawab: Q%d (%s), Q%d (%s), Q%d (%s). Bila butir cepat sekaligus banyak salah, itu tanda peserta merasa sudah tahu padahal keliru - jenis miskonsepsi yang paling sulit dikoreksi karena peserta tidak merasa perlu bertanya." % (
        fast[0]["no"], SHORT[fast[0]["no"]], fast[1]["no"], SHORT[fast[1]["no"]], fast[2]["no"], SHORT[fast[2]["no"]]),
    "Total waktu yang dihabiskan seluruh peserta: %d menit %d detik untuk 541 jawaban. Jika pelatihan hendak mengulang kuis ini sebagai post-test, alokasikan 12–15 menit dan pastikan seluruh peserta sudah masuk sebelum butir pertama tampil." % (
        sum(tt.values()) // 60, sum(tt.values()) % 60),
    "Peserta dengan waktu total terpanjang (Elisabet bunga, 8 menit 32 detik) hanya memperoleh 6 jawaban benar, sedangkan Yovita menyelesaikan dalam 3 menit 40 detik dengan 10 benar. Lamanya waktu bukan indikator kesungguhan pada tes jenis ini.",
]:
    note(ws, r, t, 24, 34); r += 1
