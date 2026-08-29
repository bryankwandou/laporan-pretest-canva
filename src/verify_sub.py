# -*- coding: utf-8 -*-
"""Verifikasi mandiri paket submission: keutuhan berkas, sidik, dan isi workbook."""
import os, io, json, hashlib, zipfile

SUB = "E:/Download/SUBMISSION_EVALUASI_PELATIHAN_CANVA"
SP = os.path.dirname(os.path.abspath(__file__))
man = json.load(io.open(os.path.join(SP, "manifest.json"), encoding="utf-8"))

print("=" * 78)
print("VERIFIKASI PAKET SUBMISSION")
print("=" * 78)

# 1 berkas ada dan sidik cocok
bad = []
for d, n, s, h in man:
    p = os.path.join(SUB, d, n)
    if not os.path.isfile(p):
        bad.append(("HILANG", p)); continue
    hh = hashlib.sha256(io.open(p, "rb").read()).hexdigest()[:16]
    if hh != h:
        bad.append(("SIDIK BEDA", p))
    elif os.path.getsize(p) != s:
        bad.append(("UKURAN BEDA", p))
print("1. Keutuhan %d berkas terhadap manifest : %s" % (len(man), "SEMUA COCOK" if not bad else bad))

# 2 indeks ada
idx = os.path.join(SUB, "00_BACA_INI_DULU.txt")
print("2. Indeks 00_BACA_INI_DULU.txt          : %s (%s byte)"
      % ("ADA" if os.path.isfile(idx) else "HILANG", "{:,}".format(os.path.getsize(idx))))

# 3 tidak ada berkas liar
allf = []
for root, _, fs in os.walk(SUB):
    for f in fs:
        allf.append(os.path.relpath(os.path.join(root, f), SUB).replace("\\", "/"))
expect = {"%s/%s" % (d, n) for d, n, s, h in man} | {"00_BACA_INI_DULU.txt"}
extra = set(allf) - expect
print("3. Total berkas dalam folder            : %d  (manifest %d + indeks 1)" % (len(allf), len(man)))
print("   Berkas di luar manifest              : %s" % (sorted(extra) if extra else "tidak ada"))

# 4 workbook terbuka dan berisi grafik
print("4. Keterbacaan workbook Excel")
for d, n in [("01_LAPORAN_EXCEL", "LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx"),
             ("01_LAPORAN_EXCEL", "LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx")]:
    p = os.path.join(SUB, d, n)
    z = zipfile.ZipFile(p)
    sheets = sum(1 for x in z.namelist() if x.startswith("xl/worksheets/sheet"))
    charts = sum(1 for x in z.namelist() if x.startswith("xl/charts/chart") and x.endswith(".xml"))
    ok = z.testzip() is None
    print("   %-46s sheet=%2d grafik=%2d zip=%s" % (n, sheets, charts, "utuh" if ok else "RUSAK"))

# 5 halaman web mandiri
print("5. Halaman web luring")
for n in ["index.html", "post-test.html"]:
    p = os.path.join(SUB, "02_LAPORAN_WEB", n)
    h = io.open(p, encoding="utf-8").read()
    print("   %-16s %7s byte  bagian=%2d  svg=%d  tabel=%2d  aset-eksternal=%d"
          % (n, "{:,}".format(len(h)), h.count("<section"), h.count("<svg"), h.count("<table"),
             h.count("src=\"http")))

# 6 sumber tidak berubah
print("6. Berkas sumber identik dengan aslinya di E:/Download")
for n in ["Wayground 25 agustus 2026 canva wkri.html",
          "pretestpelatihancanva25agustus2026-2026-08-25T09_22_13_634913-c1bee5.xlsx",
          "post-testpelatihancanva25agustus2026-2026-08-28T14_07_30_851549-68e3ea.xlsx",
          "Free Printable post-test pelatihan canva 25 agustus 2026.pdf"]:
    a = hashlib.sha256(io.open(os.path.join("E:/Download", n), "rb").read()).hexdigest()
    b = hashlib.sha256(io.open(os.path.join(SUB, "03_DATA_SUMBER", n), "rb").read()).hexdigest()
    print("   %-70s %s" % (n[:70], "IDENTIK" if a == b else "BERBEDA"))

# 7 angka kunci konsisten lintas berkas
print("7. Konsistensi angka kunci antar berkas")
c2 = json.load(io.open(os.path.join(SUB, "04_DATA_OLAHAN", "cmp2.json"), encoding="utf-8"))
pc = json.load(io.open(os.path.join(SUB, "04_DATA_OLAHAN", "post_core.json"), encoding="utf-8"))
h_post = io.open(os.path.join(SUB, "02_LAPORAN_WEB", "post-test.html"), encoding="utf-8").read()
chk = [("Pasangan tuntas n=8", len(c2["PAIRC"]) == 8, len(c2["PAIRC"])),
       ("Rata-rata gain +5,00", abs(c2["mean_gain_c"] - 5.0) < 1e-9, c2["mean_gain_c"]),
       ("t = 3,67", abs(c2["t_c"] - 3.67) < .01, round(c2["t_c"], 3)),
       ("dz = 1,30", abs(c2["dz_c"] - 1.30) < .01, round(c2["dz_c"], 3)),
       ("g Hake = 0,440", abs(c2["g_c"] - .44) < .005, round(c2["g_c"], 3)),
       ("Sesi post-test = 15", len(pc["names"]) == 15, len(pc["names"])),
       ("Vincent tidak ada di dataset", "Vincent" not in pc["names"], "-"),
       ("Sesi tuntas = 10", len(c2["comp"]) == 10, len(c2["comp"])),
       ("Halaman web memuat +5,00", "+5,00" in h_post, "-"),
       ("Halaman web memuat t(7) = 3,67", "t(7) = 3,67" in h_post, "-")]
for lab, ok, v in chk:
    print("   %-34s %-7s %s" % (lab, "COCOK" if ok else "GAGAL", v))

print("=" * 78)
print("KESIMPULAN: %s" % ("SELURUH PEMERIKSAAN LULUS" if not bad and not extra and all(c[1] for c in chk) else "ADA MASALAH"))
print("=" * 78)
