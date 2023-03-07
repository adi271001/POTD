class Solution:
    def maxLevelSum(self, root):
        # Code here
        hs={}
        ans=-10**4
        def fun(root,level):
            if root==None:
                return
            if level not in hs:
                hs[level]=[root.data]
            else:
                hs[level].append(root.data)
            fun(root.left, level+1)
            fun(root.right, level+1)
        fun(root, 0)
        for i in hs:
            ans=max(ans, sum(hs[i]))
        return ans
