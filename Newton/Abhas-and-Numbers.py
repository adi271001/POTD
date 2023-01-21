a,b=map(int,input().split())
if (b % 2 == 0):
        c = a // b
        d = (a + (b // 2)) // b
        print( c * c * c + d * d * d)
else:
    c = a // b
    print( c * c * c)
