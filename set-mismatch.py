class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep = None
        i = 0
        while i < len(nums):
            if i == nums[i]-1 or nums[i] == 0:
                i += 1
            else:
                if nums[i] != nums[nums[i]-1]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    rep = nums[i]
                    nums[i] = 0

        idx = nums.index(0)+1
        return [rep, idx]