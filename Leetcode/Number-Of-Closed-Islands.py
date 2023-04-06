class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        co = 0
        
        def dfs(k, l):
            if k < 0 or l < 0 or k >= r or l >= c:
                return False
            if grid[k][l] == 1:
                return True
            grid[k][l] = 1 # mark as visited
            le = dfs(k, l-1)
            ri = dfs(k, l+1)
            u = dfs(k-1, l)
            d = dfs(k+1, l)
            return le and ri and u and d
        
        for k in range(r):
            for l in range(c):
                if grid[k][l] == 0 and dfs(k, l):
                    co += 1
        
        return co
