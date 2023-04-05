class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = 2**len(nums)
        
        ans = []
        for i in range(n):
            temp = []
            for k in range(len(nums)-1, -1,-1):
                val = 1 << k
     
                if (val & i):
                    temp.append(nums[len(nums)-1-k])
            ans.append(temp)

        return ans