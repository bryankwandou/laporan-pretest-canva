# -*- coding: utf-8 -*-
import re as _re
from difflib import SequenceMatcher as _SM


def _sim(a, b):
    return _SM(None, _re.sub(r"[^a-z0-9]", "", a.lower()), _re.sub(r"[^a-z0-9]", "", b.lower())).ratio()


# ============ 07 SOAL, KUNCI, DISTRAKTOR
ws = wb.create_sheet("07 Soal Kunci Distraktor")
title(ws, "NASKAH SOAL POST-TEST, KUNCI JAWABAN DAN SEBARAN PILIHAN SETIAP OPSI",
      "Naskah dan seluruh opsi diambil dari berkas cetak resmi Wayground. Kunci direkonstruksi dari data respons lalu diverifikasi "
      "terhadap naskah tersebut — cocok pada 20 dari 20 butir. Opsi bertanda [MATI] tidak dipilih oleh satu pun peserta.", 8)
r = 4
head(ws, r, ["Butir", "Naskah soal", "Opsi dan jumlah pemilih", "p", "D", "r-pbis", "Pengecoh\nhidup", "Catatan"],
     [7, 66, 74, 8, 8, 9, 11, 40])
r += 1
deadtot = 0
for n in range(1, 21):
    q = QO[n]
    chosen = dict(q["distr"])
    lines = []
    live = 0
    for let, txt in OPT[n]["opts"]:
        c_ = 0
        for o, k in chosen.items():
            if _sim(o, txt) >= .80:
                c_ = k
        iskey = _sim(txt, q["key"]) >= .80
        if iskey:
            lines.append("%s) [KUNCI] %s  — %d pemilih" % (let, txt, c_))
        elif c_ == 0:
            lines.append("%s) [MATI]  %s  — 0 pemilih" % (let, txt))
            deadtot += 1
        else:
            lines.append("%s) %s  — %d pemilih" % (let, txt, c_))
            live += 1
    cat = ("%d dari 3" % live)
    note_ = ""
    if live == 0:
        note_ = "Seluruh pengecoh mati. Butir efektif hanya menyisakan satu opsi masuk akal."
    elif live == 1:
        note_ = "Hanya satu pengecoh berfungsi. Peluang tebakan benar naik menjadi 50%."
    elif q["p"] < .30:
        note_ = "Butir tersukar. Pengecohnya justru terlalu kuat."
    putrow(ws, r, [n, q["text"], "\n".join(lines), round(q["p"], 2), round(q["D"], 2),
                   round(q["rpb"], 2), cat, note_], ctr=(1, 4, 5, 6, 7), bold=(1,), h=86, fsz=9)
    ws.cell(r, 1).fill = HDR; ws.cell(r, 1).font = Font(size=11, bold=True, color="FFFFFF")
    ws.cell(r, 7).fill = RED if live <= 1 else (YEL if live == 2 else GRN)
    r += 1
ws.freeze_panes = "B5"
r += 1

secrow(ws, r, "PENGECOH MATI — REKAPITULASI", 8); r += 1
note(ws, r, "Dari 60 opsi salah pada post-test, %d (%.0f%%) tidak dipilih oleh satu pun peserta. "
            "Pengecoh yang tidak pernah dipilih tidak menyumbang informasi apa pun dan secara efektif memperkecil jumlah opsi. "
            "Pada Q8, Q19 dan Q20 ketiga pengecohnya mati sekaligus, sehingga butirnya praktis hanya menyisakan kunci sebagai satu-satunya pilihan masuk akal — "
            "peluang menjawab benar dengan menebak naik dari 25%% menjadi 100%% pada butir semacam itu."
     % (deadtot, deadtot / 60 * 100), 8, 60)
r += 2

head(ws, r, ["Butir", "Opsi mati", "Teks opsi yang tidak pernah dipilih", "", "", "", "", ""], [8, 10, 110])
r += 1
for n in sorted(DEAD):
    for let, txt in DEAD[n]:
        putrow(ws, r, ["Q%d" % n, "%s)" % let, txt], ctr=(1, 2), bold=(1,), h=18, fsz=9)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
        ws.cell(r, 2).fill = RED
        r += 1
r += 1
for t in [
    "Pengecoh mati bukan sekadar cacat teknis. Butir dengan tiga pengecoh mati mengukur hampir tidak ada: peserta yang sama sekali tidak tahu jawabannya pun kemungkinan besar akan memilih kunci, karena ketiga pilihan lain terbaca jelas keliru. Q8 (p=0,73) dan Q20 (p=0,67) — dua butir termudah pada post-test — keduanya berada dalam kondisi ini.",
    "Perbaikan yang disarankan: tulis ulang pengecoh agar setiap opsi merupakan kekeliruan yang benar-benar mungkin dipercaya seseorang. Sumber terbaik untuk menulis pengecoh yang baik adalah jawaban salah yang nyata muncul pada tes sebelumnya — laporan pre-test memuat daftar miskonsepsi yang dapat langsung dipakai.",
]:
    note(ws, r, t, 8, 46); r += 1
