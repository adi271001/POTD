class Solution:
    def jump(self, nums: List[int]) -> int:
        a, m, e = 0, 0, 0                
        for k, n in enumerate(nums[:-1]):                                    
            m = max(m, k + n)                                              
            if k == e:                         
                a += 1                                    
                e = m
        return a
