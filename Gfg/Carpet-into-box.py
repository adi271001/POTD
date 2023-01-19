Question Link: https://practice.geeksforgeeks.org/problems/230d87552a332a2970b2092451334a007f2b0eec/1
    
class Solution:
    def carpetBox(self, A,B,C,D):
        #code here
        maxi=max(A,B)
        mini=min(A,B)
        moves=0
        while maxi>max(C,D):
            maxi//=2
            if maxi<=mini:
                maxi,mini=mini,maxi #swapping
            moves+=1
        while mini>min(C,D):
            mini//=2
            moves+=1
        return moves
