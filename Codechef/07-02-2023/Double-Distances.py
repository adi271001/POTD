Question Link: https://www.codechef.com/problems/DOUBLEDDIST
    
def check(a):
    for k in range(len(a)-2):
        d = a[k+1] - a[k]
        e = a[k+2] - a[k+1]
        if d != 2*e and e != 2*d:
            return 'No'
    return 'Yes'
for _ in range(int(input())):
    n = int(input()) 
    a = [int(x) for x in input().split()] 
    a = sorted(a)
    print(check(a))
