class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                temp = [grid[i+k][j:j+3] for k in range(3)]
                check_nums = [num for row in temp for num in row]
                if sorted(check_nums) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    row_sums = [sum(row) for row in temp]
                    col_sums = [sum([row[i] for row in temp]) for i in range(3)]
                    diag_sums = [sum([temp[i][i] for i in range(3)]), (temp[0][2] + temp[1][1] + temp[2][0])]
                    row_sums.extend(col_sums)
                    row_sums.extend(diag_sums)
                    if len(set(row_sums)) == 1:
                        result += 1
        
        return result
