# -*- coding: utf-8 -*-
# ===== 06 PESERTA
sec("peserta", "06", "Peserta Post-test",
    "Peringkat memakai jumlah jawaban benar, bukan poin Wayground. Sesi atas nama Vincent (QA tester) tidak ditampilkan.")
cnt = Counter(sc_post.values())
A(vbars([(str(k), cnt.get(k, 0), pcol(k / 20)) for k in range(0, 21)]))
A('<p class="cap">Sebaran jumlah jawaban benar atas 15 sesi post-test.</p>')
A('<div class="scroll"><table class="dense"><thead><tr><th class="n">#</th><th>Nama</th><th class="n">Benar</th><th class="n">Salah</th><th class="n">Kosong</th><th class="n">Dijawab</th><th class="n">Nilai</th><th class="n">Waktu</th><th class="n">Pre-test</th><th class="n">Gain</th><th>Status sesi</th><th>Kategori</th></tr></thead><tbody>')
for i, n in enumerate(ORDP, 1):
    p = pmap.get(n); v = sc_post[n]; a_ = att[n]; nil = v / 20 * 100
    gr = "A Sangat Baik" if nil >= 85 else ("B Baik" if nil >= 70 else ("C Cukup" if nil >= 55 else ("D Kurang" if nil >= 40 else "E Sangat Kurang")))
    cl = {"A": "good", "B": "good", "C": "ok", "D": "warn", "E": "bad"}[gr[0]]
    tuntas = a_ == 20
    g = (v - sc_pre[p]) if p else None
    A('<tr><td class="n">%d</td><td class="b">%s</td><td class="n b">%d</td><td class="n">%d</td><td class="n">%d</td><td class="n">%d</td><td class="n">%.0f</td><td class="n">%d:%02d</td><td class="n">%s</td><td class="n b" style="color:%s">%s</td><td><span class="tag %s">%s</span></td><td><span class="tag %s">%s</span></td></tr>'
      % (i, E(n), v, CO[n].count("X"), CO[n].count("-"), a_, nil,
         PO[n]["time_s"] // 60, PO[n]["time_s"] % 60,
         ("%d/20" % sc_pre[p]) if p else "—",
         GOOD if (g or 0) > 0 else BAD, ("%+d" % g) if g is not None else "—",
         "good" if tuntas else "bad", "Tuntas" if tuntas else "Terputus %d/20" % a_, cl, gr))
A("</tbody></table></div>")
note("Sepuluh dari 15 sesi diselesaikan penuh. Lima sesi terputus, dan empat di antaranya berhenti dalam waktu kurang dari satu menit — pola yang menunjuk ke kendala perangkat atau tautan, bukan ke peserta yang menyerah setelah membaca soal. Yovita tercatat dua kali: satu sesi tuntas 13 benar dan satu sesi nol jawaban; sesi terbaik yang dipakai.")
note("Korelasi waktu pengerjaan dengan jumlah benar pada sesi tuntas hanya r = 0,115 — praktis nol. Dalam mode take-home tiga hari, waktu tercatat tidak lagi menjadi ukuran usaha yang bermakna. Empat peserta post-test tidak mengikuti pre-test (Mien 18 benar, Netty Nusaly 12, Silvya Runturambi 7), sehingga nilainya tidak dapat dipakai mengukur dampak pelatihan.")
endsec()

# ===== 07 MATRIKS
sec("matriks", "07", "Matriks Respons",
    "Setiap baris satu sesi, setiap kolom satu butir. Hijau benar, merah salah, abu-abu tidak dijawab. Ini sumber tunggal seluruh analisis post-test.")
A('<div class="scroll"><table class="mx"><thead><tr><th class="nm">Nama</th>')
for i in range(1, 21):
    A("<th>%d</th>" % i)
A('<th class="n">Σ</th></tr></thead><tbody>')
for n in ORDP:
    A('<tr><td class="nm">%s</td>' % E(n))
    for s_ in CO[n]:
        A('<td class="c%s">%s</td>' % (s_.replace("-", "z"), {"C": "●", "X": "×", "-": ""}[s_]))
    A('<td class="n b">%d</td></tr>' % sc_post[n])
A('</tbody><tfoot><tr><td class="nm">Benar per butir</td>')
for q in sorted(post["Q"], key=lambda x: x["no"]):
    A('<td class="n">%d</td>' % q["correct_excl"])
A('<td class="n b">%d</td></tr></tfoot></table></div>' % sum(sc_post.values()))
endsec()

# ===== 08 PENGECOH
sec("pengecoh", "08", "Keberfungsian Pengecoh",
    "Naskah cetak resmi memuat keempat opsi setiap butir, sehingga dapat diketahui opsi mana yang tidak pernah dipilih oleh satu pun peserta. Ini tidak dapat diketahui dari ekspor data saja.")
A('<div class="kpis">')
for k, v, s_ in [("Total opsi salah", "60", "20 butir × 3 pengecoh"),
                 ("Pengecoh mati", str(ndead), "tidak dipilih satu pun peserta"),
                 ("Proporsi mati", "%.0f%%" % (ndead / 60 * 100), "hampir separuh instrumen tidak bekerja"),
                 ("Butir tanpa pengecoh hidup", "3", "Q8, Q19, Q20 — praktis hanya menyisakan kunci")]:
    A('<div class="kpi"><div class="kl">%s</div><div class="kv">%s</div><div class="ks">%s</div></div>' % (k, v, s_))
A("</div>")
warn("Pengecoh mati bukan sekadar cacat teknis. Butir dengan tiga pengecoh mati mengukur hampir tidak ada: peserta yang sama sekali tidak tahu jawabannya pun kemungkinan besar memilih kunci, karena ketiga pilihan lain terbaca jelas keliru. Q8 (p=0,73) dan Q20 (p=0,67) — dua butir termudah pada post-test — keduanya berada dalam kondisi ini, sehingga tingginya angka p pada kedua butir itu tidak boleh dibaca sebagai bukti penguasaan.")
A('<div class="scroll"><table class="dense"><thead><tr><th class="n">Butir</th><th class="n">Pengecoh hidup</th><th>Opsi yang tidak pernah dipilih</th></tr></thead><tbody>')
for n in range(1, 21):
    d = DEAD.get(n, [])
    live = 3 - len(d)
    txt = "<br>".join("<b>%s)</b> %s" % (l, E(t)) for l, t in d) if d else "<em>seluruh pengecoh berfungsi</em>"
    A('<tr><td class="n b">Q%d</td><td class="n"><span class="tag %s">%d dari 3</span></td><td class="s">%s</td></tr>'
      % (n, "bad" if live <= 1 else ("warn" if live == 2 else "good"), live, txt))
A("</tbody></table></div>")
note("Perbaikan yang disarankan: tulis ulang pengecoh agar setiap opsi merupakan kekeliruan yang benar-benar mungkin dipercaya seseorang. Sumber terbaik untuk itu adalah jawaban salah yang nyata muncul pada tes sebelumnya — laporan pre-test memuat daftar miskonsepsi yang dapat langsung dipakai.")
endsec()
