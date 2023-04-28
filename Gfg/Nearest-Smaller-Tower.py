class Solution:
    def nearestSmallestTower(self,A):
        #code here
        def _pre(r, out):
            stk = [(A[r.start], r.start)]
            for i in r[1:]:
                v = A[i]
                while stk and stk[-1][0] >= v: stk.pop()
                out[i] = INV if not stk else stk[-1][1]
                stk.append((v,i))
        
        N, INV = len(A), 10**9
        LL, LR = [INV]*N, [INV]*N
        ans = [-1] * N
        _pre(range(N), LL)
        _pre(range(N-1, -1, -1), LR)
        for i in range(N):
            if LL[i] == LR[i] == INV: continue
            Ldif, Rdif = abs(i-LL[i]), abs(LR[i]-i)
            if Ldif < Rdif: ans[i] = LL[i]
            elif Ldif > Rdif: ans[i] = LR[i]
            elif A[LL[i]] <= A[LR[i]]: ans[i] = LL[i]
            else: ans[i] = LR[i]
        return ans