class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans =""

        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        for n in nums:
            ans+="".join(str(n))

        return ans
