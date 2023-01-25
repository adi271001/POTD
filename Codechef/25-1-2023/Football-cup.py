Question Link: https://www.codechef.com/problems/FOOTCUP
    
p=int(input())
for k in range(p):
    a,b=map(int,input().split())
    if(a==b and (a!=0 and b!=0)):
        print("YES")
    else:
        print("NO")
