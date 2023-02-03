https://practice.geeksforgeeks.org/problems/2e068e2342b9c9f40cfda1ed8e8119542d748fd8/1

class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        #right , down,left,up
        def dfs(i,j,d):
            # print(i,j,d)
            if i<0 or i>=R or j<0 or j>=C:
                return [i,j]
                # return [i,j]
            if matrix[i][j] == 0:
                ni = i+dir[d][0]
                nj = j+dir[d][1]
                if ni<0 or ni>=R or nj<0 or nj>=C:
                    # print(i,
                    return [i,j]
                else:
                    return dfs(ni,nj,d)
            else:
                if d==0:
                    d= 1
                elif d==1:
                    d = 2
                elif d==2:
                    d = 3
                else:
                     d =0
                matrix[i][j] = 0
                ni = i+dir[d][0]
                nj = j+dir[d][1]
                if ni<0 or ni>=R or nj<0 or nj>=C:
                    return [i,j]
                else:
                    return dfs(ni,nj,d)
        return dfs(0,0,0)
