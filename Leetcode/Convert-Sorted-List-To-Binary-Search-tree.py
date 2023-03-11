class Solution:
    def constructBST(self, leftHead: ListNode, rightHead: ListNode) -> TreeNode:
        if leftHead == rightHead:
            return None
        slow, fast = leftHead, leftHead
        while fast != rightHead and fast.next != rightHead:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.constructBST(leftHead, slow)
        root.right = self.constructBST(slow.next, rightHead)
        return root
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        return self.constructBST(head, None)
