# -*- coding: utf-8 -*-
# ============================================================ 08 RANAH MATERI
ws = wb.create_sheet("08 Ranah Materi")
title(ws, "PENGUASAAN PER RANAH MATERI DAN PER LEVEL KOGNITIF",
      "Butir dikelompokkan ke enam ranah materi dan tiga level taksonomi Bloom. Penguasaan ranah dihitung sebagai total jawaban benar dibagi total kesempatan pada ranah tersebut. "
      "Sheet ini menjawab pertanyaan: materi apa yang paling perlu diprioritaskan pada hari pelatihan.", 12)

r = 4
secrow(ws, r, "A. PENGUASAAN PER RANAH MATERI", 12); r += 1
head(ws, r, ["Ranah materi", "Butir", "Jml\nbutir", "Kesempatan\njawab", "Benar", "Salah",
             "Kosong", "Penguasaan\n(dari total sel)", "Penguasaan atas\nyang dijawab",
             "Rata-rata p", "Prioritas", "Implikasi untuk pelatihan"],
     [26, 24, 7, 12, 8, 8, 8, 14, 15, 11, 11, 74])
r += 1
dom_rows = []
DOMS = defaultdict(list)
for it in items:
    DOMS[DOMAIN[it["no"]]].append(it)
order = sorted(DOMS.items(), key=lambda kv: st.mean(i["p"] for i in kv[1]))
arow0 = r
for dname, its in order:
    nos = [i["no"] for i in its]
    opp = len(its) * 37
    cor = sum(i["correct"] for i in its)
    wrg = sum(i["incorrect"] for i in its)
    blk = opp - cor - wrg
    mp = st.mean(i["p"] for i in its)
    pr = "TERTINGGI" if mp < .26 else ("Tinggi" if mp < .33 else "Sedang")
    IMPL = {
        "Teknis Output & Ukuran": "Sediakan lembar contekan ukuran kanvas dan tabel format ekspor. Ini hafalan murni yang tidak bisa dinalar, jadi berikan rujukannya, jangan diajarkan lewat ceramah.",
        "Materi Internal Pelatihan": "Wajar rendah - materi ini memang belum pernah disampaikan. Jangan dibaca sebagai kelemahan peserta. Ulangi butir-butir ini pada post-test untuk mengukur daya ingat isi pelatihan.",
        "Akses & Model Bisnis": "Buka pelatihan dengan praktik langsung: buat akun gratis di tempat. Miskonsepsi bahwa Canva harus dibayar adalah penghalang pertama yang harus dirobohkan.",
        "Prinsip Desain Grafis": "Ajarkan lewat contoh visual berdampingan (buruk versus baik), bukan definisi. Peserta sudah punya intuisi; yang kurang adalah kosakata dan alasannya.",
        "Sejarah & Profil": "Materi pelengkap, bukan prioritas. Cukup disebut sekilas di pembukaan.",
        "Konsep & Fitur Canva": "Ranah terkuat, tetapi tetap di bawah 40%. Gunakan sesi praktik terpandu: buka editor, tunjuk Panel Kiri, tunjuk Area Desain, langsung praktikkan.",
    }[dname]
    row = [dname, ", ".join("Q%d" % x for x in nos), len(its), opp, cor, wrg, blk,
           cor / opp, cor / (cor + wrg), round(mp, 3), pr, IMPL]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i in (3, 4, 5, 6, 7, 8, 9, 10, 11):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.cell(r, 1).font = Font(size=10, bold=True)
    ws.cell(r, 8).number_format = "0.0%"
    ws.cell(r, 9).number_format = "0.0%"
    ws.cell(r, 11).fill = {"TERTINGGI": RED, "Tinggi": YEL, "Sedang": F("D9EAD3")}[pr]
    ws.cell(r, 11).font = Font(size=10, bold=True)
    ws.row_dimensions[r].height = 44
    dom_rows.append((dname, cor / opp, mp))
    r += 1
arow1 = r - 1
r += 2

secrow(ws, r, "B. PENGUASAAN PER LEVEL KOGNITIF (TAKSONOMI BLOOM)", 12); r += 1
head(ws, r, ["Level", "Butir", "Jml\nbutir", "Kesempatan", "Benar", "Penguasaan",
             "Rata-rata p", "Rata-rata D", "Tafsiran", "", "", ""],
     [16, 30, 7, 11, 8, 12, 11, 11, 90])
r += 1
brow0 = r
BLS = defaultdict(list)
for it in items:
    BLS[BLOOM[it["no"]]].append(it)
