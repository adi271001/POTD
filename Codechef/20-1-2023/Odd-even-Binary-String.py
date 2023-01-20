Question Link: https://www.codechef.com/problems/ODDEVENBS
    
t_n=int(input())
for tt in range(t_n):
    p = int(input())
    m = list(map(int,input().split()))
    if(p%2==sum(m)%2):
        print("yes")
    else:
        print("no")
