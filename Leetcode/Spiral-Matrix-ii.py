class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1
        row = 0
        col = 0
        direction = 0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        while num <= n * n:
            matrix[row][col] = num
            num += 1
            nextRow = row + dr[direction]
            nextCol = col + dc[direction]
            if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or matrix[nextRow][nextCol] != 0:
                direction = (direction + 1) % 4
            row += dr[direction]
            col += dc[direction]
        return matrix
