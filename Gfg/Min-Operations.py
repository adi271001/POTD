Question Link: https://practice.geeksforgeeks.org/problems/5a7e1a52f1b7796238f9efea4c6fda389f26c327/1
    
class Solution:
    def solve(self, a : int, b : int) -> int:
        z=0
        while a!=b:
            if a>b:
                a,b=b,a
            b=b&a
            z+=1
        return z
