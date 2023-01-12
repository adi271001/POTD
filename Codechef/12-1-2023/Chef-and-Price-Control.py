Question Link: https://www.codechef.com/problems/PRICECON
    
for i in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    s=sum(p)
    l=0
    for i in p:
        if i>k:
            l+=k 
        else:
            l+=i 
    print(s-l)
