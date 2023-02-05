Question Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mt, mq, t , q, b = len(s), len(p), 0, 0, []
        if mq > mt: 
            return []
        for i in range(mq): t, q = t + hash(s[i]), q + hash(p[i])
        if t== q: b.append(0)
        for i in range(mq, mt):
            t += hash(s[i]) - hash(s[i-mq])
            if t == q: b.append(i-mq+1)
        return b
