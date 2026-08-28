# -*- coding: utf-8 -*-
NAV = [("ringkasan", "Ringkasan"), ("peringatan", "Batas Tafsir"), ("berpasangan", "Analisis Berpasangan"),
       ("konstruk", "Per Konstruk"), ("butir", "Analisis Butir"), ("peserta", "Peserta"),
       ("matriks", "Matriks Respons"), ("pengecoh", "Pengecoh"), ("rekomendasi", "Rekomendasi"),
       ("metode", "Metodologi"), ("unduh", "Unduh")]

# ===== 01 RINGKASAN
sec("ringkasan", "01", "Ringkasan Eksekutif",
    "Post-test Pelatihan Canva — Wanita Katolik RI. Dibuka 25 Agustus 2026 pukul 22:51 dan ditutup 28 Agustus 2026 pukul 22:07 dalam mode Homework. "
    "Sesi atas nama Vincent (QA tester) dikeluarkan dari seluruh perhitungan. Kunci jawaban diverifikasi terhadap naskah cetak resmi: cocok pada 20 dari 20 butir.")
KPI = [
    ("Sesi post-test", "15", "dari 37 sesi pre-test — penyusutan 60%"),
    ("Sesi tuntas", "10", "lima sesi terputus, dua di antaranya nol jawaban"),
    ("Peserta berpasangan", "8", "mengikuti kedua tes sampai tuntas"),
    ("Rata-rata gain", "+5,00", "butir, dari 8,62 menjadi 13,62"),
    ("Naik / turun", "8 / 0", "seluruh peserta berpasangan tuntas naik"),
    ("Uji-t berpasangan", "t(7) = 3,67", "melampaui kritis 2,365 — signifikan"),
    ("Ukuran efek", "dz = 1,30", "tergolong besar"),
    ("Gain ternormalisasi", "0,44", "44% jarak menuju sempurna tertutup — sedang"),
]
A('<div class="kpis">')
for k, v, s_ in KPI:
    A('<div class="kpi"><div class="kl">%s</div><div class="kv">%s</div><div class="ks">%s</div></div>' % (k, v, s_))
A("</div>")
A('<h3>Kesimpulan dalam dua kalimat</h3>')
note("<strong>Yang didukung data.</strong> Pada delapan peserta yang menyelesaikan pre-test maupun post-test, penguasaan materi Canva naik rata-rata 5,00 butir dari 20, dan kenaikan itu terjadi pada seluruh delapan orang tanpa kecuali (t(7)=3,67; p&lt;0,05; dz=1,30; uji tanda p=0,0039). Konsistensi pada tiap individu inilah bukti terkuatnya, bukan besarnya rata-rata.")
warn("<strong>Yang tidak didukung data.</strong> Bahwa akurasi kelas naik dari 32,3% menjadi 49,7% sebagai akibat pelatihan. Angka itu membandingkan dua kelompok peserta berbeda, dua perangkat soal berbeda, dan dua mode pelaksanaan berbeda — ketiganya berubah bersamaan, sehingga sebabnya tidak dapat dipisahkan.")
endsec()

# ===== 02 PERINGATAN
sec("peringatan", "02", "Tiga Hal yang Membatasi Tafsir Angka Ini",
    "Ketiganya bekerja ke arah yang sama: membuat angka kenaikan terlihat lebih besar daripada sebenarnya. Karena itu +5,00 butir sebaiknya diperlakukan sebagai batas atas dampak pelatihan, bukan sebagai perkiraan tak bias.")
A('<div class="segs">')
for t, big, d in [
    ("Instrumen berubah", "14 dari 20", "Post-test bukan pengulangan pre-test. Hanya 14 konstruk beririsan; hanya dua butir yang praktis identik kata per kata. Enam butir post-test menguji materi yang tidak pernah ada di pre-test, dan enam butir pre-test tidak diulang."),
    ("Mode berubah", "3 hari", "Pre-test dikerjakan langsung dengan batas waktu per butir. Post-test dibuka tiga hari penuh sebagai Homework, tanpa pengawasan, dengan materi pelatihan tersedia. Sebagian kenaikan mencerminkan kesempatan membuka materi."),
    ("Peserta menyusut", "−60%", "Dari 37 sesi menjadi 15. Yang bertahan rata-rata pre-testnya 8,62 berbanding 6,46 untuk seluruh kelas — yang bertahan adalah yang sejak awal lebih menguasai. Ini bias seleksi."),
]:
    A('<div class="seg warn"><div class="segh"><span class="segn">%s</span><div><strong>%s</strong></div></div><p class="segp">%s</p></div>' % (big, t, d))
A("</div>")
A("<h3>Mengapa basis pembanding menentukan jawabannya</h3>")
A(vbars([("Pre 37 sesi", round(st.mean(sc_pre.values()), 2), "#8a94a6"),
         ("Post 15 sesi", round(st.mean(sc_post.values()), 2), ACC),
         ("Post 10 tuntas", round(st.mean(compv), 2), ACC),
         ("Pasangan pre", round(st.mean(gaC), 2), "#8a94a6"),
         ("Pasangan post", round(st.mean(gbC), 2), GOOD)], w=560, h=210))
