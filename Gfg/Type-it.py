Question Link: https://practice.geeksforgeeks.org/problems/95080eb9efbf7cc5cb4851ddf8d7946e3f212a49/1
    
class Solution:
    def minOperation(self, s): 
        #code here
        big = ''
        s1=''
        for x in range(len(s)):
            s1+=s[x]
            if s1 in s[x+1:]:
                big = s1
        if big:
            return len(s)-len(big)+1
        return len(s)
