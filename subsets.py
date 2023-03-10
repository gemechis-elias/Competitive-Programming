class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(nums, i, arr):
            if len(res) == 2**len(nums):
                return  
            
            if i < len(nums):
                arr.append(nums[i])
                backtrack(nums, i+1, arr)
                res.append(arr[::])
                arr.pop()
                backtrack(nums, i+1, arr)
            
        backtrack(nums, 0, []) 
        res.append([])

        return res