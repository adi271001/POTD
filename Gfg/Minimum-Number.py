from math import gcd
class Solution:
    def minimumNumber(self, n, arr):
        #code here
        a= arr[0]
        for i in range(n):
            a=gcd(a,arr[i])
        return (a)
