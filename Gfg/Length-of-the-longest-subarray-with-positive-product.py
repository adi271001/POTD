Question Link: https://practice.geeksforgeeks.org/problems/4dfa8ba14d4c94f4d7637b6b5246782412f3aeb8/1
    
class Solution:
    def maxLength(self,arr,n):
        #code here
        p_l, n_l, a = 0, 0, 0
        for k in arr:
            if k == 0:
                p_l = n_l = 0
            elif k < 0:
                p_l, n_l = n_l+1 if n_l else 0, p_l+1
            else:
                n_l, p_l = n_l+1 if n_l else 0, p_l+1
            a = max(a, p_l)
        return a
