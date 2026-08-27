# -*- coding: utf-8 -*-
BODY = "".join(buf)
NAVHTML = "".join('<a href="#%s">%s</a>' % (i, t) for i, t in NAV)

CSS = """
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:#fff;color:#1b2431;font:15px/1.62 'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
header.top{border-bottom:1px solid #e6e9ef;padding:56px 0 40px}
.eyebrow{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#8a94a6;font-weight:600;margin:0 0 14px}
h1{font-size:38px;line-height:1.16;letter-spacing:-.02em;margin:0 0 16px;font-weight:600;color:#12284b;max-width:22ch}
.sub{font-size:16px;color:#5a6474;margin:0;max-width:80ch}
.meta{display:flex;flex-wrap:wrap;gap:8px 34px;margin-top:28px;font-size:13px;color:#6b7484}
.meta b{color:#12284b;font-weight:600}
nav.toc{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.95);backdrop-filter:blur(8px);border-bottom:1px solid #e6e9ef}
nav.toc .wrap{display:flex;gap:20px;overflow-x:auto;padding-top:12px;padding-bottom:12px;scrollbar-width:none}
nav.toc .wrap::-webkit-scrollbar{display:none}
nav.toc a{color:#5a6474;text-decoration:none;font-size:13px;white-space:nowrap;padding-bottom:2px;border-bottom:2px solid transparent}
nav.toc a:hover{color:#12284b;border-color:#2f6fb5}
section{padding:56px 0;border-bottom:1px solid #eef0f4}
section:last-of-type{border:none}
.secno{font-size:11px;letter-spacing:.16em;color:#a6adba;font-weight:600;margin-bottom:8px}
h2{font-size:25px;letter-spacing:-.015em;margin:0 0 12px;font-weight:600;color:#12284b}
h3{font-size:16px;margin:40px 0 14px;font-weight:600;color:#12284b}
h4{font-size:15px;margin:0 0 10px;font-weight:600;color:#12284b;line-height:1.5}
.lead{color:#5a6474;margin:0 0 26px;max-width:90ch;font-size:14.5px}
.note{background:#f7f9fc;border-left:3px solid #2f6fb5;padding:14px 18px;margin:24px 0 0;font-size:14px;color:#3d4756;max-width:98ch}
.note strong{color:#12284b}
.cap{font-size:12.5px;color:#8a94a6;margin:6px 0 26px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:1px;background:#e6e9ef;border:1px solid #e6e9ef}
.kpi{background:#fff;padding:20px 18px}
.kl{font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:#8a94a6;font-weight:600}
.kv{font-size:29px;font-weight:600;color:#12284b;letter-spacing:-.02em;margin:6px 0 4px;font-variant-numeric:tabular-nums}
.ks{font-size:12.5px;color:#6b7484;line-height:1.45}
ol.findings{counter-reset:f;list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:1px;background:#e6e9ef;border:1px solid #e6e9ef}
ol.findings li{counter-increment:f;background:#fff;padding:20px 20px 20px 56px;position:relative}
ol.findings li:before{content:counter(f,decimal-leading-zero);position:absolute;left:20px;top:20px;font-size:12px;font-weight:600;color:#2f6fb5;font-variant-numeric:tabular-nums}
ol.findings strong{display:block;color:#12284b;font-weight:600;margin-bottom:5px;font-size:14.5px}
ol.findings span{font-size:13.5px;color:#5a6474;line-height:1.55}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin:0 0 8px}
thead th{background:#12284b;color:#fff;font-weight:600;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;padding:10px;text-align:left;vertical-align:bottom}
td{padding:9px 10px;border-bottom:1px solid #eef0f4;vertical-align:top}
tbody tr:hover td{background:#f7f9fc}
tfoot td{padding:9px 10px;border-top:2px solid #12284b;font-weight:600;background:#f7f9fc}
.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
th.n{text-align:right}
.b{font-weight:600;color:#12284b}
.s{font-size:12.5px;color:#5a6474}
.mono{font-family:ui-monospace,'SF Mono',Consolas,monospace;font-size:12.5px}
table.dense td{padding:7px 9px;font-size:13px}
.scroll{overflow-x:auto;border:1px solid #e6e9ef;margin-bottom:8px}
.scroll table{margin:0}
.tag{display:inline-block;padding:2px 8px;border-radius:3px;font-size:11.5px;font-weight:600;white-space:nowrap}
.tag.good{background:#e6f4ec;color:#20624a}.tag.ok{background:#eaf1fa;color:#26578c}
.tag.warn{background:#fdf3e0;color:#8a5f11}.tag.bad{background:#fbebe9;color:#9c332c}
.ok2{color:#20624a}
.chart{width:100%;height:auto;display:block;margin:8px 0 0}
.cl{font-size:11px;fill:#5a6474}.cv{font-size:11px;fill:#12284b;font-weight:600}
.segs{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px}
.seg{border:1px solid #e6e9ef;border-top:3px solid #2f6fb5;padding:18px}
.seg.good{border-top-color:#2e7d5b}.seg.ok{border-top-color:#2f6fb5}
.seg.warn{border-top-color:#c58a1a}.seg.mut{border-top-color:#a6adba}
.segh{display:flex;gap:14px;align-items:baseline;margin-bottom:10px}
.segn{font-size:32px;font-weight:600;color:#12284b;line-height:1;font-variant-numeric:tabular-nums}
.segh strong{display:block;font-size:14.5px;color:#12284b}
.segh em{font-style:normal;font-size:12px;color:#8a94a6}
.segp{font-size:13px;color:#5a6474;margin:0 0 10px;line-height:1.55}
.segw{font-size:11.5px;color:#8a94a6;margin:0;padding-top:10px;border-top:1px solid #eef0f4;line-height:1.5}
.prios{display:grid;gap:1px;background:#e6e9ef;border:1px solid #e6e9ef}
.prio{background:#fff;display:flex;gap:18px;padding:22px 20px}
.pn{font-size:26px;font-weight:600;color:#c8d0dc;line-height:1;min-width:30px;font-variant-numeric:tabular-nums}
.pb{flex:1;min-width:0}
.pill{display:inline-block;background:#eaf1fa;color:#26578c;font-size:11px;font-weight:600;padding:2px 8px;border-radius:3px;vertical-align:middle}
.pill.light{background:#f2f4f8;color:#6b7484}
.pev,.pme,.puk{margin:0 0 6px;font-size:13px;color:#5a6474;line-height:1.55}
.pev span,.pme span,.puk span{display:inline-block;min-width:138px;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#a6adba;font-weight:600;vertical-align:top}
.puk{color:#20624a}
ul.ul{margin:0;padding-left:20px;max-width:98ch}
ul.ul li{margin-bottom:10px;font-size:14px;color:#3d4756;line-height:1.62}
ul.ul strong{color:#12284b}
.warnul li{color:#5a6474}
table.mx{font-size:11px;border-collapse:collapse}
table.mx th{padding:6px 4px;text-align:center;font-size:10px}
table.mx th.nm{text-align:left;min-width:158px;padding-left:10px}
table.mx td{padding:0;text-align:center;width:26px;height:22px;border:1px solid #fff;font-size:10px;line-height:22px}
table.mx td.nm{text-align:left;padding:0 10px;font-size:12px;white-space:nowrap;background:#fff;font-weight:500;border-bottom:1px solid #eef0f4}
td.cC{background:#d6ecdf;color:#20624a}
td.cX{background:#fadfdc;color:#9c332c}
td.cz{background:#f1f3f6}
table.mx tfoot td{border-top:2px solid #12284b}
.dl{display:flex;align-items:center;gap:18px;border:1px solid #e6e9ef;padding:20px 22px;text-decoration:none;max-width:620px;transition:border-color .15s,background .15s}
.dl:hover{border-color:#2f6fb5;background:#f7f9fc}
.dlx{background:#12284b;color:#fff;font-size:11px;font-weight:600;letter-spacing:.08em;padding:9px 12px;border-radius:3px}
.dlt strong{display:block;color:#12284b;font-size:14.5px;font-weight:600}
.dlt em{font-style:normal;font-size:12.5px;color:#8a94a6}
footer{padding:36px 0 64px;font-size:12.5px;color:#8a94a6;line-height:1.75}
footer b{color:#5a6474;font-weight:600}
@media(max-width:720px){
 .wrap{padding:0 18px}h1{font-size:27px}h2{font-size:21px}
 section{padding:40px 0}
 .prio{flex-direction:column;gap:8px}
 .pev span,.pme span,.puk span{display:block;min-width:0;margin-bottom:2px}
}
@media print{nav.toc{display:none}section{break-inside:avoid;padding:24px 0}}
"""

