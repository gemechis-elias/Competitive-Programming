class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if (n*m) != (r*c) or (n==r and m==c):
            return mat
        
        result = []
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(result)< r :
                    if len(temp)<c-1:
                        temp.append(mat[i][j])
                    else:
                        temp.append(mat[i][j])
                        result.append(temp)
                        temp = [] 
        return result
