Question Link: https://codeforces.com/contest/1775/problem/D
    
m=3*100001
d,b=[],[]
def gap():
	global d,b
	d,b=[[]for _ in range(m)],[0]*m
	for i in range(2,m):
		if b[i]:continue
		for j in range(i,m,i):b[j]=1;d[j].append(i)
def main():
	n=int(input());a=list(map(int,input().split()));s,t=map(int,input().split())
	s,t,p,q,l,r,y=s-1,t-1,[-1]*n,[],[0]*m,[-1]*m,[]
	for i in range(n):r[a[i]]=i
	r[a[s]],r[a[t]]=s,t
	p[s]=s
	q.append(s)
	for i in q:
		v=a[i]
		for u in d[v]:
			if l[u]:continue
			l[u]=1
			for j in range(u,m,u):
				if r[j]!=-1 and p[r[j]]<0:p[r[j]]=i;q.append(r[j])
	if p[t]==-1:
		print(-1)
	else:
		while t!=s:y.append(t+1);t=p[t]
		y+=[s+1]
		print(len(y));print(*y[::-1])
gap(),main()
