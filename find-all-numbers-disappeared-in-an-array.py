class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        arr = [0] * len(nums)
        ans = []
        
        for i in range(len(nums)):
            arr[nums[i]-1] += nums[i]
        
        
        for i in range(len(arr)):
            if arr[i] == 0:
                ans.append(i+1)
        return ans