Question Link: https://leetcode.com/problems/concatenated-words/description/
  
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        p = set()
        cw = []
        for w in words:
            p.add(w)
        for w in words:
            if self.checkConcatenate(w, p) == True:
                cw.append(w)
        return cw
    def checkConcatenate(self, w: str, p: set) -> bool:
        for k in range(1, len(w)):
            pW = w[:k]
            sW = w[k:]
            if pW in p and (sW in p or self.checkConcatenate(sW, p)):
                return True
        return False
