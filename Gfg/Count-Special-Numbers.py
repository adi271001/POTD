class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        m_e = max(arr)
        r = [0 for i in range (m_e + 1)]
        for k in arr:
            if r[k] <= 1:
                for l in range(k, m_e + 1, k):
                    r[l] = r[l] + 1
        return sum(r[k] > 1 for k in arr)
