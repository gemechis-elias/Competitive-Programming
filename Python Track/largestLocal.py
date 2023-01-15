class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid)-2):
            row = []
            for j in range(len(grid)-2):
                max_ = 0
                temp = [grid[i+k][j:j+3] for k in range(3)]
                for l in temp:
                    if max_ < max(l):
                        max_ = max(l) 
                    else:
                        max_ = max_
                row.append(max_)
            ans.append(row)
        return ans
