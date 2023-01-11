Question Link: https://www.codechef.com/problems/CHEFWORK
  
n = int(input())
a = [int(x) for x in input().split()] 
b = [int(x) for x in input().split()] 
d = {1: 999999, 2: 999999, 3: 999999}
for i in range(n):
    if b[i] == 1:
        d[1] = min([a[i], d[1]])
    elif b[i] == 2:
        d[2] = min([a[i], d[2]])
    else:
        d[3] = min([a[i], d[3]])
print(min([d[1]+d[2],d[3]]))
