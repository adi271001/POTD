Question Link: https://leetcode.com/problems/find-the-town-judge/description/
    
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dbbtat = defaultdict(int)
        for x,y in trust:
            dbbtat[x] -= 1
            dbbtat[y] += 1
        for k in range(1,n+1):
            if dbbtat[k] == n-1:
                return k
        return -1
