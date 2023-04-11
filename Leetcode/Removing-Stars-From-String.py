class Solution:
    def removeStars(self, s: str) -> str:
        i, j = 0, 0
        n = len(s)
        while i < n:
            if s[i] == '*':
                j -= 1
            else:
                s = s[:j] + s[i] + s[j+1:]
                j += 1
            i += 1
        return s[:j]
