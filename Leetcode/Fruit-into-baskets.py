Question Link:
  
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c = defaultdict(int) 
        k, l = 0, 0 
        for l in range(len(fruits)):
            c[fruits[l]] += 1 
            if len(c) > 2: 
                c[fruits[k]] -= 1 
                if c[fruits[k]] == 0:
                    del c[fruits[k]] 
                k += 1 
        return l - k + 1 
