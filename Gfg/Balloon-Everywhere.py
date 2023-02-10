Question Link: https://practice.geeksforgeeks.org/problems/45fa306a9116332ece4cecdaedf50f140bd252d4/1

class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        k = {}
        l = 'balon'
        c = float('inf')
        for i in s:
            if i in k:
                k[i]+=1
            else:
                k[i] = 1
        for m, v in k.items():
            if m in l:
                if m == 'l' or m == 'o':
                    c = min(v//2, c)
                else:
                    c = min(c, v)
        return c
