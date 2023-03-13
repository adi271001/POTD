class Solution:
    def maxPossibleValue(self, N, A, B): 
        #code here
        ans=0
        c=0
        mi=10**10
        for i in range(N):
            if B[i]//2>0:
                ans+=2*(B[i]//2)*A[i]
                c+=B[i]//2
                mi=min(mi,A[i])
        if c%2==1:
                ans-=2*mi
        return ans
