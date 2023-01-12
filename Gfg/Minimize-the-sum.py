Question Link: https://practice.geeksforgeeks.org/problems/86e609332c9ef4f6b8aa79db11a6c0808c4a1bca/1

import heapq
class Solution:
    def minimizeSum(self, N, arr):
        # Code here
        sum1 = 0
        heapq.heapify(arr)
        while N>1:
            x, y = heapq.heappop(arr), heapq.heappop(arr)
            sum1 += (x+y)
            heapq.heappush(arr, x+y)
            N-=1
        return sum1
