Question Link: https://www.codechef.com/problems/DIAGMOVE
    
for _ in range(int(input())):
    x,y=map(int,input().split())
    if((x+y)%2 == 0):
        print('YES')
    else:
        print('NO')
