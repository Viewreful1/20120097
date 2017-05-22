f=lambda:map(int,input().split());n,m,v=f();g={};[g.setdefault(c,{c}).add(d)for a,b in eval('f(),'*m)for c,d in[(a,b),(b,a)]]
for z in-1,0:
 t,*r=[v],
 while t:
  s=t.pop(z)
  if(s in r)<1:r+=s,;t+=sorted(g[s])[::z+z+1]
 print(*r)