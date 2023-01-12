Question Link: https://www.codechef.com/problems/SUMDIV2
    
def ans(x,y):
    if (x==1) and (y==1):
        return 5
    if  (x*y-x-y)==-1:
        return (max(x,y)-1)
    elif (x*y-x-y)<=0:
        return max(x,y)
    else:
        return  (x*y-x-y)
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    print(ans(x,y))
