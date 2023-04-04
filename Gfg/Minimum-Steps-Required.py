class Solution:
    def minSteps(self, str : str) -> int:
        # code here
        c=1
        ch=str[0]
        for i in range(1,len(str)):
            if ch!=str[i]:
                c+=1
                ch=str[i]
        return c//2+1
