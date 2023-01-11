Question Link:
  
for i in range(int(input())):
    n, x = map(int, input().split())
    a = []
    if n%2==0:
        initial = x-n//2
        k = initial
        while k < x:
            a += [k]
            k+=1
        k+=1
        while k <= x+n//2:
            a += [k]
            k+=1
    else:
        a+= range(x-n//2, x+n//2+1)
    print(*a)
