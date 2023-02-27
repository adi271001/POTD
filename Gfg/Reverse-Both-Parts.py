class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        # code here
        cur = head
        dummy = Node(0)
        while k > 0:
            t, cur = cur, cur.next
            dummy.next, t.next = t, dummy.next
            k -= 1
        while cur:
            t, cur = cur, cur.next
            head.next, t.next = t, head.next
        return dummy.next
