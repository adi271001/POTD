class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            capacity=mid
            count_days=1
            for weight in weights:
                if weight > capacity :
                    if count_days >= days:return True
                    count_days += 1
                    capacity = mid     
                capacity -= weight
            return False
        left = max(weights)
        right = math.ceil(len(weights) / days) * max(weights)
        while left<right:
            mid = (left+right)//2
            if check(mid):left=mid+1
            else:right=mid
        return left
