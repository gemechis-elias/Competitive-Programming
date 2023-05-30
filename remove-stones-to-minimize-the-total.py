class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapify(piles)

        for _ in range(k):
            tt = -heappop(piles)
            heappush(piles, -(tt - tt//2))

        return -sum(piles)