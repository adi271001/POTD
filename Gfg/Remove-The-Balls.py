from typing import List
class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        st = []
        i = 0
        while(i<N):
            if len(st)!=0 and st[-1][0]==color[i] and st[-1][1]==radius[i]:
                st.pop()
            else:
                st.append((color[i],radius[i]))
            i+=1
        return len(st)
