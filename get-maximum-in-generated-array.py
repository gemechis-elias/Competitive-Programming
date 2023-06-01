class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        max_ = 0

        def dp(num):
            if num < 2:
                return num
            a = 0
            if num not in memo:
                if num%2:
                    a = dp(num//2) + dp(num//2 + 1)
                else:
                    a = dp(num//2)
                memo[num] = a
            return memo[num]
        
        for i in range(n, -1, -1):
            max_ = max(max_, dp(i))
        
        return max_