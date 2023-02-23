class Solution:
    def uniquePaths(self, n, m, grid):
        # code here 
        if grid[0][0] == 0 or grid[n-1][m-1] == 0: return 0
        vs = [0]*m; vs[0] = 1
        for r in range(n):
            vs[0] = 0 if grid[r][0] == 0 else vs[0] 
            for c in range(1, m):
                if grid[r][c]: vs[c] += vs[c-1]
                else: vs[c] = 0
        return vs[m-1] % (10**9+7)
