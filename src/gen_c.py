# -*- coding: utf-8 -*-
# ===== 06 SEGMENTASI
sec("segmen", "06", "Segmentasi Peserta",
    "Empat segmen berdasarkan jumlah jawaban benar, masing-masing dengan perlakuan yang disarankan pada hari pelatihan.")
SEG = [("Siap jadi asisten", "12 benar ke atas", lambda n: sc[n] >= 12, "good",
        "Sudah mengenal Canva. Jadikan pendamping meja saat sesi praktik; beri tugas tambahan membuat template komunitas."),
       ("Siap ikut penuh", "8–11 benar", lambda n: 8 <= sc[n] <= 11, "ok",
        "Fondasi cukup. Bisa mengikuti kecepatan normal. Fokuskan pada praktik ekspor dan ukuran kanvas."),
       ("Perlu pendampingan", "1–7 benar", lambda n: 1 <= sc[n] <= 7, "warn",
        "Kelompok terbesar. Butuh langkah demi langkah di layar besar, jangan hanya instruksi lisan. Pastikan setiap orang berhasil membuat satu desain utuh sebelum lanjut."),
       ("Sesi tidak valid", "0 benar, 0 jawaban", lambda n: sc[n] == 0, "mut",
        "Bukan indikator kemampuan. Hubungi kembali, pastikan perangkat dan koneksi siap sebelum hari pelatihan.")]
A('<div class="segs">')
for nm, kr, fn, cl, act in SEG:
    who = [n for n in ORDR if fn(n)]
    A('<div class="seg %s"><div class="segh"><span class="segn">%d</span><div><strong>%s</strong><em>%s</em></div></div><p class="segp">%s</p><p class="segw">%s</p></div>'
      % (cl, len(who), nm, kr, act, E(", ".join(who))))
A("</div>")
A("<h3>Profil kelompok atas, tengah dan bawah</h3>")
A('<table><thead><tr><th>Indikator</th><th class="n">Atas (10)</th><th class="n">Tengah (17)</th><th class="n">Bawah (10)</th><th class="n">Selisih atas−bawah</th></tr></thead><tbody>')
RW = [("Rata-rata jawaban benar", lambda L: round(st.mean(sc[n] for n in L), 2)),
      ("Rata-rata jawaban terkirim", lambda L: round(st.mean(att[n] for n in L), 1)),
      ("Rata-rata sel kosong", lambda L: round(st.mean(CORR[n].count("-") for n in L), 1)),
      ("Akurasi atas butir yang dijawab (%)", lambda L: round(sum(sc[n] for n in L) / max(1, sum(att[n] for n in L)) * 100, 1)),
      ("Rata-rata waktu total (detik)", lambda L: round(st.mean(tt[n] for n in L))),
      ("Rata-rata detik per butir dijawab", lambda L: round(st.mean([tt[n] / max(1, att[n]) for n in L]), 1))]
for lab, fn in RW:
    a, m_, b = fn(UPN), fn(MID), fn(LWN)
    A('<tr><td>%s</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td><td class="n b">%s</td></tr>' % (lab, a, m_, b, round(a - b, 2)))
A("</tbody></table>")
note("Kelompok atas mengirim rata-rata %.1f jawaban, kelompok bawah %.1f — selisih %.1f butir, sementara selisih jawaban benar hanya %.1f butir. Artinya hampir seluruh kesenjangan skor dapat dijelaskan oleh perbedaan jumlah butir yang sempat dijawab, bukan oleh perbedaan ketepatan. Hambatan utamanya teknis, bukan kognitif."
     % (st.mean(att[n] for n in UPN), st.mean(att[n] for n in LWN),
        st.mean(att[n] for n in UPN) - st.mean(att[n] for n in LWN),
        st.mean(sc[n] for n in UPN) - st.mean(sc[n] for n in LWN)))
endsec()

# ===== 07 PESERTA
sec("peserta", "07", "Peringkat Peserta",
    "Peringkat memakai jumlah jawaban benar, bukan poin Wayground — poin memuat bonus kecepatan sehingga tidak mencerminkan kemampuan. Tanda bintang menandai sesi kedua atau ketiga dari nama yang sama.")
