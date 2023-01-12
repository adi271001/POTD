Question Link: https://www.codechef.com/problems/TABLETS
    
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    if((3*a)<=b):
        print("yes")
    else:
        print("no")
    t=t-1
