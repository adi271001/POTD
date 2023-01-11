Question Link: https://codeforces.com/contest/1775/problem/A1
    
for s in[*open(0)][1:]:
    print(s[0],*((s[1],s[2:-1]),(s[1:-2],s[-2]))[s[1]>'a'])
