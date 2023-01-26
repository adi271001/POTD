Question Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        a = [[] for _ in range(n)]
        for f in flights:
            a[f[0]].append((f[1], f[2]))
        
        t = [(src, 0)]
        mC = [float('inf') for _ in range(n)]
        st = 0
        
        while t and st <= k:
            s = len(t)
            for l in range(s):
                cN , c = t.pop(0)
                for nb, pc in a[cN]:
                    if pc + c >= mC[nb]:
                        continue
                    mC[nb] = pc + c
                    t.append((nb, mC[nb]))
            st += 1
        
        return -1 if mC[dst] == float('inf') else mC[dst]
