Question Link: https://codeforces.com/contest/1775/problem/C
    
for j in range(int(input())):
    b, c = [int(j) for j in input().split()]
    bc = bin(b)[2:]
    cc = bin(c)[2:]
    y = b
    z = b
    found = False
    while y > 0:
        if y == c:
            found = True
            print(z)
            break
        z += z & -z
        y &= z
    if c == 0:
        print(z)
    elif not found:
        print(-1)
