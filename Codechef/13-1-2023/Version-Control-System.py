Question Link: https://www.codechef.com/problems/VCS
    
for t in range(int(input())):
    n,m,k=map(int,input().split())
    sq1=list(map(int,input().split()))
    sq2=list(map(int,input().split()))
    c1=c2=0
    for i in range(1,n+1):
        if (i in sq1) and (i in sq2):
            c1+=1 
        elif (i not in sq1) and (i not in sq2):
            c2+=1 
    print(f"{c1} {c2}")
