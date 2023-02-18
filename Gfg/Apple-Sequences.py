class Solution:
    def appleSequences(self, n, m, arr):
        # code here 
        res = count = l = r = 0
        while r < n:
            if arr[r] == 'O': count += 1
            while l < n and count > m:
                if arr[l] == 'O': count -= 1
                l += 1 
            res = max(res, r - l + 1)
            r += 1
        return res
