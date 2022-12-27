class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n=len(nums)
        for i in range(n-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return (nums[i]+nums[i+1]+nums[i+2])
        return 0