Question Link:https://practice.geeksforgeeks.org/problems/d7e0ce338b11f0be36877d9c35cc8dfad6636957/1

class Solution:
    def toSumTree(self, node) :
        #code here
        if not node:
            return 0
        ret_val = node.data
        node.data = self.toSumTree(node.left) + self.toSumTree(node.right)
        return ret_val + node.data
