from heapq import heappop, heappush
from math import inf
class Solution:
    def dijkstra(self, graph, src):
        n = len(graph)
        dist = [inf]*n
        dist[src] = 0
        heap = [(dist[src], src)]
        
        while heap:
            d, u = heappop(heap)
            if dist[u] < d:
                continue
            for v, wt in graph[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heappush(heap, (dist[v], v))
        return dist
    
    def shortestPath(self, n, m, a, b, edges):
        graph = [[] for _ in range(n)]
        for u, v, w1, _ in edges:
            graph[u-1].append((v-1, w1))
            graph[v-1].append((u-1, w1))
            
        dista = self.dijkstra(graph, a-1)
        distb = self.dijkstra(graph, b-1)
        
        res = dista[b-1]
        for u, v, _, w2 in edges:
            res = min(res, dista[u-1] + w2 + distb[v-1])
            res = min(res, distb[u-1] + w2 + dista[v-1])
        
        return res if res != inf else -1
