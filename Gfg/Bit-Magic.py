from typing import List
class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        ans = 0
        cnt = 0
        i=0
        j = len(arr)-1
        while (i<=j):
            if arr[i]!=arr[j]:
                cnt+=1
            i+=1
            j-=1
        if cnt==1:
            return (1) 
        if cnt%2!=0:
            cnt+=1
        return (cnt//2)
