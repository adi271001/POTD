class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        arr = {}
        for k in range(N):
            arr[lines[k][0]] = arr.get(lines[k][0],0)+1
            arr[lines[k][1]+1] = arr.get(lines[k][1]+1,0)-1
        a = 0
        t = 0
        for k in sorted(arr):
            t += arr[k]
            a = max(a,t)
        return a
