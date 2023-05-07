class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        n = len(heights)
        
        for i in range(n-1):
            dc = heights[i+1] - heights[i]
            if dc > 0:
                heapq.heappush(heap, dc)
            if len(heap) > ladders:
                bricks = bricks - heapq.heappop(heap)
            if bricks < 0:
                return i
        
        return n-1