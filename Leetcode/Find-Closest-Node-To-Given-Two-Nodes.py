Question Link:
  
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(u: int, d: List[int], vis: List[bool], edges: List[int]) -> None:
            vis[u] = True
            v = edges[u]
            if v != -1 and not vis[v]:
                d[v] = d[u] + 1
                dfs(v, d, vis, edges)
        n = len(edges)
        d1, d2 = [float("inf")] * n, [float("inf")] * n
        vis1, vis2 = [False] * n, [False] * n
        d1[node1], d2[node2] = 0, 0
        dfs(node1, d1, vis1, edges)
        dfs(node2, d2, vis2, edges)
        ans = -1
        mi = float("inf")
        for i in range(n):
            if max(d1[i], d2[i]) < mi:
                mi = max(d1[i], d2[i])
                ans = i
        return ans
