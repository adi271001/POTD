class Solution:
    def equalSum(self,A, N):
        # Your code here
        if len(A)==1:
            return 1
        t=sum(A)
        c=0
        for k in range(N):
            if t-A[k]==2*c:
                return k+1
            c+=A[k]    
        return -1 
