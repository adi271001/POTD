Question Link: https://practice.geeksforgeeks.org/problems/b64485d3994958cca8748991bb58668204b3e4c0/1

class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        arr = [0]*N
        for x in range(N):
            if Edge[x] != -1:
                arr[Edge[x]] += x
        return arr.index(max(arr))
