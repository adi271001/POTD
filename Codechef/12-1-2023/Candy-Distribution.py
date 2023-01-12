Question Link: https://www.codechef.com/problems/CANDYDIST
    
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n%m==0 and (n//m)%2==0:print("YES")
    else:print("NO")
