class Solution():
    def maximizeMinHeight(self, n, k, w, a):
        #your code goes here
        def _try(tar):
            mods = [0]*n
            add, left = 0, k
            for i in range(n):
                add += mods[i]
                v = a[i] + add
                if v < tar:
                    Δ = tar-v
                    mods[i] += Δ
                    if i+w < n: mods[i+w] -= Δ
                    add += Δ
                    left -= Δ
                    if left < 0: return False
            return True
        L = min(a)
        R = L + k + 1
        while L<R:
            m = (L+R)//2
            if _try(m): L=m+1
            else: R=m
        return L-1
