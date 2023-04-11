class Solution:
    def solve(self, a: int, b: int, c: int) -> int:
        mx = max(a, max(b, c))
        return a + b + c if mx <= 2*(a + b + c - mx + 1) else -1
