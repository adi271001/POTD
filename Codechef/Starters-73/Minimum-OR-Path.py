Question Link: https://www.codechef.com/problems/MINORPATH
    
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    def check(mask):
        if arr[0]|mask!=mask:
            return False
        if arr[-1]|mask!=mask:
            return False
        dp=[False]*(n)
        dp[0]=True
        j=0
        for i in range(n):
            if arr[i]|mask!=mask:
                continue
            if not dp[i]:
                continue
            r=min(n-1,i+arr[i])
            while j<=r:
                if arr[j]|mask==mask:
                    dp[j]=True
                j+=1
        return dp[-1]
    mask=(1<<19)-1
    if not check(mask):
        print(-1)
    else:
        for i in range(18,-1,-1):
            mask^=(1<<i)
            if not check(mask):
                mask|=(1<<i)
                
        print(mask)
