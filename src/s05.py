# -*- coding: utf-8 -*-
# ============================================================ 05 ANALISIS PENGECOH
ws = wb.create_sheet("05 Analisis Pengecoh")
title(ws, "ANALISIS PENGECOH (DISTRACTOR ANALYSIS) — SETIAP OPSI, SETIAP BUTIR",
      "Setiap opsi jawaban yang benar-benar dipilih peserta ditampilkan beserta jumlah pemilih, persentase terhadap penjawab butir tersebut, dan sebaran pemilih di kelompok atas versus bawah. "
      "Pengecoh yang sehat dipilih minimal 5% penjawab dan lebih banyak dipilih kelompok bawah daripada kelompok atas. "
      "Opsi yang dipilih lebih banyak oleh kelompok atas adalah tanda soal menjebak atau kunci meragukan.", 10)
cols = ["Butir", "Ranah", "Opsi jawaban", "Status", "Dipilih", "% dari\npenjawab",
        "Kelompok\natas (10)", "Kelompok\nbawah (10)", "Selisih\natas−bawah", "Diagnosis"]
head(ws, 4, cols, [7, 22, 96, 10, 9, 11, 10, 10, 11, 46])
upper = set(S["upper"]); lower_names = S["lower"]
UP = [n for n in P if n in upper]
# rebuild exact upper/lower name lists (may contain duplicate base names)
ORDR = sorted(P, key=lambda n: -sc[n])
UPN = ORDR[:10]; LWN = ORDR[-10:]
r = 5
for it in items:
    no = it["no"]
    q = [x for x in Q if x["no"] == no][0]
    resp = it["correct"] + it["incorrect"]
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
    c = ws.cell(r, 1, "Q%d  ·  %s  ·  %s  ·  p=%.2f  ·  D=%.2f  ·  %d penjawab dari 37  —  %s"
                % (no, SHORT[no], DOMAIN[no], it["p"], it["D"], resp, q["text"].replace("\n", " ")))
    c.fill = SUBF; c.font = Font(color="FFFFFF", bold=True, size=10)
    c.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
    ws.row_dimensions[r].height = 30
    r += 1
    for a, cnt in it["distr"]:
        iskey = (a == it["key"])
        u = sum(1 for n in UPN if q["answers_real"].get(n) == a)
        l = sum(1 for n in LWN if q["answers_real"].get(n) == a)
        share = cnt / resp
        if iskey:
            diag = "KUNCI. Dipilih %d dari %d penjawab." % (cnt, resp)
            if u - l >= 4:
                diag += " Sangat diskriminatif."
            elif u - l <= 0:
                diag += " PERINGATAN: kunci tidak lebih dipilih kelompok atas."
        elif share < 0.05:
            diag = "Pengecoh mati — hampir tak ada yang tergoda. Ganti opsi ini."
        elif u > l:
            diag = "Pengecoh menjebak justru bagi peserta kuat. Periksa kembali redaksinya."
        elif share >= 0.30:
            diag = "MISKONSEPSI DOMINAN — wajib dibahas eksplisit saat pelatihan."
        else:
            diag = "Pengecoh berfungsi normal."
        row = [no, DOMAIN[no], a, "KUNCI" if iskey else "pengecoh", cnt, share, u, l, u - l, diag]
        for i, v in enumerate(row, 1):
            cc = ws.cell(r, i, v); cc.border = BOX; cc.font = Font(size=10)
            if i in (1, 4, 5, 6, 7, 8, 9):
                cc.alignment = Alignment(horizontal="center")
            else:
                cc.alignment = Alignment(wrap_text=True, vertical="center")
        ws.cell(r, 6).number_format = "0.0%"
        if iskey:
            for i in range(1, 11):
                ws.cell(r, i).fill = GRN
            ws.cell(r, 3).font = Font(size=10, bold=True)
        elif share >= 0.30:
            for i in range(3, 11):
                ws.cell(r, i).fill = RED
        elif share < 0.05:
            for i in range(3, 11):
                ws.cell(r, i).fill = F("EDEDED")
        ws.row_dimensions[r].height = 24
        r += 1
    r += 1
ws.freeze_panes = "A5"

secrow(ws, r, "SEPULUH MISKONSEPSI TERBESAR YANG HARUS DIBONGKAR SAAT PELATIHAN", 10); r += 1
head(ws, r, ["No", "Butir", "Miskonsepsi (opsi salah yang dipilih)", "Pemilih",
             "% penjawab", "Ranah", "Yang sebenarnya benar", "", "", ""])
r += 1
MIS = []
for it in items:
    resp = it["correct"] + it["incorrect"]
    for a, cnt in it["distr"]:
        if a != it["key"]:
            MIS.append((cnt / resp, cnt, it, a, resp))
MIS.sort(reverse=True, key=lambda x: (x[0], x[1]))
for idx, (share, cnt, it, a, resp) in enumerate(MIS[:10], 1):
    ws.cell(r, 1, idx).alignment = Alignment(horizontal="center")
    ws.cell(r, 2, "Q%d" % it["no"]).alignment = Alignment(horizontal="center")
    ws.cell(r, 3, a).alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 4, cnt).alignment = Alignment(horizontal="center")
    c = ws.cell(r, 5, share); c.number_format = "0.0%"; c.alignment = Alignment(horizontal="center")
    ws.cell(r, 6, DOMAIN[it["no"]]).alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=10)
    ws.cell(r, 7, it["key"]).alignment = Alignment(wrap_text=True, vertical="center")
    for i in range(1, 11):
        ws.cell(r, i).border = BOX; ws.cell(r, i).font = Font(size=10)
    ws.cell(r, 3).fill = RED
    ws.cell(r, 7).fill = GRN
    ws.row_dimensions[r].height = 30
    r += 1
