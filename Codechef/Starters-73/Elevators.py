Question Link: https://www.codechef.com/problems/ELEVATORS
  
for _ in range(int(input())):
    [n,m,h]=list(map(int,input().split()))
    arr=[]
    for i in range(n):
        [a,b]=list(map(int,input().split()))
        arr.append(b)
    arr.sort()
    def solve(k):
        # no of persons=n
        # no of ele=m 
        # time=k
        index=n-1
        elevs=m
        time=arr[index]-1
        while(index>=0 and elevs):
            while(index>=0 and time+2*h<=k):
                time+=2*h
                index-=1 
            if index<0:
                break 
            elevs-=1 
            time=arr[index]-1
        if index<0:
            return 1 
        return 0
    l=arr[-1]+2*h-1
    r=arr[-1]+2*h*n-1 
    while(l<r):
        mid=(l+r)//2
        # print(l,r)
        if solve(mid):
            r=mid
        else:
            l=mid+1
    print(l)
