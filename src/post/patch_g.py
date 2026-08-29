# -*- coding: utf-8 -*-
import io

p = "pw_g.py"
s = io.open(p, encoding="utf-8").read()
BS = chr(92)  # backslash

old_head = ('head(ws, r, ["#", "Nama", "Benar", "Salah", "Kosong", "Dijawab", "Nilai", "Akurasi atas'
            + BS + 'nyang dijawab",\n'
            '             "Waktu", "Detik/butir", "Skor pre-test", "Gain", "Status sesi", "Kategori"],\n'
            '     [5, 26, 8, 8, 8, 9, 8, 13, 10, 11, 12, 8, 15, 16])')
new_head = ('head(ws, r, ["#", "Nama", "Benar", "Salah", "Kosong", "Dijawab", "Nilai", "Akurasi'
            + BS + 'nWayground",\n'
            '             "Poin' + BS + 'nWayground", "Waktu", "Detik/butir", "Skor pre-test", "Gain",\n'
            '             "Status sesi", "Kategori"],\n'
            '     [5, 26, 8, 8, 8, 9, 8, 11, 11, 10, 11, 12, 8, 15, 16])')
assert old_head in s, "header tidak cocok"
s = s.replace(old_head, new_head, 1)

old_row = '''    putrow(ws, r, [i, n, v, CO[n].count("X"), CO[n].count("-"), a_, round(nil),
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
        ws.cell(r, 12).fill = GRN if v > sc_pre[p] else (RED if v < sc_pre[p] else GRY)'''
new_row = '''    putrow(ws, r, [i, n, v, CO[n].count("X"), CO[n].count("-"), a_, round(nil),
                   PO[n]["acc"], PO[n]["score"],
                   "%d:%02d" % (PO[n]["time_s"] // 60, PO[n]["time_s"] % 60),
                   round(PO[n]["time_s"] / a_, 1) if a_ else 0,
                   ("%d/20" % sc_pre[p]) if p else "tidak ikut",
                   (v - sc_pre[p]) if p else "—",
                   "Tuntas" if tuntas else "Terputus (%d/20)" % a_, gr],
           ctr=tuple(range(1, 16)), bold=(2, 3), h=20)
    ws.cell(r, 9).fill = BLU
    ws.cell(r, 14).fill = GRN if tuntas else RED
    ws.cell(r, 15).fill = GRN if nil >= 70 else (YEL if nil >= 40 else RED)
    if p:
        ws.cell(r, 13).fill = GRN if v > sc_pre[p] else (RED if v < sc_pre[p] else GRY)'''
assert old_row in s, "baris tidak cocok"
s = s.replace(old_row, new_row, 1)

anchor = '"Korelasi waktu pengerjaan dengan jumlah benar pada sesi tuntas hanya r = 0,115'
i = s.index(anchor)
extra = ('    "Kolom Akurasi dan Poin Wayground disalin apa adanya dari sheet Participant Data ekspor resmi, '
         'disertakan agar setiap angka pada laporan ini dapat dicocokkan langsung ke berkas sumber. Poin Wayground '
         'memuat bonus kecepatan, sehingga peringkat poin TIDAK sama dengan peringkat kemampuan. Seluruh analisis '
         'akademik pada workbook ini memakai jumlah jawaban benar, bukan poin.",\n')
s = s[:i - 4] + extra + s[i - 4:]

io.open(p, "w", encoding="utf-8").write(s)
print("pw_g.py diperbarui")
