Question Link: https://leetcode.com/problems/maximum-sum-circular-subarray/description/
    
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        bp = [[0,0] for _ in range(len(nums))]
        bp[0][0] = nums[0]
        r = nums[0]
        for k in range(1,len(nums)):
            bp[k][0] = max(bp[k-1][0]+nums[k], nums[k])
            bp[k][1] = min(bp[k-1][1]+nums[k], nums[k])
            r = max(r, bp[k][0], s - bp[k][1])
        return r
