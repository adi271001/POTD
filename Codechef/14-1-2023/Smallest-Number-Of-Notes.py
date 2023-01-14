Question Link: https://www.codechef.com/problems/FLOW005
    
for i in range(int(input())):
    n=int(input())
    a=[100,50,10,5,2,1]
    c=0
    for i in a:
        if(n//i!=0):
            c+=n//i
            n=n%i
    print(c)
