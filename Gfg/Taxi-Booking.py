from typing import List
class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        i=0
        p=abs(cur-pos[i])*time[i]
        m=p
        for i in range(N):
            p=abs(cur-pos[i])*time[i]
            if m>p:
                m=p
        return m
