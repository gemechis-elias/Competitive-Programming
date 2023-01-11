import numpy as np
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid = np.array(grid)
        m, n = grid.shape
        
        rSum = []
        for i in range(m):
            rSum.append(sum(grid[i, :]))
            
        cSum = []
        for j in range(n):
            cSum.append(sum(grid[:, j]))
            
        diff = np.zeros(shape=(m, n), dtype=int)
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2*(rSum[i] + cSum[j]) - (m + n)
        
        return diff
