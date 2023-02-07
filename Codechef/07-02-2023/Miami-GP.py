Question Link: https://www.codechef.com/problems/F1RULE

l=int(input())
for k in range(l):
    a,b=map(int,input().split())
    if b<=a*107/100:
        print("yes")
    else:
        print("no")
