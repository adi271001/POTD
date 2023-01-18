Question Link: http://www.codechef.com/problems/BESTOFTWO
    
a=int(input())
for l in range(a):
    fa,sa=map(int,input().split())
    print(max(fa,sa))
