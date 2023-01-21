Question Link: https://www.codechef.com/problems/COVID19
    
p=int(input())
def adha(m,q):
    e=1
    s=[]
    for k in range(m-1):
        if(q[k+1]-q[k]>2):
            s.append(e)
            e=1 
        else:
            e+=1
    s.append(e)
    return min(s),max(s)
for _ in range(p):
    m=int(input())
    q=list(map(int,input().split()))
    c,d=adha(m,q)
    print(c,d)
