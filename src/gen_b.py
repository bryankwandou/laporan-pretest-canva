# -*- coding: utf-8 -*-
NAV = [("ringkasan", "Ringkasan"), ("temuan", "Temuan Utama"), ("sebaran", "Sebaran Skor"),
       ("butir", "Analisis Butir"), ("ranah", "Ranah &amp; Kognitif"), ("segmen", "Segmentasi"),
       ("peserta", "Peringkat Peserta"), ("matriks", "Matriks Respons"),
       ("miskonsepsi", "Miskonsepsi"), ("waktu", "Waktu"), ("rekomendasi", "Rekomendasi"),
       ("metode", "Metodologi"), ("unduh", "Unduh")]

it_ = {i["no"]: i for i in items}

# ===== 01 RINGKASAN
sec("ringkasan", "01", "Ringkasan Eksekutif",
    "Pre-test Pelatihan Canva — Wanita Katolik RI, 25 Agustus 2026. Diselenggarakan melalui Wayground (Quizizz) dengan 20 butir pilihan ganda. Seluruh angka pada laporan ini diverifikasi silang antara snapshot HTML laporan admin dan berkas ekspor resmi XLSX; kecocokan tercapai pada 20 dari 20 butir.")
KPI = [
    ("Sesi terekam", "37", "33 sesi aktif, 4 sesi nol jawaban"),
    ("Butir soal", "20", "pilihan ganda, 3–4 opsi"),
    ("Akurasi kelas", "%.1f%%" % (acc_all * 100), "%.1f%% bila dihitung atas sesi aktif" % (acc_act * 100)),
    ("Rata-rata benar", "%.2f" % mean, "dari 20 butir · simpangan baku %.2f" % sd),
    ("Reliabilitas KR-20", "%.3f" % kr20, "kategori cukup untuk keputusan kelompok"),
    ("Kesalahan baku ukur", "±%.2f" % sem, "butir — selisih di bawah ini tidak bermakna"),
    ("Median / Q1 / Q3", "%d / %d / %d" % (med, q1, q3), "rentang antarkuartil %d butir" % (q3 - q1)),
    ("Sel tidak terjawab", "%d" % tot_b, "%.1f%% dari %d sel" % (tot_b / tot_cells * 100, tot_cells)),
]
A('<div class="kpis">')
for k, v, s_ in KPI:
    A('<div class="kpi"><div class="kl">%s</div><div class="kv">%s</div><div class="ks">%s</div></div>' % (k, v, s_))
A("</div>")
note("<strong>Kesimpulan singkat.</strong> Kemampuan awal peserta terhadap Canva berada pada tingkat sangat rendah dan merata. Akurasi %.1f%% hanya sedikit di atas peluang tebakan acak (25%%), dan tidak ada satu pun peserta yang mencapai kategori Sangat Baik. Kelemahan terbesar bersifat prosedural, bukan konseptual — implikasinya tegas: porsi praktik harus melebihi porsi ceramah." % (acc_all * 100))
endsec()

# ===== 02 TEMUAN
sec("temuan", "02", "Sepuluh Temuan Utama",
    "Setiap temuan disertai angka yang dapat ditelusuri ke tabel pada bagian berikutnya.")
q17 = it_[17]; q1i = it_[1]
mD = st.mean(i["D"] for i in items)
FIND = [
    ("Tidak ada peserta pada kategori Sangat Baik",
     "Skor tertinggi %d dari 20 butir. Ambang ketuntasan 70%% (14 butir) hanya dicapai %d sesi dari 37."
     % (max(vals), sum(1 for v in vals if v >= 14))),
    ("Instrumen bekerja dengan baik",
     "KR-20 %.3f dan rata-rata daya beda %.3f. Sembilan belas dari dua puluh butir berfungsi sebagaimana mestinya." % (kr20, mD)),
    ("Butir Q17 gagal total",
     "Daya beda %.2f dan r-pbis %.2f. Nol jawaban benar baik pada kelompok atas maupun bawah — butir ini tidak menyumbang informasi apa pun dan harus dikeluarkan dari penilaian." % (q17["D"], q17["rpb"])),
    ("Penghalang pertama adalah akses, bukan desain",
     "Q1 (langkah pertama membuat akun) p=%.2f — hanya %d dari %d penjawab benar. Enam orang mengira harus menunggu panitia membagikan akun bersama."
     % (q1i["p"], q1i["correct"], q1i["correct"] + q1i["incorrect"])),
    ("Ranah terlemah: Teknis Output &amp; Ukuran",
     "Penguasaan 20,3%. Tidak ada satu pun peserta yang menguasai kedua butirnya. Ini hafalan murni yang paling cepat ditutup dengan satu lembar rujukan."),
    ("Memahami lebih tinggi daripada menerapkan",
     "C2 35,9% berbanding C3 27,9%. Pola khas peserta yang pernah mendengar tentang Canva tetapi belum pernah benar-benar memakainya."),
    ("Kesenjangan skor berasal dari jumlah butir terjawab",
     "Kelompok atas mengirim rata-rata %.1f jawaban, kelompok bawah %.1f — selisih %.1f butir, sementara selisih jawaban benar hanya %.1f butir."
     % (st.mean(att[n] for n in UPN), st.mean(att[n] for n in LWN),
        st.mean(att[n] for n in UPN) - st.mean(att[n] for n in LWN),
        st.mean(sc[n] for n in UPN) - st.mean(sc[n] for n in LWN))),
    ("Kehilangan data terkonsentrasi di butir awal",
     "Q1 kehilangan %d dari 37 sel, Q2 %d sel, Q3 %d sel, lalu menurun tajam. Pola khas keterlambatan bergabung, bukan menyerah di tengah jalan."
     % (it_[1]["blank"], it_[2]["blank"], it_[3]["blank"])),
    ("Empat sesi tidak menghasilkan satu jawaban pun",
     "Keempatnya mencatat waktu total di bawah 30 detik. Ini kegagalan teknis, bukan hasil ujian, dan tidak boleh dipakai sebagai garis dasar pembanding post-test."),
    ("Tidak ada pertukaran kecepatan dan ketepatan",
     "Rata-rata sekitar 17 detik untuk jawaban benar berbanding 19 detik untuk jawaban salah. Peserta tidak salah karena terburu-buru."),
]
A('<ol class="findings">')
for t, b in FIND:
    A("<li><strong>%s</strong><span>%s</span></li>" % (t, b))
