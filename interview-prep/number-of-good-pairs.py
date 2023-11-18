class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        result = 0
        for number in nums:
            if number in repeat:
                if repeat[number] == 1:
                    result += 1
                else:
                    result += repeat[number]
                repeat[number] += 1
            else:
                repeat[number] = 1
        return result