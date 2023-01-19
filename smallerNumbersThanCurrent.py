class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            idx = 0
            count = 0
            while idx <len(nums):
                if nums[idx]< nums[i]:
                    count+=1
                idx +=1
            result.append(count)
        return result
