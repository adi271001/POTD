class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        frogset = set()
        for f in sorted(frogs):
            if f not in frogset:
                i = 1
                while f * i <= leaves:
                    frogset.add(f * i)
                    i += 1
        res = 0
        for i in range(1, leaves + 1):
            if i not in frogset:
                res += 1
        return res
