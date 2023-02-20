class Solution:
    def countPaths (self, N):
        # code here 
        if N==1:
            return 0
        m = 10**9+7
        a1=1
        a2=0
        for k in range(2,N):
            a2, a1 = a1, (2*a1 + 3*a2)%m
        a = (3*a1)%m
        return a
