class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        dic={}
        lis=[]
        for i in range(N):
            c=mat[i].count(1)
            if c not in dic:
              dic[c]=i
            lis.append(c)
        lis.sort()
        return dic[lis[-1]],lis[-1]
