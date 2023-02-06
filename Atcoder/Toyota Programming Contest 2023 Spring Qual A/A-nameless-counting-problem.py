mod=998244353
def cmb(n,r):
  if r<0 or r>n:
    return 0
  return ((g1[n]*g2[r]%mod)*g2[n-r])%mod
 
def Bcmb(n,r):
  if r<0 or r>n:
    return 0
  a=g2[r]
  for i in range(1,r+1):
    a=a*(n+1-i)%mod
  return a
 
N=300000
g1=[1]*(N+3)
for i in range(2,N+3):
  g1[i]=g1[i-1]*i%mod
g2=[0]*len(g1)
g2[-1]=pow(g1[-1],mod-2,mod)
for i in range(N+1,-1,-1):
  g2[i]=g2[i+1]*(i+1)%mod
inv=[0]*(N+3)
for i in range(1,N+3):
  inv[i]=g2[i]*g1[i-1]%mod
def f(n,k):
  if k<0:
    return 0
  Y=1<<n
  X=Bcmb(k+Y-1,k)
  if k&1:
    X=X*pow(Y,mod-2,mod)%mod
  else:
    Z=Bcmb((k>>1)+(Y>>1)-1,(k>>1))
    X=(X-Z)*pow(Y,mod-2,mod)%mod
  return X
 
V0=[[0]*202 for i in range(31)]
V1=[[0]*202 for i in range(31)]
for k in range(202):
  for n in range(31):
    V1[n][k]=f(n,k)
    V0[n][k]=(Bcmb((1<<n)+k-1,k)-V1[n][k]*((1<<n)-1))%mod
N,M,X=map(int,input().split())
if M==0:
  if X==0:
    print(1)
  else:
    print(0)
  exit()
if M.bit_length()<X.bit_length():
  print(0)
  exit()
M+=1
B=[]
for i in range(31):
  if (M>>i)&1:
    B.append(i)
B=B[::-1]
L=len(B)
B.append(-1)
DP=[[[0,0] for j in range(N+1)] for i in range(L+1)]
DP[0][0][0]=1
for i in range(L):
  for j in range(N+1):
    for k in range(N-j+1):
      v=(N-j-k)&1
      a,b,c=DP[i][j][1],DP[i][j][1]*((1<<B[i])-1)%mod,DP[i][j][1]
      if (X>>B[i])&1==v:
        a=DP[i][j][0]
      d=1
      for l in range(B[i]-1,B[i+1],-1):
        if (X>>l)&1:
          d=0
      if d:
        DP[i+1][j+k][0]=(DP[i+1][j+k][0]+a*V0[B[i]][k]+b*V1[B[i]][k])%mod
        DP[i+1][j+k][1]=(DP[i+1][j+k][1]+a*V1[B[i]][k]+(b-c)*V1[B[i]][k]+c*V0[B[i]][k])%mod
      else:
        DP[i+1][j+k][0]=(DP[i+1][j+k][0]+a*V1[B[i]][k]+(b-c)*V1[B[i]][k]+c*V0[B[i]][k])%mod
        DP[i+1][j+k][1]=(DP[i+1][j+k][1]+a*V1[B[i]][k]+(b-c)*V1[B[i]][k]+c*V0[B[i]][k])%mod
 
 
print(DP[L][N][0])
