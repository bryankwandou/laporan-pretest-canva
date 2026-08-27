# -*- coding: utf-8 -*-
import io, sys
from common import *
wb = openpyxl.Workbook()
g = dict(globals())
for f in sys.argv[1:]:
    exec(compile(io.open(f, encoding="utf-8").read(), f, "exec"), g)
g["wb"].save("LAPORAN_EVALUASI_PRETEST_CANVA_25AGT2026.xlsx")
print("saved", [w.title for w in g["wb"].worksheets])
