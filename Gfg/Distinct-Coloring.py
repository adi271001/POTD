Question Link: https://practice.geeksforgeeks.org/problems/844b4fdcd988ac5461324d62d43f7892749a113c/1
    
class Solution:
    def distinctColoring (self, N, r, g, b):
        # code here 
        print(r)
        print(g)
        print(b)
        x=[[0,0,0]]*N
        x[0] = [r[0],g[0],b[0]]
        for i in range(1,N):
            x[i][0] = min(x[i-1][1],x[i-1][2])+r[i]
            x[i][1] = min(x[i-1][0],x[i-1][2])+g[i]
            x[i][2] = min(x[i-1][0],x[i-1][1])+b[i]
        return min(x[N-1][0],x[N-1][1],x[N-1][2])
