class Solution():
    def minCost(self, colors, N):
        #your code goes here
        for k in range(1,N):
            colors[k][0] = min(colors[k][0]+colors[k-1][1], colors[k][0]+colors[k-1][2])
            colors[k][1] = min(colors[k][1]+colors[k-1][0], colors[k][1]+colors[k-1][2])
            colors[k][2] = min(colors[k][2]+colors[k-1][0], colors[k][2]+colors[k-1][1])
        return min(colors[-1])
