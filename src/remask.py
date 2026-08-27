# -*- coding: utf-8 -*-
import json
from collections import Counter
d=json.load(open("core.json",encoding="utf-8"))
Q,CORR=d["Q"],d["CORR"]
bad=0
for q in Q:
    qi=q["no"]-1
    real={}
    for n,st in CORR.items():
        a=q["answers"].get(n)
        if st[qi]=='-' or a in (None,"None"): real[n]=None
        else: real[n]=a
    q["answers_real"]=real
    c=Counter(v for v in real.values() if v)
    tot=sum(c.values())
    ok = tot==q["correct"]+q["incorrect"] and c.get(q["key"],0)==q["correct"]
    if not ok: bad+=1; print("MISMATCH Q",q["no"],tot,q["correct"]+q["incorrect"],c.get(q["key"],0),q["correct"])
    q["distr_real"]=c.most_common()
print("mismatches:",bad)
json.dump(d,open("core.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
