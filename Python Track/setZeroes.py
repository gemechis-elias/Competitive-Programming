class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_column.add(j)
        for row in zero_row:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        for column in zero_column:
            for i in range(len(matrix)):
                matrix[i][column] = 0
