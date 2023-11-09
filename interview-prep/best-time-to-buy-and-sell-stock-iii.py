class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [inf for _ in range(3)]
        profit = [0 for _ in range(3)]
        for currPrice in prices:
            for i in range(1, 3):
                buy[i] = min(buy[i], currPrice - profit[i-1])
                profit[i] = max(profit[i], currPrice - buy[i])

        return profit[2]