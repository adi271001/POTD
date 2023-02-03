Question Link: https://leetcode.com/problems/zigzag-conversion
    
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zz = range(numRows)
        p = list(zz) + list(range(numRows-2, 0, -1))
        t = math.ceil(len(s)/len(p))
        ps = p*t
        a = ["" for _ in zz] 
        for d,e in zip(ps, s):
            a[d] += e
        return "".join(a)
