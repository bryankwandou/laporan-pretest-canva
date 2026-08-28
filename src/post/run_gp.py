import io
for f in ["gp_a.py","gp_b.py","gp_c.py","gp_d.py","gp_e.py","gp_f.py"]:
    exec(compile(io.open(f,encoding="utf-8").read(),f,"exec"),globals())
