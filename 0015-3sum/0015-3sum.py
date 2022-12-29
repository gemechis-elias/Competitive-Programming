class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []
        nums.sort()

        for index, target in enumerate(nums):

            if index > 0 and  nums[index-1] == nums[index]:
                continue 

            left = index + 1
            right = len(nums) - 1
            [1,1,4,4,4,5,5]
            while left < right:
                _sum = target + nums[left] + nums[right]

                if _sum == 0:
                    answer.append([target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                       left += 1
                    left += 1

                    while right > left and nums[right] == nums[right-1]:
                       right -= 1
                    right -= 1

                elif _sum > 0:
                    right -= 1
                else:
                    left += 1

        return answer
