class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapify(stones)

        while len(stones) > 1:
            num1 = heappop(stones)
            num2 = heappop(stones)

            item = (-1*num1) - (-1*num2)
            heappush(stones, -1 * item)

        return -1 * stones[0]