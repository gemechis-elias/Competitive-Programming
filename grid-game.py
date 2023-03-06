class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]
            print(ans, topSum, bottomSum)

        return ans