class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        for i in range(len(matrix)):
            n = len(matrix)-1
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[n-j][i])
            ans.append(temp)
        matrix.clear()
        matrix.extend(ans)
                
