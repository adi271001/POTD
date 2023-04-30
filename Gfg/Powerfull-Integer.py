from typing import List
class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        l=[]
        for n1,n2 in intervals:
            l.append((n1,-1))
            l.append((n2,1))
        l.sort()
        
        n=0
        ans=-1
        for n1,n2 in l:
            if n2==-1:
                n+=1
            else:
                if n>=k:
                    ans=max(ans,n1)
                n-=1
        return ans
