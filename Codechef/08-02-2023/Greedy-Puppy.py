Question Link: https://www.codechef.com/problems/GDOG
    
p=int(input())
for k in range(p):
    a,b = map(int, input().split())
    d=0
    for l in range(1,b+1):
        d=max(d,a%l)
    print(d)
