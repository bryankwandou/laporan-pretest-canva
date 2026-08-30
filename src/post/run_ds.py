import io
from collections import Counter
for f in ["ds_a.py","ds_b.py","ds_c.py","ds_d.py"]:
    exec(compile(io.open(f,encoding="utf-8").read(),f,"exec"),globals())
