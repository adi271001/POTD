Question Link: https://www.codechef.com/problems/HAMTREE
  
from sys import stdin , setrecursionlimit
input = stdin.readline
setrecursionlimit(3 * (10 ** 5))
inp = lambda : list(map(int,input().split()))
def dfs(p , prev , t):
    if(dp[p][t] != -1):return dp[p][t]
    best = []
    for i in child[p]:
        if(i == prev):continue
        tv1 , tv2 = dfs(i , p , 0) , dfs(i , p , 1)
        best.append([tv1 - tv2 , tv1 , tv2])
    best.sort()
    ans = 0
    if(t == 0):
        counter = 2
        while(len(best) and counter):
            counter -= 1
            diff , tv1 , tv2 = best.pop()
            ans += tv2
        while(len(best)):
            diff , tv1 , tv2 = best.pop()
            ans += tv1 + 1
    else:
        counter = 1
        while(len(best) and counter):
            counter -= 1
            diff , tv1 , tv2 = best.pop()
            ans += tv2
        while(len(best)):
            diff , tv1 , tv2 = best.pop()
            ans += tv1 + 1
    dp[p][t] = ans
    return ans
