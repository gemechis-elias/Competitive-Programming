class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(hp := [-s for s in stones])
        while len(hp) > 1:
            if (diff := heappop(hp) - heappop(hp)) != 0:
                heappush(hp, diff)
        return -heappop(hp) if hp else 0