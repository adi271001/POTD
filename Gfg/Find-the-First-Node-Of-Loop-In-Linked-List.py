Question Link: https://practice.geeksforgeeks.org/problems/44bb5287b98797782162ffe3d2201621f6343a4b/1
    
from collections import defaultdict
class Solution:
    #Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        dicts = defaultdict(int)
        c = head
        while c is not None:
            if dicts[c]==0:
                dicts[c] = 1
                c=c.next
            else:
                return c.data
        return -1
