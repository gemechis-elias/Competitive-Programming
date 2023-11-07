class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4451:
            return 1
        memo = {}
        num = ceil(n / 25)
        def dp(a, b):
            if (a,b) in memo:
                return memo[(a,b)]
            if a <= 0 and b > 0:
                return 1
            if a <= 0 and b <= 0:
                return 0.5
            if b <= 0:
                return 0
            memo[(a,b)] = 0.25 * (dp(a-4,b) + dp(a-3, b-1) + dp(a-2,b-2) + dp(a-1, b-3))
            return memo[(a,b)]
        return dp(num, num)
            
            