Question Link: http://www.codechef.com/problems/AGELIMIT
    
x=int(input())
for l in range(x):
    ll,ul,ca=map(int,input().split())
    if ca>=ll and ca<ul:
        print("YES")
    else:
        print("NO")
