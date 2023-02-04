Question Link: https://practice.geeksforgeeks.org/problems/7a33c749a79327b2889d420dd80342fff33aac6d/1
    
class Solution:
	def findMaxSum(self,arr, n):
		# code here
		if n == 1:
            return arr[0]
        pPM = arr[0]
        pM = arr[1]
        a = max(pM, pPM)
        for k in range(2, n):
            c = arr[k] + pPM
            a = max(a, c)
            pPM = max(pPM, pM)
            pM = max(pM, c)
        return a
