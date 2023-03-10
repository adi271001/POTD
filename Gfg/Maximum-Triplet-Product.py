class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        mx1,mx2,mx3=float('-inf'),float('-inf'),float('-inf')
        mi1,mi2=float('inf'),float('inf')
        for i in arr:
            if i>mx1:
                mx3,mx2,mx1=mx2,mx1,i
            elif i>mx2:
                mx3,mx2=mx2,i
            elif i>mx3:
                mx3=i
            if i<mi1:
                mi2,mi1=mi1,i
            elif i<mi2:
                mi2=i
        return max(mx1*mx2*mx3,mx1*mi1*mi2)
