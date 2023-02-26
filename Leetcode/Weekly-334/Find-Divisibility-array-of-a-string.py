class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        prefix_sum = 0
        div = [0] * n
        for i in range(n):
            prefix_sum = (prefix_sum * 10 + int(word[i])) % m
            if prefix_sum == 0:
                div[i] = 1
        if div[0] == 1:
            return div
        prefix_sum = int(word[0]) % m
        for i in range(1, n):
            prefix_sum = (prefix_sum * 10 + int(word[i])) % m
            if prefix_sum == 0:
                div[i] = 1
        return div