A("</ol>")
endsec()

# ===== 03 SEBARAN
sec("sebaran", "03", "Sebaran Skor",
    "Distribusi jumlah jawaban benar atas 37 sesi. Konversi nilai memakai 5 poin per butir benar.")
cnt = Counter(vals)
A(vbars([(str(k), cnt.get(k, 0), pcol(k / 20)) for k in range(0, max(vals) + 1)]))
A('<p class="cap">Jumlah sesi menurut jumlah jawaban benar (0–%d dari 20 butir).</p>' % max(vals))
gc = Counter(grade(v) for v in vals)
A('<table><thead><tr><th>Kategori nilai</th><th>Rentang benar</th><th class="n">Jumlah sesi</th><th class="n">Proporsi</th></tr></thead><tbody>')
for lab, rng in [("A — Sangat Baik", "17–20"), ("B — Baik", "14–16"), ("C — Cukup", "11–13"),
                 ("D — Kurang", "8–10"), ("E — Sangat Kurang", "0–7")]:
    c_ = gc.get(lab, 0)
    A('<tr><td class="b">%s</td><td class="s">%s</td><td class="n">%d</td><td class="n">%.1f%%</td></tr>' % (lab, rng, c_, c_ / N * 100))
A("</tbody></table>")
note("Sebaran menumpuk di ujung bawah: %d dari 37 sesi (%.0f%%) masuk kategori Sangat Kurang. Dengan kesalahan baku ukur ±%.2f butir, peserta dengan 9 benar dan 7 benar secara statistik tidak dapat dibedakan — peringkat individu tidak layak dipakai untuk keputusan perorangan."
     % (gc.get("E — Sangat Kurang", 0), gc.get("E — Sangat Kurang", 0) / N * 100, sem))
endsec()

# ===== 04 BUTIR
sec("butir", "04", "Analisis Butir",
    "Tingkat kesukaran (p) adalah proporsi benar atas 37 sesi. Daya beda (D) adalah selisih proporsi benar kelompok atas dan bawah, masing-masing 10 sesi. r-pbis adalah korelasi butir dengan skor total. Keputusan mengikuti ambang Ebel &amp; Frisbie.")
A(hbar([("Q%d · %s" % (i["no"], SHORT[i["no"]][:24]), i["p"], "%.0f%%" % (i["p"] * 100))
        for i in sorted(items, key=lambda x: -x["p"])], maxv=1.0, w=700, labw=250, colorfn=pcol))
A('<p class="cap">Tingkat kesukaran per butir, terurut dari termudah. Merah = sukar (p&lt;0,30), kuning = sedang, hijau = mudah.</p>')
A('<div class="scroll"><table class="dense"><thead><tr><th>Butir</th><th>Pokok yang diuji</th><th>Ranah</th><th>Bloom</th><th class="n">p</th><th>Kategori</th><th class="n">Atas</th><th class="n">Bawah</th><th class="n">D</th><th class="n">r-pbis</th><th class="n">Kosong</th><th>Keputusan</th></tr></thead><tbody>')
for it in sorted(items, key=lambda i: i["no"]):
    p, d, r = it["p"], it["D"], it["rpb"]
    kat = "Sukar" if p < .30 else ("Sedang" if p <= .70 else "Mudah")
    if d < .20 or r < .20:
        dec, dc = "Buang / tulis ulang", "bad"
    elif d >= .40 and .30 <= p <= .70:
        dec, dc = "Unggulan — pertahankan", "good"
    elif d >= .30:
        dec, dc = "Pertahankan", "good"
    else:
        dec, dc = "Revisi redaksi opsi", "warn"
    A('<tr><td class="b">Q%d</td><td>%s</td><td class="s">%s</td><td class="s">%s</td><td class="n">%.2f</td><td><span class="tag %s">%s</span></td><td class="n">%d</td><td class="n">%d</td><td class="n b">%.2f</td><td class="n">%.2f</td><td class="n">%d</td><td><span class="tag %s">%s</span></td></tr>'
      % (it["no"], E(SHORT[it["no"]]), E(DOMAIN[it["no"]]), E(BLOOM[it["no"]]), p,
         {"Sukar": "bad", "Sedang": "warn", "Mudah": "good"}[kat], kat, it["U"], it["L"], d, r, it["blank"], dc, dec))
