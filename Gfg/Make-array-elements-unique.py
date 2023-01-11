Question Link: https://practice.geeksforgeeks.org/problems/6e63df6d2ebdf6408a9b364128bb1123b5b13450/1

class Solution:
    def minIncrements(self, arr, N): 
        # Code here
        inc = 0
        unique = set()
        for ele in arr:
            while True:
                if ele not in unique:
                    unique.add(ele)
                    break
                ele += 1
                inc += 1
        return inc
