class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size=len(nums)
        index_r=size-1
        index_l=0
        while index_l<=index_r:
            if nums[index_l]==val:
                nums[index_l]=nums[index_r]
                nums[index_r]="_"
                index_r-=1
            else:
                index_l+=1
        return index_r+1
