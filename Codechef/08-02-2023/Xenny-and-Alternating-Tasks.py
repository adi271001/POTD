Question Link: https://www.codechef.com/problems/XENTASK
    
import sys
for _ in range(int(sys.stdin.readline())):
    p=int(sys.stdin.readline())
    y=list(map(int,sys.stdin.readline().split()))
    y+=list(map(int,sys.stdin.readline().split()))
    c,d=0,0
    for k in range(p):
        if k%2==0:
            c+=y[k]
            d+=y[p+k]
        else:
            c+=y[p+k]
            d+=y[k]
    sys.stdout.write(str(min(c,d))+'\n')
