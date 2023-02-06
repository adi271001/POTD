n,m = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
D = [0]*n
for x in map(int,input().split()):
  D[x-1] = 1
dp = [1<<60]*(n+1)
dp[0] = 0
for i in range(n):
  M = [C[i]]*(i+1)
  for j in range(i):
    M[j+1] = min(M[j],C[i-1-j])
  for j in range(i+1)[::-1]:
    dp[j+1] = min(dp[j+1],dp[j]+A[i]+M[j])
    if D[i]:
      dp[j] = 1<<60
print(min(dp))
