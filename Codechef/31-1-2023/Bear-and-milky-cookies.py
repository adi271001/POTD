Question Link: https://www.codechef.com/problems/COOMILK
    
k = int(input())
for l in range(k):
    p = int(input())
    b = list(map(str,input().split()))
    
    if p == 1 and b[0] == 'cookie':
        print('NO')
    elif b[-1] == 'cookie':
        print('NO')
    else:
        l = 0
        f = 0
        while l < (p-1):
            if b[l] == 'cookie' and b[l+1] == 'cookie':
                f = 1
                break
            l = l + 1
        if f == 1:
            print('NO')
        else:
            print('YES')
