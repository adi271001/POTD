Question Link: https://leetcode.com/problems/best-team-with-no-conflicts/description/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        eq = [0]*(1+max(ages))                         
        s_a = sorted(zip(scores, ages))
        for s, a in s_a:           
            eq[a] = s + max(eq[:a+1])   
        return max(eq) 
