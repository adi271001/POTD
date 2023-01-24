Question Link: https://www.codechef.com/problems/BRACKETS
    
import sys
tc = int(input())
while(tc > 0):
    fS = input()
    mB = 0
    cB = 0
    for l in fS:
        if(l == '('):
            cB += 1
        else:
            cB -= 1
        if(cB > mB):
            mB = cB
    rS = ""
    i1 = mB
    while(i1 > 0):
        rS += "("
        i1 -= 1
    i1 = mB
    while(i1 > 0):
        rS += ")"
        i1 -= 1
    print(rS)
    tc -= 1
