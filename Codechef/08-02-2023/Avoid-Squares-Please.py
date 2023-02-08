k=int(input())
for c in range(k):
    p=int(input())
    m=[]
    for l in range(1,p+1):
        m.append(p)
        p-=1
    for l in m:
        print(l,end=" ")
    print()
