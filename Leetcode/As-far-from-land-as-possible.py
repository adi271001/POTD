Question Link:
  
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        p = len(grid)
        dq = deque((i, j) for i in range(p) for j in range(p) if grid[i][j])
        r = 0
        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < p and 0 <= c1 < p and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    r = max(r, grid[r1][c1])
        return r - 1
