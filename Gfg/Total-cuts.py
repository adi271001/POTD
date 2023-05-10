from typing import List
class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        ans = 0
        ml = A[0]
        mr = [0]*N
        mr[N-1] = A[N-1]
        for i in range(N-2,-1,-1):
            mr[i] = min(mr[i+1],A[i])
        for i in range(N-1):
            ml = max(ml,A[i])
            if ml + mr[i+1] >= K:
                ans += 1
        return ans
