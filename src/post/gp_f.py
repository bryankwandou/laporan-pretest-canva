# -*- coding: utf-8 -*-
BODY = "".join(buf)
NAVHTML = "".join('<a href="#%s">%s</a>' % (i, t) for i, t in NAV)
CSS = io.open("style.css", encoding="utf-8").read()

EXTRA = """
.warnbox{border-left-color:#c58a1a;background:#fdfaf3}
.twocol{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:28px;align-items:start}
ol.ol{margin:0;padding-left:20px;max-width:98ch;counter-reset:none}
ol.ol li{margin-bottom:10px;font-size:14px;color:#3d4756;line-height:1.62}
ol.ol strong{color:#12284b}
.sitenav{border-bottom:1px solid #e6e9ef;background:#12284b}
.sitenav .wrap{display:flex;gap:4px;align-items:center;padding:0}
.sitenav a{color:rgba(255,255,255,.72);text-decoration:none;font-size:13px;padding:13px 16px;border-bottom:2px solid transparent}
.sitenav a:hover{color:#fff}
.sitenav a.on{color:#fff;border-bottom-color:#7fb0e8;font-weight:600}
.sitenav .brand{color:#fff;font-weight:600;font-size:13px;padding:13px 16px 13px 0;margin-right:8px;letter-spacing:.01em}
.dl+.dl{margin-top:12px}
"""

SHELL = """<!doctype html>
<html lang="id"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>%s
%s</style>
</head><body>
<nav class="sitenav"><div class="wrap">
<span class="brand">Evaluasi Pelatihan Canva &middot; WKRI</span>
<a href="./"%s>Pre-test</a>
<a href="post-test.html"%s>Post-test &amp; Perbandingan</a>
</div></nav>
<header class="top"><div class="wrap">
<p class="eyebrow">%s</p>
<h1>%s</h1>
<p class="sub">%s</p>
<div class="meta">%s</div>
</div></header>
<nav class="toc"><div class="wrap">%s</div></nav>
<main class="wrap">%s</main>
<footer><div class="wrap">%s</div></footer>
</body></html>"""

META = "".join("<span>%s <b>%s</b></span>" % (a, b) for a, b in [
    ("Pelatihan", "25 Agustus 2026"), ("Post-test ditutup", "28 Agustus 2026"),
    ("Sesi post-test", "15"), ("Peserta berpasangan", "8"), ("Mode", "Homework, 3 hari")])

FOOT = ("<b>Sumber data:</b> ekspor resmi Wayground (XLSX), naskah cetak resmi 20 butir (PDF), dan dataset pre-test 25 Agustus 2026. "
        "Kunci jawaban direkonstruksi dari pola respons lalu diverifikasi terhadap naskah cetak — cocok pada 20 dari 20 butir.<br>"
        "<b>Catatan:</b> sesi atas nama Vincent (QA tester) dikeluarkan dari seluruh perhitungan. Angka gain +5,00 butir berlaku untuk 8 peserta "
        "yang menyelesaikan kedua tes, dan merupakan batas atas dampak pelatihan mengingat instrumen, mode pelaksanaan dan komposisi peserta "
        "seluruhnya berubah antara kedua pengukuran.")

out = SHELL % (
    "Post-test Pelatihan Canva &mdash; Analisis dan Perbandingan terhadap Pre-test",
    "Analisis post-test pelatihan Canva dan perbandingannya terhadap pre-test: 8 peserta berpasangan, gain +5,00 butir, t(7)=3,67, dz=1,30.",
    CSS, EXTRA, "", ' class="on"',
    "Laporan Evaluasi &middot; Wanita Katolik RI",
    "Post-test dan Perbandingan",
    "Analisis hasil post-test pelatihan Canva dan perbandingannya terhadap pre-test. Mencakup analisis berpasangan, pemetaan konstruk antara kedua instrumen, analisis butir, keberfungsian pengecoh, serta batas tafsir yang harus disertakan pada setiap angka yang dikutip.",
    META, NAVHTML, BODY, FOOT)
io.open("site/post-test.html", "w", encoding="utf-8").write(out)
print("post-test.html bytes=%d sections=%d" % (len(out), out.count("<section")))

# --- sisipkan site nav + tautan ke index.html yang sudah ada
idx = io.open("site/index.html", encoding="utf-8").read()
if "sitenav" not in idx:
    idx = idx.replace("</style>", EXTRA + "\n</style>", 1)
    idx = idx.replace('<header class="top">',
                      '<nav class="sitenav"><div class="wrap">'
                      '<span class="brand">Evaluasi Pelatihan Canva &middot; WKRI</span>'
                      '<a href="./" class="on">Pre-test</a>'
                      '<a href="post-test.html">Post-test &amp; Perbandingan</a>'
                      '</div></nav>\n<header class="top">', 1)
    idx = idx.replace(
        '<a class="dl" href="LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx" download>',
        '<a class="dl" href="LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx" download>'
        '<span class="dlx">XLSX</span><span class="dlt"><strong>Laporan Post-test dan Perbandingan</strong>'
        '<em>12 lembar kerja &middot; 18 grafik &middot; data berpasangan siap olah</em></span></a>'
        '<a class="dl" href="LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx" download>', 1)
    io.open("site/index.html", "w", encoding="utf-8").write(idx)
    print("index.html diperbarui: bytes=%d" % len(idx))
else:
    print("index.html sudah memuat sitenav")
