from bs4 import BeautifulSoup
import re,json
h=open(r"E:/Download/Wayground 25 agustus 2026 canva wkri.html",encoding="utf-8",errors="ignore").read()
s=BeautifulSoup(h,"html.parser")
basics=s.select('.player-basic-detail'); rows=s.select('.player-question-detail')
data=[]
for b,r in zip(basics,rows):
    txt=b.get_text("|",strip=True)
    score=b.select_one('.score').get_text(strip=True)
    acc=b.select_one('.accuracy').get_text(strip=True)
    # name: the div with whitespace-nowrap
    nm=b.select_one('.whitespace-nowrap')
    name=nm.get_text(strip=True) if nm else txt.split("|")[0]
    cells=[]
    for c in r.select('[data-testid="time-taken-card"]'):
        cls=[x for x in c.get("class") if x.startswith("bg-")][0]
        st={'bg-ds-success-500':'C','bg-red-light':'X','bg-ds-dark-100':'-'}[cls]
        t=c.get_text(strip=True)
        cells.append({"s":st,"t":None if t=='-' else int(t.rstrip('s'))})
    m=re.match(r"(\d+)%\((\d+)/(\d+)pts\)",acc.replace(" ",""))
    data.append({"rank":len(data)+1,"name":name,"score":int(score),
        "acc_pct":int(m.group(1)),"pts":int(m.group(2)),"max":int(m.group(3)),"cells":cells})
qavg=[e.get_text(strip=True) for e in s.select('.question-percent-count')]
json.dump({"players":data,"q_avg_time":[int(x.rstrip('s')) for x in qavg]},open("data.json","w"),indent=1)
print(len(data), data[0]["name"], data[0]["score"], sum(p["pts"] for p in data))
print(sum(1 for p in data for c in p["cells"] if c["s"]=="C"))
