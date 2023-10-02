class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon) - 1
        n = len(dungeon[0]) - 1

        dp = dungeon
        dp[m][n] = max(1,1-dp[m][n])
        for i in range(m-1,-1,-1):
            dp[i][n] = max(1,dp[i+1][n] - dp[i][n])
        for j in range(n-1,-1,-1):
            dp[m][j] = max(1,dp[m][j+1] - dp[m][j])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1]) -dp[i][j])        
        return dp[0][0]
