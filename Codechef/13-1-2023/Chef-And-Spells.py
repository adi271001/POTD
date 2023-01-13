Question Link: https://www.codechef.com/problems/CHFSPL
    
for i in range(T):
    l=[int(x) for x in input().split()]
    m=max(l)
    l.remove(m)
    n=max(l)
    print(m+n)
