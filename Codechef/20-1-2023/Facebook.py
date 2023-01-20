Question Link: https://www.codechef.com/problems/FACEBOOK
    
p=int(input())
for e in range(p):
    q=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k=max(a)
    res=0
    c=0
    for l in range(q):
        if a[l]==k and c<b[l]:
            res=l
            c=b[l]
    print(res+1)
