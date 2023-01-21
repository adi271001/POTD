Question Link: https://www.codechef.com/problems/SUMM
    
for l in range(int(input())):
    x,y,z=map(int,input().split())
    if(x+y==z):
        print("YES")
    else:
        print("NO")
