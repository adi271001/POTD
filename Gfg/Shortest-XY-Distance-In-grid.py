class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here 
        visited = [[0 for i in range(M)] for j in range(N)]
        queue = []
        for i in range(N):
            for j in range(M):
                if(grid[i][j] == 'X'):
                    queue.append([[i,j],0])
                    visited[i][j] = 1
        dr = [0,0,-1,1]
        dc = [1,-1,0,0]
        while(len(queue)>0):
            node = queue.pop(0)
            cr = node[0][0]
            cc = node[0][1]
            gap = node[1]
            if(grid[cr][cc] == 'Y'):
                return gap
            for k in range(4):
                nr = cr+dr[k]
                nc = cc+dc[k]
                if(0<=nr<len(grid) and 0<=nc<len(grid[0]) and visited[nr][nc] == 0):
                    queue.append([[nr,nc],gap+1])
                    visited[nr][nc] = 1
        return -1
