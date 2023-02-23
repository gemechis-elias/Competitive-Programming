class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return float(max(nums))
        n = len(nums)
        max_mean = sum_ = sum(nums[:k])
        for i in range(n-k):
            sum_ += nums[i+k]-nums[i]
            max_mean= max(max_mean, sum_)

        return max_mean/k
