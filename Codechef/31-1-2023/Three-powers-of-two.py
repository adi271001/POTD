Question Link: https://www.codechef.com/problems/THREEPOW2
    
for _ in range(int(input())):
    n=int(input())
    t=input()
    k=0
    e=0
    if t=="1" or t=="10" or t=="01":
        print("NO")
    else:
        while k<len(t):
                if t[k]=="1":
                    e+=1
                k+=1
        if e<=3:
            print("YES")
        else:
            print("NO")
        
