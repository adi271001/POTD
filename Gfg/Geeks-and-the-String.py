Question Link: https://practice.geeksforgeeks.org/problems/466faca80c3e86f13880710491c634d26abd44a7/1
    
class Solution:
    def removePair(self,s):
        tu = []
        for k in range(len(s)):
            if tu and tu[-1] == s[k]:
                tu.pop()
            else:
                tu.append(s[k])
        if not tu:
            return -1
        return "".join(tu)
