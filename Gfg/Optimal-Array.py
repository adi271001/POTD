from typing import List
class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        li=[]
        li.append(0)
        for i in range(1,n):
            li.append(li[0]+li[i-1]+abs(a[i]-a[i//2]))
        return li
