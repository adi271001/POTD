Question Link: https://practice.geeksforgeeks.org/problems/total-decoding-messages1235/1
    
class Solution:
	def CountWays(self, str):
		# Code here
		l = len(str)
        a = [0] * (l + 1)
        a[0] = 1
        a[1] = 1 if str[0] != '0' else 0
        for k in range(2, l + 1):
            if str[k - 1] != '0':
                a[k] += a[k - 1]
            if str[k - 2] == '1' or (str[k - 2] == '2' and str[k - 1] <= '6'):
                a[k] += a[k - 2]
            a[k] %= 10**9 + 7
        return a[l]
