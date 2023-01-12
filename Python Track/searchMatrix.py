class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for m in matrix:
            if target in m:
                return True
        return False
