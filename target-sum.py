class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        
        def dp(idx, sum_):
            if idx == -1:
                if sum_ == target:
                    return 1
                return 0

            plus = dp(idx-1, sum_ + nums[idx])
            minus = dp(idx-1, sum_ - nums[idx])
            return plus + minus

        return dp(n-1, 0)