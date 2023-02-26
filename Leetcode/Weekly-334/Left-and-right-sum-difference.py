class Solution:
    def leftRigthDifference(self, arr):
        n = len(arr)
        leftSum = [0]*n
        rightSum = [0]*n
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + arr[i-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + arr[i+1]
        ans = [abs(leftSum[i]-rightSum[i]) for i in range(n)]
        return ans
