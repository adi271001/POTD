Question Link: http://1.codechef.com/problems/TALLER
    
p = int(input())
for l in range(p):
    x, y = map(int, input().split())
    if x > y:
        print("A")
    elif x < y:
        print("B")
