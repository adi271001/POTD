Question Link: https://www.codechef.com/problems/LCM_GCD
    
import math
for _ in range(int(input())):
    d,e=[int(d) for d in input().split()]
    y=math.gcd(d,e)
    ll=math.lcm(d,y)
    gl=math.gcd(e,y)
    print(ll-gl)
