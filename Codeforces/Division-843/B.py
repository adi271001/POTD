Question Link: https://codeforces.com/contest/1775/problem/B
    
from collections import*
T=lambda:[*map(int,input().split())]
for _ in[0]*T()[0]:
 b=[];d=Counter()
 for _ in[0]*T()[0]:b+=T()[1:],;d.update(b[-1])
 print('YNeos'[all(any(d[y]<2for y in z)for z in b)::2])
