class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nextVal = -matrix[row][col]
                if len(heap) < k:
                    heapq.heappush(heap, nextVal)
                elif nextVal > heap[0]:
                    heapq.heappushpop(heap, nextVal)
        return -heap[0]