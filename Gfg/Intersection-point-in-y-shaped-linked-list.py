Question Link: https://practice.geeksforgeeks.org/problems/eae1fbd0ac8f213a833d231e26ba4d829e79dd9c/1
    
class Solution:
    
    def intersetPoint(self,head1,head2):
        #code here
        x = head1
        y = head2
        n_i = 0
        while x!=y and n_i!=2:
            if x.next == None:
                n_i+=1
                x = head2
            if y.next == None:
                y = head1
            x = x.next
            y = y.next
        if n_i == 2:
            return -1
        return x.data
