class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                if i != correct:
                    ans.append(nums[i])
                i += 1
        return set(ans)