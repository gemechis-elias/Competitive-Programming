class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = [-1] * len(nums)

        left, window_sum, diameter = 0, 0, 2 * k + 1
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == diameter:
                result[left + k] = window_sum // diameter
                window_sum -= nums[left]
                left += 1
        return result