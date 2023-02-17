class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        a, b = 0, K
        N -= K
        summ = sum(GeekNum[:K])
        while N:
            GeekNum.append(summ)
            summ = summ + GeekNum[b] -GeekNum[a]
            a+=1
            b+=1
            N-=1
        return GeekNum[-1]
