Question Link: https://www.codechef.com/problems/CHEFAPAR
    
for _ in range(int(input())):
    p = int(input())
    q = list(map(int,input().split()))
    l = False
    t = 0
    for k in range(len(q)):
        if not l:
            if q[k] == 0:
                t += 1100
                l = True
        else:
            if q[k] == 0:
                t += 1100
            else:
                t += 100
    print(t)
