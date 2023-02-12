class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in hashmap:
                    hashmap[i + j] =[mat[i][j]]
                else:
                    hashmap[i + j].append(mat[i][j])
        for val in hashmap.items():
            if val[0] % 2 == 0:
                [ans.append(x) for x in val[1][::-1]]
            else:
                [ans.append(x) for x in val[1]]
        return ans
        