A('<div class="scroll"><table class="dense"><thead><tr><th class="n">#</th><th>Nama</th><th class="n">Benar</th><th class="n">Salah</th><th class="n">Kosong</th><th class="n">Terjawab</th><th class="n">Akurasi</th><th class="n">Nilai</th><th class="n">z</th><th class="n">T</th><th class="n">Persentil</th><th class="n">Waktu</th><th>Kategori</th></tr></thead><tbody>')
for i_, n in enumerate(ORDR, 1):
    v = sc[n]; z = (v - mean) / sd; T = 50 + 10 * z
    lower_c = sum(1 for x in vals if x < v); same = sum(1 for x in vals if x == v)
    pr = (lower_c + .5 * same) / N * 100
    gr = grade(v)
    cl = {"A": "good", "B": "good", "C": "ok", "D": "warn", "E": "bad"}[gr[0]]
    A('<tr><td class="n">%d</td><td class="b">%s</td><td class="n b">%d</td><td class="n">%d</td><td class="n">%d</td><td class="n">%d</td><td class="n">%.0f%%</td><td class="n">%.0f</td><td class="n">%+.2f</td><td class="n">%.0f</td><td class="n">%.0f</td><td class="n">%d:%02d</td><td><span class="tag %s">%s</span></td></tr>'
      % (i_, E(n), v, CORR[n].count("X"), CORR[n].count("-"), att[n],
         (v / att[n] * 100) if att[n] else 0, v / 20 * 100, z, T, pr, tt[n] // 60, tt[n] % 60, cl, gr))
A("</tbody></table></div>")
endsec()

# ===== 08 MATRIKS
sec("matriks", "08", "Matriks Respons",
    "Setiap baris satu sesi, setiap kolom satu butir. Hijau benar, merah salah, abu-abu tidak dijawab. Ini sumber tunggal seluruh analisis pada laporan ini.")
A('<div class="scroll"><table class="mx"><thead><tr><th class="nm">Nama</th>')
for i_ in range(1, 21):
    A("<th>%d</th>" % i_)
A('<th class="n">Σ</th></tr></thead><tbody>')
for n in ORDR:
    A('<tr><td class="nm">%s</td>' % E(n))
    for s_ in CORR[n]:
        A('<td class="c%s">%s</td>' % (s_.replace("-", "z"), {"C": "●", "X": "×", "-": ""}[s_]))
    A('<td class="n b">%d</td></tr>' % sc[n])
A('</tbody><tfoot><tr><td class="nm">Benar per butir</td>')
for it in sorted(items, key=lambda i: i["no"]):
    A('<td class="n">%d</td>' % it["correct"])
A('<td class="n b">%d</td></tr></tfoot></table></div>' % tot_c)
note("Blok abu-abu pekat di kolom kiri atas menunjukkan peserta yang bergabung setelah kuis dimulai — bukan peserta yang menyerah di tengah jalan. Memperbaiki pelaksanaan teknis akan memperbaiki kualitas data lebih besar daripada memperbaiki soalnya.")
endsec()

# ===== 09 MISKONSEPSI
sec("miskonsepsi", "09", "Miskonsepsi Terkuat",
    "Opsi salah yang paling banyak dipilih. Setiap baris adalah keyakinan keliru yang nyata dipegang peserta dan perlu dibantah secara eksplisit pada hari pelatihan.")
MIS = []
for it in items:
    resp = it["correct"] + it["incorrect"]
    for opt, c_ in it["distr"]:
        if opt != it["key"] and c_ > 0:
            MIS.append((c_, c_ / max(1, resp), it["no"], opt, it["key"]))
MIS.sort(key=lambda x: (-x[0], -x[1]))
A('<div class="scroll"><table><thead><tr><th class="n">Butir</th><th>Miskonsepsi — opsi salah yang dipilih</th><th class="n">Pemilih</th><th class="n">% penjawab</th><th>Jawaban yang benar</th></tr></thead><tbody>')
for c_, fr, no, opt, key in MIS[:12]:
    A('<tr><td class="n b">Q%d</td><td>%s</td><td class="n b">%d</td><td class="n">%.0f%%</td><td class="s ok2">%s</td></tr>'
      % (no, E(fix(opt)), c_, fr * 100, E(fix(key))))
A("</tbody></table></div>")
endsec()

# ===== 10 WAKTU
sec("waktu", "10", "Analisis Waktu",
    "Rata-rata waktu respons per butir, dibandingkan dengan tingkat kesukarannya.")
A('<div class="scroll"><table class="dense"><thead><tr><th class="n">Butir</th><th>Pokok yang diuji</th><th class="n">Rata-rata waktu</th><th class="n">p</th><th class="n">Jumlah penjawab</th></tr></thead><tbody>')
for it in sorted(items, key=lambda i: i["no"]):
    A('<tr><td class="n b">Q%d</td><td>%s</td><td class="n">%s</td><td class="n">%.2f</td><td class="n">%d</td></tr>'
      % (it["no"], E(SHORT[it["no"]]), it["avg_t"][3:], it["p"], it["correct"] + it["incorrect"]))
A("</tbody></table></div>")
note("Rata-rata sekitar 17–18 detik per butir. Beberapa butir memuat empat pernyataan yang harus dibandingkan (Q2, Q5, Q9, Q11) dan pantas diberi 45–60 detik, atau redaksi opsinya diperpendek.")
endsec()
