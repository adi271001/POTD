class Solution:
    def average(self, salary: List[int]) -> float:
        ts=sum(salary)-min(salary)-max(salary)
        tp=len(salary)-2
        return ts/tp
