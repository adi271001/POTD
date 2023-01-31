Question Link: https://practice.geeksforgeeks.org/problems/fda70097eb2895ecfff269849b6a8aace441947c/1
    
class Solution:
    def minRepeats(self, A, B):
        # code here 
        x = set(A)
        y = set(B)
        if y.issubset(x):
            z = ""
            res = 0
            while len(z) < len(B):
                z += A
                res +=1
            if B in z:
                return res
            elif B in z+A:
                return res + 1
            else:
                return -1
        else:
            return -1
