# -*- coding: utf-8 -*-
"""Ekstrak matriks waktu per butir post-test dari sheet Time Data."""
import openpyxl, io, json, re

PT = "E:/Download/post-testpelatihancanva25agustus2026-2026-08-28T14_07_30_851549-68e3ea.xlsx"
wb = openpyxl.load_workbook(PT, data_only=True)
rows = [list(r) for r in wb["Time Data"].iter_rows(values_only=True)]
hdr = rows[0]
pcols = [(i, str(hdr[i]).strip()) for i in range(5, len(hdr)) if hdr[i] is not None]


def secs(v):
    if v is None:
        return None
    s = str(v).strip()
    if s in ("-", "", "None"):
        return None
    m = re.match(r"^(\d+):(\d+):(\d+)$", s)
    if not m:
        return None
    h, mi, se = [int(x) for x in m.groups()]
    return h * 3600 + mi * 60 + se


TIME = {n: {} for i, n in pcols}
AVG = {}
for r in rows[1:]:
    if r[0] is None:
        continue
    q = int(r[0])
    AVG[q] = secs(r[4])
    for i, n in pcols:
        TIME[n][q] = secs(r[i])

json.dump({"TIME": TIME, "AVG": AVG}, io.open("post_time.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
n_cells = sum(1 for n in TIME for q in TIME[n] if TIME[n][q] is not None)
print("peserta=%d butir=%d sel_terisi=%d" % (len(TIME), len(AVG), n_cells))
print("Vincent entri 1 detik:", sum(1 for q, v in TIME["Vincent"].items() if v == 1))
