Question Link: https://leetcode.com/problems/naming-a-company
    
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        a = 0
        s = [set() for _ in range(26)]
        for ide in ideas:
            s[ord(ide[0]) - ord('a')].add(ide[1:])
        for k in range(25):
            for l in range(k + 1, 26):
                c = len(s[k] & s[l])
                a += 2 * (len(s[k]) - c) * (len(s[l]) - c)
        return a
