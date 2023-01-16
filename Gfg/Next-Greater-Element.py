Question Link: https://practice.geeksforgeeks.org/problems/214734e358208c1c6811d9b237b518f6b3c3c094/1

class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack=[-1]
        res=[]
        for i in range(n-1, -1, -1):
            while len(stack)>1 and arr[i]>=stack[-1]:
                stack.pop()
            res.append(stack[-1])
            stack.append(arr[i])
        for i in range(n):
            arr[i]=res[i]
        return arr[::-1]
