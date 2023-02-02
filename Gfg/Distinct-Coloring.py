Question Link: https://practice.geeksforgeeks.org/problems/844b4fdcd988ac5461324d62d43f7892749a113c/1
    
class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        dp = [[0 for i in range(3)] for _ in range(N)]
        dp[0][0] = r[0]
        dp[0][1] = g[0]
        dp[0][2] = b[0]
        for i in range(1,N):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + r[i]
            dp[i][1] = min(dp[i-1][0],dp[i-1][2])+g[i]
            dp[i][2] = min(dp[i-1][0],dp[i-1][1])+b[i]
            
        return min(dp[N-1][0],dp[N-1][1],dp[N-1][2])
