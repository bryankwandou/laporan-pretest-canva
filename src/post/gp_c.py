# -*- coding: utf-8 -*-
# ===== 04 KONSTRUK
sec("konstruk", "04", "Perbandingan per Konstruk",
    "Karena naskah soal berubah, perbandingan dilakukan pada tingkat konstruk (pokok pengetahuan yang diuji), bukan pada nomor butir. Pemetaan ditetapkan dengan membaca naskah kedua tes satu per satu.")
CR = sorted(C1["crows"], key=lambda x: -x[3])
A(dumbbell([(lab[:34], a, b, "%+.0f pp" % (d * 100)) for lab, a, b, d, jen, bt in CR]))
A('<p class="cap">Lingkaran kosong = pre-test, lingkaran penuh = post-test. Hijau naik, merah turun. Skala proporsi benar.</p>')
TAFC = {
    "Ukuran kanvas per platform": "Kenaikan terbesar. Hafalan murni yang jelas tersampaikan lewat rujukan tabel ukuran.",
    "Tujuan pelatihan": "Wajar naik tajam — pada pre-test materinya memang belum pernah disampaikan.",
    "Asal usul Canva (Fusion Books)": "Butir identik kata per kata pada kedua tes. Bukti hafalan paling bersih pada laporan ini.",
    "Format ekspor PNG untuk gambar": "Ranah terlemah pre-test kini terangkat. Praktik ekspor langsung terbukti bekerja.",
    "Pernyataan benar tentang Canva": "Pemahaman umum tentang sifat platform membaik.",
    "Kolaborasi tim real-time": "Naik sehat, konsisten dengan Q1 post-test (p=0,67).",
    "Hierarki visual — pernyataan yang bertentangan": "Naik, meski kuncinya berubah dari 'ukuran teks seragam' menjadi 'terlalu banyak font'.",
    "Batas jumlah font dan warna": "Naik, sejalan dengan hierarki visual. Prinsip desain tersampaikan.",
    "Menu panel kiri editor": "Naik tipis dan masih rendah (p=0,33). Pengenalan antarmuka belum tuntas.",
    "Empat nilai berkarya dengan hati": "Naik tipis meski materi disampaikan langsung — daya ingat isi pelatihan lemah.",
    "Teori warna (skema warna)": "Naik tipis. Konstruk bergeser dari warna analog ke monokromatik, jadi tidak sepenuhnya setara.",
    "Paket harga Canva": "Praktis tidak berubah, tetapi soalnya bergeser dari penalaran memilih paket menjadi hafalan angka.",
    "Urutan langkah prosedural di editor": "Turun. Butir yang menuntut mengingat urutan langkah adalah yang paling cepat luntur.",
    "Komentar pada elemen desain": "Turun paling tajam. Pada post-test hanya 2 dari 15 peserta menjawab benar.",
}
A('<div class="scroll"><table class="dense"><thead><tr><th>Konstruk</th><th class="n">Butir</th><th>Jenis</th><th class="n">p pre</th><th class="n">p post</th><th class="n">Δ p</th><th>Arah</th><th>Tafsiran</th></tr></thead><tbody>')
for lab, a, b, d, jen, bt in CR:
    arah = "Naik" if d > .05 else ("Tetap" if d >= -.05 else "Turun")
    A('<tr><td class="b">%s</td><td class="n s">%s</td><td><span class="tag %s">%s</span></td><td class="n">%.2f</td><td class="n">%.2f</td><td class="n b" style="color:%s">%+.2f</td><td><span class="tag %s">%s</span></td><td class="s">%s</td></tr>'
      % (E(lab), E(bt), "ok" if jen == "sama" else "warn", jen, a, b,
         GOOD if d > .05 else (BAD if d < -.05 else "#5a6474"), d,
         "good" if arah == "Naik" else ("bad" if arah == "Turun" else "ok"), arah, E(TAFC.get(lab, ""))))
A('</tbody><tfoot><tr><td class="b">RATA-RATA 14 KONSTRUK</td><td></td><td></td><td class="n">%.2f</td><td class="n">%.2f</td><td class="n">%+.2f</td><td></td><td></td></tr></tfoot></table></div>'
  % (st.mean(x[1] for x in CR), st.mean(x[2] for x in CR), st.mean(x[3] for x in CR)))
A("<h3>Enam butir post-test tanpa padanan di pre-test</h3>")
WHY = {3: "Materi baru yang tidak pernah diuji sebelumnya. Butir tersukar kedua — Brand Kit belum tersampaikan.",
       8: "Materi liturgi, bukan materi Canva. p tertinggi di seluruh post-test, tetapi mengukur pengetahuan yang sudah dimiliki peserta sebelum pelatihan.",
       9: "Format ekspor video. Melengkapi ranah teknis yang pada pre-test hanya diwakili PNG dan ukuran kanvas.",
       12: "Perluasan dari butir asal usul Canva. Wajar untuk hafalan nama yang baru disampaikan.",
       13: "Fitur Eyedropper. Separuh peserta mengenalinya setelah pelatihan.",
       18: "Etika penggunaan AI. Materi paling baru dan paling jauh dari Canva teknis."}
