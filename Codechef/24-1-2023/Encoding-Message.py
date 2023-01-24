Question Link: https://www.codechef.com/problems/ENCMSG
    
n = int(input())
for y in range(n):
    l = int(input())
    s = input()
    ls = list(s)
    if (l % 2 != 0):
        lx = l - 1
    else:
        lx = l
    for z in range(0, lx, 2):
        t = ls[z]
        ls[z] = ls[z + 1]
        ls[z + 1] =  t
    a = 'abcdefghijklmnopqrstuvwxyz'
    for y in range(0, l):
        ls[y] = a[25 - a.index(ls[y])]
    st = ''.join(ls)
    print(st)
