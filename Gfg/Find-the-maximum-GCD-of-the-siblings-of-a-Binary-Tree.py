Question Link: https://practice.geeksforgeeks.org/problems/6eb51dc638ee1b936f38d1ab4b2f7062d4425463/1
    
import math
class Solution:
    def maxGCD(self, root):
        ans=0
        max_gcd=float("-inf")
        def solve(root):
            nonlocal ans,max_gcd
            if root is None:
                return 0
            if root.left and root.right:
                val=math.gcd(root.left.data,root.right.data)
                if val>max_gcd or (val ==max_gcd and root.data>ans):
                    max_gcd = val
                    ans = root.data
            solve(root.left)
            solve(root.right)
        if root is None:
            return -1
        solve(root)
        return ans
