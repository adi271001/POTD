Question Link: https://leetcode.com/problems/n-th-tribonacci-number/
    
class Solution:
    def tribonacci(self, n: int) -> int:
        C = [0]*(n+1)
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        C[0] = 0
        C[1] = 1
        C[2] = 1
        for k in range(3, n+1):
            C[k] = C[k-1] + C[k-2] + C[k-3]
        return C[n]
