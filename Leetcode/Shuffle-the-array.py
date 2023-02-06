Question Link: https://leetcode.com/problems/shuffle-the-array/
    
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = [0] * (2 * n)
        for k in range(n):
            a[2 * k] = nums[k]
            a[2 * k + 1] = nums[k + n]
        return a
