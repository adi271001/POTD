Question Link: https://www.codechef.com/problems/M1ENROL
    
p = int(input())
for l in range(p):
    a, b = map(int, input().split())
    if (b > a):
        print(b-a)
    else:
        print(0)
