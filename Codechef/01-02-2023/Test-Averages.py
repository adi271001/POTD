Question Link: https://www.codechef.com/problems/TESTAVG
    
def avg(d,e):
    f = (d+e)/2
    if(f>=35):
        return 1 
    else:
        return 0
for t in range(int(input())):
    d,e,f = map(int,input().split())
    g1 = avg(d,e)
    g2 = avg(e,f)
    g3 = avg(d,f)
    if(g1 ==1 and g2 ==1 and g3 ==1):
        print("PASS")
    else:
        print("Fail")
