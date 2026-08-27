# -*- coding: utf-8 -*-
import json, math, statistics as st
from collections import Counter, defaultdict
d=json.load(open("core.json",encoding="utf-8"))
Q,P,TIME,CORR=d["Q"],d["P"],d["TIME"],d["CORR"]
N=37
# ---- dedupe map
import re
def base(n): return re.sub(r"\*+$","",n).strip()
groups=defaultdict(list)
for n in P: groups[base(n)].append(n)
best={}
for b,lst in groups.items():
    best[b]=max(lst,key=lambda n:(P[n]["correct"],P[n]["score"]))
UNIQ=sorted(best.values(), key=lambda n:-P[n]["score"])
# ---- item stats on full 37
scores={n:P[n]["correct"] for n in P}
order=sorted(P,key=lambda n:-scores[n])
k=round(0.27*N)  # 10
upper,lower=order[:k],order[-k:]
def right(n,qi): return 1 if CORR[n][qi]=="C" else 0
items=[]
sc_list=[scores[n] for n in P]
mean_s=st.mean(sc_list); sd_s=st.pstdev(sc_list)
for q in Q:
    qi=q["no"]-1
    p=q["correct"]/N
    U=sum(right(n,qi) for n in upper); L=sum(right(n,qi) for n in lower)
    D=(U-L)/k
    # point-biserial
    g1=[scores[n] for n in P if right(n,qi)]; g0=[scores[n] for n in P if not right(n,qi)]
    if g1 and g0 and sd_s>0:
        rpb=(st.mean(g1)-st.mean(g0))/sd_s*math.sqrt(p*(1-p))
    else: rpb=float('nan')
    cnt=Counter(dict(q["distr_real"]))
    distr=q["distr_real"]
    nonkey=[(a,c) for a,c in distr if a!=q["key"]]
    eff=sum(1 for a,c in nonkey if c/max(1,sum(dict(distr).values()))>=0.05)
    items.append(dict(no=q["no"],text=q["text"],p=p,U=U,L=L,D=D,rpb=rpb,
        correct=q["correct"],incorrect=q["incorrect"],blank=N-q["correct"]-q["incorrect"],
        key=q["key"],distr=distr,eff_distr=eff,nopt=len(distr),
        avg_t=q["avgt"], top_wrong=nonkey[0] if nonkey else ("-",0)))
# KR-20
var_tot=st.pvariance(sc_list)
kr20=(20/19)*(1-sum(i["p"]*(1-i["p"]) for i in items)/var_tot)
sem=sd_s*math.sqrt(1-kr20)
# active cohort (score>0)
act=[n for n in P if P[n]["correct"]>0]
out=dict(items=items,kr20=kr20,sem=sem,mean=mean_s,sd=sd_s,var=var_tot,
    upper=[base(n) for n in upper],lower=[base(n) for n in lower],
    uniq=UNIQ,best=best,n_active=len(act))
json.dump(out,open("stats.json","w",encoding="utf-8"),ensure_ascii=False,indent=1,default=str)
print("KR20=%.3f SEM=%.2f mean=%.2f sd=%.2f"%(kr20,sem,mean_s,sd_s))
print("unique",len(UNIQ),"active",len(act))
for i in items: print(i["no"],"p=%.2f D=%.2f rpb=%.2f eff=%d"%(i["p"],i["D"],i["rpb"],i["eff_distr"]))
