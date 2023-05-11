from typing import List
class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        c = 0
        nz = 0
        for i in range(n):
            if arr[i] != 0:
                nz = 1
            elif arr[i] == 0 and nz == 1:
                c += 1
                nz = 0
        if nz == 1:
            c += 1
        return c
