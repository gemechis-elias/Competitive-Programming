class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dp(n, k, p):
            if not n or not k:
                return int(p == 0)
            k -= 1
            ans = dp(n, k, p)
            if (dn := group[k]) <= n:
                ans += dp(n-dn, k, max(p-profit[k], 0))
            return ans % 1_000_000_007
        return dp(n, len(group), minProfit)