class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here 
        x_positions = []
        y_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'X':
                    x_positions.append((i, j))
                elif grid[i][j] == 'Y':
                    y_positions.append((i, j))
        min_distance = float('inf')
        for x in x_positions:
            for y in y_positions:
                distance = abs(x[0] - y[0]) + abs(x[1] - y[1])
                min_distance = min(min_distance, distance)
        return min_distance