SHELL = """<!doctype html>
<html lang="id"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Laporan Evaluasi Pre-test Pelatihan Canva &mdash; 25 Agustus 2026</title>
<meta name="description" content="Analisis statistik lengkap hasil pre-test pelatihan Canva: 37 sesi, 20 butir, reliabilitas KR-20 0,751. Analisis butir, segmentasi peserta, pemetaan miskonsepsi dan rekomendasi.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>%s</style>
</head><body>
<header class="top"><div class="wrap">
<p class="eyebrow">Laporan Evaluasi &middot; Wanita Katolik RI</p>
<h1>Pre-test Pelatihan Canva</h1>
<p class="sub">Analisis statistik menyeluruh atas hasil pre-test yang diselenggarakan melalui Wayground (Quizizz). Mencakup analisis butir, reliabilitas instrumen, segmentasi peserta, pemetaan miskonsepsi dan rekomendasi rancangan pelatihan.</p>
<div class="meta"><span>Tanggal pelaksanaan <b>25 Agustus 2026</b></span><span>Sesi terekam <b>37</b></span><span>Butir <b>20</b></span><span>Platform <b>Wayground / Quizizz</b></span></div>
</div></header>
<nav class="toc"><div class="wrap">%s</div></nav>
<main class="wrap">%s</main>
<footer><div class="wrap">
<b>Sumber data:</b> ekspor resmi Wayground (XLSX) dan snapshot HTML laporan admin, keduanya tertanggal 25 Agustus 2026. Seluruh angka telah diverifikasi silang antara kedua sumber dengan kecocokan 20 dari 20 butir.<br>
<b>Catatan:</b> kunci jawaban direkonstruksi dari pola respons dan tidak diambil dari dokumen kunci resmi. Peringkat individu tidak layak dipakai untuk keputusan perorangan mengingat kesalahan baku ukur &plusmn;%.2f butir.
</div></footer>
</body></html>"""

out = SHELL % (CSS, NAVHTML, BODY, sem)
io.open("site/index.html", "w", encoding="utf-8").write(out)
print("OK bytes=%d sections=%d" % (len(out), out.count("<section")))
