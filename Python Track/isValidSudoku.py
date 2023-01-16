class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row dupilicate
        for i in range(9):
            dup = []
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in dup or int(board[i][j]) > 9:
                        return False
                    else:
                        dup.append(board[i][j])
                        
        #check col duplication 
        for col in range(9):
            dup = []
            for row in range(9):
                if board[row][col]!=".":
                    if board[row][col] in dup or int(board[row][col]) > 9:
                        return False
                    else:
                        dup.append(board[row][col])
        
        # check 3x3 matrix
        for c in range(0, len(board)-2,3):
            for r in range(0, len(board)-2, 3):
                dup = []
                three_matrix =[board[c+y][r:r+3] for y in range(3)]
                     
                for e in range(len(three_matrix)):
                    for l in range(len(three_matrix)):
                        if three_matrix[e][l]!=".":
                            
                            if three_matrix[e][l] in dup:
                                return False
                            else:
                                dup.append(three_matrix[e][l])
               
        return True

            
