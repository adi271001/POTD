class Solution:
    def findNumber(self, N : int) -> int:
        # code here
        a = []
        N -= 1
        while N >= 0:
            a.append(N % 5)
            N = N // 5 - 1
        d = [1, 3, 5, 7, 9]
        ans = 0
        for i in reversed(a):
            ans = ans * 10 + d[i]
        return ans
