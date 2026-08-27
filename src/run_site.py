import io
for f in ["gen_a.py","gen_b.py","gen_c.py","gen_d.py","gen_e.py"]:
    exec(compile(io.open(f,encoding="utf-8").read(),f,"exec"),globals())
