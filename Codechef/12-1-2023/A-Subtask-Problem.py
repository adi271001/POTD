Question Link: https://www.codechef.com/problems/SUBTASK
    
t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        l = list(map(int, input().split()))
        c = 0
        for i in l:
            if i == 1:
                c += 1
            else:
                break
        if c == n:
            print(100)
        elif c >= m:
            print(k)
        else:
            print(0)