A("</tbody></table></div>")
A(hbar([("Q%d" % i["no"], max(i["D"], 0), "%.2f" % i["D"]) for i in sorted(items, key=lambda x: -x["D"])],
       maxv=1.0, w=620, labw=60, rowh=22, colorfn=dcol))
A('<p class="cap">Daya beda per butir. Hijau ≥0,40 sangat baik · biru 0,30–0,39 baik · kuning 0,20–0,29 perlu revisi · merah &lt;0,20 ditolak.</p>')
endsec()

# ===== 05 RANAH
sec("ranah", "05", "Penguasaan per Ranah Materi dan Level Kognitif",
    "Penguasaan dihitung sebagai total jawaban benar dibagi total kesempatan menjawab pada ranah tersebut. Urutan pada tabel menjawab satu pertanyaan: materi apa yang paling perlu diprioritaskan pada hari pelatihan.")
DOMS = defaultdict(list)
for it in items:
    DOMS[DOMAIN[it["no"]]].append(it)
dord = sorted(DOMS.items(), key=lambda kv: sum(i["correct"] for i in kv[1]) / (len(kv[1]) * N))
A(hbar([(d, sum(i["correct"] for i in its) / (len(its) * N),
         "%.1f%%" % (sum(i["correct"] for i in its) / (len(its) * N) * 100)) for d, its in dord],
       maxv=.5, w=680, labw=200, rowh=30, colorfn=pcol))
A('<p class="cap">Penguasaan per ranah materi, terurut dari terlemah. Skala maksimum 50%.</p>')
IMPL = {
    "Teknis Output & Ukuran": "Sediakan lembar rujukan ukuran kanvas dan tabel format ekspor. Ini hafalan murni yang tidak bisa dinalar — berikan rujukannya, jangan diajarkan lewat ceramah.",
    "Materi Internal Pelatihan": "Wajar rendah — materi ini memang belum pernah disampaikan. Jangan dibaca sebagai kelemahan peserta. Ulangi butirnya pada post-test untuk mengukur daya ingat isi pelatihan.",
    "Akses & Model Bisnis": "Buka pelatihan dengan praktik langsung: buat akun gratis di tempat. Miskonsepsi bahwa Canva harus dibayar adalah penghalang pertama yang harus dirobohkan.",
    "Prinsip Desain Grafis": "Ajarkan lewat contoh visual berdampingan (buruk versus baik), bukan definisi. Peserta sudah punya intuisi; yang kurang adalah kosakata dan alasannya.",
    "Sejarah & Profil": "Materi pelengkap, bukan prioritas. Cukup disebut sekilas di pembukaan.",
    "Konsep & Fitur Canva": "Ranah terkuat, tetapi tetap di bawah 40%. Gunakan sesi praktik terpandu: buka editor, tunjuk Panel Kiri, tunjuk Area Desain, langsung praktikkan.",
}
A('<table><thead><tr><th class="n">Prioritas</th><th>Ranah materi</th><th>Butir</th><th class="n">Benar</th><th class="n">Kesempatan</th><th class="n">Penguasaan</th><th>Implikasi untuk pelatihan</th></tr></thead><tbody>')
for i_, (d, its) in enumerate(dord, 1):
    cor = sum(x["correct"] for x in its); opp = len(its) * N
    A('<tr><td class="n b">%d</td><td class="b">%s</td><td class="s">%s</td><td class="n">%d</td><td class="n">%d</td><td class="n b">%.1f%%</td><td class="s">%s</td></tr>'
      % (i_, E(d), ", ".join("Q%d" % x["no"] for x in its), cor, opp, cor / opp * 100, E(IMPL[d])))
A("</tbody></table>")
BLS = defaultdict(list)
for it in items:
    BLS[BLOOM[it["no"]]].append(it)
A("<h3>Level kognitif (taksonomi Bloom)</h3>")
A(vbars([(b, round(sum(i["correct"] for i in BLS[b]) / (len(BLS[b]) * N) * 100), ACC) for b in sorted(BLS)], w=460, h=200))
A('<p class="cap">Penguasaan (persen) menurut level kognitif.</p>')
note("Level C2 (memahami) lebih tinggi daripada C3 (menerapkan) dengan selisih sekitar 8 poin persen. Peserta mampu menalar tentang fungsi dan konsep, tetapi belum bisa memilih tindakan yang tepat dalam situasi nyata — persis kesenjangan yang seharusnya ditutup oleh sesi praktik.")
endsec()
