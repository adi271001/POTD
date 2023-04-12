from typing import List
class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        i, j, ans = 0, n//2, 0
        arr[:j] = sorted(arr[:j])
        arr[j:] = sorted(arr[j:])
        while i < n//2:
            if j < n and arr[i] >= 5*arr[j]:
                j += 1
            else:
                ans += j - (n//2)
                i += 1
        return ans
