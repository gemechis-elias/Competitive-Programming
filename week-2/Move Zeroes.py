class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        left=0
        right=1
        for i in range(n):

            if nums[left]!=0: left,right= left+1 ,right+1
            else:
                if right <n and nums[right]!=0:
                    nums[right],nums[left]=nums[left],nums[right]
                    left= left+1
                right+=1
        return nums
