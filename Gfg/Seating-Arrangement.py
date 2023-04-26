from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, a : List[int]) -> bool:
        # code here
        c=0
        if m==1:
            if a[0]==0:
                c+=1
            if c>=n:
                return True
            else:
                return False
        for i in range(m):
            if i==0 and a[i]==0 and a[i+1]==0:
                c+=1
                a[i]=1
            elif i==m-1and a[i-1]==0 and a[i]==0 :
                c+=1
                
            elif a[i-1]==0 and a[i]==0 and a[i+1]==0 :
                c+=1
                a[i]=1
        if c>=n:
            return True
        else:
            return False
