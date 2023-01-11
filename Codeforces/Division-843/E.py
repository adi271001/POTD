Question Link: https://codeforces.com/contest/1775/problem/E
    
v = int(input())
for _ in range(v):
	p = int(input())
	d = [ 0 ] + list(map(int, input().split()))
	for j in range(p):
		d[j + 1] += d[j]
	print(max(d) - min(d))