A('<p class="cap">Rata-rata jawaban benar (dari 20) menurut basis pembanding yang dipakai.</p>')
A('<table><thead><tr><th>Basis pembanding</th><th class="n">n</th><th class="n">Rata-rata</th><th class="n">Akurasi</th><th>Menjawab pertanyaan apa</th></tr></thead><tbody>')
for lab, n_, v, q in [
    ("Pre-test, seluruh sesi", 37, st.mean(sc_pre.values()), "Berapa akurasi yang tercatat sebelum pelatihan"),
    ("Post-test, seluruh sesi", 15, st.mean(sc_post.values()), "Berapa akurasi yang tercatat sesudahnya — bukan berapa yang dipelajari"),
    ("Post-test, sesi tuntas", 10, st.mean(compv), "Berapa penguasaan mereka yang benar-benar mengerjakan sampai selesai"),
    ("Berpasangan, pre", 8, st.mean(gaC), "Titik awal orang-orang yang sama"),
    ("Berpasangan, post", 8, st.mean(gbC), "Titik akhir orang-orang yang sama — satu-satunya basis yang mengendalikan siapa yang ikut"),
]:
    A('<tr><td class="b">%s</td><td class="n">%d</td><td class="n b">%.2f</td><td class="n">%.1f%%</td><td class="s">%s</td></tr>' % (lab, n_, v, v / 20 * 100, q))
A("</tbody></table>")
endsec()

# ===== 03 BERPASANGAN
sec("berpasangan", "03", "Analisis Berpasangan",
    "Bukti terkuat pada laporan ini: membandingkan orang yang sama dengan dirinya sendiri, sehingga perbedaan komposisi peserta tidak lagi menjadi penjelasan tandingan.")
A('<div class="twocol"><div>')
A(slope([(o, a, b) for o, p, a, b in sorted(PAIRC, key=lambda x: -x[3])]))
A('<p class="cap">Delapan peserta berpasangan yang tuntas. Setiap garis satu orang; seluruhnya naik.</p>')
A('</div><div>')
A(hbar([(o[:20], b - a, "+%d" % (b - a)) for o, p, a, b in sorted(PAIRC, key=lambda x: -(x[3] - x[2]))],
       maxv=14, w=460, labw=160, rowh=30, colorfn=lambda v: GOOD))
A('<p class="cap">Besar kenaikan per peserta, dalam butir.</p>')
A("</div></div>")
A('<table><thead><tr><th class="n">#</th><th>Nama pada post-test</th><th>Nama pada pre-test</th><th class="n">Pre</th><th class="n">Post</th><th class="n">Gain</th><th class="n">Gain ternorm.</th><th class="n">Dijawab</th><th>Status sesi</th></tr></thead><tbody>')
for i, (o, p, a, b) in enumerate(sorted(PAIR, key=lambda x: -(x[3] - x[2])), 1):
    g = b - a
    tuntas = att[o] == 20
    A('<tr><td class="n">%d</td><td class="b">%s</td><td class="s">%s</td><td class="n">%d</td><td class="n">%d</td><td class="n b" style="color:%s">%+d</td><td class="n">%s</td><td class="n">%d/20</td><td><span class="tag %s">%s</span></td></tr>'
      % (i, E(o), E(p), a, b, GOOD if g > 0 else BAD, g,
         ("%.0f%%" % (g / (20 - a) * 100)) if a < 20 else "—", att[o],
         "good" if tuntas else "bad", "Tuntas" if tuntas else "Terputus"))
A('</tbody><tfoot><tr><td></td><td class="b">RATA-RATA (8 sesi tuntas)</td><td></td><td class="n">%.2f</td><td class="n">%.2f</td><td class="n">%+.2f</td><td class="n">%.0f%%</td><td></td><td></td></tr></tfoot></table>'
  % (st.mean(gaC), st.mean(gbC), st.mean(gg), C2["g_c"] * 100))
A("<h3>Uji statistik atas 8 peserta berpasangan yang tuntas</h3>")
A('<table><thead><tr><th>Ukuran</th><th class="n">Nilai</th><th>Ambang pembanding</th><th>Kesimpulan</th></tr></thead><tbody>')
for a_, b_, c_, d_ in [
    ("Rata-rata gain", "+5,00 butir", "SEM ±1,76 butir", "Gain hampir tiga kali kesalahan baku ukur — bukan sekadar derau pengukuran."),
    ("Uji-t berpasangan", "t(7) = 3,67", "kritis 2,365 (α=0,05 dua sisi)", "<b>Signifikan.</b> Kenaikan tidak dapat dijelaskan oleh kebetulan semata."),
    ("Uji tanda (binomial)", "8 dari 8 naik", "p = 0,0039 satu sisi", "Konsisten pada tiap individu. Tidak bergantung pada asumsi sebaran normal — bukti lebih kuat daripada rata-rata."),
    ("Ukuran efek Cohen dz", "1,30", "0,20 kecil · 0,50 sedang · 0,80 besar", "<b>Besar.</b>"),
    ("Gain ternormalisasi &lt;g&gt;", "0,440", "&lt;0,30 rendah · 0,30–0,70 sedang", "<b>Sedang.</b> 44% jarak menuju skor sempurna tertutup; rata-rata masih tersisa 6,4 butir."),
    ("Uji kepekaan tanpa nilai ekstrem", "t(6) = 7,12 · dz = 2,69", "kritis 2,447", "Mengeluarkan gain +14 justru menguatkan hasil (rata-rata turun ke 3,71 tetapi sebarannya menyempit). Kesimpulan tidak bergantung pada satu pengamatan."),
]:
    A('<tr><td class="b">%s</td><td class="n b">%s</td><td class="s">%s</td><td>%s</td></tr>' % (a_, b_, c_, d_))
A("</tbody></table>")
warn("Tiga peserta berpasangan lain — Tintin tityn, Maria dan Ivonne runturambi — dikeluarkan dari uji statistik karena tidak menyelesaikan post-test (masing-masing hanya menjawab 0, 3 dan 2 butir, seluruhnya berhenti di bawah 45 detik). Memasukkan mereka menurunkan rata-rata gain dari +5,00 menjadi +2,55 dan menghapus signifikansi statistiknya, padahal yang terukur di situ adalah kegagalan teknis, bukan pengetahuan.")
endsec()
