class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.row= len(matrix)
        self.column=len(matrix[0])
        self.prefixsummatrix=[[0]*(self.column+1) for i in range(self.row+1)]
    
        for row_element in range(self.row):
            prefixsum=0
            for column_element in range(self.column):
                prefixsum += matrix[row_element][column_element]
                temp= prefixsum + self.prefixsummatrix[row_element][column_element+1]
                self.prefixsummatrix[row_element+1][column_element+1]=temp
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total=self.prefixsummatrix[row2+1][col2+1]
        left=self.prefixsummatrix[row2+1][col1]
        above=self.prefixsummatrix[row1][col2+1]
        double=self.prefixsummatrix[row1][col1]
        
        answer =total - left - above + double
        
        return answer
