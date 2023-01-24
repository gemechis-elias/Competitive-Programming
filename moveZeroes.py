class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        placeholder  = 0
        while placeholder < len(nums):
            if nums[placeholder] !=0:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                seeker +=1
            placeholder +=1
            
            
        
