from collections import deque
class Solution:
    def inverse(self, x, MOD):
        return pow(x, MOD-2, MOD)
            
    def bestNumbers(self, N : int, A : int, B : int, C : int, D : int) -> int:
        MOD = 10**9 + 7
        fact = [1]*(N+1)
        for i in range(1, N+1):
            fact[i] = (fact[i-1]*i)%MOD
        
        res = 0
        for x in range(N+1):
            y = N - x
            S = set(map(int, str(A*x + B*y)))
            if {C,D} >= S:
                res = (res + fact[N] * self.inverse(fact[x], MOD) * self.inverse(fact[y], MOD)) % MOD
        
        return res
