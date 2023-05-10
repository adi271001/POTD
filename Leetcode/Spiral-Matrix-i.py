class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        remains = m * n
        i = 0
        j = 0
        order = 0
        answer = []
        while remains > 0:
            answer.append(matrix[i][j])
            matrix[i][j] = -999
            remains -= 1

            for _ in range(len(move)):
                di, dj = move[order]
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] >= -100:
                    i = ni
                    j = nj
                    break
                else:
                    order = (order + 1) % len(move)
        return answer
