class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        runningSum = 0
        total = 0
        
        for num in nums:
            runningSum += num
            if runningSum - goal in count:
                total += count[runningSum - goal]
            count[runningSum] += 1
            
        return total