class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        M = max( j.deadline for j in Jobs )
        avail = list(range(M+1))
        cnt, ans = 0, 0
        Jobs.sort(key=lambda x: (-x.profit, x.deadline))
        for job in Jobs:
            dl, prof = job.deadline, job.profit
            par, i = avail[dl], dl
            while i>0 and i!=par:
                avail[i] = avail[par]
                i = par
                par = avail[par]
            if i>0:
                avail[i] = i-1
                cnt += 1
                ans += prof
        return cnt, ans
