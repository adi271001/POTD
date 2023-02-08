Question Link: https://www.codechef.com/problems/STRPALIN
    
for _ in range(int(input())):
    d=input()
    e=input()
    f=0
    for k in d:
        for l in e:
            if k==l:
                f=1
                break
    if f==1:
        print("Yes")
    else:
        print("No")
