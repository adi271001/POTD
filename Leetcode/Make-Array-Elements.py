class Solution:
    def minOperations(self, N):
        # Code here
        if N==1:
            return 1
        return (N//2)*N-(N//2)*(N//2)
