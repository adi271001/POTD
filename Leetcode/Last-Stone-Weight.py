class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)
        if max_heap:
            return -max_heap[0]
        else:
            return 0
