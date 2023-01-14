Question Link: https://www.codechef.com/problems/SLAB
    
T=int(input())
while T:
    T-=1
    n=int(input())
    m=n
    tax=0
    if(n>1500000):
        tax+=0.3*(n-1500000)
        n=1500000
    if(n>1250000):
        tax+=0.25*(n-1250000)
        n=1250000
    if(n>1000000):
        tax+=int(0.2*(n-1000000))
        n=1000000
    if(n>750000):
        tax+=int(0.15*(n-750000))
        n=750000
    if(n>500000):
        tax+=int(0.1*(n-500000))
        n=500000
    if(n>250000):
        tax+=int(0.05*(n-250000))
    print(int(m-tax))
