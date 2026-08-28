import io
for f in ["pw_a.py","pw_b.py","pw_c.py","pw_d.py","pw_e.py","pw_f.py","pw_g.py","pw_h.py","pw_i.py","pw_j.py","pw_k.py"]:
    exec(compile(io.open(f,encoding="utf-8").read(),f,"exec"),globals())