TAF = {
    "C1 Mengingat": "Paling rendah (27,9%). Ini masuk akal karena separuh butir C1 menguji isi pelatihan yang belum disampaikan (Q13, Q17, Q19) dan fakta hafalan (Q10, Q14).",
    "C2 Memahami": "Tertinggi (35,9%). Peserta mampu menalar tentang fungsi dan konsep meski belum pernah memakai Canva secara serius. Modal awal yang baik.",
    "C3 Menerapkan": "27,9%, setara C1. Peserta belum bisa memilih tindakan yang tepat dalam situasi nyata - persis kesenjangan yang seharusnya ditutup oleh sesi praktik.",
}
for bname in ["C1 Mengingat", "C2 Memahami", "C3 Menerapkan"]:
    its = BLS[bname]
    nos = [i["no"] for i in its]
    opp = len(its) * 37
    cor = sum(i["correct"] for i in its)
    row = [bname, ", ".join("Q%d" % x for x in nos), len(its), opp, cor, cor / opp,
           round(st.mean(i["p"] for i in its), 3), round(st.mean(i["D"] for i in its), 3), TAF[bname]]
    for i, v in enumerate(row, 1):
        c = ws.cell(r, i, v); c.border = BOX; c.font = Font(size=10)
        if i in (3, 4, 5, 6, 7, 8):
            c.alignment = Alignment(horizontal="center")
        else:
            c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.merge_cells(start_row=r, start_column=9, end_row=r, end_column=12)
    ws.cell(r, 1).font = Font(size=10, bold=True)
    ws.cell(r, 6).number_format = "0.0%"
    ws.row_dimensions[r].height = 42
    r += 1
brow1 = r - 1
r += 2

secrow(ws, r, "C. PETA PENGUASAAN PER PESERTA PER RANAH (jumlah benar / jumlah butir ranah)", 12); r += 1
dnames = [d for d, _, _ in dom_rows]
head(ws, r, ["Nama"] + dnames + ["Total"], [24] + [22] * len(dnames) + [9])
r += 1
for n in sorted(P, key=lambda n: -sc[n]):
    c = ws.cell(r, 1, n); c.font = Font(size=10, bold=True); c.border = BOX
    for j, dn in enumerate(dnames, 2):
        nos = [i["no"] for i in DOMS[dn]]
        got = sum(1 for x in nos if CORR[n][x - 1] == "C")
        cell = ws.cell(r, j, "%d/%d" % (got, len(nos)))
        cell.alignment = Alignment(horizontal="center"); cell.border = BOX
        cell.font = Font(size=10)
        frac = got / len(nos)
        if frac >= .6:
            cell.fill = GRN
        elif frac >= .34:
            cell.fill = F("D9EAD3")
        elif frac > 0:
            cell.fill = YEL
        else:
            cell.fill = RED
    c = ws.cell(r, len(dnames) + 2, sc[n]); c.font = Font(bold=True, size=10)
    c.alignment = Alignment(horizontal="center"); c.border = BOX
    r += 1
ws.freeze_panes = "B%d" % (r - 37)
r += 2

for t in [
    "Urutan prioritas pelatihan berdasarkan data: (1) Teknis Output & Ukuran 20,3%, (2) Materi Internal Pelatihan 25,2%, (3) Akses & Model Bisnis 31,1%, (4) Prinsip Desain Grafis 35,1%, (5) Konsep & Fitur Canva 36,3%, (6) Sejarah & Profil 36,5%.",
    "Ranah Materi Internal Pelatihan (tujuan, slogan, nilai) sebaiknya dikeluarkan dari perhitungan kemampuan awal. Materinya belum pernah disampaikan, sehingga skor rendah di sana mengukur ketiadaan informasi, bukan ketiadaan kemampuan. Bila ketiga butir itu (Q13, Q17, Q19) dikeluarkan, akurasi kelas naik dari 32,3% menjadi 33,6%.",
    "Tidak ada satu pun peserta yang menguasai ranah Teknis Output & Ukuran secara penuh (2 dari 2). Ini kesenjangan yang seragam di seluruh kelas dan paling mudah ditutup: satu slide berisi tabel ukuran dan format sudah cukup.",
    "Level C2 (memahami) lebih tinggi daripada C3 (menerapkan) dengan selisih 8 poin persen. Pola ini khas peserta yang pernah mendengar tentang Canva tetapi belum pernah benar-benar memakainya. Implikasinya jelas: perbanyak porsi praktik, kurangi porsi penjelasan konsep.",
]:
    note(ws, r, t, 12, 40); r += 1
