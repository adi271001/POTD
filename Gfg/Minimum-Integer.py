from typing import List
class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        S=0
        for i in A:
            S+=i
        min=A[0]
        A=sorted(A)
        for i in A:
            if S<=N*i:
                min =i 
                return i
        if not S<=N*min:
            return min(A)
