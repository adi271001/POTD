class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        v = [10**9] * n
        ans = []
        for x in obstacles:
            ub = bisect.bisect_right(v, x)
            ans.append(ub + 1)
            v[ub] = x
        return ans
