class Solution:
    def addMinChar (self, s):
        size = len(str1)
        ans = 0
        i = 0
        j = size -1  
        while i<= j:
            if str1[i] == str1[j]:
                i+=1 
                j -=1 
            else:
                ans += 1
                i = 0
                j = size - 1 - ans 
        return ans
