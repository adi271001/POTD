Question Link: https://www.codechef.com/problems/PRACTICEPERF
    
k = list(map(int,input().split()))
c = 0
for l in k:
    if l>=10:
        c = c + 1
print(c)
