Question Link: https://www.codechef.com/problems/CABS
    
m=int(input())
for m in range(m):
    x,y=map(int, input().split())
    if(x<y):
        print("FIRST")
    elif(x==y):
        print("ANY")
    else:
        print("SECOND")
