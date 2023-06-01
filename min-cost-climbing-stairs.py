class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        m = n + 1
        dp = [0] * m
        #print("dp", dp)
        for i in range(2, m):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            #print("new dp", dp)
        
        return dp[n]