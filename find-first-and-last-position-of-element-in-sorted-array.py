class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [bisect_left(nums, target), bisect_right(nums, target)-1]