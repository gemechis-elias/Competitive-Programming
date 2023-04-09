class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y: x | y, nums)

        count = 0
        n = len(nums)
        for i in range(1, (1 << n)):
            
            subset_or = reduce(lambda x, j: x | nums[j], [0] + [k for k in range(n) if (i >> k) & 1])
            if subset_or == max_or:
                count += 1

        return count