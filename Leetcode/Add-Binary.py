class Solution:
    def addBinary(self, a: str, b: str) -> str:
        t = []
        c = 0
        k = len(a) - 1
        l = len(b) - 1
        while k >= 0 or l >= 0 or c:
            if k >= 0:
                c += int(a[k])
                k -= 1
            if l >= 0:
                c += int(b[l])
                l -= 1
            t.append(str(c % 2))
            c //= 2
        return ''.join(reversed(t))
