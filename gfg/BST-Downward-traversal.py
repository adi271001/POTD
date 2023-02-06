Question Link: https://practice.geeksforgeeks.org/problems/c85e3a573a7de6dfd18398def16d05387852b319/1
  
class Solution:
    def dfs(self, root, tV, hF=False, tP=0, cP=0):
        if root is None:
            return 0
        a = 0
        if hF and tP == cP:
            a += root.data
            
        if not hF and root.data == tV:
            hF = True
            tP = cP
            a += 1
        a += self.dfs(root.left, tV, hF, tP, cP - 1)
        a += self.dfs(root.right, tV, hF, tP, cP + 1)
        return a
    def verticallyDownBST(self, root, target):
        return self.dfs(root, target) - 1
