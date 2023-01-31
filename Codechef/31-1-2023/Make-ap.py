Question Link: https://www.codechef.com/problems/MAKEAP
    
for k in range(int(input())):
    x,y=map(int,input().split())
    if(x+y)%2==0:
        print((x+y)//2)
    else:
        print(-1)
