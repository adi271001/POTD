Question Link: https://www.codechef.com/problems/CYCLICQD
    
for _ in range(int(input())):
    w,x,y,z = map(int,input().split())
    if w + y == 180:
        print('yes')
    else:
        print('no')
