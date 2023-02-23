class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = len(nums)+1
        sum_ = 0
        left = right = 0
        flag = True
        while right < len(nums):
            sum_ += nums[right]
            while left<=right and sum_ >= target:
                flag = False
                min_len = min(min_len, right-left+1)
                sum_ -= nums[left]
                left +=1
            right+=1
        if flag:
            return 0
        return min_len
