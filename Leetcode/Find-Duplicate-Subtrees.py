class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node, map):
            if not node:
                return "#"
            left = traverse(node.left, map)
            right = traverse(node.right, map)
            serialized = str(node.val) + "," + left + "," + right
            nodes = map.setdefault(serialized, [])
            nodes.append(node)
            return serialized
        map = {}
        traverse(root, map)
        result = []
        for nodes in map.values():
            if len(nodes) > 1:
                result.append(nodes[0])
        return result
