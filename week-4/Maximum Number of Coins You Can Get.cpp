class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        length=len(piles)
        p=length//3
        right=length-2
        MaximumCoin=0
        while p > 0:
            MaximumCoin += piles[right]
            right-=2
            p-=1
        return MaximumCoin
