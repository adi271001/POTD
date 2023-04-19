class Solution:
    def wifiRange(self, N, S, X): 
        #code here
        t = "0"*X
        S = t + S + t
        if(S.find("0"*(2*X + 1)) != -1):
            return 0
        else:
            return 1
