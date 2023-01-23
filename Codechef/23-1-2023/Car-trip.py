Question Link: https://www.codechef.com/problems/CARTRIP
    
p=int(input())
for k in range(p):
    a=int(input())
    if a<=300:
        print(3000)
    else:
        print(a*10)
