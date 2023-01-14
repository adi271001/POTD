Question Link: https://www.codechef.com/problems/PERMUT2
    
while(True):
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    temp=a.copy()
    for i in range(n):
        temp[a[i]-1]=i+1
    if(a==temp):
        print("ambiguous")
    else:
        print("not ambiguous")
