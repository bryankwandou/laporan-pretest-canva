# -*- coding: utf-8 -*-
import os, io, shutil, glob, hashlib, json, sys

D = "E:/Download"
SUB = os.path.join(D, "SUBMISSION_EVALUASI_PELATIHAN_CANVA")
SP = r"C:\Users\arche\AppData\Local\Temp\claude\E--Download-BAHAN-UAJMESPORT-VERCEL-APP\372bfd8c-3915-4ac6-a120-28d5f34d7220\scratchpad"

DIRS = ["01_LAPORAN_EXCEL", "02_LAPORAN_WEB", "03_DATA_SUMBER", "04_DATA_OLAHAN",
        "05_SKRIP_REPRODUKSI", "05_SKRIP_REPRODUKSI/pre", "05_SKRIP_REPRODUKSI/post",
        "06_KELUARAN_PERHITUNGAN"]
for d in DIRS:
    os.makedirs(os.path.join(SUB, d), exist_ok=True)

XPRE = "LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx"
XPOST = "LAPORAN_POSTTEST_DAN_PERBANDINGAN_CANVA.xlsx"

PLAN = [
    ("01_LAPORAN_EXCEL", [os.path.join(D, XPRE), os.path.join(D, XPOST)]),
    ("02_LAPORAN_WEB", [os.path.join(SP, "site", f) for f in ("index.html", "post-test.html", "vercel.json")]
     + [os.path.join(SP, "site", XPRE), os.path.join(SP, "site", XPOST)]),
    ("03_DATA_SUMBER", [os.path.join(D, f) for f in (
        "Wayground 25 agustus 2026 canva wkri.html",
        "pretestpelatihancanva25agustus2026-2026-08-25T09_22_13_634913-c1bee5.xlsx",
        "post-testpelatihancanva25agustus2026-2026-08-28T14_07_30_851549-68e3ea.xlsx",
        "Free Printable post-test pelatihan canva 25 agustus 2026.pdf")]),
    ("04_DATA_OLAHAN", [os.path.join(SP, f) for f in (
        "core.json", "stats.json", "post_core.json", "post_core_raw.json",
        "cmp.json", "cmp2.json", "pdf_opts.json", "post_time.json")]),
    ("05_SKRIP_REPRODUKSI", [os.path.join(SP, f) for f in (
        "mk_sub.py", "mk_index.py", "verify_sub.py", "audit_xlsx.py")]),
    ("05_SKRIP_REPRODUKSI/pre",
     [os.path.join(SP, f) for f in ("extract.py", "build_core.py", "remask.py", "stats_calc.py",
                                    "common.py", "runner.py", "run_site.py", "style.css")]
     + sorted(glob.glob(os.path.join(SP, "s[01][0-9].py")))
     + sorted(glob.glob(os.path.join(SP, "gen_?.py")))),
    ("05_SKRIP_REPRODUKSI/post",
     [os.path.join(SP, f) for f in ("post_extract.py", "post_build.py", "cmp_calc.py",
                                    "cmp_calc2.py", "pdf_opts.py", "post_time.py", "post_time.json",
                                    "run_pw.py", "run_gp.py", "style.css")]
     + sorted(glob.glob(os.path.join(SP, "pw_?.py")))
     + sorted(glob.glob(os.path.join(SP, "gp_?.py")))),
    ("06_KELUARAN_PERHITUNGAN", [os.path.join(SP, f) for f in (
        "cmp_out.txt", "cmp_out2.txt", "cmp_out3.txt", "pdf.txt", "cmp_items.txt")]
     + [(os.path.join(SP, "verify_sub.txt"), "HASIL_VERIFIKASI_PAKET.txt"),
        (os.path.join(SP, "audit_run2.txt"), "HASIL_AUDIT_KECUKUPAN_EXCEL.txt")]),
]

man = []
missing = []
for d, files in PLAN:
    for src in files:
        ren = None
        if isinstance(src, tuple):
            src, ren = src
        if not os.path.isfile(src):
            missing.append(src); continue
        dst = os.path.join(SUB, d, ren or os.path.basename(src))
        shutil.copy2(src, dst)
        h = hashlib.sha256(io.open(dst, "rb").read()).hexdigest()[:16]
        man.append((d, ren or os.path.basename(src), os.path.getsize(dst), h))

print("copied %d, missing %d" % (len(man), len(missing)))
for m in missing:
    print("  MISSING:", m)
json.dump(man, io.open(os.path.join(SP, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
