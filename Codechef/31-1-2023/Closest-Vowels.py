Question Link: https://www.codechef.com/problems/CLOSEVOWEL
    
from collections import defaultdict

MOD = 1000000007
def closest_vow():
    vo='aeiou'
    co='bcdfghjklmnpqrstvwxyz'
    d = defaultdict(list)
    for c in co:
        min_dist = float('inf')
        for v in vo:
            dist = abs(ord(v) - ord(c))
            if dist < min_dist:
                min_dist = dist
                d[c] = [v]
            elif dist == min_dist and len(d[c]) == 1:
                d[c].append(v)
    return {k:v for k,v in d.items() if len(v) == 2}

def beaut_str(s, cl):
    count=0
    for c in s:
        if c in cl:
            count+=1
    return (2**count)%MOD

for _ in range(int(input())):
    n = int(input())
    s = input()
    cl=closest_vow()
    print(beaut_str(s, cl))
