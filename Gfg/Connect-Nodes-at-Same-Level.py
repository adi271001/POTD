class Solution:
    def connect(self, root):
        def populate(node, level=0, m = {}):
            if not node:
                return
            populate(node.right, level+1, m)
            node.nextRight = m.get(level, None)
            m[level] = node 
            populate(node.left, level+1, m)
        populate(root)
        return root
