class Solution:
    def inSequence(self, A, B, C):
        # code here
        if C==0:
            return int(A==B)
        l=B-A
        if(l%C==0 and l/C>=0):
            return 1
        return 0
