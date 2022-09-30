class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for j in range(len(nums)-1):
            for i in range(len(nums)-1-j):
                if nums[i]> nums[i+1]:
                    nums[i+1],nums[i]=nums[i],nums[i+1]
        
        return nums
