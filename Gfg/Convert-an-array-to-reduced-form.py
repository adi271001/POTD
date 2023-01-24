Question Link: https://practice.geeksforgeeks.org/problems/convert-an-array-to-reduced-form1101/1
    
class Solution:
	def convert(self,arr, n):
		t = sorted(enumerate(arr), key= lambda y: y[1])
	    t = sorted(enumerate(t), key = lambda y: y[1][0])
	    for y in range(n):
	        arr[y] = t[y][0]
