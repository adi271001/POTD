Question Link: https://practice.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/1
    
import heapq
class Solution:
    def caseSort(self,s,n):
        a = []
        b = []
        for k in range(len(s)):
            if ord(s[k])<97:
                a.append(ord(s[k]))
            else:
                b.append(ord(s[k]))
        heapq.heapify(a)
        heapq.heapify(b)
        a1 = ""
        for l in range(len(s)):
            if ord(s[l])>=97:
                a1 += chr(heapq.heappop(b))
            else:
                a1 += chr(heapq.heappop(a))
        return a1
