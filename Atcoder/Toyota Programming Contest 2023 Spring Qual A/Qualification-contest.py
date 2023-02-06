n, k = map(int, input().split())
s = [input() for _ in range(n)]
t=s[:k]
t=sorted(t)
for i in range(k):
  print(t[i])
