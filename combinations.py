class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, k, combination):
       
            if k == 0:
                res.append(combination)
                return
            #print(res)
            for i in range(start, n+1):
                backtrack(i+1, k-1, combination+[i])
           
        res = []
        backtrack(1, k, [])
        return res