Question Link: https://www.codechef.com/problems/EVMHACK
    
t=int(input())
for i in range(t):
    a,b,c,p,q,r=map(int, input().split())
    x=(p+q+r)/2
    if a+b+r>x:
        print("YES")
    elif a+q+c>x:
        print("YES")
    elif p+b+c>x:
        print("YES")
    else:
        print("NO")
