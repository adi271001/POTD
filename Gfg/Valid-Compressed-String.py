class Solution:
    def checkCompressed(self, S, T):
        # code here 
        i=0
        j=0
        m=len(S)
        n=len(T)

        while i<m and j<n:
            if not T[j].isdigit():
                if T[j]!=S[i]:
                    return 0
                i+=1
                j+=1
            else:
                k=j+1
                while k<n and T[k].isdigit():k+=1
                i+=int(T[j:k])
                j=k
        return 1 if i==m and j==n else 0
