Question Link: https://www.codechef.com/problems/APPENDOR
    
for _ in range(int(input())):
    n,y= map(int,input().split())
    a=list(map(int,input().split()))
    col=0
    for i in a:
        col|=i
    sum1=y-col
    if sum1|col==y:
        print(sum1)
    else:
        print("-1")
