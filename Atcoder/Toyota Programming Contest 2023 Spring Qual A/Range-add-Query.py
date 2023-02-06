import sys
N, K = map(int, sys.stdin.buffer.readline().split())
A = list(map(int, sys.stdin.buffer.readline().split()))
Q, *LR = map(int ,sys.stdin.buffer.read().split())
S = [[0]*(N+1) for _ in range(K)]
for k in range(N):
  S[k%K][k+1] = A[k]
for k in range(K):
  for l in range(N):
    S[k][l+1] += S[k][l]
ans = ['Yes']*Q
for k in range(Q):
  l, r = LR[2*k]-1, LR[2*k+1]
  val = S[0][r]-S[0][l]
  for m in range(1, K):
    if S[m][r]-S[m][l] != val:
      ans[k] = 'No'
      break
print(*ans)
