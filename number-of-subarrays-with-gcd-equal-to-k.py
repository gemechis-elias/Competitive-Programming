class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] % k == 0:
                    nums[i] = math.gcd(nums[i], nums[j])
                    res += nums[i] == k
                else:
                    break
        return res