Question Link: https://www.codechef.com/problems/PLAYFIT
    
for _ in range(int(input())):
    n=int(input())
    x=list(map(int, input().split()))
    i=1
    s=x[0]
    b=0
    d=0
    while i<n:
        if x[i]<x[i-1]:
            s=min(s,x[i])
            i+=1
        else:
            d=max(d,x[i]-s)
            i+=1
    if d==0:
        print("UNFIT")
    else:
        print(d)