A('<table><thead><tr><th class="n">Butir</th><th>Materi</th><th class="n">p post</th><th>Mengapa penting dicatat</th></tr></thead><tbody>')
for no in sorted(NEWP):
    A('<tr><td class="n b">Q%d</td><td class="b">%s</td><td class="n">%.2f</td><td class="s">%s</td></tr>' % (no, E(NEWP[no]), QO[no]["p"], E(WHY[no])))
A("</tbody></table>")
A("<h3>Enam butir pre-test yang tidak diulang</h3>")
LOSS = {1: "Penghalang nomor satu pada pre-test dan rekomendasi utama laporan sebelumnya. Karena tidak diulang, keberhasilan menutup penghalang itu tidak terukur.",
        4: "Konsep drag-and-drop tidak diuji ulang, padahal ini fondasi cara kerja Canva.",
        11: "Prinsip ruang kosong hilang dari pengukuran, padahal termasuk kelemahan prinsip desain yang paling menonjol.",
        12: "Manfaat penyimpanan cloud tidak diuji ulang; sebagian tercakup tidak langsung oleh Q1 dan Q17 post-test.",
        17: "Butir gagal pada pre-test yang memang sudah direkomendasikan untuk dikeluarkan. Satu-satunya penghapusan yang sejalan dengan rekomendasi.",
        20: "Profil pemateri. Kehilangannya tidak merugikan karena mengukur hafalan yang tidak berkaitan dengan kemampuan desain."}
A('<table><thead><tr><th class="n">Butir</th><th>Materi</th><th class="n">p pre</th><th>Akibat tidak diulang</th></tr></thead><tbody>')
for no in sorted(DROPP):
    A('<tr><td class="n b">Q%d</td><td class="b">%s</td><td class="n">%.2f</td><td class="s">%s</td></tr>' % (no, E(DROPP[no]), preit[no]["p"], E(LOSS[no])))
A("</tbody></table>")
warn("Kehilangan butir “daftar akun gratis” dari post-test adalah kelemahan rancangan yang paling merugikan. Rekomendasi utama laporan pre-test adalah mengalokasikan 15 menit pertama untuk memastikan setiap peserta berhasil mendaftar akun sendiri. Karena butirnya tidak diulang, keberhasilan rekomendasi itu tidak dapat dibuktikan maupun dibantah oleh data post-test.")
endsec()

# ===== 05 BUTIR
sec("butir", "05", "Analisis Butir Post-test",
    "n = 15 sesi. Kelompok atas dan bawah masing-masing 4 sesi (27% dari 15). Kunci diverifikasi terhadap naskah cetak resmi — cocok pada 20 dari 20 butir.")
A(hbar([("Q%d · %s" % (q["no"], SHORTP[q["no"]][:24]), q["p"], "%.0f%%" % (q["p"] * 100))
        for q in sorted(post["Q"], key=lambda x: -x["p"])], maxv=1.0, w=700, labw=250, colorfn=pcol))
A('<p class="cap">Tingkat kesukaran per butir, terurut dari termudah. Merah = sukar (p&lt;0,30), kuning = sedang, hijau = mudah.</p>')
A('<div class="scroll"><table class="dense"><thead><tr><th>Butir</th><th>Pokok yang diuji</th><th>Kunci</th><th class="n">B</th><th class="n">S</th><th class="n">Kosong</th><th class="n">p</th><th>Kategori</th><th class="n">D</th><th class="n">r-pbis</th></tr></thead><tbody>')
for q in sorted(post["Q"], key=lambda x: x["no"]):
    n = q["no"]; p = q["p"]
    kat = "Sukar" if p < .30 else ("Sedang" if p <= .70 else "Mudah")
    A('<tr><td class="b">Q%d</td><td>%s</td><td class="s ok2">%s</td><td class="n">%d</td><td class="n">%d</td><td class="n">%d</td><td class="n b">%.2f</td><td><span class="tag %s">%s</span></td><td class="n">%.2f</td><td class="n">%.2f</td></tr>'
      % (n, E(SHORTP[n]), E(q["key"][:56]), q["correct_excl"], q["incorrect_excl"], q["unatt_excl"],
         p, {"Sukar": "bad", "Sedang": "warn", "Mudah": "good"}[kat], kat, q["D"], q["rpb"]))
A("</tbody></table></div>")
note("Seluruh 20 butir masuk kategori Sukar atau Sedang; tidak ada butir yang terlalu mudah. Rata-rata p = %.2f. Q17 (komentar pada elemen desain) adalah butir tersukar dengan p=0,13 — hanya 2 dari 15 peserta benar, dan 8 memilih “unduh desain lalu kirim via email”. Ini miskonsepsi yang bertahan setelah pelatihan." % st.mean(q["p"] for q in post["Q"]))
warn("Daya beda post-test menggelembung: sepuluh butir mencapai D = 1,00. Angka ini harus dibaca hati-hati — dengan kelompok atas dan bawah masing-masing hanya 4 sesi, dan sebagian sesi bawah tidak menjawab sama sekali, nilai D lebih mencerminkan perbedaan siapa yang menyelesaikan tes daripada perbedaan penguasaan materi. Nilai D post-test tidak sebanding dengan nilai D pre-test.")
endsec()
