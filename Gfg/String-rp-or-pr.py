class Solution:
    def solve (self, X, Y, S):
        #code here
        if X>=Y:
            order = [('pr', X), ('rp', Y)]
        else: 
            order = [('rp', Y), ('pr', X)]
        ans = 0
        for (c0, c1), score in order:
            N, NS = len(S), []
            for i in range(N):
                NS.append(S[i])
                if S[i] == c1 and len(NS)>1 and NS[-2]==c0:
                    ans += score
                    NS.pop(); NS.pop()
            S = NS
        return ans
