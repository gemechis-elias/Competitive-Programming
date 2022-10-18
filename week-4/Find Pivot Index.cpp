class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summation=sum(nums)
        leftsum=0
        rightsum=0

        for i in range(len(nums)):
            if i>0 : leftsum+=nums[i-1]
            rightsum=summation-leftsum-nums[i]
            if leftsum==rightsum:
                return i
        return -1
