Question Link: https://www.codechef.com/problems/EITA

for k in range(int(input())):
        e,a,b,c=map(int,input().split())
        print(max(a*7,b*e+(c*(7-e))))
