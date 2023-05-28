def getNthFromLast(head,n):
    res,cur,i = head,head,0
    while cur and i<n: cur,i = cur.next,i+1
    while cur: cur,res = cur.next,res.next
    return res.data if i==n else -1
