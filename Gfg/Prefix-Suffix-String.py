class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        hshset = set(s1)
        for w in s1:
            for i in range(1, len(w)):
                hshset.add(w[:i])
                hshset.add(w[-i:])
        return sum(w in hshset for w in s2)
