Question Link: https://practice.geeksforgeeks.org/problems/51afa710a708c0681748445b509696dd588d5c40/1
  
import sys
sys.setrecursionlimit(10**6)

class Solution():
    def dfs(self, graph, visited, u):
        if visited[u] == 2:
            return -1
        elif visited[u] == 1:
            res, cur = u, u
            while graph[cur] != u:
                cur = graph[cur]
                res += cur
            return res
        elif graph[u] != -1:
            visited[u] = 1
            res = self.dfs(graph, visited, graph[u])
            visited[u] = 2
            return res
        else:
            visited[u] = 2
            return -1
    
                
    def largestSumCycle(self, N, Edge):
        #your code goes here
        visited = [0]*N
        res = -1
        for u in range(N):
            res = max(res, self.dfs(Edge, visited, u))
        return res
