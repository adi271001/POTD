Question Link: https://www.codechef.com/problems/EVENTUAL
    
e=int(input())
for k in range(e):
    s=int(input())
    t=input()
    u=0
    for k in t:
        u=t.count(k)
        if(u%2==0):
            u=0
        else:
            u=1
            break 
    if(u!=0):
        print("NO")
    else:
        print("YES")
