Question Link: https://www.codechef.com/problems/ELECTIONS
    
t = int(input())
for i in range(t):
    a,b,c = (map(int,input().split()))
    if a>50:
        print("A")
    elif b>50:
        print("B")
    elif c>50:
        print("C")
    else:
        print("NOTA")
