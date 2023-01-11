Question Link: https://www.codechef.com/problems/XLSQUARE
    
for _ in range(int(input())):
    n,a=map(int,input().split())
    for i in range(1,n+1):
        if(i*i>n):
            print((i-1)*a)
            break
        elif (i*i==n):
            print(i*a)
            break
  
