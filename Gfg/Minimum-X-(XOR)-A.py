Question Link: https://practice.geeksforgeeks.org/problems/1fc4278adf2a36780f637c7b4cd06391dd1487e4/1
  
class Solution:
    def minVal(self, a, b):
        #code here
        ones=sum([int(k) for k in bin(b).replace('0b','')])
        a=bin(a).replace('0b','')
        ans=[]
        for i in a:
            if i=='0':
                ans+=['0']
            else:
                if ones:
                    ans+=['1']
                    ones-=1
                else:
                    ans+=['0']
        i=len(ans)-1
        while ones and i>=0:
            if ans[i]=='0':
                ans[i]='1'
                ones-=1
            i-=1
        if ones:
            ans=['1']*ones+ans
        return int(''.join(ans),2)
