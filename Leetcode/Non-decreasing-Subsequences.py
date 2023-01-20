Question Link: https://leetcode.com/problems/non-decreasing-subsequences/description/
  
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        c = [[nums[0]]]
        for a in nums[1:]:
            c += [b+[a] for b in c if a>=b[-1]]
            c += [[a]]
        c = [tuple(a) for a in c if len(a)>=2]
        return list(set(c))
