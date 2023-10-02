class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = [[False] * (total + 1) for _ in range(len(stones) + 1)]
        dp[0][0] = True
        for i in range(1, len(stones) + 1):
            for j in range(total + 1):
                dp[i][j] = dp[i-1][j] or (j >= stones[i-1] and dp[i-1][j-stones[i-1]])
        ans = total
        for j in range(total // 2 + 1):
            if dp[len(stones)][j]:
                ans = min(ans, total - 2 * j)
        return ans
