Question Link: https://practice.geeksforgeeks.org/problems/90a81c305b1fe939b9230a67824749ceaa493eab/1
    
class Solution():
    def countZero(self, n, k ,arr):
        #your code here
        r = [0] * k
        ro = [False] * (n+1)
        co = [False] * (n+1)
        v = n * n
        rw, cl = 0, 0
        for l in range(k):
            if not ro[arr[l][0]]:
                ro[arr[l][0]] = True
                v = v - n + cl
                rw += 1
            if not co[arr[l][1]]:
                co[arr[l][1]] = True
                cl += 1
                v = v - n + rw
            r[l] = v
        return r
