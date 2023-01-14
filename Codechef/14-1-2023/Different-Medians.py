Question Link: https://www.codechef.com/problems/DIFFMED
    
for i in range(int(input())):
    n = int(input())
    h = n//2+1
    flag = False
    for i in range(0, n):
        if not flag:
            h = h+i
        if flag:
            h = h-i
        flag = not flag
        print(h, end=" ")
    print()
