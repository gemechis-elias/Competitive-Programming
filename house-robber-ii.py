class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp_fun(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return max(dp[-1], dp[-2])
        
        if len(nums) <=2 : return max([0] + nums)
        return max( dp_fun(nums[1:]), dp_fun(nums[:-1]) )