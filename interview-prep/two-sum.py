class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 1
        n = len(nums)
        while l < n:
            if nums[l] + nums[r] == target:
                return [l, r]
            if r+1 == n:
                l += 1
                r = l + 1
            else:
                r += 1