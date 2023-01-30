Question Link: https://www.codechef.com/problems/FINDSHOES
    
k=int(input())
for l in range(k):
    x,y=list(map(int,input().split()))
    if(x<=y):
        print(x)
    else:
        print(x+(x-y))
