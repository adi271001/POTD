Question Link: https://codeforces.com/contest/1775/problem/A2
  
for p in[*open(0)][1:]:
    j=2-4*(p[1]>'a')
    print(p[0],p[1:j],p[j:-1])
