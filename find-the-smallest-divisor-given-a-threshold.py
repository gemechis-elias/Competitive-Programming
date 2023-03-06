class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            print(sum((n + mid - 1) // mid for n in nums))
            if sum((n + mid - 1) // mid for n in nums) > threshold:
                left = mid + 1
            else:
                right = mid
        return left