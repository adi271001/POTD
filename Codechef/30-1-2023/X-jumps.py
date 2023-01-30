Question Link: https://www.codechef.com/problems/XJUMP
    
g = int(input())
for d in range(g):
    l, w = map(int, input().split())
    print((l % w) + (l // w))
