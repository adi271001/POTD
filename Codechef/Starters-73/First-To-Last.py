Question Link: https://www.codechef.com/problems/FTOL
    
for _ in range(int(input())):
    [n,m,k]=list(map(int,input().split()))
    tot=(m-1)*(n-1)
    arr=[]
    for i in range(k):
        [a,b]=list(map(int,input().split()))
        if a<n and b<m:
            arr.append((a,b))
    arr.sort(key=lambda x:(x[0],-1*x[1]))
    import bisect
    x=[]
    for i in arr:
        k=len(x)
        temp=bisect.bisect_left(x,i[1])
        if temp==k:
            x.append(i[1])
        else:
            x[temp]=i[1]
    print(m+n-2-len(x))
