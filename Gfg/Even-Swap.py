class Solution():
    def lexicographicallyLargest(self, a, n):
        #your code here
        b=[]
        small=[]
        for i in range(n):
            if not small:
                small.append(a[i])
            elif not (small[-1]+a[i])%2:
                small.append(a[i])
            else:
                small.sort()
                while small:
                    b.append(small.pop())
                small.append(a[i])
        if small:
            small.sort()
            while small:
                b.append(small.pop())
        return b
