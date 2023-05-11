import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        i,j = 0,len(s)-1
        count = 0
        while(i<j):
            if s[i]!='?':count +=1
            if s[j]!='?':count +=1
            if s[i]!=s[j] and (s[j]!='?' and s[i]!='?'):
                return -1
            else:
                if s[i]!='?' and s[j]=='?':
                    s = s[:j]+s[i]+s[j+1:]
                elif s[i]=='?' and s[j]!='?':
                    s = s[:i]+s[j]+s[i+1:]
            i +=1
            j -=1
        l,ch,sum = len(s),'',0
        if count ==0 or count ==1:
            return 0

        for i in range(l):
            if s[i]!='?':
                ch = s[i]
                break
            
        for i in range(l):
            if s[i]!='?':
                ch = s[i]
            if s[i]=='?':
                if i <= l-2:
                    s = s[:i]+ch+s[i+1:]
                else:
                    s = s[:i]+ch
               
        for i in range(l-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum
