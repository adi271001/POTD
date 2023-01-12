Question Link: https://www.codechef.com/problems/TWODISH
    
n=int(input())
for i in range(n):
    n,a,b,c=map(int,input().split())
    d = a+c
    if n<=a+c and n<=b:
        print("YES")
    else:
        print("NO")
