class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        data = [-stone for stone in stones]
        
        heapq.heapify(data)

        while len(data) > 1:
            x = -heapq.heappop(data)
            y = -heapq.heappop(data)


            if x != y:
                heapq.heappush(data, -(x-y))
            else:
                heapq.heappush(data, 0)
        return abs(data[0])