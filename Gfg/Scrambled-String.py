Question Link: https://practice.geeksforgeeks.org/problems/scrambled-string/1
  
class Solution:
    def isScramble(self,S1: str, S2: str):
        ##code here
        if S1 == S2:
            return True
        for k in range(1, len(S1)):
            if self.isScramble(S1[:k], S2[:k]) and self.isScramble(S1[k:], S2[k:]):
                return True
            if self.isScramble(S1[:k], S2[-k:]) and self.isScramble(S1[k:], S2[:len(S2)-k]):
                return True
        return False
