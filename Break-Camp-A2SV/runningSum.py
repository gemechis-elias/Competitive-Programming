class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans =[]
        sum_ = 0
        for i in nums:
            sum_ += i
            ans.append(sum_)
        return ans
