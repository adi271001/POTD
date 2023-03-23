class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        def result(root):
            if root==None:
                return 1e9
            if root.left==None and root.right==None:
                return root.data
            l=result(root.left)
            r=result(root.right)
            return min(l,r)+root.data
        val=[0]
        def solve(root,t):
            if root==None:
                return -1
            if root.data==t:
                val[0]=min(result(root.left),result(root.right))
                return 0
            
            if root.data>t:
                ans=solve(root.left,t)
            else:
                ans=solve(root.right,t)
            if ans!=-1:
                return ans+root.data
            else:
                return -1
        res=solve(root,target)
        if val[0]==1e9:
            return res
        return res-val[0]
