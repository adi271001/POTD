from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = deque([root])
        while q[0] is not None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)
        while q and q[0] is None:
            q.popleft()
        return not bool(q)
