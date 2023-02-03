Question Link: https://www.codechef.com/problems/RACE400M
    
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    t = min(a,b,c)
    if temp == a: print("ALICE")
    elif temp == b: print("BOB")
    else: print("CHARLIE")
