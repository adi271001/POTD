import heapq
class Solution:
    def isStraightHand(self, N, groupSize, hand):
        if N%groupSize:
            return False
        count={}
        for n in hand:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        minH=list(count.keys())
        heapq.heapify(minH)
        while minH:
            first=minH[0]
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
