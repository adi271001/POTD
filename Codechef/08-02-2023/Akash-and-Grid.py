Question Link: https://www.codechef.com/problems/CHEFGRD
    
for _ in range(int(input())):
    p,a,b = map(int,input().split())
    if (a+b)%2 ==0:
        print("0")
    else:
        print("1")
