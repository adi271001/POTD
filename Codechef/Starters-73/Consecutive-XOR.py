t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n%2==1:
        print('YES')
        continue
    res = 0
    for i in a:
        res = res^i
    if res == 0:
        print('YES')
    else:
        print('NO')
