class Solution:
    def stringMirror(self, s : str) -> str:
        # code here
        res = tmp = s[0]
        for ch in s[1:]:
            if tmp < ch or ch == s[0]:
                break
            res += ch
            tmp = ch
        return res + res[::-1]
